#!/usr/bin/python3

import libvirt
from pyroute2 import IPRoute

list_interfaces = ['vnet0', 'vnet1']
ip = IPRoute()

list_index_interfaces = []
for interface in list_interfaces:
    index_interface = ip.link_lookup(ifname=interface)[0]
    list_index_interfaces.append(index_interface)


vf_mac_addresses = [x.get_attr('IFLA_ADDRESS') for x in ip.get_links(*list_index_interfaces)]
print(vf_mac_addresses)


conn = libvirt.open('qemu:///system')


if conn is None:
    print('Failed to open connection to qemu:///system')
    exit(1)

virtual_machines = conn.listAllDomains(0)

if len(virtual_machines) != 0:
    list_of_vm1 = {}
    for virtual_machine in virtual_machines:
        dom = conn.lookupByName(virtual_machine.name())
        ifaces = dom.interfaceAddresses(libvirt.VIR_DOMAIN_INTERFACE_ADDRESSES_SRC_LEASE)
        for (name, val) in ifaces.iteritems():
            if val['addrs']:
                for ipaddr in val['addrs']:
                    if ipaddr['type'] == libvirt.VIR_IP_ADDR_TYPE_IPV4:
                        list_of_vm1[virtual_machine.name()] = {'ip': ipaddr['addr'], 'mac': val['hwaddr']}
else:
    print('  None')
print(list_of_vm1)

conn.close()
exit(0)

# conn = libvirt.open('qemu+ssh:///192.168.226.4/system')
#
# if conn is None:
#     print('Failed to open connection to qemu:///system')
#     exit(1)
#
# virtual_machines = conn.listAllDomains(0)
#
# if len(virtual_machines) != 0:
#     list_of_vm2 = {}
#     for virtual_machine in virtual_machines:
#         dom = conn.lookupByName(virtual_machine.name())
#         ifaces = dom.interfaceAddresses(libvirt.VIR_DOMAIN_INTERFACE_ADDRESSES_SRC_LEASE)
#         for (name, val) in ifaces.iteritems():
#             if val['addrs']:
#                 for ipaddr in val['addrs']:
#                     if ipaddr['type'] == libvirt.VIR_IP_ADDR_TYPE_IPV4:
#                         list_of_vm2[virtual_machine.name()] = {'ip': ipaddr['addr'], 'mac': val['hwaddr']}
# else:
#     print('  None')
# print(list_of_vm2)
#
# conn.close()
# exit(0)

