from client import Client
import time

c1 = Client("Shayan")
c2 = Client("Joe")


c1.send_message("hello")
time.sleep(1)
c2.send_message("What is up?")
time.sleep(1)
c1.send_message("notmuch")
c2.send_message("Nice ")

c1.disconnect()
time.sleep(2)
c2.disconnect()