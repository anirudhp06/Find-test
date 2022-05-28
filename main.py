count=0
word=["COMPILER","SERVER","IMPORT","CPU","PSEUDOCODE",'PROMPT']
with open("test.txt","r") as f:
    lines=f.read().split("\n")
    for j in word:
        for i,line in enumerate(lines):
            if j in line:
                count+=1
        print("{} has repeated {} times".format(j,count))
        count=0