from src.utils import *
from NetworkManager import *
import ipaddress


@click.command()
@click.option('--ip_address', default='192.168.0.123', help='The IP Address you want to assign', show_default=True)
@click.option('--subnet_mask', default='255.255.255.0', help='The subnet mask you want to use', show_default=True)
@click.option('--gateway', default='192.168.0.1', help='The gateway address you want to use', show_default=True)
@click.option('--dns', default='8.8.8.8', help='The DNS server(s) you want to use. Use comma separated list for multiple dns', show_default=True)
def run(ip_address, subnet_mask, gateway, dns):
    '''This command changes ipv4 ip address on Red Hat, Debian, Arch Linux based distros'''
    devices = list(filter(lambda _device: _device.ActiveConnection is not None, NetworkManager.GetAllDevices()))

    inform("List of devices with active connection:")
    for index, device in enumerate(devices):
        click.echo(message=str(index) + ") " + device.Interface)

    choice = click.prompt("Insert the index of target device", type=int)

    assign_ip(devices[choice], ip_address, subnet_mask, gateway, dns)


def assign_ip(device, ip_address, subnet_mask, gateway, dns):
    connection = device.ActiveConnection.Connection
    connection_settings = connection.GetSettings()

    inform("Selected device: " + device.Interface)
    inform("Active Connection: " + connection_settings['connection']['id'])
    inform("Network configuration:")
    inform("IP Address: " + ip_address)
    inform("Subnet Mask: " + subnet_mask)
    inform("Gateway: " + gateway)
    inform("DNS: " + dns)

    if click.confirm("Proceed?", abort=True):
        dns = dns.split(',')
        ip_network = ipaddress.IPv4Network((ip_address, subnet_mask), False).compressed
        prefix = int(ip_network.split('/')[1])

        connection_settings['ipv4']['dns'] = dns
        connection_settings['ipv4']['addresses'][0] = [ip_address, prefix, gateway]
        connection_settings['ipv4']['gateway'] = gateway
        connection_settings['ipv4']['address-data'][0]['address'] = ip_address
        connection_settings['ipv4']['address-data'][0]['prefix'] = prefix

        device.Disconnect()
        connection.Update(connection_settings)
        NetworkManager.ActivateConnection(connection, device, '/')

    print_current_configuration_for(device, connection)


if __name__ == "__main__":
    run()
