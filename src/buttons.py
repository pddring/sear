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

while True:
	for b in buttons:
		if b[0].is_pressed:
			start_press = time.time_ns()
			print(b[1])
			while b[0].is_pressed:
				time.sleep(.1)
			elapsed_time = time.time_ns() - start_press
			
			if elapsed_time / 1000000 > LONG_PRESS:
				print("Long press")
			else:
				print("Short press")
	time.sleep(0.1)
		
