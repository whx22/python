# use socket build simple server
import socket

# AF_INET : ipv4 address family
# SOCK_STREAM : use TCP protocol
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(("0.0.0.0", 1234))   # 0.0.0.0 表示主机上的任意网卡可以使用该socket通信
    s.listen()  # 将s_socket置为监听状态
    # socket s : use listen
    # socket c : communication with client
    c, addr = s.accept()
    with c:
        print(addr, "connected.")

        while True:
            data = c.recv(1024)
            if not data:
                break
            c.sendall(data)
