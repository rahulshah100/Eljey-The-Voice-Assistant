import pyttsx3  #text-to-speech converting lib;works offline,is compatible with both Python 2 & 3. #pip install commands were used to install this libraries
import speech_recognition as sr #SpeechRecognizing lib to tap what user says to recognize it
import datetime #for providing starting wish as per contemporary timing
import webbrowser   #for opening up sited
import wikipedia    #for wiki's functionality
import os           #to access music file
import random       #to generate a random song number
import smtplib      #for sending mail
import time         #to pause program

from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox as tmsg
import os

root=Tk()

root.geometry("325x380")
root.minsize(300,350)
root.maxsize(400,400)
root.title("Eljey - The ChatBot")

root.configure(background='lightgrey')

my_var=Label(text="--- Welcome to ELjey App ---",bg ="green", fg="black", padx=5, pady=4, font="comicsansms 10 italic", borderwidth=5, relief=GROOVE)
my_var.pack()

myimageVar=Image.open("chatbotimg.jpg")
photto=ImageTk.PhotoImage(myimageVar)
Label(image=photto).pack()

def consolemessage(message):
    f1=Frame(root,bg="grey",padx=73,borderwidth=5,pady=5)
    f1.pack(side=LEFT,anchor='sw')
    Label(f1,text=f"{message}",borderwidth=4,relief=GROOVE,padx=100,pady=10).pack()

root.iconbitmap(r"C:\\Users\\Bhavin\\Desktop\\de\\titimg.ico")

# --------------------------------------------------------------------------------------
def rate():
    value = tmsg.askquestion("Rates", "You used this gui.. Was your experience Good?")
    if value == "yes":
        msg = "Great U enjoyed"
    else:
        msg = "Tell us what went wrong by mailing us at rktempacc@gmail.com"
    tmsg.showinfo("Experience", msg)

def contrfunc():
    tmsg.showwarning('Message','You can support to this open source project by contributing to it.For contributing check how to Reach us menu from File->Reach Us')

def reachus():
    value=tmsg.askquestion('Reach To Us',"We only want serious contributors who could add value to our Project !\nDo you think you have that perseverance ?")
    if value=="yes":
        tmsg.showerror("Disclaimer",'Okay ,to contibute \nHere ~ you can fork your improvement in our project at out git handle :https://github.com/rahulshah100/Eljey-The-Voice-Assistant')
    elif value=="no":
        tmsg.showerror("Disclaimer","Sorry,this is a Serious open source porject if u lack perseverance we cant accept your contributions")

def contactfunc():
    tmsg.showinfo("Our Mail Id","Contact us on :rktempacc00@gmail.com ")

def helpfunc():
    tmsg.showinfo("Help", "To find the intricate details of this open source program ,kindly visit this github handle:https://github.com/rahulshah100/Eljey-The-Voice-Assistant")

mainmenu = Menu(root)

m1 = Menu(mainmenu, tearoff=0)                  #
m1.add_command(label="Rate Us", command=rate)
m1.add_command(label="Contribute?", command=contrfunc)
m1.add_separator()              #this is responsible for drawing off a continuous line in menu's dropdown
m1.add_command(label="Reach Us", command=reachus)
m1.add_command(label="Our Contact", command=contactfunc)
mainmenu.add_cascade(label="File", menu=m1) #This adds the name to this tab i.e. this complete menu

mainmenu.add_command(label="Help", command=helpfunc)    #

mainmenu.add_command(label="Exit", command=quit) #

root.config(menu=mainmenu)

#--------------------------------------------------------------------------------------------------------------------

engine = pyttsx3.init('sapi5')  #sapi5 is Microsoft provided api for speech recognition #makes an instant of engine which can access driver(a driver is a software component that lets the operating system and a device communicate with each other)
voices = engine.getProperty('voices')   #provides voices with two voice in an array form
# print(voices) #will show all available voice i.e. data in variable voicess
engine.setProperty('voice', voices[1].id)   #out of above discussed array form we're selecting one voice by specifying it by its indexNumber in voices
# engine's used just to speak, not for accessing mic or recognition the voice

def speak(audio):
    '''function to make system speak ! It will be called at all instance where somthing wouldve to be spoken'''
    engine.say(audio)
    engine.runAndWait() #blocks executions of further commands till processing all currently queud commands.If we didnt use this command then what happened was after just encountering engine.say() interpreter ran suddenly to next lines and we'll not get our starting greets of our bot wishing hello and things+++


def wishMe():
    '''for wishing user a greet just at starting of program'''
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Hey Good Morning!")
    elif hour>=12 and hour<18:
        speak("Yo Good Afternoon!")
    else:
        speak("Hello Good Evening!")
    speak("I am Eljey Sire. Please tell me how may I help you  ??")


