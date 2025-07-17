print('DataIO for Python (Indev)')
data= {}
while True:
    command = input('>_').split(' ')
    if command[0] == 'set':
        data[command[1]] = command[2]
        print((('Sucsessful setted ' + command[1]) + (' to ' + command[2])))
        print(data)
    elif command[0] == 'read':
        try:
            print((('The value of ' + command[1]) + (' is ' + data[command[1]])))
        except Exception as e:
            print((("It looks like there's no variable called: " + command[1]) + ('. Exception: ' + str(e))))
    elif command[0] == 'del':
        if input(('(y/n) Confirn for deleting variable: ' + command[1])) == 'y':
            try:
                data.pop(command[1])
                print('Deleted sucsessful.')
            except Exception as e:
                print("It looks like there's no variable called: " + command[1]+'. Exception: '+str(e))
    else:
        print('Unknown command')
