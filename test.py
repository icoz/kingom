#!/usr/bin/env python3

import tools
import sys

def testTools():
	print("Running test tools.inputNum...")
	n = tools.inputNum("Enter 5: ")
	if n != 5:
		print("Test tools.inputNum failed!")
		return False
	n = tools.inputNum("Enter 'a', then '5': ")
	if n != 5:
		print("Test tools.inputNum failed!")
		return False
	print("Test tools.inputNum success!")
	return True

if __name__ == "__main__":
	print("Running tests...")
	testTools()