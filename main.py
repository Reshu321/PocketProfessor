import discord
import os
import requests
import ratemyprofessor
import json
import math

#STRING FORMAT EXAMPLE
#print('Hello {}'.format("World"))

client = discord.Client() #creates bot

#basic summation in python
#numbers = [2.5, 3, 4, -5]
# start parameter is not provided
#numbers_sum = sum(numbers)
#print(numbers_sum)


def getProfInfo(profName):
 
  professor = ratemyprofessor.get_professor_by_school_and_name(
    ratemyprofessor.get_school_by_name("The University of Texas at Dallas"), profName)
  if professor is not None:
    return ("{0} works in the {1} Department of {2}.\nRating: {3} / 5.0\nDifficulty: {4} / 5.0 \nTotal Ratings: {5} ".format(professor.name, professor.department, professor.school.name, professor.rating,professor.difficulty,professor.num_ratings))
    
    
  #Error message if not found 
  if professor is None: 
    return ("The prof is not on rate my professor")  
    

@client.event #message when you log in
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

#@client.event
#await channel.send('Enter Name')

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
    profName = message.content[1:]
    profInfo = getProfInfo(profName)
    await message.channel.send(profInfo)

  if message.content.startswith('$grades'):
    await message.channel.send('Enter professor name and class number: (Ryan Lux)')
 

 

# load the json data
with open('complete.json') as f:
  items = json.load(f)
  




#just to confirm
#def checktotal (subj, prof):
 # for keyval in items:
  #  if (subj == keyval['subj']) and (prof == keyval['prof']):
   #   print(keyval['num'], keyval['term'], keyval['sect'])
    #grade calculation
    #  print(keyval['grades']['A'])
      #totalA = (keyval['grades']['A'])
     # totalA = totalA + int(keyval['grades']['A'])

  
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
  #grade percentages

  

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
   
# Input the item name that you want to search
subj = "CS"
num = "1336"
prof = "Le, Khiem V"
#print("The number is:", search_subj(subj,prof))
#checktotal(subj, prof)
search_subj(subj, num, prof)
  
#print(data)




client.run(os.getenv('TOKEN'))