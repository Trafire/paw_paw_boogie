import inputs


def get_input():
    events = inputs.get_gamepad()
    for event in events:
        if event.ev_type == 'Key':
            print(event.code, 1 == event.state)
            return (event.code, 1 == event.state)


def update_control_map(control_map):
    while True:
        i = get_input()
        if i:
            control_map[i[0]] = i[1]




key_map = {'BTN_BASE3': False, 'BTN_TRIGGER': False, 'BTN_BASE': False, 'BTN_THUMB2': False, 'BTN_BASE2': False,
               'BTN_TOP': False, 'BTN_TOP2': False, 'BTN_BASE4': False, 'BTN_THUMB': False, 'BTN_PINKIE': False}
