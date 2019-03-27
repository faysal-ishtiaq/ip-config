import click
import ipaddress

def inform(message):
    click.secho(message, fg='blue')


def success(message):
    click.secho(message, fg='green')


def print_current_configuration_for(device, connection):
    connection_settings = connection.GetSettings()
    inform("Device: " + device.Interface)
    inform("Connection: " + connection_settings['connection']['id'])

    address_data = connection_settings['ipv4']['address-data'][0]
    subnet_mask = str(ipaddress.IPv4Network((address_data['address'], address_data['prefix']), False).netmask)

    success("Updated network configuration:")
    inform("IP Address: " + address_data['address'])
    inform("Subnet Mask: " + subnet_mask)
    inform("Gateway: " + connection_settings['ipv4']['gateway'])
    inform("DNS: " + ','.join(connection_settings['ipv4']['dns']))
