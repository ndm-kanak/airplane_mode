# Copyright (c) 2024, Nikhil Dhiman and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class FlightPassenger(Document):
	
	def validate(self):
		self.set_passenger_name()

	def set_passenger_name(self):
		self.full_name = " ".join(
			filter(lambda x: x, [self.first_name, self.last_name])
		)
