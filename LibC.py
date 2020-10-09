import socket
hostname = '127.0.0.1'
port = 6666
addr = (hostname,port)
clientsock = socket.socket()
clientsock.connect(addr)

class index:

    def menu0(self):
        while True:
            clientsock.send(bytes("menu0", encoding='gbk'))
            recvdata = clientsock.recv(1024)
            print(str(recvdata, encoding='gbk'))
            button = input("请选择操作")
            clientsock.send(bytes(button, encoding='gbk'))

            if button == '1':
                clientsock.send(bytes(input("请输入ID"), encoding='gbk'))
                clientsock.send(bytes(input("请输入密码"), encoding='gbk'))
                recvdata = clientsock.recv(1024)
                print(str(recvdata, encoding='gbk'))
                recvdata = clientsock.recv(1024)
                print(str(recvdata, encoding='gbk'))
                index.menu1_1(0)

            elif button == '2':
                clientsock.send(bytes(input("请输入管理员ID"), encoding='gbk'))
                clientsock.send(bytes(input("请输入管理员密码"), encoding='gbk'))
                recvdata = clientsock.recv(1024)
                print(str(recvdata, encoding='gbk'))

                index.menu2_1(0)

            elif button == '3':
                clientsock.send(bytes(input("请输入书名"), encoding='gbk'))
                recvdata = clientsock.recv(1024)
                print(str(recvdata, encoding='gbk'))

            elif button == '4':
                clientsock.send(bytes(input("请输入用户ID"), encoding='gbk'))
                clientsock.send(bytes(input("请输入用户姓名"), encoding='gbk'))
                clientsock.send(bytes(input("请输入用户密码"), encoding='gbk'))
                recvdata = clientsock.recv(1024)
                print(str(recvdata, encoding='gbk'))
                index.menu0(0)

    def menu1_1(self):
        while True:
            clientsock.send(bytes("menu1_1", encoding='gbk'))
            recvdata = clientsock.recv(1024)
            print(str(recvdata, encoding='gbk'))
            button = input("请选择操作")
            clientsock.send(bytes(button, encoding='gbk'))

            if button == '1':
                clientsock.send(bytes(input("请输入ID"), encoding='gbk'))
                clientsock.send(bytes(input("请输入书名"), encoding='gbk'))
                recvdata = clientsock.recv(1024)
                print(str(recvdata, encoding='gbk'))
                # index.menu1_1(0)

            elif button == '2':
                clientsock.send(bytes(input("请输入书名"), encoding='gbk'))
                recvdata = clientsock.recv(1024)
                print(str(recvdata, encoding='gbk'))
                # index.menu1_1(0)

            elif button == '3':
                clientsock.send(bytes(input("请输入书名"), encoding='gbk'))
                recvdata = clientsock.recv(1024)
                print(str(recvdata, encoding='gbk'))
                # index.menu1_1(0)

            elif button == '4':
                clientsock.send(bytes(input("请输入ID"), encoding='gbk'))
                recvdata = clientsock.recv(1024)
                print(str(recvdata, encoding='gbk'))
                # index.menu1_1(0)

            elif button == '5':
                recvdata = clientsock.recv(1024)
                print(str(recvdata, encoding='gbk'))
                index.menu0(0)
                break


    def menu2(self):
        clientsock.send(bytes("menu2", encoding='gbk'))
        while True:
            clientsock.send(bytes("menu2", encoding='gbk'))
            recvdata = clientsock.recv(1024)
            print(str(recvdata, encoding='gbk'))
            button = input("请选择操作")
            clientsock.send(bytes(button, encoding='gbk'))

            if button == '1':
                clientsock.send(bytes(input("请输入管理员ID"), encoding='gbk'))
                clientsock.send(bytes(input("请输入管理员密码"), encoding='gbk'))
                index.menu2_1(0)
            elif button == '2':
                recvdata = clientsock.recv(1024)
                print(str(recvdata, encoding='gbk'))
                index.menu0(0)
            else:
                print("输入错误")
                index.menu2(0)


    def menu2_1(self):
        while True:
            clientsock.send(bytes("menu2_1", encoding='gbk'))
            recvdata = clientsock.recv(1024)
            print(str(recvdata, encoding='gbk'))


            button = input("请选择操作")
            clientsock.send(bytes(button, encoding='gbk'))

            if button == '1':
                clientsock.send(bytes(input("请输入用户ID"), encoding='gbk'))
                recvdata = clientsock.recv(1024)
                print(str(recvdata, encoding='gbk'))
                index.menu2_1(0)

            if button == '2':
                clientsock.send(bytes(input("请输入用户ID"), encoding='gbk'))
                clientsock.send(bytes(input("验证：请输入密码"), encoding='gbk'))
                recvdata = clientsock.recv(1024)
                print(str(recvdata, encoding='gbk'))

                index.menu2_1(0)

            if button == '3':
                clientsock.send(bytes(input("请输入用户ID"), encoding='gbk'))
                clientsock.send(bytes(input("请输入用户姓名"), encoding='gbk'))
                clientsock.send(bytes(input("请输入用户密码"), encoding='gbk'))
                recvdata = clientsock.recv(1024)
                print(str(recvdata, encoding='gbk'))
                index.menu2_1(0)

            if button == '4':
                clientsock.send(bytes(input("请输入图书ID"), encoding='gbk'))
                clientsock.send(bytes(input("请输入图书NAME"), encoding='gbk'))
                clientsock.send(bytes(input("请输入图书AUTHER"), encoding='gbk'))
                clientsock.send(bytes(input("请输入图书PRESS"), encoding='gbk'))
                clientsock.send(bytes(input("请输入图书NUM"), encoding='gbk'))
                recvdata = clientsock.recv(1024)
                print(str(recvdata, encoding='gbk'))
                index.menu2_1(0)

            if button == '5':
                clientsock.send(bytes(input("请输入书名"), encoding='gbk'))
                recvdata = clientsock.recv(1024)
                print(str(recvdata, encoding='gbk'))
                index.menu2_1(0)

            if button == '6':
                clientsock.send(bytes(input("请输入书名"), encoding='gbk'))
                recvdata = clientsock.recv(1024)
                print(str(recvdata, encoding='gbk'))
                index.menu2_1(0)

            if button == '7':
                recvdata = clientsock.recv(1024)
                print(str(recvdata, encoding='gbk'))
                index.menu0(0)
                break


    def menu3(self):
        while True:
            clientsock.send(bytes("menu2", encoding='gbk'))
            recvdata = clientsock.recv(1024)
            print(str(recvdata, encoding='gbk'))
            button = input("请选择操作")
            clientsock.send(bytes(button, encoding='gbk'))
            if button == '1':
                clientsock.send(bytes(input("请输入书名(带单引号)"), encoding='gbk'))
            else:
                index.menu0(0)


if __name__ == '__main__':
    index.menu0(0)