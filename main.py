import os
import threading
import time
from datetime import datetime
from getaudio import record_audio
from audiorec import transcribe_audio
from translate import arr_translate


start = time.perf_counter()
fo = open(f"output_{str(datetime.now()).split()[0]}.txt", "a", encoding="utf-8")
record_duration = 60

res = []
def record_and_process1(index):
    # lock.acquire()
    path = f"./chunks/chunk_{index}.wav"
    record_audio(path)
    text = transcribe_audio(path)
    print(text)
    time.sleep(2)
    res.append(text)
    fo.write(text)
    fo.write("\n")
    os.remove(path)
    pool.release()
    # lock.release()


# lock = threading.Lock()
pool = threading.BoundedSemaphore(4)
thread_list = []
index = 0
while True:
    if index == 4:
        index = 0
    # if len(res) == 4:
    #     trans = arr_translate(res)

    pool.acquire()
    thread = threading.Thread(target=record_and_process1, args=[index])
    index += 1
    thread.start()
    thread_list.append(thread)
    time.sleep(3)
    if time.perf_counter() - start > record_duration:
        break

for t in thread_list:
    t.join()

finish = time.perf_counter()
fo.close()
arr_translate(res)

