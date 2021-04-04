import pyttsx3

robot_mouth = pyttsx3.init()

robot_mouth.setProperty('rate', 130)

volume = robot_mouth.getProperty('volume')
robot_mouth.setProperty('volume', 1.0)

robot_brain = "Hmm I can't hear you, try again"

robot_mouth.say(robot_brain)
robot_mouth.runAndWait()