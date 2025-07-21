import hashlib #用于哈希加密功能
print('DataIO for Python (v1.0)')
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
                if istype.values()==[False,False,False,False]:
                    print('Unknown or unsupported type: '+command[2]+'. Setted to default(str).')
            try:
                command[2]=eval(command[2]+'('+command[1]+')')
            except Exception as e:
                print('Type translation failed! Exception: '+type(e)+':'+str(e))
                continue

        data[command[1]] = command[2]
        print('Sucsessfully setted '+command[1]+' to ' + command[2]+'. (type:'+command[3]+')')
        print(data)
    elif command[0] == 'read':
        try:
            print('The value of ' + command[1] + ' is ' + str(data[command[1]])+'. (type: '+type(data[command[1]])+' )')
        except Exception as e:
            print("It looks like there's no variable called: "+command[1]+'. Exception: '+type(e)+':'+str(e))
            continue
    elif command[0] == 'del':
        if input(('(y/n) Confirn for deleting variable: ' + command[1])) == 'y':
            try:
                data.pop(command[1])
                print('Deleted sucsessful.')
            except Exception as e:
                print("It looks like there's no variable called: " + command[1]+'. Exception: '+type(e)+':'+str(e))
                continue
    elif command[0]=='json':
        print(data,'\n\nPrinted DataIO as dict.')
    elif command[0]=='save':
        f=open(command[1],'w')
        f.write(str(data))
        f.close()
        print('Sucsessfully saved DataIO to '+command[1]+'.')
    elif command[0]=='open':
        try:
            f=open(command[1],'r')
        except:
            print('This file may not exist. Check if your path, filename, etc. is correct.')
            continue
        try:
            data=dict(f.read())
            print('Readed file sucsessful. Reseted DataIO to the file.')
        except:
            print('Not a DataIO, JSON or dictionary file.')
            continue
    elif command[0]=='append':
        try:
            f=open(command[1],'r')
        except:
            print('This file may not exist. Check if your path, filename, etc. is correct.')
            continue
        try:
            data2=dict(f.read())
            print('Readed file sucsessful.')
        except:
            print('Not a DataIO, JSON or dictionary file.')
            continue
        for i in data2:
            data[i]=data2[i]
            print('Appended variables in the file to DataIO.')
    elif command[0]=='append-to':
        
        try:
            f=open(command[1],'r')
        except:
            print('This file may not exist. Check if your path, filename, etc. is correct.')
            continue
        try:
            data2=dict(f.read())
            print('Readed file sucsessful.')
        except:
            print('Not a DataIO, JSON or dictionary text file.')
            continue
        for i in data:
            data2[i]=data[i]
            f.close()
            f=open(command[1],'w')
            f.write(str(data2))
            f.close()
            print('Appended variables from DataIO to the file.')
    elif command[0]=='compare':
        print(data[command[1]]+'\n'+data[command[2]])
        maxx=0
        if len(data[command[1]])>len(data[command[2]]):
            maxx=1
            data[command[2]]+=' '*len(data[command[1]])-len(data[command[2]])
        elif len(data[command[1]])==len(data[command[2]]):
            maxx=2
        else:
            maxx=2
            data[command[1]]+=' '*len(data[command[2]])-len(data[command[1]])
        sum=0
        for i in range(len(command[maxx])-1):
            if data[command[2]][i]!=data[command[1]][i]:
                print('*',end='')
                sum+=1
            else:
                print(' ',end='')
        print('\n'+sum+' differences between '+command[1]+' and '+command[2])
    elif command[0]=='hash':
        if command[2] in ['md5','sha1','sha224','sha256','sha384','sha512','sha3_224','sha3_256','sha3_384','sha3_512','scrypt','shake_128','shake_256']:
            data[command[1]]=eval('hashlib.'+command[2]+'('+data[command[1]]+').hexdigest()')
        else:
            print('Unknown hash type: '+command[2])
    else:
        print('Unknown command. Check your keywords carefully.')
