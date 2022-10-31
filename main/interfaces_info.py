from subprocess import check_output


def discover_wifi_names():
    get_wlan_interfaces_command = "ipconfig | findstr Wireless"
    wlan_names = check_output(get_wlan_interfaces_command, shell=True) \
        .decode(encoding="ISO-8859-1") \
        .split("Wireless LAN adapter ")

    for i in range(len(wlan_names)):
        wlan_names[i] = wlan_names[i].split(":")[0].strip()

    # remove empty strings
    return list(filter(None, wlan_names))


def discover_lan_names():
    get_lan_interfaces_command = "ipconfig | findstr Ethernet"

    lan_names = check_output(get_lan_interfaces_command, shell=True) \
        .decode(encoding="ISO-8859-1") \
        .split("Ethernet adapter ")

    for i in range(len(lan_names)):
        lan_names[i] = lan_names[i].split(":")[0].strip()

    # remove empty strings
    return list(filter(None, lan_names))
