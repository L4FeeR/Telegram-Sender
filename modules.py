import os, sys, time
from colors import *
def loading(msg="", err=""):
	bar= ["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]
	bar.extend(bar)
#	bar.extend(bar)
	try:
		for i in bar:
			sys.stdout.write("\r"+msg+i)
			time.sleep(0.09)
			sys.stdout.flush()
	except KeyboardInterrupt:
		print("")
		print("\t"+err)
		time.sleep(0.5)
def loading1():
	bar=[x for x in range(0, 101)]
	for i in bar *1:
			sys.stdout.write("\r   "+str(i))
			time.sleep(0.01)
			sys.stdout.flush()


def loading2():
        bar=[':)', ':(', ':/', ':\\', '' ':]']
        for i in bar *10:
                        sys.stdout.write("\r   "+i)
                        time.sleep(0.1)
                        sys.stdout.flush()


