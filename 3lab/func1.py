"""A recipe you are reading states how many grams you need for the ingredient. 
Unfortunately, your store only sells items in ounces. Create a function to convert grams to ounces. 
ounces = 28.3495231 * grams"""
'''
converter = lambda x: x*28.3495231
print(converter(5))
'''
"""Read in a Fahrenheit temperature. 
Calculate and display the equivalent centigrade temperature. 
The following formula is used for the conversion: C = (5 / 9) * (F - 32)"""
'''
converter2 = lambda F: (5 / 9) * (F - 32)
print(converter2(60))
'''
"""Write a program to solve a classic puzzle: We count 35 heads and 94 legs among the chickens and rabbits in a farm. 
How many rabbits and how many chickens do we have? create function: solve(numheads, numlegs):"""
'''
def solve(nh,nl):
    rab = (nl-nh*2)/2
    ch = nh-rab
    return (rab,ch)
sol = solve(35,94)
print(str(int(sol[0]))+" rabbits and "+str(int(sol[1]))+" chickens")
'''
"""You are given list of numbers separated by spaces. 
Write a function filter_prime which will take list of numbers as an agrument and returns only prime numbers from the list."""
'''
def isitprime(x):
    if x==1: return False
    for i in range(2,x):
        if x%i==0:
            return False
    return True

def filter_prime(l1):
    l=[]
    for i in l1:
        if (isitprime(i)):
            l.append(i)
    return l

l1 = [1,2,3,4,5,6,7,8,9,10]
print (filter_prime(l1))
'''
"""Write a function that accepts string from user and print all permutations of that string."""
'''
list_of_permutations = []
def all_permutation(list1,string1=''):
    if len(list1)==1:
        list_of_permutations.append(string1+list1[0])
    else:
        for i in range(len(list1)):
            all_permutation(list1[:i]+list1[i+1:],string1+list1[i])
all_permutation(list("abcde"))
print(list_of_permutations)
'''
"""Write a function that accepts string from user, return a sentence with the words reversed. We are ready -> ready are We"""
'''
def reverser():
    s = input()
    return s[::-1]

print(reverser())
'''
"""Given a list of ints, return True if the array contains a 3 next to a 3 somewhere."""
'''
def has_33(nums):
    i=1
    while i<len(nums):
        if nums[i]==nums[i-1]: return True
        i+=1
    return False
nums = [1,2,3,4,5,3,3,6]
print(has_33(nums))
'''
"""Write a function that takes in a list of integers and returns True if it contains 007 in order"""
'''
def spy_game(num):
    string = ''.join(num)
    if "007" in string: return True
    else: return False

num = [1,2,3,4,0,0,7,8]
print(spy_game(map(lambda x:str(x),num)))
'''
"""Write a function that computes the volume of a sphere given its radius."""
'''
vol = lambda r:(3.14*4*r**3)/3
print(vol(3))
'''
"""Write a Python function that takes a list and returns a new list with unique elements of the first list. Note: don't use collection set."""
'''
def unique(l2):
    dict = {}
    for i in l2:
        dict[i]=0
    return dict.keys()
l2 = [1,2,3,4,4,4,5,6,5,1]
print(list(unique(l2)))
'''
"""Write a Python function that checks whether a word or phrase is palindrome or not. 
Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam"""
'''
def ispalindrome(s):
    if len(s)==1: return True
    elif len(s)==2:
        if s[0]==s[1]: return True
        else: return False
    else:
        if s[0]==s[len(s)-1]:
            return ispalindrome(s[1:-1])
        else: return False
print(ispalindrome("saippuakivikauppias"))
'''
"""Define a function histogram() that takes a list of integers and prints a histogram to the screen. 
For example, histogram([4, 9, 7]) should print the following:"""
'''
def histogram(l3):
    m = max(l3)
    while 0<=m:
        for i in l3:
            if i>=m: print('* ',end='')
            else: print('  ',end='')
        m-=1
        print("")
l3 = [3,9,5,7,1,8]
histogram(l3)
'''
"""Write a program able to play the "Guess the number" - game, where the number to be guessed is randomly chosen between 1 and 20. 
This is how it should work when run in a terminal:"""
'''
from random import randint as rn
def Guessing_Game():
    name = input("Hello! What is your name?\n")
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    randomn = rn(1,20)
    g = 1
    n = 0
    while randomn!=n:
        n = int(input("Take a guess.\n"))
        if n == randomn: print(f"Good job, KBTU! You guessed my number in {g} guesses!")
        elif abs(randomn-n)<2: print(f"Wow,it is so close! Keep going!")
        elif abs(randomn-n)<6: print(f"Warmer, try again!")
        else: print("Way off, c'mon you can do better!")
        g+=1
ans = "Yes"
while ans=="Yes":
    Guessing_Game()
    ans = input("Would you like to play again? Enter Yes or No\n")
'''