import argparse
import sys
import yaml

from simple_rest_client.api import API
from simple_rest_client.resource import Resource

parser = argparse.ArgumentParser(description='Configure email aliases from config file.')
parser.add_argument('file',
                    metavar='FILE',
                    type=str,
                    default='email-aliases.yml',
                    help='a yml file specifying aliases',
                    )
parser.add_argument('--mock',
                    help='Use a mock server url',
                    action='store_true',
                    )
args = parser.parse_args()

CONFIG_FILE = args.file

MOCK_SERVER = 'https://private-anon-e19b2e8aa7-mailcow.apiary-mock.com'
PROD_SERVER = 'https://mailninja.aseriesoftubez.com'

base_url = MOCK_SERVER if args.mock else PROD_SERVER

class AliasResource(Resource):
    actions = {
        'list': {'method': 'GET', 'url': '/get/alias/{}'},
        'add': {'method': 'POST', 'url': '/add/alias'},
        'edit': {'method': 'POST', 'url': '/edit/alias'},
    }

default_headers = {'X-API-Key': '1234567890'}

mailcow_api = API(
    api_root_url=base_url + '/api/v1',
    headers=default_headers,
    json_encode_body=True,
)

mailcow_api.add_resource(resource_name='aliases', resource_class=AliasResource)


def expand_config_entries(entries):
    aliases = []

    for e in entries:
        ins = e['in']
        ins = [ins] if isinstance(ins, str) else ins
        outs = e['out']
        outs = [outs] if isinstance(outs, str) else outs
        e['out'] = outs

        if len(ins) > 1:
            for i in ins:
                e['in'] = i
                aliases.append(e)
        else:
            aliases.append(e)

    return aliases

# Get live aliases
response = mailcow_api.aliases.list('all')
if response.status_code != 200:
    raise

existing_aliases = response.body

with open(CONFIG_FILE, 'r') as f:
    contents = yaml.safe_load(f)
    entries = contents['aliases']
    aliases = expand_config_entries(entries)
    for a in aliases:
        alias_id = 'blah'
        if alias_id:
            # POST update alias by ID
            payload = {
                "items": [alias_id],
                "attr": {
                    "address": a['in'],
                    "goto": ','.join(a['out']),
                }
            }
            print(payload)
            response = mailcow_api.aliases.edit(body=payload)
            print(response)

        else:
            # POST create alias
            payload = {
                "address": a['in'],
                "goto": ','.join(a['out']),
            }
            print(payload)
            response = mailcow_api.aliases.add(body=payload)

# TODO: Write code from strict mode, to remove aliases not configured

# TODO: Write code for generating aliases from GitHub teams
