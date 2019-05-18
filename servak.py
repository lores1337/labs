import datetime
import socket
sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()
so="Поступившего ранее сообщения не было"
print('connected:', addr)
a=""
while(a!="0"):
    a = conn.recv(1024)
    a=a.decode()
    if a=="1":
        today = datetime.datetime.today()
        data=today.strftime("%Y-%m-%d-%H.%M.%S")
        conn.send(data.encode())
    if a=="2":
        aa= conn.recv(1024)
        b = conn.recv(1024)
        c = conn.recv(1024)
        k = conn.recv(1024)
        aa=int(aa.decode())
        b=int(b.decode())
        c=int(c.decode())
        k=int(k.decode())
        if aa!=0 and b!=0 and k!=0:
            rs=1-(aa**2/b**2 + c**2*aa**2)/(aa+b+c*(k-aa/b**3)) + c + (k/b -k/aa)*c
            conn.send(str(rs).encode())
        else:
            rq="Ошибка: деление на 0"
            conn.send(rq.encode())
d=input()
conn.close()

