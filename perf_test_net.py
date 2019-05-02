#!/usr/bin/python3


from get_vf_mac_addresses import get_vf_mac_addresses_for_interfaces
from get_names_of_vms import get_names_of_vms_from_host_machine
from sort_vms_to_physical_interfaces import sort_vms_to_physical_interfaces

host1_uri = 'qemu:///system'
host2_uri = 'qemu+ssh://ubuntu@192.168.14.136/system'

host1_list_interfaces = ['enp3s0', 'vnet0', 'vnet1']
host2_list_interfaces = ['enp3s0', 'vnet0', 'vnet1']

vf_mac_addresses_host1 = get_vf_mac_addresses_for_interfaces(host1_list_interfaces)
vf_mac_addresses_host2 = get_vf_mac_addresses_for_interfaces(host2_list_interfaces)

vms_name_host1 = get_names_of_vms_from_host_machine(host1_uri)
vms_name_host2 = get_names_of_vms_from_host_machine(host2_uri)

vms_with_host1_interfaces = sort_vms_to_physical_interfaces(vf_mac_addresses_host1, vms_name_host1)
vms_with_host2_interfaces = sort_vms_to_physical_interfaces(vf_mac_addresses_host2, vms_name_host2)













