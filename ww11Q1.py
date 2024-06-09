try:
    num=int(input())
    if (num<=100 and num>=1):
        print("Valid input.")
    else:
        print("Error: Number out of allowed range")
except ValueError:
    print("Error: invalid literal for int()")
