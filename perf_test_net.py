#!/usr/bin/python3


from get_vf_mac_addresses import get_vf_mac_addresses_for_interfaces
from get_names_of_vms import get_names_of_vms_from_host_machine

host_uri = 'qemu:///system'
# remoute_uri = 'qemu+ssh://ubuntu@192.168.14.136/system'
host_list_interfaces = ['enp3s0', 'vnet0', 'vnet1']

get_vf_mac_addresses_for_interfaces(host_list_interfaces)
get_names_of_vms_from_host_machine(host_uri)








