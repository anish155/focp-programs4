def input_numbers():
    numbers=int(input("enter the integer:"))
    return numbers

def factor(call):
    lst=[]
    i=1
    while i <= call:
        if call % i == 0:
            lst.append(i)
        i+=1 
    return lst

call=input_numbers()
result=factor(call)
print(result)
