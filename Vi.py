import socket
sock = socket.socket()
sock.connect(('localhost', 9090))
a=""
while(a!="0"):
    print("1 - Дата и время")
    print("2 - (a^2/b^2 + c^2*a^2)/(a+b+c*(k-a/b^3)) + c + (k/b -k/a)*c")
    print("0 - Выход")
    a=input('Введите номер действия: ')
    sock.send(a.encode())
    if a=="1":
        data=sock.recv(1024)
        print(data.decode())
    if a=="2":
        aa=input("Введите число а = ")
        sock.send(aa.encode())
        b=input("Введите число b = ")
        sock.send(b.encode())
        c=input("Введите число с = ")
        sock.send(c.encode())
        k=input("Введите число k = ")
        sock.send(k.encode())
        rs=sock.recv(1024)
        print("Ответ = ", rs.decode())
    print(" ")
sock.close()
ddr=input()
