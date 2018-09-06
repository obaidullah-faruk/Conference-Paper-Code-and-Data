import time
def PrefixArrayCreation(pat,m,preArray):
    start=time.time()
    j=0
    i=1
    preArray[0]=0
    while i<m:
        if pat[i]==pat[j]:
            preArray[i]=j+1
            j=j+1
            i=i+1
        else:
            if j!=0:
                j=preArray[j-1]
            else:
                preArray[i]=0
                i=i+1
    end=time.time()
    print("Total Execution time in Preprocessing phase : " , end-start)

def KMPSearch(text,pat):
    n=len(text)
    m=len(pat)
    preArray=[0]*m
    PrefixArrayCreation(pat,m,preArray)

    start = time.time()
    i=0
    j=0
    k=0
    shift=0
    charComparsion=0
    while i<n:
        if text[i]==pat[j]:
            charComparsion=charComparsion+1
            i+=1
            j+=1
        if j==m:
            print("Pattern found at position {}". format(i-j))
            print("Total Shift : {}" . format(shift))
            print("Total Character Comparison : {}" .format(charComparsion))
            j=preArray[j-1]
            k+=1
        elif i<n and text[i]!=pat[j]:
            charComparsion=charComparsion+1
            if j!=0:
                j=preArray[j-1]
            else:
                i+=1
            shift=shift+1
    if k==0:
          print("No match found")
    end=time.time()
    print("Total Execution time in searching phase : ", end-start)

def inputFunc():
    while 1:
        #text= input('Enter the text : ')
        f=open("bible.txt")
        text=f.read()
        f.close()
        pat=input('Enter the pattern : ')
        KMPSearch(text,pat);
        
inputFunc()