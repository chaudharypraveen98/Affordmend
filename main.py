def compress(string):
    res = ""
    count = 1
    res += string[0]
    for i in range(len(string)-1):
        if(string[i] == string[i+1]):
            count+=1
        else:
            if(count > 1):
                res += str(count)
            res += string[i+1]
            count = 1
    if(count > 1):
        res += str(count)
    return res
    
def decompress(string):
    res=""
    i=0
    while i<len(string)-1:
        if string[i+1].isnumeric():
            next_num = int(string[i+1])
            res+=string[i]*next_num
            i+=2
        else:
            res+=string[i]
            i+=1
    print(res)
compress_string = compress("praaaavvvv")
decompress(compress_string)
