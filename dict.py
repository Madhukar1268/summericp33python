def word_count(string):
    my_string = string.split()    #This will split the string
    my_dict = {}
    for item in sorted(my_string): #This makes the items in a sorted way
        if item in my_dict:        #check if this item is in my_dict
            my_dict[item] += 1     #increment it
        else:                      #otherwise
            my_dict[item] = 1      #count=1
    print(my_dict)                 #print my_dict
x=input('text')                    #input thae text
word_count(x)                      #count the words

