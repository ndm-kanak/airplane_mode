import frappe

def get_context(context):
    # Fetch only published flights
    flights = frappe.get_all(
        "Airplane Flight",
        filters={"published": 1, "route": context.name},
        fields=["name", "source_airport_code", "destination_airport_code",
                "date_of_departure", "time_of_departure", "duration", "route"]
    )

    context.flights = flights
    context.title = "Flights"
    return context