import soundcard as sc
import numpy

speakers = sc.all_speakers()
default_speaker = sc.default_speaker()
mics = sc.all_microphones()
default_mic = sc.default_microphone()

data = default_mic.record(samplerate=48000, numframes=48000)
default_speaker.play(data / numpy.max(numpy.abs(data)), samplerate=48000)

with default_mic.recorder(samplerate=48000) as mic, \
        default_speaker.player(samplerate=48000) as sp:
    for _ in range(100):
        data = mic.record(numframes=1024)
        sp.play(data)
