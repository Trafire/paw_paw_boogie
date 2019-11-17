def map_to_grid(event):
    m = {
        'BTN_TOP2': (0, 2),
        'BTN_TRIGGER': (0, 1),
        'BTN_BASE': (0, 0),

        'BTN_THUMB': (1, 2),
        'BTN_THUMB2': (1, 0),

        'BTN_PINKIE': (2, 2),
        'BTN_TOP': (2, 1),
        'BTN_BASE2': (2, 0),

        'BTN_BASE3': 'select',
        'BTN_BASE4': 'start',
    }
    if event in m:
        return m[event]

key_map = {'BTN_BASE3': False, 'BTN_TRIGGER': False, 'BTN_BASE': False, 'BTN_THUMB2': False, 'BTN_BASE2': False,
           'BTN_TOP': False, 'BTN_TOP2': False, 'BTN_BASE4': False, 'BTN_THUMB': False, 'BTN_PINKIE': False}
