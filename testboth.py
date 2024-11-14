import speech_recognition as sr
import pygame

pygame.mixer.init()
pygame.mixer.music.load("audio1.wav")

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak now...")
    recognizer.adjust_for_ambient_noise(source)

    try:
        audio = recognizer.listen(source, timeout=10, phrase_time_limit=10)
        print("Now recognizing.")
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")

    except sr.UnknownValueError:
        print("Couldn't understand")
    except sr.RequestError as e:
        print(f"SR error: {e}")

if text == "play music":
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
