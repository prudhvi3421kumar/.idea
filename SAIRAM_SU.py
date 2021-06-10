name=input("enter the File:")
handle=open('D://Prudhvi//2019//Python_Learning//.idea//New Text Document.txt','r')
counts=dict()
for line in handle:
    words=line.split()
    for word in words:
        counts[word]=counts.get(word,0)+1
    print(len(words))

# bigCount=None
# bigword=None
# for word,count in counts.items():
#     if bigCount is None or count>bigCount:
#         bigword=word
#         bigCount=count
# print(bigword,bigCount)
# print(name)