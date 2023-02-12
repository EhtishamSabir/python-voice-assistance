import pyttsx3 #pip install pyttsx3 ---> convert text data to speech
import datetime
import speech_recognition as sr # pip install SpeechRecognition --> convert speech to text
import smtplib
from secrets import senderemail, epwd, to
from email.message import EmailMessage
import pyautogui # pip install pyautogui
import webbrowser as wb
from time import sleep
import wikipedia 
from nltk.tokenize import word_tokenize # pip install nltk
import pywhatkit #pip install pywhatkit
import requests
from newsapi import NewsApiClient #pip install newsapi, #pip install newsapi-python
import clipboard #pip install clipboard
import pyjokes #pip install pyjokes
import time as tt
import string
import random


engine = pyttsx3.init()

def speak(audio):
  engine.say(audio)
  engine.runAndWait()

def getvoices(voice):
  voices = engine.getProperty('voices')
  # print(voices[1].id)
  if voice == 1:
    engine.setProperty('voice', voices[0].id)
    speak("hello this is Veetek")
  if voice == 2:
    engine.setProperty('voice', voices[1].id)
    speak("hello this is Natasha")
  

def time():
  Time = datetime.datetime.now().strftime("%I:%M:%S") #format time ---> hour = I, minutes = M, seconds = S
  speak("the current time is:")
  speak(Time)

def date():
  year = int(datetime.datetime.now().year)
  month = int(datetime.datetime.now().month)
  date = int(datetime.datetime.now().day)
  speak("the current date is: ")
  speak(date)
  speak(month)
  speak(year)

def greeting():
  hour = datetime.datetime.now().hour
  if hour >= 6 and hour <12:
    speak("good morning love!")
  elif hour >= 12 and hour <18:
    speak("good afternoon my darling!")
  elif hour >= 18 and hour <24:
    speak("good evening sweetheart!")
  else:
    speak("good night my dear!")


def wishme():
  speak("Welcome back love!")
  # time()
  # date()
  greeting()
  speak("Veetek at your service, please tell me how can I help you?")

# while True:
#   voice = int(input("Press 1 for voice version 1\nPress 2 or voice version 2\n"))
# #   speak(audio)
#   getvoices(voice)

# wishme()

def takeCommandCMD():
  query = input("Please tell me how can I help you?")
  return query

def takeCommandMic():
  r = sr.Recognizer()
  with sr.Microphone() as source:
    print("Listening...")
    r.pause_threshold = 1
    audio = r.listen(source)
  try:
    print("Recognizing...")
    query = r.recognize_google(audio, language='en-GB')
    print(query)
  except Exception as e:
    print(e)
    speak("Could you please repeat what you just said for me?")
    return "None"
  return query

def sendEmail(receiver, subject, content):
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.starttls()
  server.login(senderemail, epwd)
  email = EmailMessage()
  email['From'] = senderemail
  email['To'] = receiver
  email['Subject'] = subject
  email.set_content(content)
  server.send_message(email)
  server.close()

def sendwhatsmsg(phone_no, message):
  Message = message
  wb.open('https://web.whatsapp.com/send?phone='+phone_no+'&text='+Message)
  sleep(10)
  pyautogui.press('enter')

def searchgoogle():
  speak('what should i search for?')
  search = takeCommandMic()
  wb.open('https://www.google.com/search?q='+search)

def news():
  newsapi = NewsApiClient(api_key='a431c88a88654454a7500dbcb0cbb7ac')
  speak('what topic would you like to hear?')
  topic = takeCommandMic()
  data = newsapi.get_top_headlines(q=topic,
                                  language='en',
                                  page_size=5)
  newsdata = data['articles']
  for x,y in enumerate(newsdata):
    #provide top 5 news
    print(f'{x}{y["description"]}')
    speak((f'{x}{y["description"]}'))
  
  speak("that's it for now I will update you later")

def text2speech():
  #will speak the text that is being highlighted and copied
  text = clipboard.paste()
  print(text)
  speak(text)

def covid():
  r = requests.get('https://coronavirus-19-api.herokuapp.com/all')

  data = r.json()
  covid_data = f'Confirmed cases : {data["cases"]} \n Deaths  :{data["deaths"]} \n Recovered {data["recovered"]}'
  print(covid_data)
  speak(covid_data)

