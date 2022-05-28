#word=["COMPILER","SERVER","IMPORT","CPU","PSEUDOCODE",'PROMPT']
import sys
def search(word,count=0):
    for j in word:
        for i,line in enumerate(lines):
            if j in line:
                count+=1
        print("{} has repeated {} times".format(j,count))
        count=0
file_name=input("Enter the path for text file:")
try:
    f=open(file_name,"r")
except FileNotFoundError:
    print("File dosent exists")
    sys.exit()
lines=f.read().split("\n")
print("File loaded successfully")
word=input("Enter the word to be searched(case sensitive, for multiple add , after each word):").split(",")
search(word)
f.close()