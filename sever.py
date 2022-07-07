import socket
from threading import Thread

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ip_address="127.0.0.1"
port=8000

server.bind((ip_address,port))
server.listen()

list_of_clients=[]
questions=["When did Disney-Pixar merge and are they still together?\n a.2016,yes\n b.2006,yes \n c.2016,no \n d.2006,no",
"What was the first Disney-Pixar movie?\n a.Encanto\n b.Iron man \n c.Ratatoullie \n d.Toy story",
"When is the 4th of july? \n a.Jan 1st\n b.July 4th \n c.July 5th\n d.idk",
"Who is the quarterback that has the most superbowl rings? \n a.Barack Obama\n b.Michael Jordan \n c.Drew Lock \n d.Tom Brady",
"How many years does it take for leap day? \n a.1 year\, b.10 years\n c. 4 years\n d.100 years",
"Mr.beast is the most subscribed youtube channel\n a.True\n b.False",
"The nile river is the longest river in the world \n a.True\n b.False",
"When was the declaration of independence signed?\n a.1682\n b.1776\n c.1891\n d.2000",
"What do the stripes on the american flag represent?\n a.candy canes\n b.13 colonies\n c.13 states\n d.13th president",
"Where did albert einstein originally live?\n a.germany\n b.United States\n c. New zealand\n d.China "
]
print("server has started")

def clientThread(conn,nickname):
    conn.send("welcome to the chat room".encode('utf-8'))
    while True:
        try:
            message=conn.recv(2048).decode("utf-8")
            if message:
                print(message)
                # print("<"+addr[0]+">"+message)
                # message_to_send="<"+addr[0]+">"+message
                broadcast(message,conn)
            else:
                remove(conn)
                remove_nickname(nickname)
        except:
            continue

def broadcast(message,connection):
    for clients in list_of_clients:
        if clients != connection:
            try:
                clients.send(message.encode("utf-8"))
            except:
                remove(clients)

def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)

def remove_nickname(nickanme):
    if nickname in nicknames:
        nicknames.remove(nickname)
        

while True:
    conn,addr=server.accept()
    conn.send("NICKNAME".encode("utf-8"))
    nickname=conn.recv(2048).decode("utf-8")
    list_of_clients.append(conn)
    nicknames.append(nickname)
    message="{} joined".format(nickname)
    print(message)
    broadcast(message,conn)
    new_thread=Thread(target=clientThread,args=(conn,nickname))
    new_thread.start()
    
