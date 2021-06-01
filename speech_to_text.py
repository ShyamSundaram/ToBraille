import speech_recognition as sr

def get_speech_text():
    r=sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=2)
        print("Speak..")
        audio=r.listen(source)
        text=r.recognize_google(audio)
        return(format(text).lower())