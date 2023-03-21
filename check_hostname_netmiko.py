from netmiko import ConnectHandler

device_1 = {
    'host_name': 'access-sw01',
    'info': {
        "device_type": "cisco_ios",
        "host": "10.99.0.11",
        "username": "admin",
        "password": "itbase.tv"
    }
}
device_2 = {
    'host_name': 'access-sw02',
    'info': {
        "device_type": "cisco_ios",
        "host": "10.99.0.12",
        "username": "admin",
        "password": "itbase.tv"
    }
}

device_3 = {
    'host_name': 'core-sw01',
    'info': {
        "device_type": "cisco_ios",
        "host": "10.99.0.21",
        "username": "admin",
        "password": "itbase.tv"
    }
}
device_4 = {
    'host_name': 'core-sw02',
    'info': {
        "device_type": "cisco_ios",
        "host": "10.99.0.22",
        "username": "admin",
        "password": "itbase.tv"
    }
}
device_list = [device_1, device_2, device_3, device_4]

#check if device configured hostname correctly??

for dev in device_list:
    ssh_connect = ConnectHandler(**dev['info'])
    configured_hostname = ssh_connect.send_command("show run | i hostname")
    configured_hostname = configured_hostname.split(" ")[1]
    
    if configured_hostname != dev['host_name']:
        print(f"NOT MATCHED  \n \t {configured_hostname} -> {dev['host_name']}")
    else:
        print(f"MATCHED \n \t {dev['host_name']}")
