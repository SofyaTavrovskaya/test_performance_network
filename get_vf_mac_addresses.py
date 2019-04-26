#!/usr/bin/python3

from pyroute2 import IPRoute


def get_vf_mac_addresses_for_interfaces(list_interfaces):
    """

    :param list_interfaces:
    :return: dictionary with name of interfaces and mac_addresses
    """
    ip = IPRoute()
    list_index_interfaces = []
    for interface in list_interfaces:
        index_interface = ip.link_lookup(ifname=interface)[0]
        list_index_interfaces.append(index_interface)
    vf_mac_addresses = {x.get_attr('IFLA_IFNAME'): [x.get_attr('IFLA_ADDRESS')] for x in ip.get_links(*list_index_interfaces)}
    return vf_mac_addresses


