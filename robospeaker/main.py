import pyttsx3

engine = pyttsx3.init()

while True:
    x = input("Enter string: ")

    if(x=="exit"):
        break
    else:
        engine.say(x)
        engine.runAndWait()
