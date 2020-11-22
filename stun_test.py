import stun
import json
from pymemcache.client import base
import socket

# json.loads	json -> python
# json.dumps	python -> json

port = 54320
memcached_server_ip = '119.247.42.174'

def client(ip):
	address = (ip, port)
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	while True:
		msg = input()
		if not msg:
			break
		s.sendto(msg.encode(), address)

def server():
	address = ('0.0.0.0', port)
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind(address)

	while True:
		data, addr = s.recvfrom(2048)
		if not data:
			print( "client has exist")
			break
		print ("received:", data, "from", addr)

	s.close()

choices = {"1":"connect to stun server", "2":"connect to peer (ip, port)", "3":"listen at port %s"%port}
choice = str(input(choices))
choice = choice.split(' ')
if choice[0]=='1':
	nat_type, external_ip, external_port = stun.get_ip_info()
	
	client = base.Client((memcached_server_ip, 11212))

	peers_json = client.get('nat_peers',{})
	peers = json.loads(peers_json)
	peers[external_ip] = [nat_type, external_ip, external_port]
	peers_json = json.dumps(peers)
	client.set('nat_peers', peers_json)
	
	print(peers)
elif choice[0]=='2':
	ip = choice[1]
	client(ip)
elif choice[0]=='3':
	server()
