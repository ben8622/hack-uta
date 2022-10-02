import sounddevice as sd
import soundfile as sf

sound_file = 'C:\\Users\\matho\\OneDrive\\Desktop\\\HackUTA22\\data\\sussy_baka.wav'
data, fs = sf.read(sound_file)
sd.play(data, fs)
status = sd.wait()