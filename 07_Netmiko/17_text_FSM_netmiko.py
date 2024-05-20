from netmiko import ConnectHandler, exceptions
from pprint import pprint
lab_csr = {
    'device_type': 'cisco_ios',
    'host': '192.168.200.11',
    'username': 'admin',
    'password': 'admin'
}

try:
    print(f"\n{'#' * 35}\nConnecting to the lab_csr {lab_csr['host']}")
    net_connect = ConnectHandler(**lab_csr)
    print(f"Connected successfully to the lab_csr {lab_csr['host']} ")
    output = net_connect.send_command("show ip int brie", use_textfsm=True)
    pprint(output)
    print(f"Interface {output[0]['interface']} IP is {output[0]['ip_address']}")
    print(f"Interface {output[1]['interface']} IP is {output[1]['ip_address']}")
    net_connect.disconnect()
except exceptions.NetmikoAuthenticationException:
    print(f"Authentication Failed on {lab_csr['host']}")
except exceptions.NetmikoTimeoutException:
    print(f"Session timeout on {lab_csr['host']}")

