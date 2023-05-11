import json

def writeFile(func):
    def wrap_func(a,b):
        if type(a) == int and type(b) == int:
            key_data = ['a', 'b', 'a+b']
            value_data = [a, b, func(a,b)]
            
            data = dict(zip(key_data,value_data)) 
            f = open('result.txt', 'w')
            s = json.dumps(data, indent=4)
            f.write(s)
            f.close()
            return print('성공')
        else:
            return print('실패')
    return wrap_func

@writeFile
def add(a,b):
    return a + b

add(11,12)