

"""
This script demonstrates how to create a bare-bones, fully functional
chatbot using PyAIML.
"""

# -*- coding: utf-8 -*-
# file: server.py
 
from PyQt4.QtCore import *
import math
import dbus
import dbus.service
from dbus.mainloop.qt import DBusQtMainLoop
import aiml
import sys
import pickle
import os

# Create a Kernel object.
kern = aiml.Kernel()
path = os.path.abspath(__file__)
path = os.path.dirname(path)
print path

# When loading an AIML set, you have two options: load the original
# AIML files, or load a precompiled "brain" that was created from a
# previous run. If no brain file is available, we force a reload of
# the AIML files.
brainLoaded = False
forceReload = False
while not brainLoaded:
	if forceReload or (len(sys.argv) >= 2 and sys.argv[1] == "reload"):
		# Use the Kernel's bootstrap() method to initialize the Kernel. The
		# optional learnFiles argument is a file (or list of files) to load.
		# The optional commands argument is a command (or list of commands)
		# to run after the files are loaded.
		kern.bootstrap(learnFiles=os.path.join(path,"std-startup.xml"), commands="load aiml b")
		brainLoaded = True
		# Now that we've loaded the brain, save it to speed things up for
		# next time.
		kern.saveBrain("standard.brn")
	else:
		# Attempt to load the brain file.  If it fails, fall back on the Reload
		# method.
		try:
			# The optional branFile argument specifies a brain file to load.
			kern.bootstrap(brainFile = os.path.join(path,"standard.brn"))
			brainLoaded = True
		except:
			forceReload = True
questions = []
questions.append("what is your favorite color?")
questions.append("how much money do you have in the bank?")
questions.append("what are your first and second favorite animals?")
questions.append("you are in a jungle, hat does that jungle look like?")
questions.append("you are in a room with white walls, what are you doing?")
questions.append("what is ONE THING that you HAVE to know about someone before you get serious with them?")
answers = []

i = 2

#while(True):
#        i+=1
#	if (i%5 == 0):
#		print questions[i%3]
#		answers.append(raw_input("> "))
#		print kern.respond(answers[-1])
#	elif (i%5 == 4):
#		raw_input("> ")
#	print kern.respond(raw_input("> "), 1)

class Calculator(dbus.service.Object):
  def __init__(self):
    self.sessions = dict();
    self.QSpacing = 5
    busName = dbus.service.BusName('com.chatbot.Chatbot', bus = dbus.SessionBus())
    dbus.service.Object.__init__(self, busName, '/Chatbot')

  def inc_session(self, session_id):
    self.sessions[session_id]["counter"] +=1
    return self.sessions[session_id]["counter"]

  def create_session(self, session_id):
    if session_id in self.sessions: pass
    else:
       self.sessions[session_id] = dict()
       self.sessions[session_id]["counter"] = 2
       self.sessions[session_id]["answers"] = dict()
    return

  @dbus.service.method('com.chatbot.Chatbot', in_signature = 'x', out_signature = 's')
  def set_spacing(self, a):
    self.QSpacing = a
    return "set question spacing"

  @dbus.service.method('com.chatbot.Chatbot', in_signature = 'x', out_signature = 's')
  def remove_session(self, session_id):
    if session_id in self.sessions:
        del self.sessions[session_id]
        return "deleted successfully"
    else:
        return "session not found"
 
  @dbus.service.method('com.chatbot.Chatbot', in_signature = 'sx', out_signature = 's')
  def chat(self, a, session_id):
    a = str(a)
    self.create_session(session_id)
    i = self.inc_session(session_id)
    if (i/self.QSpacing < len(questions) and False):
      if (i%self.QSpacing == 0 False):
        return(questions[i/self.QSpacing])
      elif (i%self.QSpacing == 1 False):
       self.sessions[session_id]["answers"][questions[(i-1)/self.QSpacing]] = a
    response = kern.respond(a, session_id)
    return response
  
  @dbus.service.method('com.chatbot.Chatbot', in_signature = 'x', out_signature = 's')
  def get_answers(self, session_id):
    print type(self.sessions[session_id]["answers"])
    values = self.sessions[session_id]["answers"]
    retval = ""
    for key in values:
        retval += key + "||" + values[key] + "\n"
    print retval
    return retval

DBusQtMainLoop(set_as_default = True)
app = QCoreApplication([])
calc = Calculator()
app.exec_()


