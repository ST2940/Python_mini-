import time
from plyer import notification

if __name__ == "__main__":

    while True:
        notification.notify(
            title= "HAVE A GLASS OF WATER",
            message = "it will be very much beneficial to you",
            app_icon = "glass.ico",
            toast = False,
            timeout = 10
        )
        time.sleep(11)