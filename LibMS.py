import sqlite3
import pandas as pd
import re
import threading
import socket


hostname = '127.0.0.1'
port = 6666
addr = (hostname,port)
srv = socket.socket()
srv.bind(addr)
srv.listen(5)
print("waitting connect")

cont_book = sqlite3.connect('book.db')
book = cont_book.cursor()

cont_uesr = sqlite3.connect('user.db')
user = cont_uesr.cursor()

cont_borrow = sqlite3.connect('borrow.db')
borrowed=cont_borrow.cursor()

connect_socket, client_addr = srv.accept()
print(client_addr)



class index:

    def menu0(self):
        while True:
            connect_socket.send(bytes(str('''
            ________________xx图书馆系统_________________
                            1.用户登陆
                            2.管理员登陆
                            3.图书查询
                            4.注册新用户
            --------------------------------------------
                            '''), encoding='gbk'))
            recevent = connect_socket.recv(1024)
            print(str(recevent, encoding='gbk'))
            str_recevent = str(recevent, encoding='gbk')

            if str_recevent=='1':
                recevent1 = connect_socket.recv(1024)
                str_recevent1 = str(recevent1)[2:-1]
                print(str_recevent1)

                recevent2 = connect_socket.recv(1024)
                str_recevent2 = str(recevent2)[2:-1]
                print(str_recevent2)

                result=User.login(str_recevent1,str_recevent2)
                print(result)
                connect_socket.send(bytes(str(result), encoding='gbk'))

            elif str_recevent=='2':
                recevent1 = connect_socket.recv(1024)
                str_recevent1 = str(recevent1)[2:-1]
                print(str_recevent1)

                recevent2 = connect_socket.recv(1024)
                str_recevent2 = str(recevent2)[2:-1]
                print(str_recevent2)

                result=User.Adminlogin(recevent1,recevent2)
                print(result)
                connect_socket.send(bytes(str(result), encoding='gbk'))

            elif str_recevent=='3':
                recevent1 = connect_socket.recv(1024)
                str_recevent1 = str(recevent1, encoding='gb2312')
                print((str_recevent1))
                print(type(str_recevent1))
                result = books.seratch((str(str_recevent1)))
                print(result)
                connect_socket.send(bytes(str(result), encoding='gbk'))

            elif str_recevent=='4':
                recevent1 = connect_socket.recv(1024)
                str_recevent1 = str(recevent1)[2:-1]
                print(str_recevent1)

                recevent2 = connect_socket.recv(1024)
                str_recevent2 = str(recevent2, encoding='gbk')
                print(str_recevent2)

                recevent3 = connect_socket.recv(1024)
                str_recevent3 = str(recevent3)[2:-1]
                print(str_recevent3)

                result = User.adduser(str_recevent1, str_recevent2, str_recevent3)
                print(result)
                connect_socket.send(bytes(str(result), encoding='gbk'))

    def menu1_1(self):
        while True:
            connect_socket.send(bytes(str('''
    _______________XX图书馆用户系统___________________
                      1.借书
                      2.查找图书
                      3.还书
                      4.浏览借阅记录
                      5.退出
    ------------------------------------------------        
            '''), encoding='gbk'))

            recevent = connect_socket.recv(1024)
            print(str(recevent, encoding='gbk'))
            str_recevent = str(recevent, encoding='gbk')

            if str_recevent == '1':
                recevent1 = connect_socket.recv(1024)
                str_recevent1 = str(recevent1)[2:-1]
                print(str_recevent1)

                recevent2 = connect_socket.recv(1024)
                str_recevent2 = str(recevent2, encoding='gb2312')
                print(str_recevent2)

                result=User.userborrowbook(str(str_recevent1),str(str_recevent2))
                print(result)
                connect_socket.send(bytes(str(result), encoding='gbk'))

            elif str_recevent =='2':
                recevent1 = connect_socket.recv(1024)
                str_recevent1 = str(recevent1, encoding='gb2312')
                print((str_recevent1))
                print(type(str_recevent1))
                result = books.seratch((str(str_recevent1)))
                print(result)
                connect_socket.send(bytes(str(result), encoding='gbk'))


            elif str_recevent =='3':
                recevent1 = connect_socket.recv(1024)
                str_recevent1 = str(recevent1, encoding='gbk')
                print(str_recevent1)
                result=books.rebook(str_recevent1)
                print(result)
                connect_socket.send(bytes(str(result), encoding='gbk'))

            elif str_recevent =='4':
                recevent1 = connect_socket.recv(1024)
                str_recevent1 = str(recevent1)[2:-1]
                print(str_recevent1)
                result=User.borrowresult(str_recevent1)
                print(str(result))
                connect_socket.send(bytes(str(result), encoding='gbk'))

            elif str_recevent =='5':
                index.menu0(0)


    def menu2_1(self):
        while True:
            connect_socket.send(bytes(str('''
_____________XX图书馆管理员系统_________________
                1.查询用户
                2.删除用户
                3.新增用户
                4.新增图书
                5.删除图书
                6.查找图书
                7.退出
----------------------------------------------'''), encoding='gbk'))
            recevent = connect_socket.recv(1024)
            print(str(recevent, encoding='gbk'))
            str_recevent = str(recevent, encoding='gbk')

            if str_recevent=='1':
                recevent1 = connect_socket.recv(1024)
                str_recevent1 = str(recevent1)[2:-1]
                print(str_recevent1)
                result=User.seratchidforAD(str_recevent1)
                print(result)
                connect_socket.send(bytes(str(result), encoding='gbk'))


            if str_recevent=='2':
                recevent1 = connect_socket.recv(1024)
                str_recevent1 = str(recevent1)[2:-1]
                print(str_recevent1)

                recevent2 = connect_socket.recv(1024)
                str_recevent2 = str(recevent2)[2:-1]
                print(str_recevent2)

                result=User.deluser(str_recevent1,str_recevent2)
                print(result)
                connect_socket.send(bytes(result, encoding='gbk'))

            if str_recevent=='3':
                recevent1 = connect_socket.recv(1024)
                str_recevent1 = str(recevent1)[2:-1]
                print(str_recevent1)

                recevent2 = connect_socket.recv(1024)
                str_recevent2 = str(recevent2, encoding='gbk')
                print(str_recevent2)

                recevent3 = connect_socket.recv(1024)
                str_recevent3 = str(recevent3)[2:-1]
                print(str_recevent3)

                result=User.adduser(str_recevent1,str_recevent2,str_recevent3)
                print(result)
                connect_socket.send(bytes(str(result), encoding='gbk'))

            if str_recevent=='4':
                recevent1 = connect_socket.recv(1024)
                str_recevent1 = str(recevent1)[2:-1]
                print(str_recevent1)

                recevent2 = connect_socket.recv(1024)
                str_recevent2 = str(recevent2,  encoding='gbk')
                print(str_recevent2)

                recevent3 = connect_socket.recv(1024)
                str_recevent3 = str(recevent3, encoding='gbk')
                print(str_recevent3)

                recevent4 = connect_socket.recv(1024)
                str_recevent4 = str(recevent4, encoding='gbk')
                print(str_recevent4)

                recevent5 = connect_socket.recv(1024)
                str_recevent5 = str(recevent5)[2:-1]
                print(str_recevent5)
                result=books.addbook(str_recevent1,str_recevent2,str_recevent3,str_recevent4,str_recevent5)
                print(result)
                connect_socket.send(bytes(str(result), encoding='gbk'))

            if str_recevent=='5':
                recevent1 = connect_socket.recv(1024)
                str_recevent1 = str(recevent1, encoding='gbk')
                print(str_recevent1)
                result=books.delbook(str_recevent1)
                print(result)
                connect_socket.send(bytes(str(result), encoding='gbk'))

            if str_recevent=='6':
                recevent1 = connect_socket.recv(1024)
                str_recevent1 = str(recevent1, encoding='gb2312')
                print((str_recevent1))
                print(type(str_recevent1))
                result = books.seratch((str(str_recevent1)))
                print(result)
                connect_socket.send(bytes(str(result), encoding='gbk'))

            if str_recevent=='7':
                index.menu0(0)

