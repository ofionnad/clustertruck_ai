from pynput import keyboard
import asyncio
import websockets

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
# with keyboard.Listener(
#         on_press=on_press,
#         on_release=on_release) as listener:
#     listener.join()

# ...or, in a non-blocking fashion:
def key_listener():
    with keyboard.Events() as events:
    # Block at most one second
        event = events.get(0.5)
        if event is None:
            pass
        else:
            print('Received event {}'.format(event))

def transmit_keys():

    queue = asyncio.Queue()
    loop = asyncio.get_event_loop()

    def on_press(key):
        loop.call_soon_threadsafe(queue.pu_nowait, key.char)

    keyboard.Listener(on_press=on_press).start()
    return queue

async def main():
    key_queue = transmit_keys()
    async with websockets.connect("ws://localhost:8765") as websocket:
        while True:
            key = await key_queue.get()
            await websocket.send(f"key pressed: {key}")

asyncio.run(main())

# listener = keyboard.Listener(on_press=on_press, on_release=on_release)
# listener.start()
