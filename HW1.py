# BASIC MOLECULAR BIOLOGY OPERATIONS
def reverse(string1):
    symb1 = ["A", "G", "C", "T", "U", "a", "g", "c", "t", "u"]
    seq1 = [x for x in string1]
    for i in range(0,len(seq1)-1):
        if seq1[i] in symb1:
            for j in range(i+1, i+2):
                if (seq1[i] == "T" or seq1[i]== "t") and (seq1[j] == "U" or seq1[j] == "u") :
                    return "Invalid alphabet.Try again!"
        else:
            return "Invalid alphabet.Try again!"   
    new = seq1[::-1]
    answer = ''.join(new)
    return answer
 
def transcribe(string):
    symb = ["A", "G", "C", "T", "a", "g", "c", "t"]
    seq = [x for x in string]
    for i in range(0,len(seq)-1):
        if seq[i] in symb:
            continue
        return "Invalid alphabet.Try again!"   
    x = "AaGgCcTt"
    y = "UuCcGgAa"
    answer = string.maketrans(x,y)
    return string.translate(answer)
        


def complement(string):
    
    symb = ["A", "G", "C", "T", "U", "a", "g", "c", "t", "u"]
    seq = [x for x in string]
    for i in range(0,len(seq)-1):
        if seq[i] in symb:
            for j in range(i+1, i+2):
                if (seq[i] == "T" or seq[i]== "t") and (seq[j] == "U" or seq[j] == "u"):
                    return "Invalid alphabet.Try again!"
        else:
            return "Invalid alphabet.Try again!"   
    
    x = "AaGgCcTt"
    y = "TtCcGgAa"
    answer = string.maketrans(x,y)
    return string.translate(answer)



def reverse_complement(string):
    symb = ["A", "G", "C", "T", "U", "a", "g", "c", "t", "u"]
    seq = [x for x in string]
    for i in range(0,len(seq)-1):
        if seq[i] in symb:
            for j in range(i+1, i+2):
                if (seq[i] == "T" or seq[i]== "t") and (seq[j] == "U" or seq[j] == "u"):
                    return "Invalid alphabet.Try again!"
        else:
            return "Invalid alphabet.Try again!"   
    
    x = "AaGgCcTt"
    y = "TtCcGgAa"
    answer = string.maketrans(x,y)
    new_ans = [y for y in string.translate(answer)]
    new_ans = new_ans[::-1]
    
    return "".join(new_ans)

def command(request):
    
    while request != "exit":
        
        if request == "reverse":
            print("Enter sequence")
            print(reverse(string1 = input()))
            print("Enter command")
        elif request == "transcribe":
            print("Enter sequence")
            print(transcribe(string = input()))
            print("Enter command")
        elif request == "complement":
            print("Enter sequence")
            print(complement(string = input()))
            print("Enter command")
        elif request == "reverse complement":
            print("Enter sequence")
            print(reverse_complement(string = input()))
            print("Enter command")
        else:
            print("Use these comands: transcribe, reverse, reverse complement, complement")
        request = input()
    print("Good luck!")
print("Enter command")
request = input()
command(request)

