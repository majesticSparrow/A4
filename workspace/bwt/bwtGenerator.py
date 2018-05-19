import random

def get_bwt(line):
    array = []
    for i in range(len(line)):
        st = line[i:] + line[0:i] # generating cyclic rotations
        array.append(st)
    array.sort() # sorting the cyclic rotations according to unicode values
     
    bwt = []
    for i in range(len(array)):
        bwt.append(array[i][-1])
    return bwt


def compress(bwt):
    encoded = ""
    count = 0
    prevChar = bwt[0]
    for char in bwt:
        if char == prevChar:
            count += 1
        else:
            encoded = encoded + str(count) + prevChar
            output.write(str(count) + " " + prevChar +"\n")
            prevChar = char
            count = 1
    output.write(str(count) + " " + char)
    encoded = encoded + str(count) + char
    #print(encoded)
    return encoded
            
def getText(filename):
    infile = open(filename)
    text = ""
    for line in infile:
        text += line
    
    return text
    
def abra_cadabra(text):
    text = text.replace("*"," ")
    text = text.replace("-","\n")
    text = text.replace("FIT2004ExamPage","")
    return text

output = open('small_example.bz2', 'w')

text = getText("small_example.txt")

text=text.replace('\n','-')
text=text.replace(' ','*')

# adding $ at the end
text += "$"

bwt = get_bwt(text)

bwt_string = "".join(bwt)
#print(bwt_string)


compressed = compress(bwt)

output.close()



