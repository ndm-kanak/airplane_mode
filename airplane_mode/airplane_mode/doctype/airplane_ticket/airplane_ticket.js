// Copyright (c) 2024, Nikhil Dhiman and contributors
// For license information, please see license.txt

frappe.ui.form.on('Airplane Ticket', {
    refresh(frm) {
        frm.add_custom_button('Assign Seat', () => {
            let d = new frappe.ui.Dialog({
                title: 'Assign Seat Number',
                fields: [
                    {
                        label: 'Seat Number',
                        fieldname: 'seat_number',
                        fieldtype: 'Data',
                        reqd: true
                    }
                ],
                primary_action_label: 'Assign',
                primary_action(values) {
                    frm.set_value('seat', values.seat_number);
                    frm.refresh_field('seat');
                    frm.save();
                    d.hide();
                }
            });
            d.show();
        }, __('Actions')); // Optional group label
    }
});
