
mode=input("mode t r l: ")#t:送信 r:受信 l:波を見る

if mode=="t":
    import numpy as np
    import sounddevice as sd
    import time
    fs = 44100
    sec=1
    t = np.linspace(0, 6, fs*sec)
    wave = 20 * np.sin(2 * np.pi * 440 * t)
    wave=t
    print("sec:",sec)
    for i in range(6):
        st=time.time()
        sd.play(wave, fs)
        sd.wait()
        ed=time.time()
        print(i,":",ed-st-sec)

if mode=="r":
    import sounddevice as sd
    import soundfile as sf
    import matplotlib.pyplot as plt
    import time 
    import os
    samplerate = 44100      # サンプリングレート
    duration = 70            # 録音秒数
    filename = os.getcwd() + "\\recorded\\" + str(time.strftime("%Y-%m-%d_%H-%M-%S")) + "_d" + str(duration) + ".wav" # 保存先
    print("Recording...")
    audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1)
    sd.wait()
    print("Done.")
    plt.plot(audio)
    plt.show(block=True)
    sf.write(filename, audio, samplerate)
    print("Saved:", filename)

if mode=="l":
    from tkinter import filedialog as fd
    import matplotlib.pyplot as plt
    import soundfile as sf
    filename = fd.askopenfilename()
    print("Selected file:", filename)
    data, samplerate = sf.read(filename)
    plt.plot(data) 
    plt.show()