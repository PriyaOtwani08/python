import pyttsx3
text_speech =pyttsx3.init()
answer=input("what uh want to convert")
text_speech.say(answer)
text_speech.runAndWait()
