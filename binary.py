def input_number():
    number=int(input("enter the integer:"))
    return number
def binary_convert(number):
    binary=format(number,'b')
    return binary
number=input_number()
print(binary_convert(number))