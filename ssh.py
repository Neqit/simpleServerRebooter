from pexpect import pxssh
s = pxssh.pxssh()
IP = '127.0.0.1' # server ip or name
USERNAME = 'root' # your username
PASS = 'root' # your password
if not s.login (IP, USERNAME, PASS):
    print ("SSH session failed on login.")
    print("Fail")
else:
    print ("SSH session login successful")
    s.sendline ('reboot')
    s.prompt()         # match the prompt
    #print (s.before)    # print everything before the prompt
    s.logout()
    print("Succes")
