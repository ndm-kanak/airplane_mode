# Copyright (c) 2024, Nikhil Dhiman and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator


class AirplaneFlight(WebsiteGenerator):

	def before_save(self):
		if self.get_doc_before_save():
			old_gate = self.get_doc_before_save().gate_number
			if old_gate != self.gate_number:
				frappe.enqueue(
					"airline.airplane_flight.update_ticket_gate_numbers",
					flight_name=self.name,
					gate_number=self.gate_number,
					queue='default'
				)
	
	def on_submit(self):
		if self.status != 'Completed':
			self.status = 'Completed'