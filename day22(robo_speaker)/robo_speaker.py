import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")
while True:
    text=input("Type to Say : ")
    if text.lower() in ("exit","quit","q"):
        print("Goodbye")
        print("Robo Speaker Exiting........")
        break
    else:
       speaker.speak(text)