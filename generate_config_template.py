import sys
import yaml

master_name = 'master.yml' if len(sys.argv) == 2 else sys.argv[1]
target_name = 'master_version_conf.yml' if len(sys.argv) == 3 else sys.argv[2]

print(f"master file is {master_name} and version configuration is {target_name}")

def main(filename, target_name):
    with open(filename, "r") as f:
        s = f.read()
        master = yaml.load(s, yaml.FullLoader)

    field_basics = ['name', 'email', 'phone', 'website', 'extra_links']
    config = {}
    basics = {}
    for b in field_basics:
        if b in master.keys():
            basics[b] = True
    config['basics'] = basics

    sections = []
    for section in master['content']:
        d = {}
        d['section_name'] = section['title']
        d['mode'] = 'all'
        if section['layout'] == 'list':
            d['title'] = []
            for entry in section['content']:
                d['title'].append({entry['title']: 'all'})
        sections.append(d)
    config['order'] = sections

    stream = open(target_name, "w")
    yaml.dump(config, stream)

if __name__ == "__main__":
    main(master_name, target_name)
