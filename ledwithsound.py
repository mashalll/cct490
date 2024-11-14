from gpiozero import LED
from time import sleep
from pydub import AudioSegment
from pydub.playback import play

red = LED(2)
red.off()

aud = AudioSegment.from_file("/home/group7/Downloads/cct490/audio1.wav")
aud -= 20

red.on()

play(audio)
red.off()
