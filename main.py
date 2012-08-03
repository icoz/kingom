#!/usr/bin/env python3

import random
import namedtuple from collections

import * from food
import * from events

Resources = namedtuple("Resources", "gold human solder food country")

event_in_process = False


def run():
	init_game()
	plant_food()
	trading()
	#choose event
	for _ in range(3):
		run_some_event()
	if event_in_process:
		process_events()
	get_food()
	eat_food()

	return


if __name__ = "main":
	try:
		run()
	except Exception, e as err:
		print err
		#raise e