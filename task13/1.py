from ipaddress import ip_network

net = ip_network('140.212.98.17/255.255.248.0', False)
print(net)