#!/usr/bin/python3

from xml.dom import minidom
import libvirt

conn = libvirt.open('qemu:///system')

if conn == None:
    print('Failed to open connection to qemu:///system')
    exit(1)

virtual_machines = conn.listAllDomains(0)
o = type(virtual_machines)
print(o)

if len(virtual_machines) != 0:
    for virtual_machine in virtual_machines:

        dom = conn.lookupByName(virtual_machine.name())
        ifaces = dom.interfaceAddresses(libvirt.VIR_DOMAIN_INTERFACE_ADDRESSES_SRC_LEASE)

        for (name, val) in ifaces.iteritems():
            set_of_vm = {}
            if val['addrs']:
                for ipaddr in val['addrs']:
                    if ipaddr['type'] == libvirt.VIR_IP_ADDR_TYPE_IPV4:

                        print(ipaddr['addr'])
                        print(val['hwaddr'])

else:
    print('  None')



conn.close()
exit(0)

