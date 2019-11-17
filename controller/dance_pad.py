import inputs


def get_events():
    events = inputs.get_gamepad()
    for event in events:
        if event.ev_type == 'key':
            print(event.ev_type, event.code, event.state)
        else:
            print(event.ev_type, type(event.ev_type))



while True:
    get_events()
