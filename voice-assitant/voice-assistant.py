import speech_recognition
import pyttsx3
from datetime import date, datetime


robot_ear = speech_recognition.Recognizer()
#activate the engine
robot_mouth = pyttsx3.init()
#set the speed rate
robot_mouth.setProperty('rate', 130)

#set the volume
volume = robot_mouth.getProperty('volume')
robot_mouth.setProperty('volume', 1.0)

robot_brain = ""
while True:
	with speech_recognition.Microphone() as mic:
		print("Robot: I'm listening...")
		robot_ear.adjust_for_ambient_noise(mic)
		audio = robot_ear.record(mic, duration=3)

	print("Robot: ...")

	try:
		you = robot_ear.recognize_google(audio)
	except:
		you == ""

	print("You: " + you)


	if you == "":
		robot_brain = "I can't hear you, try again"
	elif "hello" in you:
		robot_brain = "Hello Group 4"
	elif "date" in you:
		today = date.today()
		robot_brain = today.strftime("%B %d, %Y")
	elif "time" in you:
		now = datetime.now()
		robot_brain = now.strftime("%H hours %M minutes %S seconds")
	elif "bye" in you:
		robot_brain = "Bye Group 4. See you again."
		print("Robot: " + robot_brain)
		#speak
		robot_mouth.say(robot_brain)
		robot_mouth.runAndWait()
		break
	else:
		robot_brain = "dark dark bruh bruh lmao"

	print("Robot: " + robot_brain)
	#speak
	robot_mouth.say(robot_brain)
	robot_mouth.runAndWait()