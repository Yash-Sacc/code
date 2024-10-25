import speech_recognition as sr
import webbrowser
from win32com.client import Dispatch
import os
from AppOpener import open

speak = Dispatch("SAPI.SpVoice").Speak

def say(text):
    speak(text)

musicPath = 'C:\\Users\\hp\\OneDrive\\Desktop\\Way down music.mp3'

say("Hi I am Jarvis")

def takeCommand(): # Speech recognition function
    r = sr.Recognizer()

    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            print("JARVIS--> recognizing")
            say("recognizing")
            q = r.recognize_google(audio,language="en-in")
            return q 
        except Exception as e:
            return "Speech recognition failed. Try again"


keyword_url_mapping = {
        "youtube": "https://www.youtube.com",
        "google": "https://www.google.com",
        "github": "https://www.github.com",
        "chat": "https://www.chatgpt.com"
    }
def open_website_by_keyword(keyword): # Site managing function by chatGPT
    # Check if the keyword exists in the dictionary
    if keyword in keyword_url_mapping:
        url = keyword_url_mapping[keyword]
        try:
            webbrowser.open(url, new=2)  # 'new=2' opens the URL in a new tab, if possible
            print(f"JARVIS--> Opening {url} with keyword {keyword} in browser.")
            say(f"Opening {keyword}")
        except webbrowser.Error as e:
            print(f"JARVIS--> Failed to open {url}. Error: {e}")
            say(f"Failed to open {keyword}")

while True:
    print("JARVIS--> listening...")
    say("listening")
    text = takeCommand().lower()

    print("YOU--> ",text)

    # if text == "Speech recognition failed. Try again.":
    #  say(text)

    if "stop" in text:
        break
    elif 'exit' in text:
        break
    elif 'pause' in text:
        break
    elif 'close' in text:
        break
    elif 'end' in text:
        break
    elif 'shutdown' in text:
        break

    for site in keyword_url_mapping:
        if site in text.lower():
            keyword = site
            open_website_by_keyword(keyword)

    if "music" in text:
        print("JARVIS--> Music started")
        say("Music in on")
        os.startfile(musicPath)
    elif "coding setup" in text:
        webbrowser.open_new('https://www.youtube.com/playlist?list=PLu0W_9lII9agq5TrH9XLIKQvv0iaF2X3w')
        webbrowser.open_new_tab("http://server:3000")
        webbrowser.open_new_tab("https://chatgpt.com/")
        open("VISUAL STUDIO CODE, WHATSAPP", match_closest=True)
        os.startfile(musicPath)
        print("JARVIS--> opened coding setup")
        say("opening coding setup!")
    elif "school setup" in text:
        webbrowser.open_new('https://www.thelocal.dk/category/denmark-news')
        webbrowser.open_new('https://www.danishclass101.com/lesson-library/level-1-danish')
        webbrowser.open_new_tab("https://www.dinordbok.no/en/danish-english/")
        webbrowser.open_new_tab("https://translate.google.com/?sl=da&tl=en&op=translate")
        open("WHATSAPP", match_closest=True)
        print("JARVIS--> opened danish setup")
        say("opening danish setup!")
    elif "hi" in text:
        print("JARVIS--> Hi there! I am jarvis, please say something to perform tasks")
        say("Hi there! I am jarvis, please say something to perform tasks")
    elif "hi jarvis" in text:
        print("JARVIS--> Hi there! I am jarvis, please say something to perform tasks")
        say("Hi there! I am jarvis, please say something to perform tasks")
    elif "are you there" in text:
        say("JARVIS--> Yes I am there")
    elif "nice jarvis" in text:
        print("JARVIS--> Oh yes! Thanks from me")
        say("Oh yes! Thanks from me")
    elif "search" in text:
        webbrowser.open_new(text)
    elif "www" in text:
        print('JARVIS--> ',text)
        say("opening a site")
        webbrowser.open_new(text)


say("Bye!. chat end")











