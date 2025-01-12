import speech_recognition as sr    
import pyttsx3                     
import datetime                    
import pyjokes                     
import wikipedia                   
import pywhatkit                   
import smtplib as s               
import os                          


from collection import myClass


listener = sr.Recognizer()
engine = pyttsx3.init()             
voices = engine.getProperty('voices')       

def speak(text):
    engine.say(text)
    engine.setProperty('voice', voices[0].id)      
    engine.runAndWait()                            

tt = datetime.datetime.now()     


#Conditions for greetings
if(tt.hour<12):
    speak('Good Morning, Im Alexa')
elif(tt.hour>12 and tt.hour<18):
    speak('Good Afternoon, Im Alexa')      
else: 
    speak('Good Evening, Im Alexa')


#Function use to take audio
def take(): 
    with sr.Microphone() as source:
        speak('listening')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)      
        command = command.lower()                       
        return command


#Function to continue asking
def conti(n):

    if(n>0):
        speak('Do you want to continue')
        command3=take()        
        print(command3)
        if 'yes' in command3:      
                print(command3)
                fn(2)
        elif 'no' in command3:      
                speak('Thank you')
                os.close()         
        else:
                speak("Please repeat")
                conti(n-1)
    else:
        speak("couldn't found")

def fn(n):  
    
    if(n>0):
    
        speak('How can i help you')
        com =take()
        print(com)

        if 'health' in com:
            opp = myClass()
            tan = opp.fun()
            print(tan)
            speak(tan)
                           
        elif 'time' in com:
            time = datetime.datetime.now().strftime('%I:%M %p')     
            speak('Current time is ' + time)
            speak('Thank you')
                                
        elif 'play music' in com:
            song = com.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)       
            speak('Thank you')
                
        elif 'wikipedia' in com:
            person = com.replace('who is', '')
            info = wikipedia.summary(person,2)      
            print(info)
            speak(info)   
            speak('Thank you')
                                
        elif 'joke' in com:
            speak(pyjokes.get_joke())       
            speak('Thank you')

        elif 'mail' in com:
            ob=s.SMTP('smtp.gmail.com',587)   
            ob.starttls()                      
            with open('mail.txt','r') as f:     
                password=f.read()             
            ob.login('they55446@gmail.com',password)
            speak('Please tell the subject')
            subject=take()                     
            print(subject)
            speak('please tell the body')
            body=take()                     
            print(body)
            message="Subject:{}\n\n{}".format(subject,body)    
            
            listofaddress=[]               

            while(True):
                speak('name of the person')
                person=take()            
                print(person)
                if 'at' in person:
                    sendperson = person.replace(' at the rate 'or' at ', '@')     
                    print(sendperson) 
                def remove(string):                         
                    return "".join(string.split(" "))       
                sendperson2=remove(sendperson)
                print(sendperson2)
                listofaddress.append(sendperson2)           
                speak("Want to send this to someone else")
                someoneelse=take()
                if 'yes' in someoneelse:    
                    print(someoneelse)
                    continue
                elif 'no' in someoneelse:   
                    print(someoneelse)
                    break
                break                      

            ob.sendmail('they55446@gmail.com',listofaddress,message)   
            speak('send successfully')
            print('send successfully')
            speak('Thank you')
            ob.quit()                          
            
        else:
            speak('Please try again.')
            fn(n-1)

    else:
        speak("couldn't found")
        os.close()

    conti(2)    
fn(2)           