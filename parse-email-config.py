import argparse
import sys
import yaml

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

# TODO: GET list of aliases

def expand_config_entries(entries):
    aliases = []

    for e in entries:
        ins = e['in']
        ins = [ins] if isinstance(ins, str) else ins
        if len(ins) > 1:
            for i in ins:
                e['in'] = i
                aliases.append(e)
        else:
            aliases.append(e)

    return aliases

with open(CONFIG_FILE, 'r') as f:
    contents = yaml.safe_load(f)
    entries = contents['aliases']
    aliases = expand_config_entries(entries)
    for a in aliases:
        print(a)

# TODO: for each expanded entry

  # if "in" value already exists

    # POST update alias by ID

  # else

    # POST create alias

  # end

# TODO: Write code from strict mode, to remove aliases not configured

# TODO: Write code for generating aliases from GitHub teams
