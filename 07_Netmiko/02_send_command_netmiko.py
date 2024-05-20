from netmiko import Netmiko

csr = {
    'device_type': 'cisco_ios',
    'host':   '192.168.200.11',
    'username': 'admin',
    'password': 'admin'
}
net_connect = Netmiko(**csr)
print("Connected successfully")

# cmd_output = net_connect.send_command("show ip int brief")
print(net_connect.find_prompt())
cmd_output = net_connect.send_command("ping 1.2.3.4 repeat 5", read_timeout=20, expect_string=r"r.+#")
print(cmd_output)
net_connect.disconnect()