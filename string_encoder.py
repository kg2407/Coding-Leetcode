# https://github.com/wwt/as-dotnet-string-encoder
# WWT String Encoder
def stringEncoder(inpString):
    str = inpString.lower()
    # flag = False
    dict = {}
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    ans = ''
    intString = ''

    def checkConversionFeasibility(stringToCheck):
        try:
            int(stringToCheck)
            return True
        except:
            return False


    for ind in range(26):
        a = alphabets[ind]
        if a == 'a':
            dict[a] ='1'
        elif a == 'e':
            dict[a] ='2'
        elif a=='i':
            dict[a] ='3'
        elif a== 'o':
            dict[a] = '4'
        elif a== 'u':
            dict[a] = '5'
        elif a== 'y':
            dict[a] = ' '
        else:
            dict[a] = alphabets[ind-1]
    dict[' '] = 'y'
    
    for st in str:
        flag = checkConversionFeasibility(st)
        if (flag):
            intString += st
            continue
        if len(intString) == 0 and st in dict.keys():
            ans += dict[st]
        elif len(intString) > 0:
            ans += intString[::-1]
            ans += dict[st]
            intString = ''
        else:
            ans += st
    if (len(intString)!=0):
        ans += intString[::-1]
    print(ans)

stringEncoder(' ')