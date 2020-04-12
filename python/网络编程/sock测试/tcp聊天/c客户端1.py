import socket
c=socket.socket()
c.connect(("127.0.0.1",9020))

while True:
    msg=c.recv(1024).decode("utf-8")
    if msg=="0":
        c.close()
        break
    print(msg)
    sen_msg=input(">>>").encode("utf-8")
    c.send(sen_msg)

c.close()
