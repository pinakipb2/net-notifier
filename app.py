import socket
import time
#from plyer import notification
from win32com.client import Dispatch

speak = Dispatch(("SAPI.SpVoice"))
start = False

# def connected():
#     global start
#     if(start):
#         notification.notify(
#             title = "Net Notifier",
#             app_name = "Net Notifier",
#             message = "Internet is available!! \nMade by PINAKI",
#             app_icon = "./res/internet.ico",
#             timeout = 2,
#         )
#     else:
#         notification.notify(
#             title = "Net Notifier",
#             app_name = "Net Notifier",
#             message = "Internet is not available!! \nMade by PINAKI",
#             app_icon = "./res/internet.ico",
#             timeout = 2,
#         )

def is_connected():
    try:
        socket.create_connection(("1.1.1.1", 53))
        return True
    except OSError:
        pass
    return False

def check():
    # time.sleep(0.8)
    conn = is_connected()
    global start
    if(conn!=start):
        start = conn
        if(conn):
            print("Connected")
            speak.Speak("Internet Connected")
            # connected()
        else:
            print("Disconnected")
            speak.Speak("Internet Disconnected")
            # connected()
    else:
        pass

if __name__ == "__main__":
    print("Made by PINAKI\n")
    while(True):
        check()