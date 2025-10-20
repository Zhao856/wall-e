from softnet import Server, Client
from controller import  Controller
import time



message = {}
server = Server(50007)
client = Client('192.168.0.111',50007)

while True:
    message = Controller()
    client.send(message.dic)
    # print(server.recieve())
    print(message.dic)
    time.sleep(0.01)