class books:

    def __init__(self,bookid,bookname,auther,press,num):
        self.bookid=bookid
        self.bookname=bookname
        self.auther=auther
        self.press=press
        self.num=num

    def isture(bookid,bookname,auther,press,num):
        return bookid,bookname,auther,press,num

    def numisture(num):
        if num==0:
            return False
        else:
            return True


    def seratch(self):
        beatuiful_table_book = pd.read_sql("SELECT "
                                           "bookid, bookname, auther, press, number "
                                           "FROM book "
                                           "WHERE bookname = '"+ self +"'",cont_book)
        pd.set_option('colheader_justify', 'left')
        print(beatuiful_table_book)
        return beatuiful_table_book


    def addbook(id,name,auther,press,num):
        book_information=books.isture(id, name, auther, press, num)
        # print(str(book_information))
        book.execute("INSERT INTO book VALUES"+str(book_information)+"")
        cont_book.commit()
        return "添加完成"

    def delbook(self):
        book.execute("DELETE FROM book WHERE bookname = '"+ self +"'")
        cont_book.commit()
        return "删除完成"

    def borrowbook(self):
        result=books.seratch(self)
        resultTF=books.numisture(int(result['number']))
        try:
            if resultTF==False:
                book.execute("UPDATE book SET number = number-1 WHERE bookname = '"+self+"'")
                cont_book.commit()
                print("借出成功")
                return "借出成功"
        except:
            return "没有库存了"

    def rebook(self):
        book.execute("UPDATE book SET number = number+1 WHERE bookname = '" + self + "'")
        cont_book.commit()
        return "还书成功"