def takeCommand():
    '''deals with taping voice recognizing it and showing it on console as text'''
    '''below line takes user commands from microphone and converts it into string'''
    r: Recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        '''lISTENING AND FETCHING AUDIO'''
        print("Listening...")
        consolemessage("Listening")
        r.pause_threshold = 0.6   #Ctrl+click on pause_thres.. to find its functionality .It basically considers tht for how long if user dont speak then to consider phrase as complete
        audio = r.listen(source)    #this gets audio with AudioData

    try:
        '''CONVERTS AUDIO DATA INTO TEXT'''
        print("Recognizing...")
        consolemessage("Recognizing")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        '''iN CASE OF RECOGNIZATION FAILURE'''
        print("Say that again please...")
        consolemessage("Say that again please")
        return "None"
    return query


def wikifunc(query):
    try:
        speak('Searching for Wikipedia...')
        # query=query.replace("wikipedia","")
        results = wikipedia.summary(query, sentences=1)
        speak("So According to Wikipedia")
        print(results)
        speak(results)
    except:
        speak("Sorry")
        print("Unable to Fetch the wiki result for", query)
        speak("Can U try saying that again")


def websearch(query):
    site = query.split('website', maxsplit=1)[-1] \
        .split(maxsplit=1)[0]  # Gets a word after website ,which word would be name of the site
    webbrowser.open(f'{site}.com')


def playmemusic():
    music_dir = 'C:\\Users\\Bhavin\\Desktop\\de\\music'
    songs = os.listdir(music_dir)  # returns to songs a list of all music files within music_dir location
    # print(songs)
    song_num = random.randint(0, len(songs) - 1)
    os.startfile(os.path.join(music_dir, songs[
        song_num]))  # after selecting a random sequence number of song further tht index from songs list is selected ,that name is appended at end of music_dir & tht file is further ran by os.startfile


def getmetime():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    # print(type(strTime),strTime)
    speak(f"Yo Sir, the time is {strTime}")
    print(f"{strTime}")


def openapp(query):
    appname = query.split('application', maxsplit=1)[-1] \
        .split(maxsplit=1)[0]
    if appname=='notepad':
        os.startfile("C:\\Users\\Bhavin\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad")
    elif appname=='notes':
        os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2013\\OneNote 2013.lnk")
    else:
        speak(f"Sorry ,{appname} is not accessible right now")


def emailSendingMainFunc(query):
    recipientName = query.split('send email to', maxsplit=1)[-1] \
        .split(maxsplit=1)[0]  # Gets user name which would be the word spoken after saying 'send email to'
    try:
    # 1-fetching data
        if recipientName=='rupal':
            to = "rupalshah053@gmail.com"
        elif recipientName=='rahul':
            to="rahulkshah00@gmail.com"
        else:
            to=recipientName
        speak("What should I say?")
        content = takeCommand()  # calls our recognizer function and further returns to content what we will say
    # 2-sending Email
        sendEmail(to, content)
    # 3-Confirmation
        speak("Email has been sent successfully !")
    except Exception as e:
        print(e)
        consolemessage("Sorry master ,Email Sending Failure")
        speak("Sorry master ,Email Sending Failure")

def sendEmail(to, content):
    #Here we'll use gmail server to send the mails .But here as we're not directly using gmail app to access its server but a 3rd party app which further probes the gmail severs hence we'll need to turn off a safety feature for allowing less secure apps for our google account so to send emails via this program.To do so we'd have to go to our google account from which we'll send this emails further into security section there and turn allow less secure apps on
    server = smtplib.SMTP('smtp.gmail.com', 587)    #587 is port number
    server.ehlo()
    server.starttls()
    server.login('rktempacc00@gmail.com', 'pass@gmail00')   #(gmai_id,password)
    server.sendmail('rktempacc00@gmail.com', to, content)
    server.close()


def pausefunc():
    speak("Pausing execution")
    print("Execution Paused")
    consolemessage("Execution Paused")
    # time.sleep(10)

    print("Resuming")
    speak("Services Resumed")


def quitfunc():
    speak("Quiting !")
    quit("Quiting !")


if __name__ == "__main__":
    speak("----------")       #just to get rid of starting latencies
    wishMe()
    while True:      #To keep this program perpetually runing
        query = takeCommand().lower()
                    #to synch what we say with the conditions below in which they should be executed we have ensured all chars in lowercase

        #now after getting query we could search on basis of it whether user has asked for following functionality
        if 'wikipedia' in query:
            '''Wikipedia search functionality'''
            wikifunc(query)

        elif 'open website' in query:
            '''Open websites(any)'''
            websearch(query)

        elif 'play music' in query:
            '''plays random music'''
            playmemusic()

        elif 'the time' in query:
            '''says current time'''
            getmetime()

        elif 'open application' in query:
            '''opens up applications'''
            openapp(query)

        elif 'email to' in query:
            '''sends email to a destined user only'''
            emailSendingMainFunc(query)

        elif 'pause' in query:
            '''pause the execution for while.This was needed as otherwise if no i/p is given for sometime automaticall the deafult case(below) is ran with i/p None and again listening cycle starts'''
            pausefunc()

        elif 'quit' in query:
            '''quit exectuion of program'''
            quitfunc()

        else:
            '''default case'''
            speak(f"Sorry currently we dont have any functionality regarding ,{query}")
#--------------------------------------------------------------------------------------------------------------------
root.mainloop()