import os
import pyttsx3
pyttsx3.speak("Tell me What can I open for you:")
while True:
	print("Give me a instruction what I do for you:-" , end='')
	p=input()

	if(("run" in p) or ("open" in p) or ("execute" in p)) and (("chrome" in p) or ("Browser" in p)):
		os.system("chrome")
		pyttsx3.speak("Thankyou for using chrome")
	elif(("run" in p) or ("start" in p) or("execute" in p)) and (("vlc" in p) or ("Movies" in p)):
		os.system("vlc")
		pyttsx3.speak("Thankyou for using vlc")
	elif(("run" in p) or ("open" in p) or ("execute" in p)) and (("notepad" in p) or ("Editor" in p)):
		os.system("notepad")
		pyttsx3.speak("Thankyou for using Editor")
	elif(("run" in p) or ("open" in p) or ("execute" in p)) and ("windows player" in p):
		os.system("wmplayer")
		pyttsx3.speak("Thankyou for using Windows Media Player")
	elif(("run" in p) or ("open" in p) or ("execute" in p)) and (("notepadplus" in p) or ("editorplus" in p)):
		os.system("notepad++")
		pyttsx3.speak("Thankyou for using Notepad++")
	elif(("run" in p) or ("open" in p) or ("execute" in p)) and (("anydesk" in p) or ("teamviewer" in p)):
		os.system("AnyDesk")
		pyttsx3.speak("Thankyou for using AnyDesk")
	elif(("run" in p) or ("open" in p) or ("execute" in p)) and (("internet explorer" in p) or ("Searching" in p)):
		os.system("iexplore")
		pyttsx3.speak("Thankyou for using Internet Explorer")
	elif(("run" in p) or ("open" in p) or ("execute" in p)) and (("sublime text" in p) or ("Html Code Application" in p)):
		os.system("sublime_text")
		pyttsx3.speak("Thankyou for using Sublime Text")
	elif("exit" in p) or("stop" in p):	
		break
	else:
		print("Don't Support")