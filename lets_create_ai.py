from datetime import datetime as dt
from datetime import time
import pyttsx3 as pt
engine = pt.init()
rate = engine.getProperty('rate')
voices = engine.getProperty("voices")
engine.setProperty('rate',150)
engine.setProperty('voice',voices[2].id)
engine.say("Welcome to your personal assistant , what do you want VIKAS?")
dictMonday = {"1":"QAR","2":"Cloud","3":"Plays","4":"Artificial Intelligence"}
dictTuesday = {"1":"TT","2":"Cloud","3":"Cloud","4":"Artificial Intelligence"}
dictWedday = {"1":"Artificial Inteligence","2":"Cloud","3":"QAR","4":"TT"}
dictThurday = {"1":"TT","2":"Artificial Intelligence","3":"Library","4":"Robotics"}
dictFriday = {"1":"QAR","2":"Dance","3":"Music","4":"Sports"}
dictSatday = {"1":"Maths","2":"Cloud","3":"Science","4":"Artificial Intelligence"}
user = input("Enter Your Asks ")
if "monday" in user.lower():
  if "first" in user.lower():
    value = dictMonday.get("1")
    engine.say("Your first period on monday is")
    engine.say(value)
  elif "second" in user.lower():
    value = dictMonday.get("2")
    engine.say("Your second period on monday is")
    engine.say(value)
  elif "third" in user.lower():
    value = dictMonday.get("3")
    engine.say("Your Third period on monday is")
    engine.say(value)
  elif "fourth" in user.lower():
    value = dictMonday.get("4")
    engine.say("Your fourth period on monday is")
    engine.say(value)
  else:
    engine.say("Provide valid input Please")
elif "tuesday" in user.lower():
    if "first" in user.lower():
     value = dictTuesday.get("1")
     engine.say("Your first period on tuesday is")
     engine.say(value)
    elif "second" in user.lower():
     value = dictTuesday.get("2")
     engine.say("Your second period on tuesday is")
     engine.say(value)
    elif "third" in user.lower():
      value = dictTuesday.get("3")
      engine.say("Your Third period on tuesday is")
      engine.say(value)
    elif "fourth" in user.lower():
      value = dictTuesday.get("4")
      engine.say("Your fourth period is")
      engine.say(value)
    else:
      engine.say("Provide valid input Please")
elif "wednesday" in user.lower():
     if "first" in user.lower():
      value = dictWedday.get("1")
      engine.say("Your first period on wednesday is")
      engine.say(value)
     elif "second" in user.lower():
      value = dictWedday.get("2")
      engine.say("Your second period on wednesday is")
      engine.say(value)
     elif "third" in user.lower():
       value = dictWedday.get("3")
       engine.say("Your Third period on wednesday is")
       engine.say(value)
     elif "fourth" in user.lower():
      value = dictWedday.get("4")
      engine.say("Your fourth period on wednesday is")
      engine.say(value)
     else:
      engine.say("Provide valid input Please")
elif "thursday" in user.lower():
    if "first" in user.lower():
      value = dictThurday.get("1")
      engine.say("Your first period on thursday is")
      engine.say(value)
    elif "second" in user.lower():
      value = dictThurday.get("2")
      engine.say("Your second period on thursday is")
      engine.say(value)
    elif "third" in user.lower():
       value = dictThurday.get("3")
       engine.say("Your Third period on thursday is")
       engine.say(value)
    elif "fourth" in user.lower():
      value = dictThurday.get("4")
      engine.say("Your fourth period on thursday is")
      engine.say(value)
    else:
      engine.say("Provide valid input Please")
elif "friday" in user.lower():
    if "first" in user.lower():
      value = dictFriday.get("1")
      engine.say("Your first period on friday is")
      engine.say(value)
    elif "second" in user.lower():
      value = dictFriday.get("2")
      engine.say("Your second period on friday is")
      engine.say(value)
    elif "third" in user.lower():
       value = dictFriday.get("3")
       engine.say("Your Third period on friday is")
       engine.say(value)
    elif "fourth" in user.lower():
      value = dictFriday.get("4")
      engine.say("Your fourth period on friday is")
      engine.say(value)
    else:
      engine.say("Provide valid input Please")
else:
    if "first" in user.lower():
      value = dictSatday.get("1")
      engine.say("Your first period on saturday is")
      engine.say(value)
    elif "second" in user.lower():
      value = dictSatday.get("2")
      engine.say("Your second period on saturday is")
      engine.say(value)
    elif "third" in user.lower():
       value = dictSatday.get("3")
       engine.say("Your Third period on saturday is")
       engine.say(value)
    elif "fourth" in user.lower():
      value = dictSatday.get("4")
      engine.say("Your fourth period on saturday is")
      engine.say(value)
    else:
      engine.say("Provide valid input Please")
engine.runAndWait()