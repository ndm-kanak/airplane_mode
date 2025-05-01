import frappe
import random

def execute():
	tickets = frappe.get_all("Airplane Ticket", filters={"seat": ["=", ""], "docstatus": ["!=", 2] }, fields=["name"])
	print('tickets>>>>>>>>>>>>>>>>>>>', tickets)
	for ticket in tickets:
		seat = generate_random_seat()
		frappe.db.set_value("Airplane Ticket", ticket.name, "seat", seat)
		frappe.db.commit()

def generate_random_seat():
	number = random.randint(1, 99)
	letter = random.choice(["A", "B", "C", "D", "E", "F"])
	return f"{number}{letter}"