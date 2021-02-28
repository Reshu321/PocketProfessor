import discord
import os
import requests
import ratemyprofessor
import json
import math

client = discord.Client() #creates bot

def getProfInfo(profName):
 
  professor = ratemyprofessor.get_professor_by_school_and_name(
    ratemyprofessor.get_school_by_name("The University of Texas at Dallas"), profName)
  if professor is not None:
    return ("{0} works in the {1} Department of {2}.\nRating: {3} / 5.0\nDifficulty: {4} / 5.0".format(professor.name, professor.department, professor.school.name, professor.rating,professor.difficulty))
    
  #Error message if not found 
  if professor is None: 
    return ("The prof is not on rate my professor")  
    

def cleaninput(input):
  leftspace = input.find(" ")
  rightspace = input.rfind(" ")
  course = input[rightspace +1:len(input)]
  numbers = course[len(course)-4:len(course)]
  print (numbers)
  letters = course[0:len(course)-4]
  print (letters)
  professor = input[0:rightspace]
  print (professor)
  firstname = professor[0:leftspace]
  lastname = professor[leftspace+1:rightspace]
  print(firstname)
  print(lastname)
  return(numbers,letters,professor,firstname,lastname)

  


@client.event #message when you log in
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event #this event is for when a message is sent
async def on_message(message):
  #if the message is from the bot, do nothing
  if message.author == client.user:
    return
  #if the message begins with $prof, then ask for the prof name
  if message.content.startswith('$prof'):
    await message.channel.send('Enter first and last name:')
 
  #if the message begins with !,
  #the string after is put into a variable
  if message.content.startswith("!"):
    input = message.content[1:]
    numbers,letters,professor,firstname,lastname = cleaninput(input)
    profInfo = getProfInfo(professor)
    await message.channel.send(profInfo)



# load the json data
with open('complete.json') as f:
  items = json.load(f)
  
  
# Define a function to search the item
def search_subj (subj, num, prof):
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
  

  for keyval in items:
    if (subj == keyval['subj']) and (prof == keyval['prof'] and (num == keyval['num'])):
      print(keyval['num'], keyval['term'])
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

  #printing tests 
  print(totalStudents)
  print('%',percentageA)
  print('%',percentageB)
  print('%',percentageC)
  print('%',percentageD)
  print('%',percentageF)
  print('%',percentagePassing)
  #print('{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}'.format(totalA, totalAminus,totalBplus,totalB,totalBminus,totalCplus,totalC,totalCminus,totalDplus,totalD,totalF,totalW)
   

# searches using variables inputted from user
subj = "CS"
num = "1336"
prof = "Le, Khiem V"
search_subj(subj, num, prof)





client.run(os.getenv('TOKEN'))