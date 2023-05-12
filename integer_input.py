def integer_input(msg,msg2):
    n , m = input(msg) , input(msg2)
    if n.isdigit() and m.isdigit():
        return n,m
    else:
        print("숫자가 아닙니다.")
    

test = integer_input('a : ','b : ')
print(test)