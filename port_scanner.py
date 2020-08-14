import socket


class Scanner:
    def __init__(self, ip):
        self.ip = ip
        self.open_ports = [];

    def __repr__(self):
        return 'Scanner: {}'.format(self.ip)

    def scan(self, lowerport, upperport):
        pass

    def is_open(self, port):
        pass

    def write(self, filepath):
        pass


def main():
    ip = '192.168.1.38'
    scanner = Scanner(ip)
    print(repr(scanner))




if __name__ == '__main__':
    main()
