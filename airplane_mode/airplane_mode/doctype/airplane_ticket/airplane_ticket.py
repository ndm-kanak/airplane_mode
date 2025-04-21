# Copyright (c) 2024, Nikhil Dhiman and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class AirplaneTicket(Document):

	def validate(self):
		unique_addons = []
		
		for addon in doc.add_ons:
			if addon.item not in existing_addons:
				existing_addons.add(addon.item)
			else:
				doc.add_ons.remove(addon)

	def on_submit(self):
		if doc.status != 'Boarded':
			frappe.throw(_("You can only Submit Tickets with Boarded status."))
