# Copyright (c) 2025, Nikhil Dhiman and contributors
# For license information, please see license.txt

import frappe
from frappe import _

def execute(filters=None):
    # Get all airlines
    airlines = frappe.get_all("Airline", fields=["name"])

    # Get revenue grouped by airline from Airplane Ticket
    revenue_data = frappe.db.sql("""
        SELECT
            ap.airline AS airline,
            SUM(at.total_amount) as revenue
        FROM `tabAirplane Ticket` at
        LEFT JOIN `tabAirplane Flight` f ON at.flight = f.name
        LEFT JOIN `tabAirplane` ap ON f.airplane = ap.name
        WHERE at.docstatus = 1
        GROUP BY ap.airline
    """, as_dict=True)

    # Build a map of airline → revenue
    revenue_map = {r["airline"]: r["revenue"] for r in revenue_data}

    data = []
    total_revenue = 0

    for airline in airlines:
        revenue = revenue_map.get(airline.name, 0)
        data.append({
            "airline": airline.name,
            "revenue": revenue
        })
        total_revenue += revenue

    columns = [
        {"label": _("Airline"), "fieldname": "airline", "fieldtype": "Link", "options": "Airline", "width": 250},
        {"label": _("Revenue"), "fieldname": "revenue", "fieldtype": "Currency", "width": 180},
    ]

    summary = [
        {
            "label": _("Total Revenue"),
            "value": total_revenue,
            "datatype": "Currency",
            "indicator": "Green"
        }
    ]

    chart = {
        "data": {
            "labels": [d["airline"] for d in data],
            "datasets": [
                {
                    "name": "Revenue",
                    "values": [d["revenue"] for d in data]
                }
            ]
        },
        "type": "donut"
    }

    return columns, data, None, chart, summary
