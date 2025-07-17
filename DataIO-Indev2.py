print('DataIO for Python (Indev)')
data= {}
while True:
    command = input('>_').split(' ')
    if command[0] == 'set':
        if len(command)==3:
            if command[2]=='auto':
                istype={'int':True,
                'float':True,
                'list':command[2][0]=='[' and command[2][len(command[2])-1]==']',
                'dict':command[2][0]=='{' and command[2][len(command[2])-1]=='}'}
                for i in command[2]:
                    istype['int']=istype['int'] and (int(i) in range(1,10))
                for i in command[2]:
                    istype['float']=istype['float'] and (i in ['1','2','3','4','5','6','7','8','9','0','.'])
                for i in istype:
                    if istype[i]:
                        try:
                            command[2]=eval(command[3]+'('+i+')')
                        except:
                            istype[i]=False
                command[2]='str'
                for i in istype:
                    if istype[i]:
                        command[2]=i
            try:
                command[2]=eval(command[2]+'('+command[1]+')')
            except Exception as e:
                print('Type translation failed! Exception: '+type(e)+':'+str(e))
        data[command[1]] = command[2]
        print('Sucsessful setted '+command[1]+' to ' + command[2]+'. (type:'+command[3]+')')
        print(data)
    elif command[0] == 'read':
        try:
            print('The value of ' + command[1]) + ' is ' + str(data[command[1]])+'. (type: '+type(data[command[1]])+' )')
        except Exception as e:
            print("It looks like there's no variable called: "+command[1]+'. Exception: '+type(e)+':'+str(e))
    elif command[0] == 'del':
        if input(('(y/n) Confirn for deleting variable: ' + command[1])) == 'y':
            try:
                data.pop(command[1])
                print('Deleted sucsessful.')
            except Exception as e:
                print("It looks like there's no variable called: " + command[1]+'. Exception: '+type(e)+':'+str(e))
    elif command[0]=='json':
        print(data,'\n\nPrinted DataIO as JSON')
    else:
        print('Unknown command')
