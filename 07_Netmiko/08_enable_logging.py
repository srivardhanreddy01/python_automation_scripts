from netmiko import ConnectHandler
import logging
logging.basicConfig(filename='demo_netmiko.log', level=logging.CRITICAL)
logger = logging.getLogger("netmiko")
csr = {
    'device_type': 'cisco_ios',
    'host': '192.168.200.11',
    'username': 'admin',
    'password': 'admin'
}

net_connect = ConnectHandler(**csr)
logger.info("Connected")
print("Connected successfully")
show_cmd = net_connect.send_command("show ip interface brief")

with open('sh_output.txt', 'w') as file:
    logger.info("Writing content to file")
    file.write(show_cmd)
