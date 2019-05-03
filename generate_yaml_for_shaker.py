#!/usr/bin/python3

import yaml


dictionary = {'host2': '192.168.14.145', 'host1': '192.168.14.134'}


def generate_yaml_for_shaker(dictionary):
    with open('my_file.yaml') as f:
        doc = yaml.safe_load(f)

    doc['deployment']['agents'][0]['ip'] = dictionary['host1']
    doc['deployment']['agents'][1]['ip'] = dictionary['host2']

    with open('my_file.yaml', 'w') as f:
        yaml.dump(doc, f, default_flow_style=False)


generate_yaml_for_shaker(dictionary)



