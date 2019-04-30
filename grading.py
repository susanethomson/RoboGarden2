
#grading
def grading():
    total=0
    abv=['st', 'nd', 'rd', 'th', 'th']
    for i in range(5):
        userInput=int(input(" Enter " +str(i+1)+ abv[i]+" grade between 0 and 20: "))
        total=total+userInput
    return total


sum1=grading() #grading() <- total
if sum1>= 85:
    print("Grade A")
elif 85<sum1 and sum1>=75:
    print("Grade B")
elif 75<sum1 and sum1>=65:
    print("Grade C")
elif 65<sum1 and sum1>=50:
    print("Grade D")
else:
    print("Grade FAIL")
    

    
