def input_string():
    words=input("enter the string:")
    return words

def add_space(call):
    call='    '.join(call)
    return call

def encryption(call):
    call='bajhfba'.join(call)
    return call

def decrypt(call):
    remove_call=call.replace('    ',"")
    decode_call=remove_call.replace('bajhfba',"")
    return decode_call
     
call=input_string()
print(add_space(call))
print(encryption(call))
print(decrypt(call))