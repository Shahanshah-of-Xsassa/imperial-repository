import bluetooth
import numpy as np

def search():

	devices = bluetooth.discover_devices()
	devices_list = np.zeros((1,2))

	for address in devices:
		name = bluetooth.lookup_name(address)
		print(name, address)
		if (name == "raspberrypi"):
			device = address
		newrow = [name,address]
		devices_list = np.vstack((devices_list,newrow))
	return (devices_list, address)

def print_devices(searched):
	print(searched)

def receive():
	hostMACAddress = '3c:f8:62:89:e6:89'
	port = 5
	backlog = 1
	size = 1024
	s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
	s.bind((hostMACAddress, port))
	s.listen(backlog)

	try:
		client, clientInfo = s.accept()
		while True:
			data = client.recv(size)
			if data:
				print('received: ', data)
				client.send(data)
	except:
		print("Closing socket")
		client.close()
		s.close()

def main():
	(connections, device) = search()
	print_devices(connections)
	print_devices(device)
	receive()
main()
