# Get input from user
num = int(input("Enter an integer: "))

# Positive, Negative, or Zero
if num > 0:
    print("The number is Positive.")
elif num < 0:
    print("The number is Negative.")
else:
    print("The number is Zero.")

# Even or Odd
if num % 2 == 0:
    print("The number is Even.")
else:
    print("The number is Odd.")

# Prime check
if num <= 1:
    print("The number is Not Prime.")
else:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print("The number is Prime.")
    else:
        print("The number is Not Prime.")