class User:

    def __init__(self,userid,username,password):
        self.borrowid=userid
        self.username=username
        self.password=password

    def isture(userid,username,password):
        return userid,username,password


    def seratchid(self):
        beatuiful_table_user = pd.read_sql("SELECT "
                                           "user_id, username, password "
                                           "FROM user "
                                           "WHERE user_id = '"+ self +"'" ,cont_uesr)
        pd.set_option('colheader_justify', 'right')

        return beatuiful_table_user

    def seratchidforAD(self):
        beatuiful_table_user = pd.read_sql("SELECT "
                                           "user_id, username, password "
                                           "FROM user "
                                           "WHERE user_id = '" + self + "'", cont_uesr)
        pd.set_option('colheader_justify', 'right')
        print(beatuiful_table_user)
        return beatuiful_table_user

    def login(admin,adminpw):
        admin=admin
        result=User.seratchid(admin)
        # adminpw=int(adminpw)
        # print(int(result['password']))
        try:
            adminpw=int(adminpw)
            if adminpw == int(result['password']):
                connect_socket.send(bytes("login ok", encoding='gbk'))
                # connect_socket.send(bytes("恭喜您，登陆成功",encoding='gbk'))
                print("恭喜您，登陆成功")
                index.menu1_1(0)
            else:
                print("密码不正确")
                index.menu0(0)
        except :
            return "用户不存在"
            index.menu0(0)

    def Adminlogin(ad_admin,ad_adminpw):
        ad=ad_admin
        ad_pw=ad_adminpw
        if ad_adminpw==ad_pw and ad_admin==ad:
            index.menu2_1(0)
            return "恭喜您，登陆成功"
        # else:
        #     print("密码不正确")
        #     index.menu0(0)

    def adduser(id,name,password):
        try:
            newuser=User.isture(id,name,password)
            user.execute("INSERT INTO user VALUES" + str(newuser)+ "")
            cont_uesr.commit()
            result=("注册成功,您的ID是{id},姓名是{n},密码是{p}".format(id=newuser[0],n=newuser[1],p=newuser[2]))
            print(result)
            return result
        except:
            return "抱歉，该ID已被注册"

    def deluser(self,yanzheng):
        try:
            inputpassword = User.seratchid(self)
            #print(int(inputpassword['password']))
            user.execute("DELETE FROM user WHERE user_id = '"+ self +"'")
            yanzheng=yanzheng
            if int(yanzheng)==int(inputpassword['password']):
                # print('用户删除成功')
                cont_uesr.commit()
                # index.menu2_1(0)
                return '用户删除成功'
            else:
                # print("密码不正确")
                # index.menu2_1(0)
                return '密码不正确'
        except:
            return "无此用户"

    def userborrowbook(uesrid,bookname):
        try:
            result=books.seratch(bookname)
            inputpassword = User.seratchid(uesrid)
            # yanzheng = input("验证：请输入密码")
            # if int(yanzheng) == int(inputpassword['password']):
            books.borrowbook(bookname)
            he=re.findall('book[0-9][0-9][0-9]',str(result['bookid']))
            # print(str(he)[2:9])
            borrowed.execute("INSERT INTO borrow VALUES ('"+str(he)[2:9]+"','"+str(int(inputpassword['user_id']))+"')")
            cont_borrow.commit()
            # index.menu1_1(0)
            return "借书成功"
        except:
            return "书不在架上"

    def borrowresult(nameid):
        result=pd.read_sql("SELECT bookid, name_id "
                            "FROM borrow "
                            "WHERE name_id = '"+ str(int(nameid)) +"'",cont_borrow)
        # 显示所有列
        pd.set_option('display.max_columns', None)
        # 显示所有行
        pd.set_option('display.max_rows', None)
        # 设置value的显示长度为100，默认为50
        pd.set_option('max_colwidth', 100)

        resultbookid=result['bookid']
        result=[]
        for i in resultbookid:
            beatuiful_table_bookid = pd.read_sql("SELECT "
                                           "bookname, auther, press "
                                           "FROM book "
                                           "WHERE bookid = '" + i + "'", cont_book)
            result.append(beatuiful_table_bookid)
        return result

if __name__ == '__main__':
    thread_menu = threading.Thread(target=index.menu0(0))
    thread_login = threading.Thread(target=User.login(0))
    thread_Adlogin = threading.Thread(target=User.Adminlogin(0))
    thread_borrow = threading.Thread(target=books.seratch())
    thread_seratch = threading.Thread(target=books.seratch())

    thread_menu.start()
    thread_login.start()
    thread_Adlogin.start()
    thread_borrow.start()
    thread_seratch.start()

    thread_menu.join()
    thread_login.join()
    thread_Adlogin.join()
    thread_borrow.join()
    thread_seratch.join()
    # 测试用的
    # books.addbook('book004','万历十五年','黄仁宇','三联书店出版社',9)
    # books.delbook("万历十五年")
    # print(books.borrowbook("万历十五年"))
    # print(books.rebook("万历十五年"))
    # print(books.seratch("万历十五年"))
    # print(User.login('0001','1234'))
    # print(User.Adminlogin('admin','adminpw'))
    # User.adduser('0006','hjk','1111')
    # User.deluser('0006')
    # User.userborrowbook('0001','万历十五年')
    # User.borrowresult('0001')
    index.menu0(0)
