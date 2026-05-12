import matplotlib.pyplot as plt
import numpy as np

sample_rate = 441000

def draw_wave(wave, title="Waveform"):
    plt.figure(figsize=(10, 4))
    plt.plot(wave)
    plt.title(title)
    plt.xlabel("Sample Index")
    plt.ylabel("Amplitude")
    plt.grid()
    plt.show()
