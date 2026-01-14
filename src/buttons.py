import time
from gpiozero import Button
PINS = {
	'MIDDLE': 2,	# WHITE
	'RIGHT': 3,	# GREEN
	'LEFT' : 4,	# BLUE
	'TOP'  : 22,	# RED
}

LONG_PRESS = 1000	# milliseconds for a long press

buttons = []
for pin in PINS:
	buttons.append((Button(PINS[pin]), pin))


def short_press(button_name):
	print(f"Short press detected on {button_name} button")

def long_press(button_name):
	print(f"Long press detected on {button_name} button")


while True:
	for b in buttons:
		if b[0].is_pressed:
			start_press = time.time_ns()
			print(b[1])
			while b[0].is_pressed:
				time.sleep(.1)
			elapsed_time = time.time_ns() - start_press
			
			if elapsed_time / 1000000 > LONG_PRESS:
				long_press(b[1])
			else:
				short_press(b[1])
	time.sleep(0.1)
		
