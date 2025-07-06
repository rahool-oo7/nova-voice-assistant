import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say the name...")
    audio = r.listen(source)

print("You said:", r.recognize_google(audio))
