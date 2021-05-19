import pyttsx3
tts = pyttsx3.init()
words = input("Say your text:  ")
tts.say(words)
tts.setProperty('rate', 10)
tts.runAndWait()
quit()