# Daniel Blanco, Advanced Functions

#1. What is a helper function?
    #Function called inside of a function to complete part of the task
def check_input(user_txt):
        return not any(char.isdigit() for char in user_txt)

def hello (name):
    if check_input(name):
        print(f"Hello {name}!")
    else:
        print("Okease only input letters.")
        user = input("what is your name:\n").strip().capitalize

        hello(user)

#2. What is the purpose of a helper function?
    #To make your functions simpler
#3. What is an inner function?
    #A function inside of another function thats defined
def fun1():
    msg = "this is the outer function"

    def fun2():
          print(msg)
    fun2()
fun1()
#4. What is the scope of a variable in a function WITH an inner function
    #It us local, which includes the inner function
#5. Why do we use inner functions?
    #Acces to local variables without needing to pass info in parameters
    #To organize parts of your functions
#6. What is a closure function?
    #A function object that remembers values in enclosing scopes even if they are not currently in memory.
def fun(a):
     #Outer function, remembers the value of a

    def adder(b):
        return a+b
    return adder # returning the closure

val = fun(10)

print(val(5))


#7. Why do we write closure functions?
    #To decrease the number of parameters

def end(income):
     
    def calc(cost, type):
          percent = cost/income *100
          print(f"Your {type} is ${cost:.2f} and that is {percent:.0f}")
    return calc

def user_input(type):
     return int(input(f"What is your monthly {type}: \n$"))

income = user_input("Income")
rent = user_input("rent")
utilities = user_input("utilities")
transportation = user_input("transportation")

ready = end(income)

ready(rent, "rent")
ready(utilities, "utilities")
ready(transportation, "transportation")


#8. What is recursion?
    #When you call a function inside of itself
#9. how does recursion work?
    #The function runs itself again



#the wrapper function mostly exists to keep the inner function from the rest of the code
