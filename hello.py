def hello(name): 
    print(f"Hello {name}")


def year_of_birth(name,age):
    year=2024 - age
    print(f"Hello {name}, you were born in{year}")

def my_country(country="Uganda"):
    print(f"Hello Akirachix from{country}")

# args  
def greet(*name):
    print(f"Hello{name}")  

# kwargs
def create_sentence(**words):
    print(words)
    sentence=" "
    for word in words.values():
        sentence+=word
        sentence+="  "
    return sentence   
# args and kwargs
def sum_and_greet(*args,**kwargs):
    total=0
    for x in args:
        total+=x
    f=kwargs["First_name"]
    l=kwargs["Last_name"]
    greeting =f"Hello{f}{l},total of your numbers is {total}"
    return greeting
 
