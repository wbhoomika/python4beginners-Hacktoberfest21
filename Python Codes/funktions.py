"""
    Here we learn to write and use simle functions.
"""

def first_function():   # Every function begins with def , follow with the name and tho prerentecis. Add then a colon at the end.
    print(f"This is a simple function.")
    print(f"Wen we use the this function, python will show us this message.")

first_function()        # Here we cal the funktion

"""
    But we can make this a lot more dynamic.
"""

def second_function(foo):   # Here we add an value to the function
    print(foo)              # Print our value 

second_function(f"Just another value!")

"""
    More interactiv? No problem!

    You can use an variable to past your value like this.py

    bar = input("Enter your value. ")
    second_function(bar)

    Or the shorter way…
"""

second_function(input(f"Just give me a value.: "))  # Here we call the input function directly as value. 

""" 
    If you want to set a value as default is this the way to go…
"""

def third_function(foo="You don't give me any value to print."):    # We set a default value for foo
    print(foo)

third_function()    # A call from the third_function without any value.
third_function(input(f"The second call from the third_function. Now we overwrite the default value from foo. "))  # If you just press return, so you send an empty value. 
third_function()    # Just a check. You see, foo is not set and the standard value is print again.
