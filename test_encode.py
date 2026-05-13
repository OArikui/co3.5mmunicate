codes=['utf-8', 'utf-16', 'ASCII']
strcode=codes[0]
#testdata for convert analog
d1='*あいう' 
d2="abcd"
unid1=d1.encode(strcode)
unid2=d2.encode(strcode)
print(unid1,unid2)
fusion=unid1+unid2
print(fusion.decode(strcode))
print(str(unid1))
fusionst=str(unid2)+str(unid1)
print(fusionst)