
#list_math.py
alist=[]
def count(aList):
    return len(aList)
    #length=how many items are in the list
def total(aList):
    return sum(aList)
    #total=sum of the items in the list
def average(aList):
    return total(aList)/count(aList)
    #averageOfNums=total/count


def maximum(aList): #creates tuple to include maximum value in a list, and where in the list that maximum is
    maximumNum=max(aList)
    whereMax=aList.index(maximumNum)
    maxTuple=(maximumNum,whereMax)
    return maxTuple
    
def minimum(aList): #creates tuple to include minimum value in a list, and where in the list that minumum is
    minimumNum=min(aList)
    whereMin=aList.index(minimumNum)
    minTuple=(minimumNum, whereMin)
    return minTuple


    
    
    

    

    
