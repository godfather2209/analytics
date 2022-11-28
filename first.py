def first(string):
    first_ = set()
    if string in terminals:
        first_ = {string}
    elif string in non_terminals:
        alternatives = productions_dict[string]
        for alternative in alternatives:
            first_2 = first(alternative)
            first_ = first_ | first_2
    elif string == "" or string == "@":
        first_ = {"@"}
    else:
        first_2 = first(string[0])
        if "@" in first_2:
            i = 1
            while "@" in first_2:
                first_ = first_ | (first_2 - {"@"})
                if string[i:] in terminals:
                    first_ = first_ | {string[i:]}
                    break
                elif string[i:] == "":
                    first_ = first_ | {"@"}
                    break
                first_2 = first(string[i:]) 
                first_ = first_ | first_2 - {"@"}
                i += 1
        else:
            first_ = first_ | first_2
    return first_

no_of_terminals = int(input("Enter number of terminals: "))
terminals = []
print("Enter the terminals: ")
for _ in range(no_of_terminals):
    terminals.append(input())
    
no_of_non_terminals = int(input("Enter number of non-terminals: "))
non_terminals = []
print("Enter the non-terminals: ")
for _ in range(no_of_non_terminals):
    non_terminals.append(input())

no_of_productions = int(input("Enter number of productions: "))
productions = []
print("Enter the productions: ")
for _ in range(no_of_productions):
    productions.append(input())

# productions dictionary
productions_dict = {}
for nt in non_terminals:
    productions_dict[nt] = []

for production in productions:
    prod = production.split("->")
    alternatives = prod[1].split("/")
    for alternative in alternatives:
        productions_dict[prod[0]].append(alternative)

FIRST = {}
for nt in non_terminals:
    FIRST[nt] = set()

for nt in non_terminals:
    FIRST[nt] = FIRST[nt] | first(nt)

print("{: ^20}{: ^20}".format("Non-terminal", "First"))
for nt in non_terminals:
    print("{: ^20}{: ^20}".format(nt, str(FIRST[nt])))


