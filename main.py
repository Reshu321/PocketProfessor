import discord
import os
import requests
import ratemyprofessor
import json
import math
from keep_alive import keep_alive
import re

client = discord.Client() #creates bot

#displays professor information
def getProfInfo(profName):
  professor = ratemyprofessor.get_professor_by_school_and_name(
    ratemyprofessor.get_school_by_name("The University of Texas at Dallas"), profName)
  if professor is not None:
    return ("{0} works in the {1} Department of {2}.\nRating: {3} / 5.0\nDifficulty: {4} / 5.0".format(professor.name, professor.department, professor.school.name, professor.rating,professor.difficulty))
  #Error message if not found 
  else:
    return ("The professor is not on rate my professor")  

#cleans user input
def cleanUserInput(input):
  var = input.split()
  print(var)
  first = var[0]
  last = var[1]
  courseAll = var[2]
  print(first)
  print(last)
  print(courseAll)
  match = re.match(r"([a-z]+)([0-9]+)", courseAll, re.I)
  if match:
      items = match.groups()
  print(items)
  letters = items[0]
  numb = items[1]
  print(letters)
  print(numb)

  return first, last, letters, numb
  
  
@client.event #message when you log in
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
    
@client.event
async def on_message(message):
  if message.author == client.user:
    return
  



  # outputs professor info

  
  if message.content.startswith('!'):
    inputTwo = message.content[1:]
    firstname,lastname,letters,numbers = cleanUserInput(inputTwo)
    professor = firstname + " " + lastname
    profInfo = getProfInfo(professor)
    await message.channel.send(profInfo)
 
  #if the message begins with !,
  #the string after is put into a variable
  if message.content.startswith("!"):
    input = message.content[1:]
    numbers = ""
    letters = ""
    firstname = ""
    lastname = ""

    firstname,lastname,letters,numbers = cleanUserInput(input)
    professor = firstname + " " + lastname
    await message.channel.send(search_subj(letters, numbers, firstname, lastname))



  if message.content.startswith('$hello'):
    greeting = "Welcome to Pick a Professor. Type ! Professor Name and Course Number to get information from Rate My Professor and UTD Grades. For Example '!Matthew Polze BLAW2301'"
    await message.channel.send(greeting)



# load the json data
with open('complete.json') as f:
  items = json.load(f)
  
  
# Define a function to search the item
def search_subj (subj, num, first, last):
  totalAplus = 0
  totalA = 0
  totalAminus = 0
  totalBplus = 0 
  totalB = 0
  totalBminus = 0
  totalCplus = 0
  totalC = 0
  totalCminus = 0
  totalDplus= 0 
  totalD = 0 
  totalF = 0 
  totalW = 0
  
#and (last in keyval['prof'])and (first in keyval['prof'])and (num == keyval['num'])
  for keyval in items:
    if (first in str(keyval['prof'])) and (last in str(keyval['prof'])) and (subj == keyval['subj']) and (num == keyval['num']):
    #grade calculation
      if "A+" in keyval['grades']:
        totalAplus = totalAplus + int(keyval['grades']['A+'])
      if "A" in keyval['grades']:
        totalA = totalA + int(keyval['grades']['A'])
      if "A-" in keyval['grades']:
       totalAminus = totalAminus + int(keyval['grades']['A-'])
      if"B+" in keyval['grades']:
       totalBplus = totalBplus + int(keyval['grades']['B+'])
      if "B" in keyval['grades']:
        totalB = totalB + int(keyval['grades']['B'])
      if "B-" in keyval['grades']:
        totalBminus = totalBminus + int(keyval['grades']['B-'])
      if "C+" in keyval['grades']:
        totalCplus = totalCplus + int(keyval['grades']['C+'])
      if "C" in keyval['grades']:
        totalC = totalC + int(keyval['grades']['C'])
      if "C-" in keyval['grades']:
        totalCminus = totalCminus + int(keyval['grades']['C-'])
      if "D+" in keyval['grades']:
        totalDplus = totalDplus + int(keyval['grades']['D+'])
      if "D" in keyval['grades']:
        totalD = totalD + int(keyval['grades']['D'])
      if "F" in keyval['grades']:
        totalF = totalF + int(keyval['grades']['F'])
      if "W" in keyval['grades']:
        totalW = totalW + int(keyval['grades']['W'])
  
  
  #grade percentage calculations
  totalStudents = (totalA + totalAminus + totalAplus + totalB + totalBminus + totalBplus + totalC + totalCminus + totalCplus + totalD + totalDplus + totalF)

  percentageA = round(((totalA + totalAplus + totalAminus) / totalStudents*100),2)

  percentageB = round(((totalB + totalBplus + totalBminus) / totalStudents*100),2)
  
  percentageC = round(((totalC + totalCplus + totalCminus) / totalStudents*100),2)
  
  percentageD = round(((totalD + totalDplus) / totalStudents*100),2)

  percentageF = round((totalF / totalStudents*100),2)

  percentagePassing = round(((totalStudents-totalF)/totalStudents*100),2)

  #percentageAtotalStudents   = totalStudents+""
  
  #printing tests 
  percentageA = str(percentageA)
  percentageB = str(percentageB)
  percentageC = str(percentageC)
  percentageD = str(percentageD)
  percentageF = str(percentageF)
  percentagePassing = str(percentagePassing)
  
  return ("Average grades for all semester\n")+("A:")+('%')+percentageA +(" | B:")+('%')+ percentageB+(" | C:")+('%') + percentageC + (" | D:")+('%')+percentageD +(" | F:")+('%')+ percentageF +(" | Passing avg:")+('%')+percentagePassing



#runs web server
keep_alive()
client.run(os.getenv('TOKEN'))