from client import Client
import time
from threading import Thread

c1 = Client("Shayan")
c2 = Client("Joe")
def update_messages():
    """
    updates the local list of messages
    :return: None
    """
    messages = []
    run = True
    while run:
        time.sleep(0.1) # update every 1/10 th of a second
        new_messages = c1.get_messages()
        messages.extend(new_messages)

        for message in new_messages:
            print(message)

            if message == "{quit}":
                run = False
                break

Thread(target = update_messages).start()
c1.send_message("hello")
time.sleep(1)
c2.send_message("What is up?")
time.sleep(1)
c1.send_message("not much")
time.sleep(5)
c2.send_message("Nice ")
time.sleep(5)


c1.disconnect()
time.sleep(2)
c2.disconnect()