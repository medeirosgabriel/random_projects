import json
import websocket
import datetime
import socket
import time

'''
Data Format:
{
    "e":"trade",
    "E":1706201672553,
    "s":"ETHUSDT",
    "t":1290315354,
    "p":"2190.43000000",
    "q":"0.07850000",
    "b":15733251324,
    "a":15733251570,
    "T":1706201672553,
    "m":true,"M":true
}
'''

def ws_trades(c):

    socket = f'wss://stream.binance.com:9443/ws/ethusdt@trade'

    def on_message(wsapp, message):  
        json_message = json.loads(message)
        data = handle_trades(json_message)
        print(data)
        c.send(data.encode())
        time.sleep(1)

    def on_error(wsapp, error):
        wsapp.close()
        print(error)

    wsapp = websocket.WebSocketApp(socket, on_message=on_message, on_error=on_error)
    wsapp.run_forever()
    
def handle_trades(json_message):
    date_time = datetime.datetime.fromtimestamp(json_message['E']/1000).strftime('%Y/%m/%d-%H:%M:%S')
    data = {"Symbol": json_message['s'], "Timestamp": json_message['t'], "Price": json_message['p']}
    return json.dumps(data)

def start():
    s = server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # Create a socket object
    host = "127.0.0.1" # Get local machine name
    port = 5000        # Reserve a port for your service.
    s.bind((host, port))
    s.listen(1)
    print("Listening on port: %s" % str(port))
    
    # Now wait for client connection.
    c, addr = s.accept()   # Establish connection with client.
    print("Received request from: " + str( addr ) )
    ws_trades(c)

while True:
    start()
