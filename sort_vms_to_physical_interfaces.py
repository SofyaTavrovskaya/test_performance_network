#!/usr/bin/python3

# vf_mac_addresses = {'enp4s0': ['52:54:00:8e:1a:e4'], 'enp3s0': ['40:16:7e:6e:cc:ef'], 'enp5s0': ['fe:54:00:8e:1a:e4', '00:00:00:00:00:00']}
# list_of_vm = {'ubuntu16.04': {'ip': '192.168.14.137', 'mac': '52:54:00:8e:1a:e4', 'host_interface': None}, 'ubuntu16.04-clone': {'ip': '192.168.14.136', 'mac': 'fe:54:00:8e:1a:e4', 'host_interface': None}}


def sort_vms_to_physical_interfaces(vf_mac_addresses, list_of_vm):
    for interface in vf_mac_addresses:
        if len(vf_mac_addresses[interface]) == 1:
            for inter in list_of_vm:
                if list_of_vm[inter]['mac'] == vf_mac_addresses[interface][0]:
                    list_of_vm[inter]['host_interface'] = interface
        else:
            for mac in vf_mac_addresses[interface]:
                for inter in list_of_vm:
                    if mac == list_of_vm[inter]['mac']:
                        list_of_vm[inter]['host_interface'] = interface
    return list_of_vm
