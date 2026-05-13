

import numpy as np
from test_encode import codes
strcode=codes[0]
"""
I try to convert strings to analog
"""

def code_to_ls(codes):#文字の16進数コードを受け取る。　こab##[[:/p;-@]=e38193616223235b5b3a2f703b2d405dのような
    if type(codes) is not str:#入力が文字列でない場合はエラーを出す
        raise TypeError("Input must be a string")
    code_list = [codes[i:i+2] for i in range(0, len(codes), 2)]#16進数コードを2文字ずつのリストにする
    ls=[int(code, 16) for code in code_list]#16進数コードを10進数に変換してリストにする
    return np.array(ls)

def ls_to_code(ls):#リストを受け取る。　[227, 129, 147, 97, 98, 35, 91, 91, 58, 47, 112, 59, 45, 64]のような
    if type(ls) is not np.ndarray:#入力がnumpy配列でない場合はエラーを出す
        raise TypeError("Input must be a numpy array")
    code_list = [hex(num)[2:] for num in ls]#10進数を16進数に変換してリストにする
    return ''.join(code_list)#リストを文字列にする

def ls_to_wave(ls,spl_rag):#リストを受け取る。　[227, 129, 147, 97, 98, 35, 91, 91, 58, 47, 112, 59, 45, 64]のような
    if type(ls) is not np.ndarray:#入力がnumpy配列でない場合はエラーを出す
        raise TypeError("Input must be a numpy array")
    ls/=255.0*2-1#0~255の値を-1~1の範囲に変換する
    rls=np.repeat(ls, spl_rag)#リストを繰り返して波形を作る
    return rls

def wave_to_ls(wave,spl_rag):#波形を受け取る.
    if type(wave) is not np.ndarray:#入力がnumpy配列でない場合はエラーを出す
        raise TypeError("Input must be a numpy array")
    ls=np.array([int((num+1)/2*255) for num in wave[::spl_rag]])#波形を0~255の値に変換してリストにする
    return ls