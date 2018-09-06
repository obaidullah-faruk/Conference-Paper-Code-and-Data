import time

NO_OF_CHARS = 256

def badCharHeuristic(string, size):
    start=time.time()

    badChar = [-1]*NO_OF_CHARS

    for i in range(size):
        badChar[ord(string[i])] = i;
    end=time.time()
    print("Execution time in preprocessing Phase : ", end-start)
    return badChar

def search(txt, pat):
    m = len(pat)
    badChar = badCharHeuristic(pat, m)

    start=time.time()
    n = len(txt)
    pos = 0
    shift=0
    charComparison=0
    while(pos <= n-m):
        j = m-1

        while j>=0 and pat[j] == txt[pos+j]:
            charComparison=charComparison+1
            j -= 1

        if j<0:
            print("Pattern occur at position = {}".format(pos))
            print("Total shift = {}".format(shift))
            print("Total Character Comparison = {}".format(charComparison))

            pos += (m-badChar[ord(txt[pos+m])] if pos+m<n else 1)
            charComparison = charComparison + 1
        else:
            pos += max(1, j-badChar[ord(txt[pos+j])])
            charComparison = charComparison + 1
        shift = shift + 1

    end=time.time()
    print("Execution time in searching phase : ",end-start)

def input_Func():
    while 1:
         txt=input("Enter TXT : ")
         pat=input("Enter PAT: ")
         search(txt,pat)

input_Func()
