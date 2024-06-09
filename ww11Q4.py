try:
    a=int(input())
    if a>0:
        print("You are",a,"years old.")
    else:
        print("Error: Please enter a valid age.")
except EOFError:
    print("Error: Please enter a valid age.")
except ValueError:
    print("Error: Please enter a valid age.")
