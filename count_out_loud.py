
import speech_recognition as sr

def prompt_child():
    print("Please count out loud from 1 to 5.")

def listen_to_counting():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... Speak now.")
        audio = recognizer.listen(source, phrase_time_limit=5)

    try:
        result = recognizer.recognize_google(audio)
        print(f"You said: {result}")
        return result.lower()
    except sr.UnknownValueError:
        print("Could not understand audio.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return ""

def check_counting(response):
    expected_numbers = ["1", "2", "3", "4", "5"]
    spoken_words = response.replace(",", "").split()
    matched = [word for word in spoken_words if word in expected_numbers]

    print(f"Numbers detected: {matched}")
    if len(matched) >= 3:
        print("✅ Good job! You counted correctly.")
    else:
        print("❌ Try again, say the numbers clearly.")

def count_out_loud():
    prompt_child()
    response = listen_to_counting()
    if response:
        check_counting(response)
