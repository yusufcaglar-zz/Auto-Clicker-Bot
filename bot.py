import time
from threading import Thread
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode, Controller as Kontroller

button = Button.left
start_stop_key = KeyCode(char="s")
exit_key = KeyCode(char="e")

class ClickMouse(Thread):
    def __init__(self, button, keyboard):
        super(ClickMouse, self).__init__()
        self.button = button
        self.keyboard = keyboard
        self.running = False
        self.program_running = True
        self.counter = 12

    def start_clicking(self):
        self.running = True
        keyboard.press("m")
    
    def stop_clicking(self):
        self.running = False
        keyboard.release("m")

    def exit(self):
        self.stop_clicking()
        self.program_running = False
        keyboard.release("m")

    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(0.1)
                           
                self.counter = self.counter + 1
                if self.counter >= 12:
                    keyboard.press("p")
                    time.sleep(0.5)
                    keyboard.release("p")

                    keyboard.press("q")
                    time.sleep(0.5)
                    keyboard.release("q")

                    self.counter = 0

                    print("prestige")
            time.sleep(0.1)

mouse = Controller()
keyboard = Kontroller()
click_thread = ClickMouse(button, keyboard)
click_thread.start()

def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
            print("Paused")
        else:
            click_thread.start_clicking()
            print("Started")
    elif key == exit_key:
        click_thread.exit()
        listener.stop()
        print("Stopped")
with Listener(on_press=on_press) as listener:
    listener.join()
