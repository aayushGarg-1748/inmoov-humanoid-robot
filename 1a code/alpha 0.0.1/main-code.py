#speaking
import pyttsx3
#speech conversion
import speech_recognition as sr
#searching
import wikipedia
#date and time
import datetime
from datetime import datetime
#os commands
import os
#web
import webbrowser
#system
import sys
#json
import json
#firebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

cred = credentials.Certificate('cyborg-c343f-firebase-adminsdk-23k57-8ea068b4b7.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

authoriation = False;
admin_authoriation = False;

engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    print(f"i said: {audio}\n")
    engine.runAndWait()

'''
def resgister():
#speak("commencing user registration process")
#while True:
#    speak("please say your username!")
#    usrnm = takeCommand().lower()
#    doc_ref = db.collection('credentials').document(usrnm)
#    speak("please speak your password")
#    password = takeCommand().lower()
#    speak("did you say"+ password)
#    op = takeCommand().lower()
#
#    if 'yes' in op:
#        while True:
#            try:
#                doc_ref.set({
#                'username':usrnm,
#                'password':password
#                })
#                speak("registration succesfull")
#                return True
#                break
#            except:
#                speak("registration failed")
#
#    if 'no' in op:
#        return False
#        break
 '''
 
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print ("listening")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recognizing")
        query = r.recognize_google(audio, language='en-in')
        print(f"you said: {query}\n")

    except Exception as e:
        print(" sorry try saying it again")
        return "None"
    return query    

def adminAuth():
    speak("commencing admin login process")
    speak("please say your username!")
    usrnm = takeCommand().lower()
    
    doc_ref = db.collection('credentials').document(usrnm)
    doc = doc_ref.get()
    #speak("did you say"+ usrnm)

    speak("please speak your password")
    passwor = takeCommand().lower()
    speak("is your username "+usrnm + " and your password "+ passwor)
    op = takeCommand().lower()

    if 'yes' in op:
        if doc.exists:
            document = format(doc.to_dict())
            obj = eval(document)
            admin = obj.get("admin")
            passwr = obj.get("password")

            if(passwr == passwor):
                speak("login successful")
                
                if (admin == True):
                    speak("admin-authoriation sucessful")
                    print("admin-auth successful")
                    return True
                
                else: 
                    speak("you don't have admin privilages")
                    speak("logged-in as standard user")
                    return False
            
            else:
                ("no user found")
                return False

        else:
            print('No such document!')
            return False

    if 'no' in op:
        speak("you canceled the operation")
        return False;

def LogIn():
    speak("commencing user login process")
    speak("please say your username!")
    usrnm = takeCommand().lower()
    
    doc_ref = db.collection('credentials').document(usrnm)
    doc = doc_ref.get()
    #speak("did you say"+ usrnm)

    speak("please speak your password")
    passwor = takeCommand().lower()
    speak("is your username "+usrnm + " and your password "+ passwor)
    op = takeCommand().lower()

    if 'yes' in op:
        if doc.exists:
            document = format(doc.to_dict())
            obj = eval(document)
            passwr = obj.get("password")
            print(passwr)
            if(passwr == passwor):
                print("login successful")
                speak("login successful")
                return True

        else:
            print('No such document!')
            return False
    if 'no' in op:
        
        return False
'''
#def get_custom_class():
#   
#   doc_ref = db.collection(u'cities').document(u'BJ')
#
#   doc = doc_ref.get()
#   city = City.from_dict(doc.to_dict())
#   print(city)
#      
'''

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()

        if "start admin authorisation process" in query:
            if(adminAuth() == True):
                authorization = True;
                admin_authoriation = True;
        if 'login user' in query:
            if(LogIn() == True):
                authorization = True;

        if 'current time' in query:
            if (int(datetime.today().strftime('%H')) < 12):
                
                speak(str(datetime.today().strftime('%H:%M'))+ "am")

            else:
                speak(str(datetime.today().strftime('%H:%M'))+ "pm")
        
        elif 'current date' in query:

            speak("currentdate is " + str(datetime.today().strftime('%Y-%m-%d')))
        
        elif 'search wikipedia for me' in query:
            speak('what to search?')
            search = takeCommand();
            try:
                results = wikipedia.summary(search, sentences=3)
                speak("according to wiki!" + results)
                #print("according to wiki!" + results)
            
            except Exception as e:
                speak("error occured")

        elif 'search wiki for me' in query:
            speak('what to search?')
            search = takeCommand();
            try:
                results = wikipedia.summary(search, sentences=3)
                speak("according to wiki!" + results)
                #print("according to wiki!" + results)
            
            except Exception as e:
                speak("error occured")

        elif 'wikipedia' in query:
            speak('searching wiki for you')
            query = query.replace("wikipedia" , "")
            try:
                results = wikipedia.summary(query, sentences=3)
                speak("according to wiki!" + results)
                #print("according to wiki!" + results)
            
            except Exception as e:
                speak("error occured")

        elif 'shutdown' in query:

            speak ('i will shut down killing he pogram after this, do you want to continue...?')
            print("speak your decision")
            
            decision = takeCommand();

            print(decision)
            if 'yes' in decision:
                
                try:
                    break # this always raises SystemExit
                
                except:
                    print("Something went horribly wrong") # some other exception got raised

            
            else:
                continue

        elif 'quit' in query:

            speak ('i will shut down killing he pogram after this, do you want to continue...?')
            print("speak your decision")
            
            decision = takeCommand();

            print(decision)
            if 'yes' in decision:
                
                try:
                    break # this always raises SystemExit
                
                except:
                    print("Something went horribly wrong") # some other exception got raised

            
            else:
                continue
        
        elif 'freeze all motor control' in query:
            print('freezing all motor functions')
            rest();
            freezed();
            
