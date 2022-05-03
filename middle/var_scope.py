a = 1 # 전역변수 
print(a)

def vartest(a): #지역변수 
    print(a)
    a = a+10
    return a
a = vartest(3) #

print (a)

b = 1 # 전역변수 
print(b)

def vartest(): 
    global b # 전역변수
    print (b)
    b = b+10
    return b
b = vartest() 

print (a)

if a== 24:
    pass 