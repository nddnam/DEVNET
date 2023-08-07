import json

mydict = {'deviceId': '9.9.9.20', 'system-ip': '9.9.9.20', 'host-name': 'vManage01', 'reachability': 'reachable', 'status': 'normal', 'personality': 'vmanage', 'device-type': 'vmanage', 'timezone': 'Asia/Ho_Chi_Minh', 'device-groups': ['No groups'], 'lastupdated': 1691393198233, 'domain-id': '0', 'board-serial': '248C8C6D94F28D475DD3B8FFCDE24BD2651DA0CD', 'certificate-validity': 'Valid', 'max-controllers': '0', 'uuid': 'b137e935-2b33-4e94-a669-9e4af1d4a5a9', 'controlConnections': '5', 'device-model': 'vmanage', 'version': '20.6.4', 'connectedVManages': ['9.9.9.20'], 'site-id': '999', 'latitude': '37.666684', 'longitude': '-122.777023', 'isDeviceGeoData': False, 'platform': 'x86_64', 'uptime-date': 1691376180000, 'statusOrder': 4, 'device-os': 'next', 'validity': 'valid', 'state': 'green', 'state_description': 'All daemons up', 'model_sku': 'None', 'local-system-ip': '9.9.9.20', 'total_cpu_count': '16', 'testbed_mode': False, 'layoutLevel': 1}
wishkeys = ['system-ip', 'host-name', 'site-id', 'status', 'version']

finaldict = {x: mydict[x] for x in wishkeys}

print(finaldict)