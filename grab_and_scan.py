

from port_scanner import Scanner
from grabber import Grabber


def main():
    ip = '10.0.13.231'
    port_range = (1, 1001)
    scanner = Scanner(ip)
    scanner.scan(*port_range)
    for port in scanner.open_ports:
        grabber = Grabber(ip, port)
        print(grabber.read())
        grabber.close()



if __name__ == '__main__':
    main()
