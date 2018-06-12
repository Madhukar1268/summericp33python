t=set("aeiou") #put the vowels in set
p=input('text') # This is to input the values
num= 0          #Intilaize the count as zero
for m in p:    #for some value in the input
 if m in t:    #if the some value is in t
  num=num + 1  #increment the count

print(num)    #print that count value


