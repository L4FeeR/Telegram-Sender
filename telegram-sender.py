#!/usr/bin/python3


########################################################
#IMPORTS
from colors import *
from modules import *
import os, sys, time, requests, subprocess
##########################################################
#API
token="7142033592:AAFy8APbSls_2XhjsLXtvvzm5A54TGV9jx4"
chat_id=-1002043389909
interval=1
##########################################################
#OBJECTS
msg=[]
rask=red+"root"+blue+"@"+green+"tgzen"+reset+" ---> "

ayg=yellow+"["+green+"+"+yellow+"]"+reset
agr=green+"["+yellow+"+"+green+"]"+reset
arg=red+"["+green+"+"+red+"]"+reset
aby=blue+"["+yellow+"+"+blue+"]"+reset
ayr=yellow+"["+red+"+"+yellow+"]"+reset
abg=blue+"["+green+"+"+blue+"]"+reset
ary=red+"["+yellow+"+"+red+"]"+reset
ayr=yellow+"["+red+"+"+yellow+"]"+reset
tried=0

#############################################################
#STARTUP
print("\n")
loading("\t"+aby+green+"Loading the framework...", agr+green+"Skipping the loading screen...")
print(reset)
#############################################################
#class
class TG:
	def __init__(self, token, chat_id, interval):
                self.token="7142033592:AAFy8APbSls_2XhjsLXtvvzm5A54TGV9jx4"
                self.chat_id=-1002043389909
                self.interval=0.5
	def start(err="", fin=""):
		os.system("clear")
		print(blink+"\t\t\t┌---------------------|")
		print("\t\t\t|"+blue+" Py-Telegram Sender "+reset+blink+" |")
		print(blink+"\t\t\t└---------------------|",reset)
		print("")
		print(purple+"          1"+reset+". Send Messages To Telegram")
		print(purple+"          2"+reset+". Send Terminal Command Output To Telegram")
		print(purple+"          └ 3"+reset+". History Of Commands")
		print(purple+"          4"+reset+". Open Telegram groupe --where message sent")
		print(purple+"          5"+reset+". Install Required Packages --only once.")
		print(purple+"          6"+reset+". Author Info")
		print(purple+"          0"+reset+". Quit\n\n\n")
		if (len(err))!=0:
			print("\n\n"+arg+red+err+reset+"\n")
		if len(fin)!=0:
			print("\n"+green+fin+reset+"\n\n")
		try:
			opt=int(input(ayg+rask))
			if opt==1:
				TG.msg_user()
				TG.start("Returned To Menu From Message Portal.")
			elif opt==2:
				TG.cmd_user()
				TG.start(fin="Returned To Menu From Command Portal.")
			elif opt==3:
				TG.showhist()
				TG.start(fin="Returned To Menu From History Portal.")
			elif opt==4:
				TG.tglink()
				TG.start(fin="Returned To Menu From Telegram Links.")
			elif opt==5:
				TG.msg()
				TG.start(fin="Returned To Menu From Package Installation Portal.")
			elif opt==6:
				TG.info()
				time.sleep(6)
				TG.start(fin="Returned To Menu From Author Info.")
			elif opt==0:
				TG.exit()
			elif opt==99:
				os.system("nano telegram-sender.py")
			else:
				TG.start("Entered Number Is Larger Than Required!")
		except ValueError:
			print("")
			TG.start(err="Enter A Number!")
		except KeyboardInterrupt:
			print("KeyBoard Interrupt Captured !")
			TG.start(err="Keyboard Interrupt Captured!  Press 0 To Exit")
		except EOFError:
			print("KeyBoard Interrupt Captured !")
			TG.start(err="Keyboard Interrupt Captured!  Press 0 To Exit")
	def msg_user():
		NOTES=yellow+"""        To send a multiple line program,
        u need to add %0A to the text , where it need to line break
        otherwise \\n will not work.

        These messages are currently sent to \"@l4testsubject\" telegram group.
        """+reset
		os.system("clear")
		print(cyan+"\t\t\t┌---------------------|")
		print("\t\t\t|"+blue+"     Message Sender "+reset+cyan+" |")
		print(cyan+"\t\t\t└---------------------|",reset)
		print(NOTES)
		try:
			smsg=[]
			while True:
				f=input(f"\n\t{abg}Enter message to send [CTRL^D,C to end] : ")
				smsg.append("Message : %0A %0A"+f)
				for i in smsg:
                                        print(str(i).replace("%0A %0A", ""))
		except KeyboardInterrupt:
			print(yellow+"\n\n\t["+green+"CTRL^C"+yellow+"]"+reset+"Message gathering done.")
			TG.send_msg(smsg)
			smsg=[]
		except EOFError:
			print(yellow+"\n\n\t["+green+"CTRL^C"+yellow+"]"+reset+"Message gathering done.")
			TG.send_msg(smsg)
			smsg=[]
	def histsave(save):
		for i in save:
			os.system("echo \""+i+"\""+" >> .l4_hist")
	def showhist():
		j=0
		print(subprocess.getoutput("cat .l4_hist"))
		print("\n\n\n\t Return to main menu in 10 sec")
		time.sleep(10)
	def cmd_user():
		#msg=[]
		try:
			NOTES=""
			print(NOTES)
			smsg=[]
			cmdo=[]
			while True:
				print(reset)
				m=input(f"\n\t{abg}Enter Your Shell command to send the output[CTRL^D,C to end] : ")
				cmdo.append(m)
				out=subprocess.getoutput(m)
				smsg.append("command : "+m+"%0A %0A"+out)
				print(green)
				for i in smsg:
					print(str(i).replace("%0A %0A", ""))
			smgs=[]
					#print(str(i.replace("0A", ""))+", ", end="")
		except KeyboardInterrupt:
			smgs=[]
			cmdo=[]
			print(yellow+"\n\n\t["+green+"CTRL^C"+yellow+"]"+reset+"Message gathering done.")
		except EOFError:
			print(yellow+"\n\n\t["+green+"CTRL^D"+yellow+"]"+reset+"Message gathering done.")
		TG.histsave(cmdo)


	def send_msg(tmsg):
		os.system("clear")
		print("\n\n")
		print(abg+" Sending Message To Telegram")
		try:
			num=0
			for i in tmsg:
				if tmsg[num]=="":
					print(f"\n\n{abg}"+red+"No Message"+reset+" is sent as there is no message !")
				else:
					url=f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={i}"
					requests.get(url).json()
					print(f"\n\n\n{agb}Sent : {i}")
					time.sleep(interval)
				num+=1
		except OSError:
			print("\n\n\n")
			print(f"{ary}"+cyan+"Nerwork not reaching telegram, try connect network again or the ip is blocked!")
			time.sleep(2)
	def tglink():
		print("[*]Opening Telegram ON Web...")
		os.system("xdg-open \"https://t.me/l4testsubject\" &")
		print("""

 ______________________________________
| IF ABOVE NOT WORKS THEN TRY OPEN THE |
| LINK BELOW MANUALLY, 10sec waiting.. |
 --------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/-
                ||----w |
                ||     ||



                        https://t.me/l4testsubject""")
		time.sleep(10)

	def exit():
		loading(ayr+red+"Exiting from the program..."+yellow+"")
		os.system("clear")
		print(green+"Thanks for using this program!"+reset)
	def msg():
		print("Message Function Called !")
		time.sleep(1)
		pass
	def info():
		os.system("clear")
		print("\n\n\n		┌--------------------------------|")
		print("		|"+blue+"         Tool Author           "+reset+" |")
		print("		└─-------------------------------|")
		print("		|                                |")
		print("		|"+blue+"      N"+green+"ame     : "+purple+"Muhamed Lafeer "+reset+"|")
		print("		|                                |")
		print("		|"+blue+"      G"+green+"ithub   : "+purple+"L4FeeR         "+reset+"|")
		print("		|                                |")
		print("		|"+blue+"      O"+green+"S       : "+purple+"Arch Linux "+red+":)  "+reset+"|")
		print("		|                                |")
		print("		|"+blue+"      T"+green+"elegram : "+yellow+"@"+purple+"L4feer        "+reset+"|")
		print("		|--------------------------------|")
		print("		|"+blue+" w"+green+"eb :   "+purple+"l4feer.github.io       "+reset+"|")
		print("		|"+blue+" e"+green+"m : "+purple+"muhamedlafeer837@gmail.com"+reset+"|")
		print("		└─-------------------------------|\n\n")
##################################################################3
#ctrl

a=TG
a.start()
