import pyttsx3,ctypes
import SpeechRecognition as sr
import webbrowser, subprocess
import datetime, pyjokes
import wikipedia, wolframalpha
import requests, json, os, winshell
from ecapture import ecapture as ec



				#############	#############         #          ##########     #       #     
				#					  #              #  #        #               #     #      
				#                     #             #    #       #                #   #        
				#############         #            #      #      #                  #                 
							#         #           # #####  #     #                  #                 
							#         #          #          #    #                  #
				#############         #         #            #   ##########         #



# this method is for taking the commands
# and recognizing the command from the
# speech_Recognition module we will use
# the recongizer method for recognizing
def takeCommand():

	r = sr.Recognizer()

	# from the speech_Recognition module
	# we will use the Microphone module
	# for listening the command
	with sr.Microphone() as source:
		print('Listening')
		
		# seconds of non-speaking audio before
		# a phrase is considered complete
		r.pause_threshold = 0.7
		audio = r.listen(source)
		
		# Now we will be using the try and catch
		# method so that if sound is recognized
		# it is good else we will have exception
		# handling
		try:
			print("Recognizing")
			
			# 
			Query = r.recognize_google(audio, language='en')
			print("the command is printed=", Query)
			
		except Exception as e:
			print(e)
			print("Say that again, please")
			return "None"
		
		return Query

def speak(audio):
	
	engine = pyttsx3.init()
	# getter method(gets the current value
	# of engine property)
	voices = engine.getProperty('voices')
	
	# setter method .[0]=male voice and
	# [1]=female voice in set Property.
	engine.setProperty('voice', voices[1].id)
	
	# Method for the speaking of the assistant
	engine.say(audio)
	
	# Blocks while processing all the currently
	# queued commands
	engine.runAndWait()

def tellDay():
	
	# This function is for telling the
	# day of the week
	day = datetime.datetime.today().weekday() + 1
	
	#this line tells us about the number
	# that will help us in telling the day
	Day_dict = {1: 'Monday', 2: 'Tuesday',
				3: 'Wednesday', 4: 'Thursday',
				5: 'Friday', 6: 'Saturday',
				7: 'Sunday'}
	
	if day in Day_dict.keys():
		day_of_the_week = Day_dict[day]
		print(day_of_the_week)
		speak("The day is " + day_of_the_week)


def tellTime():
	
	# This method will give the time
	time = str(datetime.datetime.now())
	
	# the time will be displayed like
	# this "2022-06-05 17:50:14.582630"
	#nd then after slicing we can get time
	self=0
	print(time)
	hour = time[11:13]
	min = time[14:16]
	speak(self, "The time is sir" + hour + "Hours and" + min + "Minutes")

def Hello():
	
	# This function is for when the assistant
	# is called it will say hello and then
	# take query
	speak("""Hello I am Stacy your virtual assistant.
			I am here to help you out with anything, feel free 
			 Tell me how may I help you. I'm listening""")


