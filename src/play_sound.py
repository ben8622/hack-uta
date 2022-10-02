import sounddevice as sd
import soundfile as sf
import random

sound_files = ['/home/pi/hack-uta/src/data/sussy_baka.wav','/home/pi/hack-uta/src/data/sus_music.wav','/home/pi/hack-uta/src/data/sus_sound.wav']
i = random.randrange(0,3,1)
data, fs = sf.read(sound_files[i])
sd.play(data, fs)
status = sd.wait()