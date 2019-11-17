from inputs import get_gamepad, get_key

def main():
    """Just print out some event infomation when the gamepad is used."""
    while 1:
        try:
            events = get_gamepad()
            for event in events:
                print(event.ev_type, event.code, event.state)
        except:
            pass

if __name__ == '__main__':
    main()