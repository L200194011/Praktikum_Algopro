import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 50003))
s.listen(5)
print "TCP server penjawab otomatis sudah siap"
data = ' '
kamus = {'nama': 'Baihaqi Fatah Muhammad',
         'NIM': 'L200190169',
         'alamat': 'Maaf, perintah tidak dimengerti',
         'keluar': 'siap!!'}
while data.lower() != 'q':
    komm, addr = s.accept()
    while data.lower() != 'q':
        data = komm.recv(1024)
        if data.lower() == 'q':
            s.close()
            break
        print 'Pertanyaan:', data
        if kamus.has_key(data):
            komm.send(kamus[data])
        else:
            komm.send('pertanyaan anda tidak relevan')
