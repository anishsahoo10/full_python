import pyttsx3

while True:
    x = input("Enter string: ")

    if x.lower() == "exit":
        break

    engine = pyttsx3.init()
    engine.say(x)
    engine.runAndWait()
    engine.stop()
