tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}

types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}


def get_unique_tickets(tickets):
    uniq_ticket_list = []
    for key, value in tickets.items():
        new_list = []
        for ticket in value:
            if ticket not in uniq_ticket_list:
                uniq_ticket_list.append(ticket)
                new_list.append(ticket)
        tickets[key] = new_list

    return tickets

def get_merge_between_types_and_tickets(types, tickets):
    tickets_by_type = {}
    for key, value in types.items():
        new_list = []
        for ticket in tickets[key]:
            new_list.append(ticket)
        tickets_by_type[value] = new_list

    return tickets_by_type

print(get_unique_tickets(tickets))
print(get_merge_between_types_and_tickets(types, tickets))
