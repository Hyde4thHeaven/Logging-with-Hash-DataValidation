import time, hashlib
def logging():
    f.write('username:'+username+'\n')
    f.write('password:'+password+'\n')
    f.write('Login Date: {}/{}/{} \n'.format(time.strftime('%d'), 
    time.strftime('%m'), int(time.strftime('%Y'))+543))
    f.write('Login Time: {}:{}:{} \n'.format(time.strftime('%H'), 
    time.strftime('%M'), time.strftime('%S')))

print('Welcome to Test Log file')

while True:
    username = input('Username: ')
    password = input('Password: ')
    hashuser = hash(username)
    hashpass = hash(password)

    if hashuser == hash('test') and hashpass == hash('1234'):
        print('Login Successful!!!!')
        f = open('db.txt', 'a')
        f.write(chr(92)*4+'Login Successful!!!!\n')
        logging()
        f.write('*'*40+'\n')
        f.close()
        break
    else:
        print('Your username or password is incorrect')
        f = open('db.txt', 'a')
        f.write(chr(92)*4+'Login Error!!!!\n')
        logging()
        f.write('*'*40+'\n')
        f.close()   



