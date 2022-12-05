import requests
from pyrogram import Client, filters
from pyrogram.types import Message
import os
import pytz
from datetime import datetime



TOKEN="5923062549:AAHflO6_m1vY6DlTI5lvgQuaZ6akaotQA88"
session="BQAyUG0mSwxhVFli6wkfoBQeZ4eXvKsJjtX8I5Nc_4eqHZO8-ef5L9m5pQojapQBx2MpDE8iDD6OPMvYlIoSjy3WdKs5KudNXN3fCoj-jRh6tF3iwI8J-EZjDy1hgyrYMUCxOl50OnKrwW3Bb7XK-2G-TBwLQboJbrXln-50dWLPRP44n-j5iI4OHEFbK9Wd84gbV9Oe2gEV-eBYUxsccXSxQzf4NjX6XE_0euJKdgMs4XChztvLjWOxD-olyRtexshlMHIDXssdyW4HJzix1oiXUFVhn0agVJH0O4wwaaj8-aTihdSkWsDOpl2N0tr2L1hfLFU4-D3UP56tJlIWhPXQSuAgXQA"
api_id =4068941
api_hash ="4b8c69be3975bd027042127fc337867a"
log_channel="-1001841565100"
myuserid="@PUBUDUPRASAD"
BOT_url='https://api.telegram.org/bot'+TOKEN
app=Client(session, api_id, api_hash)


def utc_to_time(naive, timezone="Asia/Kolkata"):
    dt_object = datetime.fromtimestamp(naive)
    return dt_object.replace(tzinfo=pytz.utc).astimezone(pytz.timezone(timezone))

async def dirup(message,pat,tgapi,otherr):
  app.set_parse_mode()
  pat=pat[:-1]
  userid = str(message.chat.id)
  name= str(message.chat.first_name) + "  " + str(message.chat.last_name)
  tes =tgapi+'?caption=' +otherr +str(message.chat.username)+"\n"+ "<b>Name:</b> " + str(message.chat.first_name) + " " + str(message.chat.last_name) +"\n" + "<b>User id:</b> " + "<code>" +str(message.chat.id) + "</code>"  + "\n" + "<b>Message:</b> "+str(message.caption) +"\n" + "<b>Date and Time:</b> " +str(utc_to_time(message.date))
  arr = os.listdir(pat)
  for files in arr:
    pathh=pat+"/"+str(files)
    file_size=os.stat(pathh).st_size
    if file_size<52428800 :
      botSend(pathh,tes,pat)
      os.remove(pathh)
    else:
      print('file size is too big')
      await message.forward(log_channel)

def botSend(fileName, tes ,pat):
    app.set_parse_mode()
    files = {pat: (fileName, open(fileName,'rb'))}  
    r = requests.post(BOT_url+tes+'&parse_mode=html'+'&chat_id='+str(log_channel),files=files)
    print(r)



@app.on_message(filters.text & filters.private & ~filters.bot)
async def msg_text(client: Client, message: Message):
  app.set_parse_mode()
  print('text recived')
  userid = str(message.chat.id)
  name= str(message.chat.first_name)
  if message.from_user.username == myuserid:
    tes ="<b>From @</b>"+str(message.from_user.username)+"<b> to @</b>"+ str(message.chat.username)+"\n"+ "<b>Name:</b> " + str(message.chat.first_name) +" " + str(message.chat.last_name) +"\n" + "<b>User id:</b> " + "<code>" +str(message.chat.id) + "</code>"  + "\n" + "<b>Message:</b> "+str(message.text) +"\n" + "<b>Date and Time:</b> " +str(utc_to_time(message.date))
  else: 
    tes ="@" + str(message.from_user.username)+"\n"+ "<b>Name:</b> " +  str(message.chat.first_name)  + " " + str(message.chat.last_name) +"\n" + "<b>User id:</b> " + "<code>" +str(message.chat.id) + "</code>"  + "\n" + "<b>Message:</b> "+str(message.text) +"\n" + "<b>Date and Time:</b> " +str(utc_to_time(message.date))
  g=requests.post(BOT_url+'/sendmessage'+'?text='+tes+'&parse_mode=html'+'&chat_id='+str(log_channel))
  print(tes)
  print(g)

@app.on_message(filters.photo & filters.private & ~filters.bot)
async def msg_photo(client: Client, message: Message):
  app.set_parse_mode()
  print('photo recived')
  pat='photo/'
  tgapi='/sendPhoto'
  if message.from_user.username  == myuserid:
    otherr="<b>From @</b>"+str(message.from_user.username)+" <b>to @</b>"
  else:
    otherr="@"
  await app.download_media(message,file_name=pat)
  await dirup(message,pat,tgapi,otherr)
@app.on_message(filters.video & filters.private & ~filters.bot)
async def msg_video(client: Client, message: Message):
  app.set_parse_mode()
  print('video recived')
  pat='video/'
  tgapi='/sendVideo'
  if message.video.file_size>50428800:
    await message.forward(log_channel)
  else:
    if message.from_user.username  == myuserid:
      otherr="<b>From @</b>"+str(message.from_user.username)+" <b>to @</b>"
    else:
      otherr="@"
    await app.download_media(message,file_name=pat)
    await dirup(message,pat,tgapi,otherr)
    
@app.on_message(filters.animation & filters.private & ~filters.bot)
async def msg_animation(client: Client, message: Message):
  app.set_parse_mode()
  print('animation recived')
  pat='animation/'
  tgapi='/sendAnimation'
  if message.animation.file_size>50428800:
    await message.forward(log_channel)
  else:
    if message.from_user.username  == myuserid:
      otherr="<b>From @</b>"+str(message.from_user.username)+" <b>to @</b>"
    else:
      otherr="@"
    await app.download_media(message,file_name=pat)
    await dirup(message,pat,tgapi,otherr)
    
@app.on_message(filters.audio & filters.private & ~filters.bot)
async def msg_audio(client: Client, message: Message):
  app.set_parse_mode()
  print('audio recived')
  pat='audio/'
  tgapi='/sendAudio'
  if message.from_user.username  == myuserid:
    otherr="<b>From @</b>"+str(message.from_user.username)+" <b>to @</b>"
  else:
    otherr="@"
  await app.download_media(message,file_name=pat)
  await dirup(message,pat,tgapi,otherr)
  
@app.on_message(filters.voice & filters.private & ~filters.bot)
async def msg_voice(client: Client, message: Message):
  print('voice recived')
  pat='voice/'
  tgapi='/sendVoice'
  if message.from_user.username  == myuserid:
    otherr="<b>From @</b>"+str(message.from_user.username)+" <b>to @</b>"
  else:
    otherr="@"
  await app.download_media(message,file_name=pat)
  await dirup(message,pat,tgapi,otherr)

@app.on_message(filters.media & filters.private & ~filters.bot & ~filters.photo & ~filters.video & ~filters.audio & ~filters.poll)
async def msg_document(client: Client, message: Message):
  app.set_parse_mode()
  print('document recived')
  pat='document/'
  tgapi='/sendDocument'
  if message.document.file_size>50428800:
    await message.forward(log_channel)
  else:
    if message.from_user.username  == myuserid:
      otherr="<b>From @</b>"+str(message.from_user.username)+" <b>to @</b>"
    else:
      otherr="@"
    await app.download_media(message,file_name=pat)
    await dirup(message,pat,tgapi,otherr)


print('bot started')
app.set_parse_mode()
app.run()



