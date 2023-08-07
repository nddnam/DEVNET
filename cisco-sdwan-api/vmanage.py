import requests
import json
import os
import sys
import csv

#optional
import urllib3
urllib3.disable_warnings()

class Authentication:

    @staticmethod
    def get_jsessionid(vmanage_host, vmanage_port, username, password):
        api = "/j_security_check"
        base_url = "https://%s:%s"%(vmanage_host, vmanage_port)
        url = base_url + api
        payload = {'j_username' : username, 'j_password' : password}

        response = requests.post(url=url, data=payload, verify=False)
        try:
            cookies = response.headers["Set-Cookie"]
            jsessionid = cookies.split(";")
            return(jsessionid[0])
        except:
            print("No valid JSESSION ID returned\n")
            exit()

    @staticmethod
    def get_token(vmanage_host, vmanage_port, jsessionid):
        headers = {'Cookie': jsessionid}
        base_url = "https://%s:%s"%(vmanage_host, vmanage_port)
        api = "/dataservice/client/token"
        url = base_url + api      
        response = requests.get(url=url, headers=headers, verify=False)
        if response.status_code == 200:
            return(response.text)
        else:
            return None

vmanage_host = '192.168.2.120'
vmanage_port = '443'
vmanage_username = os.environ['vmanage_username']
vmanage_password = os.environ['vmanage_password']

Auth = Authentication()
jsessionid = Auth.get_jsessionid(vmanage_host,vmanage_port,vmanage_username,vmanage_password)
token = Auth.get_token(vmanage_host,vmanage_port,jsessionid)
if token is not None:
    header = {'Content-Type': "application/json",'Cookie': jsessionid, 'X-XSRF-TOKEN': token}
else:
    header = {'Content-Type': "application/json",'Cookie': jsessionid}

def device_list():
    #get all device list and export to csv file
    api = "/device"
    base_url = "https://%s:%s/dataservice"%(vmanage_host, vmanage_port)

    url = base_url + api
    response = requests.get(url=url, headers=header, verify=False)
    
    if response.status_code == 200:
        items = response.json()['data']
    else:
        print(f"Failed >> {response.status_code} >> {response.text}")
        exit()
    
    #categorize neccesary information
    neccessary_info = ['system-ip', 'host-name', 'site-id', 'status', 'version']
    devices_data = []
    for item in items:
        device = {key: item[key] for key in neccessary_info}
        devices_data.append(device)

    #write to csv
    csv_filename = 'sdwan-devices-list.csv'
    with open(csv_filename, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = neccessary_info)
        writer.writeheader()
        writer.writerows(devices_data)   
    csvfile.close()
    return os.path.join(os.getcwd(), csv_filename)

def control_connections_check(system_ip):
    #get all control connections status from given device
    api = "/device/control/connections"
    base_url = "https://%s:%s/dataservice"%(vmanage_host, vmanage_port)

    #https://192.168.2.120/dataservice/device/control/connections?system-ip=10.10.10.11&deviceId=10.10.10.11

    url = f"{base_url}{api}?system-ip={system_ip}&deviceID={system_ip}"

    response = requests.get(url=url, headers=header, verify=False)
    
    if response.status_code == 200:
        items = response.json()['data']
    else:
        print(f"Failed >> {response.status_code} >> {response.text}")
        exit()
    
    return items

if __name__ == "__main__":
    print(device_list())
