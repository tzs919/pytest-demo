import socket

client = socket.socket()

r = client.connect_ex(('localhost', 6969))  # 连接服务器
print(r)
while True:
    msg = input(">>:").strip()
    if len(msg) == 0:
        continue
    client.send(msg.encode())  # 发送数据

    client.settimeout(5)

    try:
        data = client.recv(2)  # 接收数据
        socket.timeout
    except Exception as e:
        print(type(e))

    print("返回数据:", data.decode())
    print(client.getpeername())

client.close()
