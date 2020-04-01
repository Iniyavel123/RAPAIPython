# Print the repeating numbers and the number of times they repeat

# Function to count frequency
def ctFreq(mylist): 
  
    # Creating an empty dictionary  
    freq = {} 
    for item in mylist: 
        if (item in freq): 
            freq[item] += 1
        else: 
            freq[item] = 1
  
    for key, value in freq.items(): 
        if value > 1:
            print ("%d - %d"%(key, value)) 

# Input 
mylist1 =[1, 2, 3, 5, 8, 4, 7, 9, 1, 4, 12, 5, 6, 5, 2, 1, 0, 8, 1] 
ctFreq(mylist1) 