import fuzzy
soundex = fuzzy.soundex(100)
word=input()
filepath=input()
f=open(filepath,"r")
arr=[]
for x in f:
    if(soundex(word)==soundex(x)):
        arr.append(x)
print(arr)        
