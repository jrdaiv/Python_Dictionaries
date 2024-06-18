# Initialize the service_tickets dictionary
service_tickets = {
    "01": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "02": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

def open_ticket(tickets):
    tick_num = input("Enter ticket number. ")
    customer = input("Enter customers name. ")
    issue = input("What is the issue. ")
    status = input("Status open or closed? ")
    new_tick = {"Customer": customer, "Issue": issue, "Status": status}
    tickets[tick_num] = new_tick
    print(new_tick)

def close_ticket(tickets):
    for tickets in service_tickets:
        service_tickets[tickets]["status"] = "closed"
        break

def display_ticket(service_tickets):
    for service_num, info in service_tickets.items():
        print(f"Ticket {service_num}: ")
        print(f"Customer {info}: ")
        print(f"Issue {info}: ")
        print(f"Status {info}: ")

open_ticket(service_tickets)
close_ticket(service_tickets)
display_ticket(service_tickets)


