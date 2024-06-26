# from pprint import pprint
# import sys
# import time
# import traceback
# from paramiko import client, ssh_exception
# import socket
# import datetime

# new_cmd = ['show ip interface brief']

# def cisco_cmd_executor(hostname, commands, username, password):
#     try:
#         print(f"Connecting to the device {hostname}..")
#         now = datetime.datetime.now().replace(microsecond=0)
#         current_conf_file = f"{now}_{hostname}.txt"
#         ssh_client = client.SSHClient()
#         ssh_client.set_missing_host_key_policy(client.AutoAddPolicy())
#         ssh_client.connect(hostname=hostname, port=22, username=username, password=password, look_for_keys=False,
#                            allow_agent=False)

#         print(f"Connected to the device {hostname}")
#         device_access = ssh_client.invoke_shell()
#         device_access.send("terminal len 0\n")
#         with open(current_conf_file, 'w') as cmd_data:
#             for cmd in commands:
#                 device_access.send(f"{cmd}\n")
#                 time.sleep(1)
#                 output = device_access.recv(65535).decode()
#                 cmd_data.write(output)
#                 print(output)
#         ssh_client.close()
#         print("### Parsed output is ###")
#         output_list = output.splitlines()
#         interface_list = output_list[6:-1]
#         # pprint(interface_list)
#         int_parsed_list = list()
#         for interface in interface_list:
#             intf_dict = {}
#             intf = interface.split()
#             # print(intf)
#             intf_dict['int_name'] = intf[0]
#             intf_dict['ip'] = intf[1]
#             intf_dict['status'] = intf[-2]
#             int_parsed_list.append(intf_dict)

#         pprint(int_parsed_list)
#     except ssh_exception.NoValidConnectionsError:
#         print("SSH Port not reachable")
#     except socket.gaierror:
#         print("Check the hostname")
#     except ssh_exception.AuthenticationException:
#         print("Authentication failed, check credentials")

#     except:
#         print("Exception Occurred")
#         print(sys.exc_info())
#         # traceback.print_exception(*sys.exc_info())

# cisco_cmd_executor('csr1.test.lab', new_cmd, 'admin', 'admin')


from pprint import pprint
import sys
import time
import traceback
from paramiko import client, ssh_exception
import socket
import datetime


cmd='show ip int brief'

int_dict={}
def device_connection(hostname, username, password):
    try:
        print(f"Connecting to the device {hostname}..")
        ssh_client = client.SSHClient()
        ssh_client.set_missing_host_key_policy(client.AutoAddPolicy())
        ssh_client.connect(hostname=hostname, username=username, password=password, allow_agent=False, look_for_keys=False)
        # device_access= ssh_client.invoke_shell()
        stdin, stdout, stderr = ssh_client.exec_command(cmd)
        int_details= stdout.read().decode().strip().split("\n")

        ssh_client.close()

        # int_details= stdout.read().decode().split("\n")
        # print(int_details)
        for interface in int_details[1:]:
            
            # pprint(interface.strip().split())
            int_dict[interface.split()[0]]= {"Interface_ip":interface.split()[1], "Interface_status": interface.split()[-2]}

        pprint(int_dict)
        

    except ssh_exception.NoValidConnectionsError:
        print("SSH Port not reachable")
    except socket.gaierror:
        print("Check the hostname")
    except ssh_exception.AuthenticationException:
        print("Authentication failed, check credentials")

device_connection("192.168.200.11", 'admin', 'admin')