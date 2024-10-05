from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
    clientSocket = socket(AF_INET, SOCK_STREAM) #SOCK_STREAM is for TCP socket
    clientSocket.bind((mailserver, port))
    # Fill in end

    recv = clientSocket.recv(1024).decode()
    #print(recv) #You can use these print statement to validate return codes from the server.
    #if recv[:3] != '220':
    #    print('220 reply not received from server.')

    # Send HELO command and print server response.
    helo = 'HELO Alice\r\n'
    clientSocket.send(helo.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1) 
    if recv1[:3] != '250':
       print('250 reply not received from server for HELO.')

    # Send MAIL FROM command and handle server response.
    # Fill in start
    mail_from = 'MAIL FROM: <nmt8347@nyu.edu>\r\n'
    clientSocket.send(mail_from.encode())
    recv2 = clientSocket.recv(1024).decode()
    if recv2[:3] != '250':
        print('250 reply not received from server for MAIL FROM.')
    # Fill in end

    # Send RCPT TO command and handle server response.
    # Fill in start
    rcpt_to = 'RCPT TO: <nmt8347@nyu.edu>\r\n'
    clientSocket.send(rcpt_to.encode())
    recv3 = clientSocket.recv(1024).decode()
    if recv3[:3] != '250':
        print('250 reply not received from server for RCPT TO.')
    # Fill in end

    # Send DATA command and handle server response.
    # Fill in start
    data = 'DATA\r\n'
    clientSocket.send(data.encode())
    recv4 = clientSocket.recv(1024).decode()
    if recv4[:3] != '354':
        print('354 reply not received from server for DATA.')
    # Fill in end

    # Send message data.
    # Fill in start
    message = msg + endmsg
    clientSocket.send(message.encode())
    recv5 = clientSocket.recv(1024).decode()
    if recv5[:3] != '250':
        print('250 reply not received from server for email message.')
    # Fill in end

    # Message ends with a single period, send message end and handle server response.
    # Fill in start
        # THIS IS DONE IN THE SECTION RIGHT ABOVE
    # Fill in end

    # Send QUIT command and handle server response.
    # Fill in start
    quit = 'QUIT\r\n'
    clientSocket.send(quit.encode())
    recv6 = clientSocket.recv(1024).decode()
    if recv6[:3] != '221':
        print('221 reply not recieved from server for QUIT')
    # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')