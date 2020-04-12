import socket
import threading


def Conversation(conn,addr):
    print(str(addr)+"开始链接")
    send_msg="欢迎使用".encode("utf-8")
    conn.send(send_msg)
    while True:
        msg=conn.recv(1024).decode("utf-8")
        print(msg)
        send_msg=input(">>>").encode("utf-8")
        conn.send(send_msg)


    conn.close()


def main2():
    s=socket.socket()
    s.bind(("192.168.130.100",9001))
    s.listen(5)
    print("服务器启动,并监控")
    while True:
        conn,addr=s.accept()
        Conversation(conn,addr)

def main():
    s=socket.socket()
    s.bind(("127.0.0.1",9020))
    s.listen(5)
    print("服务器启动,并监控")
    while True:
        conn,addr=s.accept()
        print(str(addr)+"开始链接")
        send_msg="欢迎使用".encode("utf-8")
        conn.send(send_msg)
        while True:
            msg=conn.recv(1024).decode("utf-8")
            if msg == "0":
                conn.close()
                break
            print(msg)
            send_msg=input(">>>").encode("utf-8")
            conn.send(send_msg)
            

        conn.close()
        
    s.close()

if __name__ == "__main__":
    main()