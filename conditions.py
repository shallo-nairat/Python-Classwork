def print_numbers(n):
    numbers= range(n)
    for number in numbers:
        print(number)


def print_even_numbers(n):
    numbers = range(n)
    for number in numbers:
        if number %2 ==0:
            print(f"{number}is even")
        else:
            print(f"{number}is odd")

# using the else statement
def odd_or_even(n):
    numbers = range(n)
    for number in numbers:
        if number %2 ==0:
            print(f"{number}is even")
        else:
            print(f"{number}is odd")

# using the elif statement
def check_divisibility(n):
    numbers = range(n)
    for number in numbers:
        if number%2==0:
            print(f"{number} is divisible by 2")
        elif number%3==0:
            print(f"{number} is divisible by 3")
        elif number%5==0:
            print(f"{number} is divisible by 5")
        elif number%7==0:
            print(f"{number} is divisible by 7")
        else:
            print(f"{number} is divisible by 2,3,5 and7 ")

# while loop 
def countdown(n):
    while n >0:
        print(n)
        n-=1

def count_down_to_five(n):
    while n>0:
        print(n)
        if n==5:
         break
        n-=1

# continue statement

def divisible_by_seven(n):
    x=1
    while x<=n:
        x+=1
        if x%7!=0:
            continue
        print(x)


# using if,else,elif create a function called fizzbuzz . The function accepts a number n and generates a range of 
# numbers from 0 to n
        
def fizz_buzz(z):
    numbers= range(z)
    for number in numbers:
        if number%3==0:
           print(f"{number} fizz")
        elif number%5 == 0:
           print(f"{number} buzz")
        else:
           print(f"{number} is fizzbuzz")
         
         


# Using while loop and continue , create a function to print
#  all the even numbers between 0 and 50
        
def print_numbers_to_fifty():
    x=0
    while x<50:
        x+=1
        if x%2!=0:
          continue
        print(x)
      
        
    