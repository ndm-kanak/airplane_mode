import frappe

def create_new_role(role, enable_desk_access=True):
    if not frappe.db.exists("Role", role):
        frappe.get_doc({
            "doctype": "Role",
            "role_name": role,
            "desk_access": enable_desk_access
        }).insert(ignore_permissions=True)