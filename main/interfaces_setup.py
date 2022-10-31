import os
import subprocess

local_network_address_prefix = "192.168."
default_mask = "255.255.255.0"
chosen_device_ip = "188"


def change_ip_dns(interface_name, selected_subnetwork_address):
    default_gateway = local_network_address_prefix + selected_subnetwork_address + ".1"
    default_ip_address = local_network_address_prefix + selected_subnetwork_address + "." + chosen_device_ip

    ip_change_bat_file_path = os.path.join(os.path.dirname(os.getcwd()), 'scripts\change_ip.bat')
    change_ip_command = "Powershell -Command \"Start-Process " \
                        + str(ip_change_bat_file_path) + " -ArgumentList '" \
                        + str(default_ip_address) + "," \
                        + str(default_mask) + "," \
                        + str(default_gateway) + "," \
                        + str(interface_name) \
                        + "' -Verb RunAs\""

    print(change_ip_command)
    subprocess.check_output(change_ip_command, shell=True)

    dns_change_bat_file_path = os.path.join(os.path.dirname(os.getcwd()), 'scripts\change_dns.bat')
    change_dns_command = "Powershell -Command \"Start-Process " \
                         + str(dns_change_bat_file_path) + " -ArgumentList '" \
                         + str(default_gateway) + "," \
                         + str(interface_name) \
                         + "' -Verb RunAs\""

    print(change_dns_command)
    subprocess.check_output(change_dns_command, shell=True)


def restore_automatic(interface_name):
    ip_change_bat_file_path = os.path.join(os.path.dirname(os.getcwd()), 'scripts\\restore_automatic_ip.bat')
    change_ip_command = "Powershell -Command \"Start-Process " \
                        + str(ip_change_bat_file_path) + " -ArgumentList '" \
                        + str(interface_name) \
                        + "' -Verb RunAs\""

    print(change_ip_command)
    subprocess.check_output(change_ip_command, shell=True)

    dns_change_bat_file_path = os.path.join(os.path.dirname(os.getcwd()), 'scripts\\restore_automatic_dns.bat')
    change_dns_command = "Powershell -Command \"Start-Process " \
                         + str(dns_change_bat_file_path) + " -ArgumentList '" \
                         + str(interface_name) \
                         + "' -Verb RunAs\""

    print(change_dns_command)
    subprocess.check_output(change_dns_command, shell=True)
