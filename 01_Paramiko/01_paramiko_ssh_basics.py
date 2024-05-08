from paramiko import client
from getpass import getpass
import time
hostanme = "192.168.200.11"

username = input("Enter Username:")

if not username:
    username= 'admin'
    print(f"no username provided default {username} is used")

password = getpass("Enter password of the user {username}") or "admin"

ssh_client = client.SSHClient()
ssh_client.set_missing_host_key_policy(client.AutoAddPolicy())
ssh_client.connect(hostname=hostanme, port=22, username=username, password=password, look_for_keys=False, allow_agent=False )

commands = ['conf t', 'int gi0/1', 'ip address 1.1.1.1 255.255.255.0', 'no shut', 'end']
print("connected sucessfully")

device_access = ssh_client.invoke_shell()
device_access.send("terminal len 0\n")
# device_access.send("show run\n")

for cmd in commands:
    device_access.send(f"{cmd}\n")
    time.sleep(1)
    print(device_access.recv(65535).decode(), end=" ")

# print(output.decode())
ssh_client.close()

