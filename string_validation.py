if __name__ == '__main__':
    s = "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW"
    isAlNum = False
    isAlPha = False
    isAlDigit = False
    isLower = False
    isUpper = False
    l = []
    for i in s:
        if (i.isalnum() and  not isAlNum):
            isAlNum = True;
            l.append("True")
        if (i.isalpha() and  not isAlPha):
            isAlPha = True
            l.append("True")
        if (i.isdigit() and  not isAlDigit):
            print("-----")
            l.append("True")
            isAlDigit = True
        if (i.islower() and  not isLower):
            isLower = True
            l.append("True")
        if (i.isupper() and  not isUpper):
            isUpper = True
            l.append("True")

    print(l)    
    for i in range(5):
        try:
            print(l[i])
        except:
            print("False")    
        
        