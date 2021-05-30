import PyPDF2

def toBraille(file):
    pdfFileObj = open(file, 'rb')

    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    print("Number of pages: "+ str(pdfReader.numPages))

    pageObj = pdfReader.getPage(0)

    print(pageObj.extractText())

    string = pageObj.extractText().lower()
    Result_braille = []
    eng_bra = dict()
    eng_bra["a"] = [1, 0, 0, 0, 0, 0]
    eng_bra["b"] = [1, 0, 1, 0, 0, 0]
    eng_bra["c"] = [1, 1, 0, 0, 0, 0]
    eng_bra["d"] = [1, 1, 0, 1, 0, 0]
    eng_bra["e"] = [1, 0, 0, 1, 0, 0]
    eng_bra["f"] = [1, 1, 1, 0, 0, 0]
    eng_bra["g"] = [1, 1, 1, 1, 0, 0]
    eng_bra["h"] = [1, 0, 1, 1, 0, 0]
    eng_bra["i"] = [0, 1, 1, 0, 0, 0]
    eng_bra["j"] = [0, 1, 1, 1, 0, 0]
    eng_bra["k"] = [1, 0, 0, 0, 1, 0]
    eng_bra["l"] = [1, 0, 1, 0, 1, 0]
    eng_bra["m"] = [1, 1, 0, 0, 1, 0]
    eng_bra["n"] = [1, 1, 0, 1, 1, 0]
    eng_bra["o"] = [1, 0, 0, 1, 1, 0]
    eng_bra["p"] = [1, 1, 1, 0, 1, 0]
    eng_bra["q"] = [1, 1, 1, 1, 1, 0]
    eng_bra["r"] = [1, 0, 1, 1, 1, 0]
    eng_bra["s"] = [0, 1, 1, 0, 1, 0]
    eng_bra["t"] = [0, 1, 1, 1, 1, 0]
    eng_bra["u"] = [1, 0, 0, 0, 1, 1]
    eng_bra["v"] = [1, 0, 1, 0, 1, 1]
    eng_bra["w"] = [0, 1, 1, 1, 0, 1]
    eng_bra["x"] = [1, 1, 0, 0, 1, 1]
    eng_bra["y"] = [1, 1, 0, 1, 1, 1]
    eng_bra["z"] = [1, 0, 0, 1, 1, 1]
    eng_bra["1"] = [1, 0, 0, 0, 0, 0]
    eng_bra["2"] = [1, 0, 1, 0, 0, 0]
    eng_bra["3"] = [1, 1, 0, 0, 0, 0]
    eng_bra["4"] = [1, 1, 0, 1, 0, 0]
    eng_bra["5"] = [1, 0, 0, 1, 0, 0]
    eng_bra["6"] = [1, 1, 1, 0, 0, 0]
    eng_bra["7"] = [1, 1, 1, 1, 0, 0]
    eng_bra["8"] = [1, 0, 1, 1, 0, 0]
    eng_bra["9"] = [0, 1, 1, 0, 0, 0]
    eng_bra["0"] = [0, 1, 1, 1, 0, 0]
    eng_bra[" "] = [0, 0, 0, 0, 0, 0]
    eng_bra["."] = [1, 0, 1, 1, 0, 1]
    eng_bra[","] = [0, 0, 1, 0, 0, 0]
    eng_bra["?"] = [0, 0, 1, 0, 1, 1]
    eng_bra["_"] = [0, 1, 0, 0, 0, 1], [0, 0, 0, 0, 1, 1]
    eng_bra["-"] = [0, 0, 0, 0, 1, 1]
    eng_bra["!"] = [0, 0, 1, 1, 1, 0]
    eng_bra['"'] = [0, 0, 1, 0, 1, 1]
    eng_bra["'"] = [0, 0, 0, 0, 1, 0], [0, 0, 1, 0, 1, 1]
    eng_bra["("] = [0, 0, 0, 1, 0, 0], [1, 0, 1, 0, 0, 1]
    eng_bra[")"] = [0, 0, 0, 1, 0, 0], [0, 1, 0, 1, 1, 0]
    eng_bra[":"] = [0, 0, 1, 1, 0, 0]
    eng_bra[";"] = [0, 0, 1, 0, 1, 0]


    def split(word):
        return [char for char in word]


    capital = [0, 0, 0, 0, 0, 1]
    number = [0, 1, 0, 1, 1, 1]


    def braille_to_english(braille):
        matrix = []
        matrix.append(split(braille[0][1:]))
        matrix.append(split(braille[1][1:]))
        matrix.append(split(braille[2][1:]))
        char1 = [matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1], matrix[2][0], matrix[2][1]]
        char2 = [matrix[0][2], matrix[0][3], matrix[1][2], matrix[1][3], matrix[2][2], matrix[2][3]]
        char1 = list(map(int, char1))
        char2 = list(map(int, char2))
        flag = 0
        if char1 == capital:
            flag = 1
            for eng, bra in eng_bra.items():
                if bra == char2 and eng not in ["1","2","3","4","5","6","7","8","9","0"]:
                    result = eng.upper()
        if char1 == number:
            flag = 1
            for eng, bra in eng_bra.items():
                if bra == char2 and eng in ["1","2","3","4","5","6","7","8","9","0"]:
                    result = eng.upper()
        if flag == 0:
            for eng, bra in eng_bra.items():
                if bra == char1 and eng not in ["1","2","3","4","5","6","7","8","9","0"]:
                    result = eng
        return result
    #print(braille_to_english(['B10000000', 'B10000000', 'B10000000']))
    def add_braille(braille):
        a = []
        b = []
        c = []
        result = []
        hold = []
        a.append(split(braille[0][1:]))
        b.append(split(braille[1][1:]))
        c.append(split(braille[2][1:]))
        a.append(["0","0"]+split(braille[3][1:-2]))
        b.append(["0","0"]+split(braille[4][1:-2]))
        c.append(["0","0"]+split(braille[5][1:-2]))
        for i in range(8):
            hold.append(str(int(a[0][i]) + int(a[1][i])))
        hold = "B"+"".join(hold)
        
        result.append(hold)
        hold = []
        for i in range(8):
            hold.append(str(int(b[0][i]) + int(b[1][i])))
        hold = "B"+"".join(hold)
        result.append(hold)
        hold = []
        for i in range(8):
            hold.append(str(int(c[0][i]) + int(c[1][i])))
        hold = "B"+"".join(hold)
        result.append(hold)
        return result
        

    def convert():
        for i in range(len(string)):
            arr = []
            if string[i].isupper():
                arr.extend(capital)
                arr.extend(eng_bra[string[i].lower()])
            elif string[i].isdigit():
                arr = number
                arr.extend(eng_bra[string[i].lower()])
            elif string[i].islower():
                arr = eng_bra[string[i].lower()]
            else:
                if string[i] in eng_bra:
                    arr = eng_bra[string[i]]
                else:
                    arr = [0,0,0,0,0,0]
                
            letter_arduino = []
            for j in range(0, len(arr), 2):
                k = j//2
                binary = "B"
                if arr[j] == 1 and arr[j+1] == 1:
                    binary += "11"
                elif arr[j] == 1 and arr[j+1] == 0:
                    binary += "10"
                elif arr[j] == 0 and arr[j+1] == 1:
                    binary += "01"
                else:
                    binary += "00"
                if len(binary) == 3:
                    binary += "000000"
                elif len(binary) == 5:
                    binary += "0000"
                letter_arduino.append(binary)
            if len(letter_arduino) == 6:
                letter_arduino = add_braille(letter_arduino)
            
            # print(braille_to_english(letter_arduino) + "  "+ str(letter_arduino))
            letter_arduino[0]=int(letter_arduino[0][1:],2)
            letter_arduino[1]=int(letter_arduino[1][1:],2)
            letter_arduino[2]=int(letter_arduino[2][1:],2)
            Result_braille.append(letter_arduino)
            # print(letter_arduino)
            # print("if (x == "+string[i] + "){")
            # print("lc.setRow(0," + str(letter_arduino[0][1])+ ", "+str(letter_arduino[0][2]) +");")
            # print("lc.setRow(0," + str(letter_arduino[1][1])+ ", "+str(letter_arduino[1][2]) +");")
            # print("lc.setRow(0," + str(letter_arduino[2][1])+ ", "+str(letter_arduino[2][2]) +");")
            # print("delay(delaytime);\ncleardisp();\n}")
    convert()

    return Result_braille
#print(toBraille('test2.pdf'))

def toText(file):
    pdfFileObj = open(file, 'rb')

    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    print("Number of pages: "+ str(pdfReader.numPages))

    pageObj = pdfReader.getPage(0)

    print(pageObj.extractText())

    string = pageObj.extractText().lower()
    return string