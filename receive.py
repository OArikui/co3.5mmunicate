import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt

sample_rate = 44100
chunk = 1024  # 1回で読み取るサンプル数

plt.ion()
fig, ax = plt.subplots()
x = np.arange(0, chunk)
line, = ax.plot(x, np.zeros(chunk))
ax.set_ylim(-1, 1)

def audio_callback(indata, frames, time, status):
    line.set_ydata(indata[:, 0])
    fig.canvas.draw()
    fig.canvas.flush_events()

with sd.InputStream(callback=audio_callback,
                    channels=1,
                    samplerate=sample_rate,
                    blocksize=chunk):
    print("Listening...")
    while True:
        pass
