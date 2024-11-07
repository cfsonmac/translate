import pyaudio
import wave
import sys


def play_audio(path):
    CHUNK = 1024

    wf = wave.open(path, 'rb')

    p = pyaudio.PyAudio()

    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    data = wf.readframes(CHUNK)

    while data != b"":
        stream.write(data)
        data = wf.readframes(CHUNK)

    stream.stop_stream()
    stream.close()

    p.terminate()


def record_audio(output_path, duration=5):
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    RECORD_SECONDS = duration
    WAVE_OUTPUT_FILENAME = output_path

    p = pyaudio.PyAudio()
    target = '立体声混音'
    dev_index = -1

    for i in range(p.get_device_count()):
        dev = p.get_device_info_by_index(i)
        if dev['name'].find(target) >= 0 and dev['hostApi'] == 0:
            # print('已找到内录设备,序号是 ',i)
            dev_index = i
    if dev_index < 0:
        return

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    input_device_index=int(dev_index),
                    frames_per_buffer=CHUNK)

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


if __name__ == "__main__":
    # record_audio("./test/output.wav")
    play_audio("./test/output.wav")
