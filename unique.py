
def nsquared(word):
# O(n^2): Nested for loops will achieve this complexity
    for i, char in enumerate(word):
        #Compare each character in the string to all succeeding characters.
        for index in range(i+1, len(word)):
           if (char == word[index]):
               return "Not distinct"
    return "Distinct characters"


# O(nlogn): Traverse a list linearly.
def nlogn(word):
    # Sort the characters in the string in ascending order; 
    word = sorted(word)
    compare = None
    for char in word:
        # compare one character to the next.
        if (char == compare):
            return "Not distinct"
        compare = char
    return "Distinct characters"


#O(n)
def nnotation(word):
    #Create a set from the list of chars
    distinctchars = set(word)
    #Compare their lengths
    if (len(word) == len(distinctchars)):
        return "Distinct characters"
    return "Not distinct"


##test function##
def test():
    stringfunc = [nsquared, nlogn, nnotation]
    tries = [("Programming", "Not distinct"), ("Talking", "Distinct characters")] 
    for func in stringfunc:
        for arg, result in tries:
            assert func(arg) == result



if __name__ == "__main__":
    test()
    