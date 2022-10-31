import tkinter as tk

from main.interfaces_info import discover_wifi_names, discover_lan_names
from main.interfaces_setup import change_ip_dns, restore_automatic

lan_names = discover_lan_names()
wlan_names = discover_wifi_names()

print(lan_names)
print(wlan_names)


def make_change():
    interface_name = interfaces_list.get(interfaces_list.curselection())
    subnet = subnet_entry.get()
    print(f"Making cahnge to interface {interface_name} and subnet {subnet}")
    change_ip_dns(interface_name, subnet)


def make_default():
    interface_name = interfaces_list.get(interfaces_list.curselection())
    print(f"Restoring automatic to interface {interface_name}")
    restore_automatic(interface_name)


window = tk.Tk()

interface_label = tk.Label(text="Select interface", width=15, height=5)
interface_label.pack()

interfaces_list = tk.Listbox(selectmode=tk.SINGLE, width=50)

for name in lan_names:
    interfaces_list.insert(tk.END, name)

for name in wlan_names:
    interfaces_list.insert(tk.END, name)

# make list vertically scrollable
interfaces_list.yview()
interfaces_list.pack()

subnet_entry_label = tk.Label(text="Select subnet \n (subnet is X in example: 192.168.X.1)", width=40, height=5)
subnet_entry_label.pack()
subnet_entry = tk.Entry()
subnet_entry.insert(0, "1")
subnet_entry.pack()

button = tk.Button(
    text="Change IP!",
    width=25,
    height=5,
    bg="yellow",
    fg="black",
    command=make_change
)
button.pack()

reset_button = tk.Button(
    text="Restore Automatic!",
    width=25,
    height=5,
    bg="green",
    fg="yellow",
    command=make_default
)
reset_button.pack()

window.mainloop()
