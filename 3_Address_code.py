precedence={'/':2,'*':2,'+':1,'-':1}
def isOperator(op):
    if op in '+-*/':
        return True
    return False
    
def countOperators(expr):
    count=0
    for x in expr:
        if isOperator(x):
            count+=1
    return count

def ans(expr):
    opCount=countOperators(expr)
    addressCodeCount=0
    addressCodes={}
    for i in range(len(expr)):
        if isOperator(expr[i]) and (isOperator(expr[i-1]) or isOperator(expr[i+1])):
            print("Invalid Expression")
            return
        if (isOperator(expr[i]) and i==0) or (isOperator(expr[i]) and i==len(expr)-1):
            print("Invalid Expression")
            return   
        
    while opCount:
        loc=-1
        n=len(expr)
        for i in range(n):
            if isOperator(expr[i]):
                if loc==-1 or precedence[expr[i]]>precedence[expr[loc]]:
                    loc=i
        beg=loc-1
        end=loc+1
        while beg>=0 and isOperator(expr[beg])==False:
            beg-=1
        beg+=1
        while end<n and isOperator(expr[end])==False:
            end+=1
        end-=1
        addressCodeCount+=1
        addressCodes[f't{addressCodeCount}']=expr[beg:end+1]
        expr=expr[:beg]+f't{addressCodeCount}'+expr[end+1:]
        opCount-=1
    for i in addressCodes.items():
        print(i[0],':',i[1])

expr=input()
ans(expr)


