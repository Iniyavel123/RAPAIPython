# Calculate the total sum paid by all people

# Function to calculate amount
def amtpaid(myinput):
    
    sum = 0
    for i in myinput:
        sum = sum + myinput[i]
    
    return sum

# Input array
input1 = {"Rick": 85, "Amit": 42, "George": 53, "Tanya": 60, "Linda": 35}
print("The total sum paid is: ", amtpaid(input1))