import time
from gpiozero import Button

LONG_PRESS = 1000	# milliseconds for a long press


class ButtonManager:
	def __init__(self):
		self.buttons = []

		self.running = False

		for pin in PINS:
			self.buttons.append((Button(PINS[pin]), pin))

		self.listeners = {
			'DOWN': [],
			'SHORT_PRESS': [],
			'LONG_PRESS': []
		}

	def add_listener(self, button_name, event, callback):
		self.listeners[event].append((button_name, callback))

	def trigger(self, button_name, event):
		for (b_name, callback) in self.listeners[event]:
			if b_name == button_name:
				callback(button_name)

	def stop(self):
		self.running = False

	def start(self):
		self.running = True
		while self.running:
			for b in self.buttons:
				if b[0].is_pressed:
					start_press_time = time.time_ns()
					self.trigger(b[1], 'DOWN')
					while b[0].is_pressed:
						time.sleep(.1)
					elapsed_time = time.time_ns() - start_press_time
					
					if elapsed_time / 1000000 > LONG_PRESS:
						self.trigger(b[1], 'LONG_PRESS')
					else:
						self.trigger(b[1], 'SHORT_PRESS')
			time.sleep(0.1)

PINS = {
	'MIDDLE': 2,	# WHITE
	'RIGHT': 3,	# GREEN
	'LEFT' : 4,	# BLUE
	'TOP'  : 22,	# RED
}

if __name__ == "__main__":
	b = ButtonManager()
	print("Press the MIDDLE button to test events, long press to exit")
	b.add_listener('MIDDLE', 'SHORT_PRESS', lambda name: print(f"{name} short press"))
	b.add_listener('MIDDLE', 'LONG_PRESS', lambda name: b.stop())
	b.start()