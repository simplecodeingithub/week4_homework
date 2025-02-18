# try: <code>  # Block where you write code that might raise an error
# except <ExceptionType>: <handle error>  # Block that catches and handles specific exceptions
# finally: <cleanup>  # Block that always runs, used for cleanup or final steps
names_tuple = 'Red', 'Jane', 'Freddy'

try:
    print("######## TRY ########")
    print("The TRY attempts to run")
    print(f"Original Tuple: {names_tuple}")
    names_sorted_as_list = sorted(names_tuple)
    print(names_sorted_as_list)
    names_sorted_as_list.append("Bungle")
    print("Added Bungle:", names_sorted_as_list)
    print("Attempt to manipulate the tuple...")
    names_tuple[0] = 'Zippy'   # This raises a TypeError because tuples are immutable.
    print("Is this code reached?")
except FileNotFoundError as error:
    print("########### EXCEPT: FileNotFoundError ######")
    print("The EXCEPT / CATCH block only runs if this error happens")
    print(f"The following file can not be found: {error.filename}.Please try another file")
except TypeError as error:  #The as error part catches that exception and stores it in the variable (error).
    print("########### EXCEPT: TypeError ######")
    print("Oh dear, that is not allowed on that type")
    print(error)  # This will print: 'tuple' object does not support item assignment
except Exception as error:
    print("########### EXCEPT: Exception ######")
    print("Generic catch-all except / catch block")
    print(error)
finally:
    # Always close file handle after use
    print("The FINALLY block ALWAYS runs")
    print("The finally block is used to tidy up")
    if names_tuple:
        names_tuple = None


print("After exception handling is finished...the program can continue")
