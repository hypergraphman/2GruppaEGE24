from ipaddress import ip_network

net = ip_network('10.7.46.6/255.255.248.0', False)
for i, ad in enumerate(net):
    if str(ad) == '10.7.46.6':
        print(i)