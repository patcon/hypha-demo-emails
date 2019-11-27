import sys
import yaml

def pop_default(l, index, default):
    return l[index] if index < len(l) else default

CONFIG_FILE = pop_default(sys.argv, 1, 'email-aliases.yml')

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
