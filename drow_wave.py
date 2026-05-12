import matplotlib.pyplot as plt
import numpy as np

sample_rate = 441000

def draw_wave_just(wave, title="Waveform"):
    plt.figure(figsize=(10, 4))
    plt.plot(wave)
    plt.title(title)
    plt.xlabel("Sample Index")
    plt.ylabel("Amplitude")
    plt.grid()
    plt.show()

def draw_wave_realtime(wave, title="Waveform"):
    plt.ion()  # インタラクティブモードON
        
    x = np.linspace(0, 2*np.pi, 100)
    y = np.sin(x)
    
    def new_wave(ny=y,nx=x):
        line.set_ydata(ny)
        line.set_xdata(nx)
        print("updated wave")
    
    fig, ax = plt.subplots()
    line, = ax.plot(x, y)
    ax.set_ylim(-1.5, 1.5)
    
    for i in range(100):
        new_wave(ny=np.sin(x + i * 0.1))
        fig.canvas.draw()
        fig.canvas.flush_events()

draw_wave_realtime(np.sin(np.linspace(0, 2*np.pi, sample_rate)), title="Sine Wave") 
