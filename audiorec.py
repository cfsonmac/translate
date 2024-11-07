import speech_recognition as sr
import os
from pydub import AudioSegment
from pydub.silence import split_on_silence

status = 0
def transcribe_audio(path):
    # initialize the recognizer
    r = sr.Recognizer()
    text = "*****"
    global status
    # use the audio file as the audio source
    with sr.AudioFile(path) as source:
        r.adjust_for_ambient_noise(source)
        audio_listened = r.record(source)
        # audio = r.record(source, offset=5, duration=15)
        try:
            status = 2
            text = r.recognize_google(audio_listened, language="de-DE")
        except Exception as e:
            if status == 0 or status == 2:
                print("Listening...")
                status = 1
    return text


# a function that splits the audio file into chunks on silence
# and applies speech recognition
def get_large_audio_transcription_on_silence(path):
    """Splitting the large audio file into chunks
    and apply speech recognition on each of these chunks"""
    # open the audio file using pydub
    sound = AudioSegment.from_file(path)
    # split audio sound where silence is 500 miliseconds or more and get chunks
    chunks = split_on_silence(sound,
                              # experiment with this value for your target audio file
                              # minimum length of silence in milliseconds to be used for a split.
                              min_silence_len=600,
                              # adjust this per requirement
                              # anything quieter than this will be considered silence
                              silence_thresh=sound.dBFS - 14,
                              # keep the silence for 1 second, adjustable as well
                              # amount of silence to leave at the beginning and the end of
                              # each chunk detected in milliseconds.
                              keep_silence=500,
                              )
    folder_name = "chunks"
    # create a directory to store the audio chunks
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    whole_text = ""
    # process each chunk
    for i, audio_chunk in enumerate(chunks, start=1):
        # export audio chunk and save it in
        # the `folder_name` directory.
        chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
        audio_chunk.export(chunk_filename, format="wav")
        # recognize the chunk
        try:
            text = transcribe_audio(chunk_filename)
        except sr.UnknownValueError as e:
            print("Error:", str(e))
        else:
            text = f"{text.capitalize()}. "
            print(chunk_filename, ":", text)
            whole_text += text
    # return the text for all chunks detected
    return whole_text


if __name__ == "__main__":
    path = "./test/output.wav"
    print("\nFull text:", get_large_audio_transcription_on_silence(path))
