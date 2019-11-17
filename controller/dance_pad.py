import inputs


def get_input():
    events = inputs.get_gamepad()
    for event in events:
        if event.ev_type == 'Key':
            return (event.code, 1 == event.state)


def update_control_map(control_map):
    while True:
        i = get_input()
        if i:
            control_map[i[0]] = i[1]





