import json
import requests

thingsboard = 'demo.thingsboard.io'
username = 'anderson.bcc.uag@gmail.com'
password = 'thingsboard'
device_id = 'ffdc20f0-dd75-11ea-b1ac-638f0a979ee0'
url = 'http://{}/api/auth/login'.format(thingsboard)
payload = {"username":username, "password":password}
headers = {'content-type': 'application/json', 'Accept': 'application/json'}
r = requests.post(url, data=json.dumps(payload), headers=headers)
# print(r.json()['token'])
token = r.json()['token']
headers = {'content-type': 'application/json', 'X-Authorization': 'Bearer {}'.format(token)}
#url = 'http://thingsboard:8080/api/plugins/telemetry/DEVICE/b7fa3200-dc16-11ea-b097-7bbc10df19ff/values/timeseries?keys=x,y,z&startTs=0000000000000&endTs=9999999999999&agg=NON'
url = 'http://{}/api/plugins/telemetry/DEVICE/{}/values/timeseries?keys=x,y,z&startTs=0000000000000&endTs=9999999999999&agg=NON'.format(thingsboard, device_id)
r = requests.get(url, headers=headers)

for x, y, z in zip(r.json()['x'], r.json()['y'], r.json()['z']):
	print(x, end=' ')
	print(y, end=' ')
	print(z)
