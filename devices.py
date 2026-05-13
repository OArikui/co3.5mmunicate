import fnmatch
import sounddevice as sd
import numpy as np

from setting import splrat
from setting import code
class how_much_noise:
    """settingで決められているノイズサンプルを再生し、その送受信でノイズ量を判断します。"""
    def throw_noisesample(nspl=None):
        from setting import noisesample
        from setting import inputdex
        duration = 5  # ノイズを測定する時間（秒）
        sample_rate = splrat  # サンプリングレート
        spl=np.array(noisesample) if nspl is None else np.array(nspl)  # サンプルのリストを取得
        


def there_is_output(select=None):
    """
    音声出力デバイスを検索する関数。indexを返す。
    select==None:Headset
    select==True:ユーザーが選択
    select==文字列:その文字列を含むデバイス
    """
    audio_devices = sd.query_devices()
    if select is None:#selectがNoneの場合はHeadset Microphoneを探す
        select="Headphone*"
    elif select is True:#selectがTrueの場合はユーザーに選択させる
        print(audio_devices)
        sl=input("Select the index of the audio device you want to use and press Enter: ")
        select=audio_devices[int(sl)]['name']
    else:#selectが文字列の場合はその文字列を含むデバイスを探す
        select = [i for i, dev in enumerate(audio_devices)#selectを含むデバイスを探す。不完全一致検索
                    if fnmatch.fnmatch(dev['name'].casefold(), select+"*")]
        if len(select) == 0:#selectを含むデバイスが見つからない場合はHeadset Microphoneを探す
            print("No matching audio device found.")
            print("defulting to Headset Microphone")
            select="Headphone*"
        elif len(select) > 1:#selectを含むデバイスが複数見つかった場合　完全一致検索
            select = [i for i, dev in enumerate(audio_devices)
                    if fnmatch.fnmatch(dev['name'], select)][0]
        else:
            select=select[0]#selectを含むデバイスが1つ見つかった場合はそのデバイスを使用する
    # 1. Headset Microphone を探す
    matches = [i for i, dev in enumerate(audio_devices)
            if fnmatch.fnmatch(dev['name'], select)]
    if matches:
        audio_device_index = matches[0]
        print(f"Using output device : {audio_devices[audio_device_index]['name']}")

    else:
       audio_device_index = sd.default.device[1]  # デフォルトの出力デバイスを使用
       print(f"Using default output device : {audio_devices[audio_device_index]['name']}")
       
    return audio_device_index

def there_is_input(select=None):
    """
    音声入力デバイスを検索する関数。indexを返す。
    select==None:Headset Microphone
    select==True:ユーザーが選択
    select==文字列:その文字列を含むデバイス
    """
    audio_devices = sd.query_devices()
    if select is None:#selectがNoneの場合はHeadset Microphoneを探す
        select="Headset Microphone*"
    elif select is True:#selectがTrueの場合はユーザーに選択させる
        print(audio_devices)
        sl=input("Select the index of the audio device you want to use and press Enter: ")
        select=audio_devices[int(sl)]['name']
    else:#selectが文字列の場合はその文字列を含むデバイスを探す
        select = [i for i, dev in enumerate(audio_devices)#selectを含むデバイスを探す。不完全一致検索
                    if fnmatch.fnmatch(dev['name'].casefold(), select+"*")]
        if len(select) == 0:#selectを含むデバイスが見つからない場合はHeadset Microphoneを探す
            print("No matching audio device found.")
            print("defulting to Headset Microphone")
            select="Headset Microphone*"
        elif len(select) > 1:#selectを含むデバイスが複数見つかった場合　完全一致検索
            select = [i for i, dev in enumerate(audio_devices)
                    if fnmatch.fnmatch(dev['name'], select)][0]
        else:
            select=select[0]#selectを含むデバイスが1つ見つかった場合はそのデバイスを使用する
    # 1. Headset Microphone を探す
    matches = [i for i, dev in enumerate(audio_devices)
            if fnmatch.fnmatch(dev['name'], select)]
    if matches:
        audio_device_index = matches[0]
        print(f"Using input device : {audio_devices[audio_device_index]['name']}")

    else:
         audio_device_index = sd.default.device[0]  # デフォルトの入力デバイスを使用
         print(f"Using default input device : {audio_devices[audio_device_index]['name']}")
    return audio_device_index