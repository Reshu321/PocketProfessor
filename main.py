import discord
import os
import requests
import ratemyprofessor

#STRING FORMAT EXAMPLE
#print('Hello {}'.format("World"))

client = discord.Client() #creates bot

def getProfInfo(profName):
 
  professor = ratemyprofessor.get_professor_by_school_and_name(
    ratemyprofessor.get_school_by_name("The University of Texas at Dallas"), profName)
  if professor is not None:
    return ("{0} works in the {1} Department of {2}.\nRating: {3} / 5.0\nDifficulty: {4} / 5.0 \nTotal Ratings: {5} ".format(professor.name, professor.department, professor.school.name, professor.rating,professor.difficulty,professor.num_ratings))
    #if professor.would_take_again is not None:
    #    print(("Would Take Again: %s" % round(professor.would_take_again, 1)) + '%')
    #else:
    #    print("Would Take Again: N/A") 
    
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
    await message.channel.send('Enter professor name and class number: (Ryan Lux GOV2326)')
 

  
from replit import db
db["key"] = "value"




client.run(os.getenv('TOKEN'))