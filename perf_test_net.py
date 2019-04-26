#!/usr/bin/python3


from get_vf_mac_addresses import get_vf_mac_addresses_for_interfaces
from get_names_of_vms import get_names_of_vms_from_host_machine

host_uri = 'qemu:///system'
# remoute_uri = 'qemu+ssh://ubuntu@192.168.14.136/system'
host_list_interfaces = ['enp3s0', 'vnet0', 'vnet1']

dict1 = {'enp4s0': ['52:54:00:8e:1a:e4'], 'enp3s0': ['40:16:7e:6e:cc:ef'], 'enp5s0': ['fe:54:00:8e:1a:e4', '00:00:00:00:00:00']}
dict2 = {'ubuntu16.04': {'ip': '192.168.14.137', 'mac': '52:54:00:8e:1a:e4'}, 'ubuntu16.04-clone': {'ip': '192.168.14.136', 'mac': '52:54:00:7a:6f:b0'}}


def sort_vms_to_physical_interfaces(dict1, dict2):
    for interface in dict1:
        if len(dict1[interface]) == 1:
            for inter in dict2:
                if dict2[inter]['mac'] == dict1[interface][0]:
                    dict2.update[inter]({'interface': interface})

print(dict2)


sort_vms_to_physical_interfaces(dict1, dict2)









