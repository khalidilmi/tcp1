from socket import *

serverName = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName,serverPort))
sentence = input('add, ran, sub')



client = sentence.encode()
clientSocket.send(client)

modifiedSentence = clientSocket.recv(1024)
clientsvar = modifiedSentence.decode()

print('From Server: ', modifiedSentence.decode()) 
clientSocket.close()