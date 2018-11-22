a='g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr\'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'



def convert(char):
    if ord(char)+2>ord('z'):
        return ((ord(char)+1)%ord('z'))+ord('a')
    else:
        return ord(char)+2
def alphaCheck(string,i):
    if(string[i].isalpha()):
        return chr(convert(string[i]))
    else:
        return string[i]
def run(string):
    b=''
    for i in range(len(string)):
        tmp=alphaCheck(string,i)
        b+=tmp;
    print(b)

run(a)



c='map'
run(c)
