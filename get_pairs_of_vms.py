#!/usr/bin/python3

import itertools
#
# vms_with_host1_interfaces = {'ubuntu16.04-1': {'ip': '192.168.14.137', 'mac': '52:54:00:8e:1a:e4', 'host_interface': 'enp1s0'},
#                             'ubuntu16.04-2': {'ip': '192.168.14.136', 'mac': 'fe:54:00:8e:1a:e4', 'host_interface': 'enp2s0'},
#                             'ubuntu16.04-3': {'ip': '192.168.14.135', 'mac': 'fe:54:01:8e:1a:e4', 'host_interface': 'enp3s0'},
#                             'ubuntu16.04-4': {'ip': '192.168.14.134', 'mac': 'fe:54:02:8e:1a:e4', 'host_interface': 'enp4s0'}}
#
#
# vms_with_host2_interfaces = {'ubuntu18.04-1': {'ip': '192.168.14.147', 'mac': '52:55:00:8e:1a:e4', 'host_interface': 'enp5s0'},
#                             'ubuntu18.04-2': {'ip': '192.168.14.146', 'mac': 'fe:54:03:7e:1a:e4', 'host_interface': 'enp6s0'},
#                             'ubuntu18.04-3': {'ip': '192.168.14.145', 'mac': 'fe:54:04:7e:1a:e4', 'host_interface': 'enp7s0'},
#                              'ubuntu18.04-4': {'ip': '192.168.14.144', 'mac': 'fe:54:05:7e:1a:e4', 'host_interface': 'enp8s0'},
#                              'ubuntu18.04-5': {'ip': '192.168.14.144', 'mac': 'fe:54:05:7e:1a:e4', 'host_interface': 'enp6s0'}}
#
# connections = [{'host1': 'enp1s0', 'host2': 'enp8s0'}, {'host1': 'enp2s0', 'host2': 'enp6s0'}, {'host1': 'enp3s0', 'host2': 'enp5s0'}, {'host1': 'enp4s0', 'host2': 'enp7s0'}]


def get_pairs_of_vms(vms_with_host1_interfaces, vms_with_host2_interfaces, connections):
    vms_pair = []
    for iteritems in itertools.product(vms_with_host1_interfaces, vms_with_host2_interfaces):
        if {'host1': vms_with_host1_interfaces[iteritems[0]]['host_interface'], 'host2': vms_with_host2_interfaces[iteritems[1]]['host_interface']} in connections:
            vms_pair.append({'host1': vms_with_host1_interfaces[iteritems[0]]['ip'], 'host2': vms_with_host2_interfaces[iteritems[1]]['ip']})
    return vms_pair
