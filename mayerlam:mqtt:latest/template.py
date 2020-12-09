import paho.mqtt.client as mqtt
import random
import json

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Do something ....

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected disconnection.")

client_id = 'mqtt_' + format(random.randint(0x1000000000000, 0xfffffffffffff), 'x')
host_name = 'your.target.com'
host_port = 8888

client = mqtt.Client(client_id=client_id, clean_session=True, protocol=4, transport='websockets')

# enable ssl
client.ws_set_options(path="/mqtt")
client.tls_set_context()
client.tls_insecure_set(True)


client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect

client.connect(host_name, host_port)
client.loop_forever()