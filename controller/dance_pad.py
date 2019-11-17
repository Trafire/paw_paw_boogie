import inputs


def get_input():
    events = inputs.get_gamepad()
    for event in events:
        if event.ev_type == 'Key':
            print(event.code, 1==event.state)
            return (event.code, 1==event.state)


def update_control_map(control_map):
    i = get_input()
    if i:
        control_map[i[0]] = i[1]
        return True
    return False

control_map = {}

while True:
    if update_control_map(control_map):
        print(control_map)
