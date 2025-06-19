def even_or_odd(number):
    try:
        number = int(number)
        if number % 2 == 0:
            return "Even"
        else:
            return "Odd"
    except ValueError:
        return "please use an integer, a whole number"
    
    result = even_or_odd()
    print(result)
    
    #I had to fight for a second, I originally used input() instead of just using number
    #I don't know, this is my first time on Codewars and I wasn't sure how it would test me
    #After that, I had to make Even and Odd capitalized for the test to complete.
    
    def number_to_string(num):
    string_number = str(num)
    return str(num)
#So, I'm still not compleeeetely sure how to accept the sample tests from Codewars
#but I don't know, Like, I can make a function, but making sure it takes the test cases
#as input is, wild.


8 kyu
Remove String Spaces
Python:
def no_space(x):
    return x.replace(" ", "")
#after three Kata, I have realized: I'm blind,
#don't mind me