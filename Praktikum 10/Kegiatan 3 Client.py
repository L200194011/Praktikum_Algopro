import socket

hostname = "localhost"
pesan = ""
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, 50002))
print "Menghitung Luas Jajar Genjang"
while pesan.lower() != "keluar":
    pesan = raw_input("pesan: ")
    s.send(pesan)
    if pesan.lower() == "keluar":
        response = s.recv(1024)
        print "Response:-"
        s.close()
        break
    elif pesan.lower() != "keluar":
        response = s.recv(1024)
        print "Response: ", response
s.close()