def Take_query():

	# calling the Hello function for
	# making it more interactive
	Hello()
	
	# This loop is infinite as it will take
	# our queries continuously until and unless
	# we do not say bye to exit or terminate
	# the program
	
	while(True):
		
		# taking the query and making it into
		# lower case so that most of the times
		# query matches and we get the perfect
		# output
		query = takeCommand().lower()
		if "open geeksforgeeks" in query:
			speak("Opening GeeksforGeeks ")
			
			# in the open method we just to give the link
			# of the website and it automatically open
			# it in your default browser
			webbrowser.open("www.geeksforgeeks.com")
			continue
		
		elif "open google" in query:
			speak("Opening Google ")
			webbrowser.open("www.google.com")
			continue

		#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

			#a user asks about they being obese
		elif "am i obese" in query:
			speak("please, what is your body mass index")
			continue

			#this code block helps the user to calculate their body mass index
		elif "i don't know" in query:
			speak("""please check your body mass index by dividing your weight by your height squared, 
			do you want to know the grading of body mass index""")
			continue
		
			#the grading system of the body mass index is read out aloud to the user
			#Bmi < 18.5 is "Underweight"
			#Bmi >= 18.4 but < 25 is "Normal"
			#Bmi >= 25 but < 30 is "Overweight"
			#Bmi > 30 is obese
		elif "yes" in query:
			speak("""if your body mass index is less than 18.5, you're underweight,
					 if your body mass index is greater than 18.5, but less than 25 you're normal,
					 if your body mass index is greater than 25, but less than 30 you're overweight,
					 your obese, 
					 do you need some health tips about weight management or nutrition just say open google """)

		elif "am i underweight" in query:
			speak("please, what is your body mass index")
			continue

		elif "am i overweight" in query:
			speak("please, what is your body mass index")
			continue
		
		elif "i don't know" in query:
			speak("please check your body mass index by dividing your weight by your height squared")
			continue
		
		elif "i don't know" in query:
			speak("please check your body mass index by dividing your weight by your height squared")
			continue

		#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

			#the user can ask for the location of any place under this code
		elif "where is" in query or "find" in query or "locate" in query:
			query = query.replace("where is", "")
			location = query
			speak("User asked to locate")
			speak(location)
			webbrowser.open("https://www.google.nl / maps / place/" + location + "")
 

			#this tells which day it is if asked
		elif "which day is it" in query:
			tellDay()
			continue
			
			#tells time
		elif "tell me the time" in query:
			tellTime()
			continue
		
			# this will exit and terminate the program
		elif "bye" in query or "goodbye" in query or "exit" in query:
			speak("Bye. Thanks for your time and have a nice time")
			exit()
		

		######################################################################################
		elif "good morning" in query:
			speak("A warm" + query)
			speak("How are you")

			#the name of the assistant is mentioned here
		elif "tell me your name" in query or "your name" in query or "what is your name" in query:
			speak("I am Stacy. Your Virtual Assistant")

			#the user can ask the the age of the virtual assistant and an answer given
		elif "how old are you" in query:
			speak("I'm as old as the foundation of the earth and as young as a newborn baby")
			continue

		elif "fine" in query or "good" in query or "i am good" in query:
			speak("It's nice to hear you're fine")

		elif "who made you" in query or "who created you" in query:
			speak("I was created by Francis as his project work to help him as a virtual assistant")

		elif "joke" in query or "tell me a joke" in query or "joke for me" in query:
			speak(pyjokes.get_joke())

		elif "will you be my girlfriend" in query or "will you be my boyfriend" in query:
			speak("I'm not sure, maybe you should give me some time")

		elif "i love you" in query:
			speak("It's hard to understand")
		

		elif "search" in query or "play" in query:
			query = query.replace("search", "")
			query = query.replace("play", "")
			webbrowser.open(query)
		

		#######################################################################################

		elif "capture" in query or "snap" in query or "take a picture" in query:
			ec.capture(0, "Jarvis Camera ", "img.jpg")

		elif "restart" in query:
			subprocess.call(["shutdown", "/r"])

		elif "hibernate" in query or "sleep" in query:
			speak("Hibernating")
			subprocess.call("shutdown / h")

		elif "log off" in query or "sign out" in query or "shutdown" in query:
			speak("Make sure all the application are closed before sign-out")
			time=0
			time.sleep(5)
			subprocess.call(["shutdown", "/l"])
			
		elif "lock window" in query:
			speak("locking the device")
			ctypes.windll.user32.LockWorkStation()

		elif "shutdown system" in query:
			speak("Hold On a Sec ! Your system is on its way to shut down")
			subprocess.call('shutdown / p /f')

		elif "empty recycle bin" in query:
			winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
			speak("Recycle Bin Recycled")

		elif "from wikipedia" in query:
			
			# if any one wants to have a information
			# from wikipedia
			speak("Checking the wikipedia ")
			query = query.replace("wikipedia", "")
			
			# it will give the summary of 4 lines from
			# wikipedia we can increase and decrease
			# it also.
			result = wikipedia.summary(query, sentences=4)
			speak("According to wikipedia")
			speak(result)



if __name__ == '__main__':
	
	# main method for executing
	# the functions
	Take_query()

				#############	#############         #          ##########     #       #     
				#					  #              #  #        #               #     #      
				#                     #             #    #       #                #   #        
				#############         #            #      #      #                  #                 
							#         #           # #####  #     #                  #                 
							#         #          #          #    #                  #
				#############         #         #            #   ##########         #