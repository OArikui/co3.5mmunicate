
"""low level setting for this project
"""
splrat=44100#サンプリングレート
code='utf-8'#文字コード
splpeat=5#いくつのサンプルで一つの数字を表すか。少なければ速度は速いがノイズに弱く、多ければ速度は遅いがノイズに強い


"""high level setting for this project
"""
inputdex=None#音声入力デバイスのインデックス。Noneの場合はHeadset Microphoneを探す。
otputdex=None#音声出力デバイスのインデックス。Noneの場合はHeadphoneを探す。
datasamples={"hex016": list(range(16))
             ,"hex": [hex(i) for i in range(1,16)]
             ,"hexmaixn": [range(1,16,8)]*6}#[0, 51, 102, 153, 204, 255]のような。データのサンプルを格納するリスト
noisesample=datasamples["hex016"]+datasamples["hex"]#ノイズの大きさを測定するために使用する。

from devices import there_is_input 
if inputdex is None:
    inputdex=there_is_input()

from devices import there_is_output
if otputdex is None:
    otputdex=there_is_output()