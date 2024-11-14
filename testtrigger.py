import speech_recognition as sr

recognizer = sr.Recognizer()

def listen_for_trigger():
    print("Listening for trigger word...")

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        while True:
            try:
                print("Say something...")
                audio = recognizer.listen(source)

                text = recognizer.recognize_google(audio).lower()
                print(f"Recognized: {text}")

                if "hello" in text:
                    print("Trigger word detected! Listening for a command...")
                    listen_for_command()
                    break
            except sr.UnknownValueError:
                print("Sorry, I could not understand the audio.")
            except sr.RequestError as e:
                print(f"Sorry, there was an error with the speech recognition service: {e}")


def listen_for_command():
    print("Now, please say a command.")
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio).lower()
            print(f"You said: {text}")

            if "play music" in text:
                print("Playing music...")
                # add music code
            elif "stop" in text:
                print("Stopping.")
            else:
                print("Command not recognized.")
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            print(f"SR error: {e}")


listen_for_trigger()

