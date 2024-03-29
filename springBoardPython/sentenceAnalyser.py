text = """In communications and information processing, code is a system of rules to convert information—such as a letter, 
word, sound, image, or gesture—into another form, sometimes shortened or secret, for communication through a 
communication channel or storage in a storage medium. An early example is an invention of language, which enabled a 
person, through speech, to communicate what they thought, saw, heard, or felt to others. But speech limits the range 
of communication to the distance a voice can carry and limits the audience to those present when the speech is 
uttered. The invention of writing, which converted spoken language into visual symbols, extended the range of 
communication across space and time. """

def text_analyser(text):
    solution = {}
    for ele in text:
        ele = ele.lower()
        if ele is not ' ':
            if ele in solution:
                solution[ele] += 1
            else:
                solution[ele] = 1
    return solution

var1 = text_analyser(text)
for lett in var1:
    print('The letter', lett,'repeats',var1[lett])