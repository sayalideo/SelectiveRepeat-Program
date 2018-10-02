#Name    : Sayali Deo
#Roll No : 7926
#Class   : TE Computers
#Batch   : A
#Selective Repeat ARQ - Client Side Code

import socket

def client_program():
	n = 4
    	win_start = 0
	win_end = win_start + n - 1
	host = socket.gethostname()  # as both code is running on same pc
	port = 12344  # socket server port number
	sender = []
	flag = 0 #send whole sender list else 1 means send only win_start frame
	client_socket = socket.socket()  # instantiate
	client_socket.connect((host, port))  # connect to the server
	print 'Window Size is ', n
	print '******** Enter "bye" to close connection ***************'
        message = raw_input("Hit any key to start sending frames -> ")  # take input
        while message.lower().strip() != 'bye':
		print "Sending frames..."
		if (flag == 0):
			for i in range(n):
				sender.append(win_start + i)
			for i in sender :
				print "Frame -> ", i
		else:
			print "Frame -> ", win_start
		msg = str(win_start)
        	client_socket.send(msg.encode())  # send message
        	data = client_socket.recv(1024).decode()  # receive NAK
		msg = str(data)
		ack = int(msg)
		if ack not in sender:
			win_start = ack
			win_end = win_start + n - 1
			flag = 0         		#send new frame
			for i in range(n):
				sender.pop()
		else:
			win_start = int(msg)
			flag = 1			#send old frame
			
		print "************************************"
        	print 'Received ACK server: ' + data  # show in terminal
		
        	message = raw_input("Hit any key to start sending frames -> ")  # again take input

    	client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()


######################### OUTPUT : Client Side #################################
'''sayali@sayali:~/Desktop/Saiy/MyDocs/CN $ python cliselect.py
Window Size is  4
******** Enter "bye" to close connection ***************
Hit any key to start sending frames -> 
Sending frames...
Frame ->  0
Frame ->  1
Frame ->  2
Frame ->  3
************************************
Received ACK server: 4
Hit any key to start sending frames -> 
Sending frames...
Frame ->  4
Frame ->  5
Frame ->  6
Frame ->  7
************************************
Received ACK server: 4
Hit any key to start sending frames -> 
Sending frames...
Frame ->  4
************************************
Received ACK server: 7
Hit any key to start sending frames -> 
Sending frames...
Frame ->  7
************************************
Received ACK server: 8
Hit any key to start sending frames -> 
Sending frames...
Frame ->  8
Frame ->  9
Frame ->  10
Frame ->  11
************************************
Received ACK server: 12
Hit any key to start sending frames -> bye
sayali@sayali:~/Desktop/Saiy/MyDocs/CN '''
