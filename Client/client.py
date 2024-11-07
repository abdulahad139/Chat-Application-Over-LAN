import socket
import threading
from tkinter import *
from datetime import datetime

SERVER_HOST = 'Server_IP' # ipv4 address of the server  
SERVER_PORT = 12345
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_HOST, SERVER_PORT))

username = input("Enter your username: ")

root = Tk()
root.title("Chat Application")


message_display = Text(root, wrap="word", height=15, width=50)
message_display.pack(padx=10, pady=5)
message_display.config(state="disabled")  

message_entry = Entry(root, width=40)
message_entry.pack(padx=10, pady=(0, 5))

def send_message():
    message = message_entry.get()
    if message: 
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        full_message = f"[{timestamp}] {username}: {message}"
        client.send(full_message.encode('utf-8'))
        
        message_display.config(state="normal")
        message_display.insert(END, full_message + "\n")
        message_display.config(state="disabled")
        message_display.see(END)  
        
        message_entry.delete(0, END)

send_button = Button(root, text="Send", command=send_message)
send_button.pack(padx=10, pady=(0, 10))

def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            message_display.config(state="normal")
            message_display.insert(END, message + "\n")
            message_display.config(state="disabled")
            message_display.see(END)  
        except:
            print("An error occurred!")
            client.close()
            break

receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

root.mainloop()
