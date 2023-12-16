import lirc
import time

client = lirc.Client()

# turn on the RGB strip

for i in range(5):
    client.send_once("RGBLED", "ON")
    time.sleep(0.02)
    client.send_once("RGBLED", "OFF")
    time.sleep(0.02)

client.send_once("RGBLED", "ON")
for i in range(10):
    client.send_once("RGBLED", "GREEN")
    time.sleep(0.01)
    client.send_once("RGBLED", "RED")
    time.sleep(0.01)
    client.send_once("RGBLED", "BLUE")
    time.sleep(0.01)
    client.send_once("RGBLED", "YELLOW_LIME")
    time.sleep(0.01)


# Go to channel "33"
#client.send_once("my-remote-name", "KEY_3", repeat_count=1)