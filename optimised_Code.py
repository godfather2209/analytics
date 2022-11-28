f=open('data.txt','r')
loopVariable=''
statementsNotContainingLoopVariables=[]
loopStatementsBeingProcessed=False
for line in f:
    if 'for' in line:
        loopVariable=line[line.find('(')+1]
        loopStatementsBeingProcessed=True
    if loopStatementsBeingProcessed==False:
        print(line,end="")
        continue
    if loopVariable in line or '{' in line or '}' in line:
        print(line,end="")
        if '}' in line:
            loopStatementsBeingProcessed=False
            while statementsNotContainingLoopVariables:
                print()
                print(statementsNotContainingLoopVariables.pop(0))
    else:
        statementsNotContainingLoopVariables.append(line)