# Copyright (c) 2025, Nikhil Dhiman and contributors
# For license information, please see license.txt

import frappe
from frappe import _

def execute(filters=None):

	airline_list = frappe.get_all("Airline", fields=["name"])
	data = []

	for airline in airline_list:
		airplanes = frappe.get_all("Airplane", filters={"airline": airline.name}, pluck="name")

		airplane_flights = frappe.get_all("Airplane Flight", filters={"airplane": ["in", airplanes]}, pluck="name")

		if airplane_flights:
			tickets = frappe.get_all(
				"Airplane Ticket",
				filters={"flight": ["in", airplane_flights]},
				fields=["total_amount"]
			)
			revenue = sum(float(ticket.total_amount) for ticket in tickets)
		else:
			revenue = 0

		data.append({
			"airline": airline.name,
			"revenue": revenue
		})

	# Sort in descending order
	data.sort(key=lambda x: x["revenue"], reverse=True)

	total_revenue = sum(row["revenue"] for row in data)

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
