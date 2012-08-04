#!/usr/bin/env python3

import random
import namedtuple from collections

from food import *
from events import *
from tools import *

GameInit  = namedtuple("GameInit", "years Resources")
Solders = namedtuple("Solders", "worker mercenary")
Resources = namedtuple("Resources", "gold worker solders food country")

event_in_process = False

#******************
#returns named tuple
# .year = 
def init_game():
	y = inputNum("Введите количество лет, которое вы хотите править: ")
	res = Resources(500, 15, 0, 100, 100)
	return GameInit(y, res)

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


if __name__ = "__main__":
	try:
		run()
	except Exception, e as err:
		print err
		#raise e