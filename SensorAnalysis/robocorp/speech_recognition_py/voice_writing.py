import speech_recognition as sr


def speech_to_text():
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Capture audio from the microphone
    with sr.Microphone() as source:
        print("Say something:")
        audio = recognizer.listen(source)

    try:
        # Use Google Speech Recognition to convert audio to text
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
        return None
    except sr.RequestError as e:
        print(
            f"Could not request results from Google Speech Recognition service; {e}")
        return None


def write_to_file(text, filename="output.txt"):
    with open(filename, "w") as file:
        file.write(text)
    print(f"Text written to {filename}")


if __name__ == "__main__":
    recognized_text = speech_to_text()
    if recognized_text:
        write_to_file(recognized_text)
        print("That's the voice text: " + recognized_text )
