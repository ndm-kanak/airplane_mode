# Copyright (c) 2024, Nikhil Dhiman and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.website.website_generator import WebsiteGenerator


class AirplaneFlight(Document):
	
	def get_context(context):
	    # Fetch only published flights
	    import pdb; pdb.set_trace()
	    flights = frappe.get_all(
	        "Airplane Flight",
	        filters={"published": 1, "route": context.name},
	        fields=["name", "source_airport_code", "destination_airport_code",
	                "date_of_departure", "time_of_departure", "duration", "route"]
	    )

	    context.flights = flights
	    context.title = "Flights"
	    return context
