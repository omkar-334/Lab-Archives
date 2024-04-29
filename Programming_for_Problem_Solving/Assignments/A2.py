from string import ascii_lowercase as alc
alphabets={}
for i in alc:
    alphabets[i]=0
finout={}

def histogram(instr):
    inlist=[*instr]
    for i in inlist:
        alphabets[i]+=1
    for key in alphabets:
        if alphabets[key]!=0:
            finout[key]=alphabets[key]
    for key in finout:
        print("Letter "+key+" appears "+str(finout[key])+" times")

a=str(input('Enter word'))
histogram(a)
