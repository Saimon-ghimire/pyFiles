#!/usr/bin/env python3
import webbrowser
import speech_recognition as sr

r = sr.Recognizer()


def voiceInput():
    with sr.Microphone() as source2:

        print("Speak")

        # listens for the user's input
        audio2 = r.listen(source2)

        try:
            # Using ggogle to recognize audio
            MyText = r.recognize_google(audio2)
            key = MyText.lower()
            print(key, "joining...")
            return(key)
        except:
            print("Couldn't hear")


idInfo = {
    'key': ('PMI', "password", "link")
}


mode = input("Enter to voice")
if mode == "":
    key=voiceInput()
else:
    key = input("Name: ")

pin = idInfo[key][0]
passs = idInfo[key][1]
#pin pass not used..... joining from urls
url = idInfokey][2]
webbrowser.open(url)
