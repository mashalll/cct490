from pydub import AudioSegment
from pydub.playback import play

aud = AudioSegment.from_file("/home/group7/Downloads/cct490/audio1.wav")
aud -= 20 # lowers volume
play(aud)
