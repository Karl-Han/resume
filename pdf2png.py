import sys

from pdf2image import convert_from_path, convert_from_bytes

config_name = sys.argv[1]

images = convert_from_path(config_name + ".pdf", size=3000, dpi=400)[0]

if config_name == "config":
    images.save('config.png', 'PNG')
