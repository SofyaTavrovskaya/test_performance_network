#!/usr/bin/python3

import yaml


# dictionary = {'host2': '192.168.14.145', 'host1': '192.168.14.134'}
# input_file = 'template.yaml'


def generate_yaml_for_shaker(dictionary, template):
    with open(template) as f:
        doc = yaml.safe_load(f)

    doc['deployment']['agents'][0]['ip'] = dictionary['host1']
    doc['deployment']['agents'][1]['ip'] = dictionary['host2']

    output_file = 'shaker-'+dictionary['host1']+'-'+dictionary['host2']+'.yaml'

    with open(output_file, 'w') as f:
        yaml.dump(doc, f, default_flow_style=False)

    return output_file




