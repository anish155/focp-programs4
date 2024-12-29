def input_string():
    words=input("enter any string:")
    return words

def space_cancellation(call):
    remove_call=call.replace(" ","")
    return remove_call

def encryption(call):
    encrypt_call=call[::-1]
    return encrypt_call

call=input_string()
call_rmspace=space_cancellation(call)
print(encryption(call_rmspace))
