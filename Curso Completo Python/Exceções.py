try:
    for i in ['a','b','c']:
        print(i**2)
except:
    print('ocorreu um erro')
try:
    x = 5
    y = 0
    z = x/y
except:
    print('erro ao fazer essa divisão')
finally:
    print('all done')


while True:
    try:
        val = int(raw_input("Please enter an integer: "))
    except:
        print("Looks like you did not enter an integer!")
        continue
    else:
        print('Yep thats an integer!')
        break
    finally:
        print("Finally, I executed!")
    print(val)