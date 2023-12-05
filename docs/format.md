# YAML Format

There are two YAML formats in this repository you have to configure for fully making use of it:

- `master.yml`: master copy
- Version configuration: for example `config.yml`

## `master.yml` Master Format

Some of them can be replaced with `""` to set them to blank, but it depends.

Below is a full list of content options.

```yml
name: Your name
email: Your email
phone: Your phone
website: Your website or ""

order:
  - Section 1 title
  - Section 2 title
  - Section 3 title
  # You can omit sections to implicitly set section.show = false...
content:
  - title: Section Name
    layout: list # (options: list, text)
    content:
      - show: false # (options: true, false)
        title: Item Name (eg. Company or Project name)
        location: Location of this title
        # These two are **optional**, but you have to use both or none
        sub_title: Sub title (eg. Qualification or Job title)(optional)
        duration: Duration for the sub-title, e.g., Aug. 2022-Sept. 2023

        # NOT USED. link: Web link (eg. https://sproogen.github.io/modern-resume-theme)(optional)
        description: # this will include new lines to allow paragraphs
          - Point1 Main content area for the list item.
          - Point2 for this Item
  - title: Section Name
    layout: text # (options: list, text)
    content: # this will include new lines to allow paragraphs
      - Line1 This is where you can write a little more about yourself. You could title this section **Interests** and include some of your other interests.
      - Line2 Or you could title it **Skills** and write a bit more about things that make you more desirable, like *leadership* or *teamwork*
```

## Version Configuration

This file is to

- order the sections in the correct order
- enable specific entry with/without description

The following is the manual version of version configuration to better understand the format. I suggest you to generate the version configuration from the master copy by `python generate_config_template.py [master.yml] [version_conf.yml]`.

```yaml
# Basics Info
# Mandatory: name, email
# Optional: phone, website, extra_links
basics:
  phone: false
  website: true
  extra_links: true

# Section Order and Included Content
order:
  # mode: [all | enabled | none]
  - section_name: Education
    mode: all
    extra: none
  - section_name: Skills
    mode : all
  - section_name: Experience
    mode: enabled
    # Enabled title with `<title for entry>: [all | no_description | none]`
    # implemented with `<title for entry> in entry['title']` in python
    title:
      - CS Department, USC: no_description
  - section_name: Projects
    mode: enabled
    title:
      - Branch Predictor: all
      - Arm: none
      - Pin Tool: none
      - Tomasulo: all
      - PCIe: none
      - GPGPU: none
      - SRAM: all
      - SNN: all
      - MIPS: none
      - Layout: none
      - RSA: none
  - section_name: Leadership and Involvement
    mode: enabled
    title:
      - Hope Center: no_description
      - Network Club: no_description
```