# Copyright (c) 2024, Nikhil Dhiman and contributors
# For license information, please see license.txt

import frappe
import random
import string
from frappe.model.document import Document
from frappe import _


class AirplaneTicket(Document):

	def assign_seat_number(self):
		if not self.seat:  # Only set if seat is not already assigned
			number = random.randint(1, 99)
			letter = random.choice(["A", "B", "C", "D", "E", "F"])
			self.seat = f"{number}{letter}"

	def before_insert(self):
		self.assign_seat_number()

	def validate(self):
		airplane = frappe.db.get_value("Airplane Flight", self.flight, "airplane")

		capacity = frappe.db.get_value("Airplane", airplane, "capacity")

		ticket_count = frappe.db.count("Airplane Ticket", filters={"flight": self.flight})

		if self.is_new():
			ticket_count += 1

		# Compare with capacity
		if ticket_count > capacity:
			frappe.throw(f"Flight {self.flight} capacity of {capacity} has been reached.")

		existing_addons = []
		line_amt = 0
		for addon in self.add_ons:
			if addon.item not in existing_addons:
				existing_addons.append(addon.item)
			else:
				self.add_ons.remove(addon)
		for amt in self.add_ons:
			line_amt += amt.amount
		self.total_amount = line_amt + self.flight_price

	def on_submit(self):
		if self.status != 'Boarded':
			frappe.throw(_("You can only Submit Tickets with Boarded status."))
