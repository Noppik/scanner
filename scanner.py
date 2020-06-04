import socket
import sys

start = int(sys.argv[1])
end = int(sys.argv[2])
ip = sys.argv[3]
print('Checking:')
for port in range(start, end):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.1)
    try:
        con = s.connect((ip, port))
        print('Port ' + str(port) + ' open')
        con.close()
    except:
        pass

