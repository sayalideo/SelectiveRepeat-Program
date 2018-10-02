#Name    : Sayali Deo
#Roll No : 7926
#Class   : TE Computers
#Batch   : A
# Selective Repeat ARQ - Server Side Code

import socket
import random
def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 12344  # initiate port no above 1024
    exp = 0
    n = 4
    new = 1
    win_start = 0
    win_end   = win_start + n - 1
    receiver = []
    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print "Connection from: ", str(address)
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
	rec = int(data)
	lim = rec + n - 1
	count = 0
	flag = 0
	ack = rec
	
	
	randy = random.randint(1, 4)
	if new == 1 : 			#you received a new frame of a new window
		while(count != randy):
			temp = random.randint(rec, lim)
			
			if temp not in receiver:
				print "Received Frame -> ", temp
				count+=1
				flag = 1       #Atleast one new frame added in receiver buffer
				receiver.append(temp)
	else :
		print "Received Frame -> ", rec       #you received a new frame of an old window  
		receiver.append(rec)
		flag = 1
        if(flag == 1):
		for i in range(rec,lim+1):
			if i not in receiver:
				ack = i
				break
			ack = i+1
	
	print "Sending ACK    -> ", ack #next expected frame
        print '***************************************************'
	data = str(ack)
        conn.send(data.encode())  # send data to the client

	if ack > win_end :
		win_start = ack
		win_end   = win_start + n - 1
		new = 1			# now receive a new frame of a new window
	else :
		new = 0 		# now received a new frame of an old window

    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()

############################# OUTPUT : Server Side ##########################
'''sayali@sayali:~/Desktop/Saiy/MyDocs/CN $ python serselect.py
Connection from:  ('127.0.0.1', 40912)
Received Frame ->  0
Received Frame ->  3
Received Frame ->  2
Received Frame ->  1
Sending ACK    ->  4
***************************************************
Received Frame ->  6
Received Frame ->  5
Sending ACK    ->  4
***************************************************
Received Frame ->  4
Sending ACK    ->  7
***************************************************
Received Frame ->  7
Sending ACK    ->  8
***************************************************
Received Frame ->  9
Received Frame ->  11
Received Frame ->  8
Received Frame ->  10
Sending ACK    ->  12
***************************************************
sayali@sayali:~/Desktop/Saiy/MyDocs/CN $ '''
