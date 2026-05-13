import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt
import queue

sample_rate = 10000
chunk = 1024*500

# コールバック → メインループへデータを渡すためのキュー
q = queue.Queue()

plt.ion()
fig, ax = plt.subplots()
x = np.arange(0, chunk)
line, = ax.plot(x, np.zeros(chunk))
ax.set_ylim(-1, 1)

def audio_callback(indata, frames, time, status):
    # 描画はしない。データだけキューに渡す
    q.put(indata[:, 0].copy())

with sd.InputStream(callback=audio_callback,
                    channels=1,
                    samplerate=sample_rate,
                    blocksize=chunk):
    print("Listening...")

    while True:
        # 新しいデータがあれば描画
        if not q.empty():
            data = q.get()
            line.set_ydata(data)
            fig.canvas.draw()
            fig.canvas.flush_events()
