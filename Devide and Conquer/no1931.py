inputList=[]
outputList=[]
nowEndtime=-1
i=()
result=0

#input
numClass=int(input())
for j in range(0,numClass):
    i=list(map(int,input().split()))
    inputList.append(i)

#sort
inputList.sort(key=lambda x:x[1])

#first choice
outputList.append(inputList[0][0])
nowEndtime=inputList[0][1]
result=result+1

#choice 1) add to outputList 2) update nowEndtime
for i in inputList[1:]:
    if i[0]>=nowEndtime:
        outputList.append(i[0])
        nowEndtime=i[1]
        result=result+1
inputList=[]
outputList=[]
nowEndtime=-1
i=()
result=0

#input
numClass=int(input())
for j in range(0,numClass):
    i=list(map(int,input().split()))
    inputList.append(i)

#sort
inputList.sort(key=lambda x:x[1])

#first choice
outputList.append(inputList[0][0])
nowEndtime=inputList[0][1]
result=result+1

#choice 1) add to outputList 2) update nowEndtime
for i in inputList[1:]:
    if i[0]>=nowEndtime:
        outputList.append(i[0])
        nowEndtime=i[1]
        result=result+1


#print outputList
print(result)
#print(outputList)


#print outputList
print(result)
#print(outputList)
