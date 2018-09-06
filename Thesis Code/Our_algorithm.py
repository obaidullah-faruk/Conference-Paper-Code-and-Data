import math
import time

def search_Func(txt,pat,n,m,posIndex):
    start=time.time()
    if m%2==0:
        midPoint=int(m/2)
    else:
        midPoint=math.floor(m/2)+1

    length=len(posIndex)
    flag=0
    shift=0
    charComparison = 0
    for pos in posIndex:
        k=pos # k te milte pare oi starting position gula nilam
        l=0
        p=m+k-1 # last index of proabale match of txt
        LastCharPat=m-1 # Second last most probably m-2 hbe
        count=0
        while k<=p:
            charComparison = charComparison + 2
            if txt[k+1]==pat[l+1] and txt[p-1]==pat[LastCharPat-1]:
                k+=1
                l+=1
                p-=1
                LastCharPat-=1
                count+=1
            else:
                 break
        if count==midPoint:
            flag=1
            print("Match found at position : {}" .format(pos))
            print("Total Shift : {}" .format(shift))
            print("Total Character Comparsion : {}" .format(charComparison))
        shift=shift+1

    if flag==0:
        print("No match found")
    end=time.time()
    print("Total Execution time in searching phase : ", end-start)

def preProcess_Func(txt, pat):
    start=time.time()
    n=len(txt)
    m=len(pat)
    if m==1:
        return
    i=0
    posIndex=[]
    while i<=(n-m):
        if txt[i]==pat[0]:
            if txt[i+m-1] == pat[m-1]:
                posIndex.append(i)
        i+=1
    end=time.time()
    print("Execution time in Preprocessing Phase : ", end-start)
    search_Func(txt,pat,n,m,posIndex)

def input_Func():
    while 1:
        txt=input("Enter the text :")
        pat = input("Enter the pattern :")
        preProcess_Func(txt,pat)

input_Func()