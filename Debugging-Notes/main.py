# Daniel Blanco, Debugging/tracing notes

#What is tracing?
# - It lets you see what is happening with your functions.
#python -m trace --trackcalls C:\Users\daniel.blanco\CP2-Projects\Debugging-Notes\main.py

""""

--trace (displays function lines as they are executed)
--count (displays the number of items each function is executed)
--listfuncs (displays the functions in the projects)
--trackcalls (displays the relationships between the functions)
"""
import trace
import sys

tracer = trace.Trace(count=False, trace=True)
def trace_calls(frame, event, arg):
    if event == 'call':
        print(f'calling function: {frame.f_code.co_name}')
    elif event == 'line':
        print(f'executing line: {frame.f_lineno} in {frame.f_code.co_name}')
    elif event == 'return':
        print(f'{frame.f_code.co_name} returned {arg}')
    elif event == 'exception':
        print(f'exception in {frame.f_code.co_name}: {arg}')
    return trace_calls

sys.settrace(trace_calls)
""""

Event types:
call - When the function is called
line - when a new line is executed
return - when the function returns a value
exception - when there is an exception raised
"""

#What are some ways we can debug by tracing?
    # - So we can make a function that checks the specifics for us.
#How do you access the debugger in VS Code?
    # - By pressing F5 go to top right, click arrow, and select python debugger: debug python file.
#What is testing?
    # - Going through the code trying to break it, and having testers that are not the programmers.
#What are boundary conditions?
    # - User conditions that are strange and/or likely to cause issues.
age = 18
if age >= 18:
    print("you can vote")
elif age >= 16:
    print("You can drive")
elif age == 15:
    print("You can get your learners permit")
elif age >= 5:
    print("you can go to school")
else:
    print("You're too young for anything")
#How do you handle when users give strange inputs?
    # - After printing they have inputted something wrong you loop back so they can input correctly.

def sub(numone, numetwo):
    print( numone-numetwo)


def add(numone, numetwo):
    sub(numone, numetwo)
    return numone+numetwo

print(add(5,4))
sub(8,2)
#tracer.run('sub(8,2)')