def input_numbers():
    numbers=int(input("enter the integer:"))
    return numbers

def factor(call):
    prime=0
    for i in range(call,0,-1):
        if call%i==0:
            prime+=1
    if prime == 2:
        print(f"{call} is a prime number.")
    else:
        print(f"{call} is not a prime number.")
call=input_numbers()
result=factor(call)
