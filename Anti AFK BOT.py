from pynput.keyboard import Key, Controller, Listener
import keyboard
import time

keyboard = Controller()
time.sleep(2)

while True:
	keyboard.press('a')
	time.sleep(0.5)
	keyboard.release('a')
	keyboard.press('d')
	time.sleep(0.5)
	keyboard.release('d')