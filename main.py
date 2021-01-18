import pyttsx3 
import speech_recognition as sr
import sys
from command import openfb,input_user_pass,login


engine = pyttsx3.init()
engine.setProperty('voice',"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
engine.setProperty('rate', 140)
r = sr.Recognizer()

driver = None

def initiate():
	with sr.Microphone() as source:
		voice_data = ''
		try:
			engine.setProperty('rate', 170)
			engine.say("Hello babe! What's up")
			engine.runAndWait()
			print("Speak now")
			audio = r.listen(source)
			voice_data = r.recognize_google(audio)
		except sr.UnknownValueError:
			engine.say("Sorry I could not here that!")
			engine.runAndWait()
		except sr.RequestError:
			engine.say("Sorry my speech service is down")
			engine.runAndWait()
		return respond(voice_data)

def anything_else():
	with sr.Microphone() as source:
		voice_data = ''
		try:
			engine.setProperty('rate', 200)
			engine.say("anything else")
			engine.runAndWait()
			print("Speak now")
			audio = r.listen(source)
			voice_data = r.recognize_google(audio)
		except sr.UnknownValueError:
			engine.say("Sorry I could not here that!")
			engine.runAndWait()
		except sr.RequestError:
			engine.say("Sorry my speech service is down")
			engine.runAndWait()
		return respond(voice_data)

def respond(voice_data):
	print(type(voice_data))
	print(voice_data)
	engine.setProperty('rate', 160)
	if not voice_data:
		print("No voice detected")
		anything_else()
	elif voice_data == "open facebook":
		engine.say("Sure. Give me a second")
		engine.runAndWait()
		global driver
		driver = openfb()
		anything_else()
	elif voice_data == "login":
		engine.say("Sure!")
		engine.runAndWait()
		login(driver)
		anything_else()
	elif voice_data == "input my account":
		engine.say("Right away!")
		engine.runAndWait()
		input_user_pass(driver)
		anything_else()
	
	elif voice_data == "what is your name":
		engine.say("I'm your girlfriend. You should know me!")
		engine.runAndWait()
		anything_else()
	elif voice_data == "how old are you":
		engine.say("Younger than you")
		engine.runAndWait()
		anything_else()
	elif voice_data == "what's up sa inyo mga paa":
		engine.say("POWER!")
		engine.runAndWait()
		anything_else()
	elif voice_data == "thank you" or voice_data == "bye" or  voice_data == "that's all" or voice_data == "yun lang salamat" or voice_data == "quit":
		engine.say("Okay! See you later. I love you")
		engine.runAndWait()
	else:
		engine.say("Hmmmm. I dont know what to say")
		engine.runAndWait()
		anything_else()


myvoice = initiate()



