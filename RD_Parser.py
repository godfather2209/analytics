def generateLexicalTable():
    fp = open("expressions.txt", "r")
    lines = fp.readlines()
    result = []
    operator = {
        "+": ["AdOp", "Addition Operator"],
        "-": ["SubOp", "Subtraction Operator"],
        "*": ["MOp", "Multiplication Operator"],
        "/": ["DOp", "Division Operator"],
        "%": ["MoOp", "Modulo Operator"],
        "=": ["AOp", "Assignment Operator"]
    }
    for i in range(len(lines)):
        line = list(lines[i].split())
        for char in line:
            temp = []
            if char in operator:
                temp = [i+1, char, operator[char][0], operator[char][1]]
            elif char.isidentifier():
                temp = [i+1, char, "id", "Identifier"]
            elif int(char):
                temp = [i+1, char, "num", "Number"]
            result.append(temp)
    fp.close()
    return result 

result = generateLexicalTable()
print("LINE NO\t\tTOKEN NO\tLEXIM\t\tTOKEN\t\tPATTERN")
for i in range(len(result)):
    print(result[i][0], "\t\t", i+1, "\t\t", result[i][1], "\t\t", result[i][2], "\t\t", result[i][3])


