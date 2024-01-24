import speech_recognition as sr
from googletrans import Translator

def translate_text(text, dest_language):
    translator = Translator()
    result = translator.translate(text, dest=dest_language)
    return result.text
translator =Translator()


# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# Reading Microphone as source
# listening the speech and store in audio_text variable

with sr.Microphone() as source:
    print("Talk")
    audio_text = r.listen(source)
    print("Time over, thanks")
    # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling

    print("Text_Italian: "+r.recognize_google(audio_text, language="it-IT"))

    translation = translator.translate(r.recognize_google(audio_text, language="it-IT"), src='it', dest='en')

    print("Text_English: ", translation.text)