def screenshot():
  name_img = tt.time() #store the name of the image in a form of datetime
  name_img = f'C:\\Users\\ak\\Downloads\\JARVUS 2.0\\screenshot\\{name_img}.png'
  img = pyautogui.screenshot(name_img)
  img.show()  #open image

def passwordgen():
  s1 = string.ascii_lowercase
  s2 = string.ascii_lowercase
  s3 = string.digits
  s4 = string.punctuation

  passlen = 8
  s = []
  s.extend(list(s1))
  s.extend(list(s2))
  s.extend(list(s3))
  s.extend(list(s4))

  random.shuffle(s)
  newpass = ("".join(s[0:passlen]))
  print(newpass)
  speak(newpass)



if __name__ == "__main__":
  getvoices(1)
  # wishme()
  wakeword = "veetek"
  while True:
    query = takeCommandMic().lower()
    query = word_tokenize(query)
    print(query)
    if wakeword in query: 
      if 'time' in query:
        time()

      elif 'date' in query:
        date()

      elif 'email' in query:
        email_list = {
          'testemail': 'slkfjslkgj@kiabws.com' #create in 10minutemail
        }
        try:
          speak('To whom you want to send the email?')
          name = takeCommandMic()
          receiver = email_list[name]
          speak("what is the subject of the email?")
          subject = takeCommandMic()
          speak('what should I say?')
          content = takeCommandMic()
          sendEmail(receiver, subject, content)
          speak("email has been sent")
        except Exception as e:
          print(e)
          speak("unable to send the email")
      elif 'message' in query:
        user_name = {
          'Jarvis': '+44 5958686869' #add whatsapp phone number with country code
        }
        try:
          speak('To whom you want to send the whatsapp message?')
          name = takeCommandMic()
          phone_no = user_name[name]
          speak("what is the message?")
          message = takeCommandMic()
          sendwhatsmsg(phone_no, message)
          speak("message has been sent")
        except Exception as e:
          print(e)
          speak("unable to send the message")
      elif 'wikipedia' in query:
        speak('searching on wikipedia...')
        query = query.replace("wikipedia", "")
        result = wikipedia.summary(query, sentences = 2)
        print(result)
        speak(result)
      elif 'search' in query:
        searchgoogle()
      elif 'youtube' in query:
        speak("what should i search for on youtube?")
        topic = takeCommandMic
        pywhatkit.playonyt(topic) #open video first result in the search
      elif 'weather' in query:
        city = 'California'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid=b57e90af4835ac43eafaa77441c166df'

        res = requests.get(url)
        data = res.json()

        weather = data['weather'][0]['main']
        temp = data['main']['temp']
        desp = data['weather'][0]['description']
        temp = round((temp - 32) * 5/9)
        print(weather)
        print(temp)
        print(desp)
        speak(f'the weather in {city} city')
        speak('Temperature : {} degree celcius'.format(temp))
        speak('weather is {}'.format(desp))
      elif 'news' in query:
        news()
      elif 'read' in query:
        text2speech()
      elif 'covid' in query:
        covid()
      elif 'joke' in query:
        speak(pyjokes.get_joke())
      elif 'screenshot' in query:
        screenshot()
      elif 'remember that' in query:
        speak("what should i remember?")
        data = takeCommandMic()
        speak("you told me to remember that "+data)
        remember = open('data.txt','w')
        remember.write(data)
        remember.close()
      elif 'do you know anything' in query:
        remember = open('data.txt','r')
        speak("you told me to remember that "+remember.read())
      elif 'password' in query:
        passwordgen()
      elif 'close' in query:
        quit()


#takeCommandMic == "hey veetek what is the date today" ----> tokenize = ['hey', 'veetek', 'what', 'is', 'the', 'date', 'today']

#http://api.openweathermap.org/data/2.5/weather?q={City Name}&units=imperial&appid={API KEY HERE}

#http://api.openweathermap.org/data/2.5/weather?q=Bangkok&units=imperial&appid=b57e90af4835ac43eafaa77441c166df

