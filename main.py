#word=["COMPILER","SERVER","IMPORT","CPU","PSEUDOCODE",'PROMPT']
f=open("text.txt","r")
lines=f.read().split("\n")
def search(word,count=0):
    for i,line in enumerate(lines):
        if word in line:
            count+=1
    print("{} has repeated {} times".format(word,count))
    count=0
search("COMPILER")
f.close()