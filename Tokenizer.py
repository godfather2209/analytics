def tokenizer():
    fp = open("programFile.txt", "r")
    lines = fp.read()
    alphaCharacters = numericalValues = tabs = spaces = linesCount = specialCharacters = 0
    for char in lines:
        if char == "\n":
            linesCount += 1 
        elif char == "\t":
            tabs += 1 
        elif char.isdigit():
            numericalValues += 1 
        elif char == " ":
            spaces += 1 
        elif char.isalpha():
            alphaCharacters += 1 
        else:
            specialCharacters += 1 
    print("Alpha characters: ", alphaCharacters)
    print("Numerical Values: ", numericalValues)
    print("Special Characters: ", specialCharacters)
    print("Number of tabs: ", tabs)
    print("Number of spaces: ", spaces)
    print("Number of lines: ", linesCount)
    fp.close()


tokenizer()

    