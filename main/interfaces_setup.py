import os
import subprocess
import sys

from main.logger import log_command_output

local_network_address_prefix = "192.168."
default_mask = "255.255.255.0"
chosen_device_ip = "188"


def change_ip_dns(interface_name, selected_subnetwork_address):
    default_gateway = local_network_address_prefix + selected_subnetwork_address + ".1"
    default_ip_address = local_network_address_prefix + selected_subnetwork_address + "." + chosen_device_ip

    ip_change_bat_file_path = resource_path('scripts/change_ip.bat')
    change_ip_command = "Powershell -Command \"Start-Process " \
                        + str(ip_change_bat_file_path) + " -ArgumentList '" \
                        + str(default_ip_address) + "," \
                        + str(default_mask) + "," \
                        + str(default_gateway) + "," \
                        + str(interface_name) \
                        + "' -Verb RunAs\""

    # print(change_ip_command)
    # subprocess.check_output(change_ip_command, shell=True)
    process = subprocess.Popen(change_ip_command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = process.communicate()
    log_command_output(change_ip_command, str(output))

    dns_change_bat_file_path = resource_path('scripts/change_dns.bat')
    change_dns_command = "Powershell -Command \"Start-Process " \
                         + str(dns_change_bat_file_path) + " -ArgumentList '" \
                         + str(default_gateway) + "," \
                         + str(interface_name) \
                         + "' -Verb RunAs\""

    process = subprocess.Popen(change_dns_command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = process.communicate()
    log_command_output(change_dns_command, str(output))


def restore_automatic(interface_name):
    ip_change_bat_file_path = resource_path('scripts/restore_automatic_ip.bat')
    change_ip_command = "Powershell -Command \"Start-Process " \
                        + str(ip_change_bat_file_path) + " -ArgumentList '" \
                        + str(interface_name) \
                        + "' -Verb RunAs\""

    process = subprocess.Popen(change_ip_command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = process.communicate()
    log_command_output(change_ip_command, str(output))

    dns_change_bat_file_path = resource_path('scripts/restore_automatic_dns.bat')
    change_dns_command = "Powershell -Command \"Start-Process " \
                         + str(dns_change_bat_file_path) + " -ArgumentList '" \
                         + str(interface_name) \
                         + "' -Verb RunAs\""

    process = subprocess.Popen(change_dns_command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = process.communicate()
    log_command_output(change_dns_command, str(output))


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = getattr(sys, '_MEIPASS', os.getcwd())
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
