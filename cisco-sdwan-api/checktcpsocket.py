import socket

host='itbasetv.ddns.net'
port=9119
timeout_seconds=2
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(timeout_seconds)
result = sock.connect_ex((host,int(port)))
if result == 0:
    print("Host: {}, Port: {} - True".format(host, port))
else:
    print("Host: {}, Port: {} - False".format(host, port))
sock.close()