import inputs


def get_events():
    events = inputs.get_gamepad()
    for event in events:
        if event.ev_type == 'Key':
            print(event.code, 1==event.state)
            return (event.code, 1==event.state)




while True:
    get_events()
