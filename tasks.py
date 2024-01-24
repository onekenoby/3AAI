from robocorp.tasks import task
import speech_recognition as sr
from googletrans import Translator
from robocorp import browser
import time
from RPA.Browser.Selenium import Selenium


"""
Steps:
1. Run the Python Speech Recognition function
2. Open browser and go to http://localhost:8084
3. Paste the generated text
4. Click on "Submit"
"""

@task
def vanna_demo():
    open_browser()
    speech_to_text = speech_to_text_translator()
    time.sleep(2)
    paste_text(speech_to_text)
    submit()
    time.sleep(60)

def speech_to_text_translator():
    translator = Translator()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Talk")
        audio_text = r.listen(source)
        print("Time over, thanks")
        # Assuming the recognition is in Italian and needs to be translated to English
        text_italian = r.recognize_google(audio_text, language="it-IT")
        print("Text_Italian: " + text_italian)
        translation = translator.translate(text_italian, src='it', dest='en')
        print("Text_English: ", translation.text)
        return translation.text

def open_browser():
    browser.goto("http://localhost:8084")

def paste_text(text):
    page = browser.page()
    page.fill('input[placeholder="Ask me a question about your data that I can turn into SQL."]', text)

def submit():
    page = browser.page()
    page.click('xpath=/html/body/div/main/div[2]/footer/div[2]/div/div/div[2]/button')

# Entry point for the robot
if __name__ == "__main__":
    vanna_demo()