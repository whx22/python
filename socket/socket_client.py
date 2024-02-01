import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("127.0.0.0", 1234))
    s.sendall(b"Hello, Ross!")  # 字节序列
    data = s.recv(1024)
    print("Received : ", repr(data))