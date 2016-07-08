import zmq
import time
import sys
from PIL import Image
import pickle

port = "5556"
if len(sys.argv) > 1:
    port =  sys.argv[1]
    int(port)

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:%s" % port)


while True:
    #  Wait for next request from client
    message = socket.recv()
    print("Received request: ", message)
    image = pickle.loads(message)
    print(image)
    #time.sleep (1)
    socket.send("World from %s" % port)