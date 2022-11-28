import sys
sys.setrecursionlimit(60)

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

def follow(nt):
    follow_ = set()
    prods = productions_dict.items()
    if nt == starting_symbol:
        follow_ = follow_ | {"$"}
    for lhs, rhs in prods:
        for alt in rhs:
            for char in alt:
                if char == nt:
                    following_str = alt[alt.index(char) + 1:]
                    if following_str == "":
                        if nt == lhs:
                            continue
                        else:
                            follow_ = follow_ | follow(lhs)
                    else:
                        follow_2 = first(following_str)
                        if "@" in follow_2:
                            follow_ = follow_ | follow_2 - {"@"}
                            follow_ = follow_ | follow(lhs)
                        else:
                            follow_ = follow_ | follow_2
    return follow_

# terminals input
no_of_terminals = int(input("Enter number of terminals: "))
terminals = []
print("Enter the terminals: ")
for _ in range(no_of_terminals):
    terminals.append(input())

# non-terminals input
no_of_non_terminals = int(input("Enter number of non-terminals: "))
non_terminals = []
print("Enter the non-terminals: ")
for _ in range(no_of_non_terminals):
    non_terminals.append(input())

starting_symbol = input("Enter starting symbol: ")

# productions input
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

FOLLOW = {}
for nt in non_terminals:
    FOLLOW[nt] = set()

for nt in non_terminals:
    FIRST[nt] = FIRST[nt] | first(nt)

FOLLOW[starting_symbol] = FOLLOW[starting_symbol] | {"$"}
for nt in non_terminals:
    FOLLOW[nt] = FOLLOW[nt] | follow(nt)

print("{: ^20}{: ^20}".format("Non-terminal", "Follow"))
for nt in non_terminals:
    print("{: ^20}{: ^20}".format(nt, str(FOLLOW[nt])))

