def printPattern(s,i,action):
    print("\t{}\t\t{}\t\t{}\t".format(s,i,action))

def shiftReduce():
    global ip;
    global stack;

    if stack == "$"+starting_symbol and ip=="$":
        printPattern(stack,ip,"Reduce")
        print("String is Accepted");
        return;
    n = len(stack)
    flag = False
    for i in range(n-1,-1,-1):
        for (nt,rhs) in productions_dict.items():
            if stack[i:] in rhs:
                printPattern(stack,ip,"Reduce")
                stack = stack[0:i]+nt;
                flag = True;
                break;
        if flag:
            break;
        
    if flag==False:
        if ip=="$":
            printPattern(stack,ip,"No Operation")
            print("String is Not Accepted")
            return
        else:
            printPattern(stack,ip,"Shift")
            stack = stack + ip[0];
            ip = ip[1:];
    shiftReduce();
no_of_terminals=int(input("Enter no. of terminals: "))

terminals = []

print("Enter the terminals :")
for _ in range(no_of_terminals):
    terminals.append(input())

no_of_non_terminals=int(input("Enter no. of non terminals: "))

non_terminals = []

print("Enter the non terminals :")
for _ in range(no_of_non_terminals):
    non_terminals.append(input())

starting_symbol = input("Enter the starting symbol: ")

no_of_productions = int(input("Enter no of productions: "))

productions = []

print("Enter the productions:")
for _ in range(no_of_productions):
    productions.append(input())

print("Enter the I/P String:");

ip = input();

productions_dict = {}

for nT in non_terminals:
    productions_dict[nT] = []

for production in productions:
    nonterm_to_prod = production.split("->")
    alternatives = nonterm_to_prod[1].split("/")
    for alternative in alternatives:
        productions_dict[nonterm_to_prod[0]].append(alternative)

printPattern("Stack","I/P String","Action")
stack = "$"
ip = ip + "$"
printPattern(stack,ip,"Shift");
stack = "$"+ip[0]
ip = ip[1:]

shiftReduce();
