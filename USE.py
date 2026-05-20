import sounddevice as sd
import fnmatch
import wave
import struct
import math
import numpy as np
from time import time
from tkinter import filedialog as fd

from setting import splrat
from setting import code
from setting import smplpath
from setting import setted
from setting import signals
from digit_to_analog import convert
from digit_to_analog import makewave

if not setted:
    raise Exception ("Before you use this,DO setting")

"""受、送信モードの選択"""
use=input("send?(Y or any):")
if use=="Y":#T:Throw R:Receive
    use="T"
else:
    use="R"

sd.play(np.linspace(0, 6, 44100),44100)#音声デバイスを初期化
sd.wait()

"""処理の開始"""
if use=="T":
    filepath = fd.askopenfilename()
    print("Selected file:", filepath)
    print("Converting text to wave...")
    namewave=convert.to_wav(txt=filepath.split("/")[-1].split(".")[0])
    print("Converting file to wave...")
    wav=convert.to_wav(filepath)
    print("Making wave...")
    wav=signals[0]+namewave+signals[1]+wav+signals[2]
    input("Press Enter to play the wave...")
    sttime=int((time.time()+3)*0.1)*10#次の10の倍数秒で始めます。(time.time()+x):次の10nまでn秒いないならその次

    sd.play(wav, splrat)
    sd.wait()
    print("finished playing")
    makewave(filepath.split("/")[-1].split(".")[0], wav)
elif use=="R":
    input("Press Enter to start listening...")
    prstime=time.time()
    print("listening...")
    input("Press Enter to finish listening...")
    ###録音を開始する
    ###     wav=録音を開始
    ###filepath,_=convert.to_text(wav,prstime) #signalの読み取り、保存まで行う
    ###print(f"{filepath}を保存しました。")

print("finish")