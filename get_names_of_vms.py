#!/usr/bin/python3

import libvirt


def get_names_of_vms_from_host_machine(uri):
    conn = libvirt.open(uri)
    if conn is None:
        print('Failed to open connection to' + uri)
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
                            list_of_vm1[virtual_machine.name()] = {'ip': ipaddr['addr'], 'mac': val['hwaddr'], 'interface': None}
        return list_of_vm1
    else:
        print('  None')
    conn.close()

