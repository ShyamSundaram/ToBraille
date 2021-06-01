import PyPDF2

def toText(file):
    pdfFileObj = open('example.pdf', 'rb')

    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    print("Number of pages: "+ str(pdfReader.numPages))

    pageObj = pdfReader.getPage(0)

    print(pageObj.extractText())

    string = pageObj.extractText()
    braille_line = []
    braille_paragraph = []

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
    # eng_bra["\n"] = [0, 0, 0, 0, 0, 0]

    capital = [0, 0, 0, 0, 0, 1]
    number = [0, 1, 0, 1, 1, 1]
    for i in range(len(string)):
        if string[i].isupper():
            braille_line.append(capital)
            braille_line.append(eng_bra[string[i].lower()])
        elif string[i].isdigit():
            braille_line.append(number)
            braille_line.append(eng_bra[string[i]])
        elif string[i].islower():
            braille_line.append(eng_bra[string[i]])
        else:
            if string[i] == "\n":
                braille_paragraph.append(braille_line)
                braille_line = []
            else:
                braille_line.extend(eng_bra[string[i]])
    for q in braille_paragraph:
        print(q)

    print("Lines: " + str(len(braille_paragraph)))

    # closing the pdf file object
    pdfFileObj.close()
