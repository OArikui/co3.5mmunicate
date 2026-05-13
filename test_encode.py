codes=['utf-8', 'utf-16', 'ASCII']
strcode=codes[0]
#copilot saids unicode is based on this method 
"""
『こ』=U+3053
① まず U+3053 を2進数にする
U+3053 = 0b0011 0000 0101 0011
② UTF-8 の3バイト形式に当てはめる
1110xxxx 10xxxxxx 10xxxxxx
③ 結果が E3 81 93 になる
1110 0011 → E3
10 000001 → 81
10 0011   → 93"""

"""コードを自分で作成して、文字列に変換する実験.
koは、3.5mmから取得したanalogをデジタル変換したものを16進数で表したもの.を模している"""

ko=["e3","81","93"]
kostr=""
for i in ko:
    kostr+=i
print(kostr)
testbyte=bytes.fromhex(kostr)
print(testbyte)
print(testbyte.decode(strcode))
