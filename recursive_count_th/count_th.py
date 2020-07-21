'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
""" def count_th(word):
    
    # TBC
    
    


 """


<<<<<<< HEAD
def  count_th(str1, str2 ='th'): 
      
    n1 = len(str1) # string
    n2 = len(str2) # substring
      
    # Base Case 
    if (n1 == 0 or n1 < n2): 
        return 0; 
  
    # Recursive Case 
    # Checking if the first 
    # substring matches 
    if (str1[0 : n2] == str2): 
        return count_th(str1[n2 - 1:],  
                             str2) + 1
  
    # Otherwise, return the count  
    # from the remaining index 
    return count_th(str1[n2 - 1:],  
                         str2)
  
  
# Test Code 
  

""" if __name__ == '__main__': 
       
    str1 = "gullithwertq"  
    str2 = "th" 
    print(count_th(str1, str2)) 
  
    str1 = "hikathkathsthhi"; 
=======
def count_th(str1, str2='th'):

    n1 = len(str1)
    n2 = len(str2)

    # Base Case
    if (n1 == 0 or n1 < n2):
        return 0

    # Recursive Case
    # Checking if the first
    # substring matches
    if (str1[0: n2] == str2):
        return count_th(str1[n2 - 1:], str2) + 1

    # Otherwise, return the count
    # from the remaining index
    return count_th(str1[n2 - 1:], str2)


# Test Code


if __name__ == '__main__':

    str1 = "gullithwertq"
    str2 = "th"
    print(count_th(str1, str2))

    str1 = "hikathkathsthhi"
>>>>>>> 0e571a5e24d662c7990cfeaa5dfa996eed551164
    str2 = "th"
    print(count_th(str1, str2))
