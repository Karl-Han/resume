import yaml
import sys
from urllib.parse import urlsplit

def is_part_of_section(entry_title, conf_titles):
    for title in conf_titles:
        (k, v), = title.items()
        if k in entry_title and v != 'none':
            return v
    return None

def get_section(section, conf_section):
    """parse section to tex format

    Args:
        section (dict)
        conf_section (dict)

    Returns:
        tex: str
    """
    if conf_section['mode'] == 'none':
        return ""
    all_enabled = False
    if conf_section['mode'] == 'all':
        all_enabled = True

    sec = f"\\section{{{section['title'].upper()}}}\n"

    if section['layout'] == 'list':
        sec += "\\resumeSubHeadingListStart\n"
        for entry in section['content']:
            mode = None
            if all_enabled == False:
                mode = is_part_of_section(entry['title'], conf_section['title'])
                if mode is None:
                    continue

            subheading = r"""\resumeSubheading
    {%s}{%s}
    {%s}{%s}
"""
            subheading_notitle = r"""\resumeSubheadingNoTitle
    {%s}{%s}
"""
            if 'sub_title' in entry:
                sec += subheading % (entry['title'], entry['location'], entry['sub_title'], entry['duration'])
            else:
                if 'location' not in entry:
                    entry['location'] = ''
                sec += subheading_notitle % (entry['title'], entry['location'])
            if 'extra' in entry and 'extra' in conf_section and conf_section['extra'] == 'enabled':
                sec += "\\vspace{{+5pt}}\\\\ \\small{{{}}}\\\\ ".format(entry['extra'])
            desc = ""
            if 'description' in entry and mode != 'no_description':
                desc += "\\resumeItemListStart\n"
                for i in entry['description']:
                    desc += "\t\\resumeItemOne{%s}\n" % (i)
                desc += "\\resumeItemListEnd\n"
            sec += desc
        sec += "\\resumeSubHeadingListEnd\n\n"
    elif section['layout'] == 'text':
        for line in section['content']:
            if type(line) == str:
                sec += f'{line}\\\\ \n'
            else:
                (key, value), = line.items()
                sec += f'\\textbf{{{key}}}: {value}\\\\ \n'
    else:
        raise Exception("No 'layout' in the section.")
    return f'{sec}\n\n'

def get_heading(conf, enable_info):
    website = conf['website']
    url = urlsplit(website)
    website_path = None
    if url.path == '/':
        website_path = url.netloc
    else:
        website_path = url.netloc + url.path
    name = conf['name']
    email = conf['email']

    # order for info: email, website[, phone][, extra_links]*
    heading = r"""\textbf{\href{%s}{\LARGE {%s}}} \\
{
    \href{mailto:{%s}}{{%s}} $|$ \href{%s}{%s}"""

    if "phone" in conf and enable_info['phone']:
        phone = conf['phone']
        heading += " $|$ Phone: \href{{tel:{{}}}}{{{}}}".format(phone, phone)
    if "extra_links" in conf and enable_info['extra_links']:
        for i in conf['extra_links']:
            heading += " $|$ \href{{{}}}{{{}}} ".format(list(i.values())[0], list(i.keys())[0])

    heading += "\n}"
    return heading % (website, name, email, email, website, website_path)

def to_tex(conf):
    """convert YAML to tex format

    Args:
        conf (YAML Reader)

    Returns:
        tex: str
    """
    tex = ""
    with open("preamble.tex", "r") as f:
        tex = f.read()
    
    tex += get_heading(conf, conf['basics'])

    assert('order' in conf)

    section_dict = {}
    for section in conf['content']:
        # enumerate global content
        section_dict[section['title']] = section
    for sec_info in conf['order']:
        # decide the order and content of sections
        sec_name = sec_info['section_name']
        tex += get_section(section_dict[sec_name], sec_info)

    tex += r"\end{document}"
    return tex

def main():
    src_filename = sys.argv[1]

    if "yml" not in src_filename: 
        print(f"Please enter source yaml file with .yml or .yaml instead of {src_filename}")
        exit(1)

    dst_filename = None
    if len(sys.argv) == 3:
        dst_filename = sys.argv[2] 
    if dst_filename is not None and "tex" not in dst_filename: 
        print(f"Please enter destination tex file with .tex instead of {dst_filename}")
        exit(1)

    conf = None
    with open(src_filename, "r") as f:
        s = f.read()
        conf = yaml.load(s, yaml.FullLoader)
    with open("master.yml", "r") as f:
        s = f.read()
        master = yaml.load(s, yaml.FullLoader)
        for k, v in master.items():
            conf[k] = v
    tex = to_tex(conf)

    if dst_filename:
        f = open(dst_filename, "w")
        f.write(tex)
        f.close()
    else:
        print(tex)

if __name__ == "__main__":
    main()