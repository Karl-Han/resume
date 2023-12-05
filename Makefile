CONFIG_NAME ?= master_version_conf
MASTER_NAME ?= master
DATE := $(shell date -u +%Y%m%d)
SHELL := /bin/bash
SKIP_VC := 0

.PHONY: pre-build build

# build CONFIG_NAME.tex and CONFIG_NAME.pdf
build: ${CONFIG_NAME}.yml preamble.tex pre-build gen_vc
	`which python3` conf2tex.py ${CONFIG_NAME}.yml ${CONFIG_NAME}.tex ${MASTER_NAME}.yml
	pdflatex ${CONFIG_NAME}.tex
	`which python3` pdf2png.py ${CONFIG_NAME}

gen_vc: generate_master_version_conf

generate_master_version_conf:
	if [ -e master_version_conf.yml ] && [ ${SKIP_VC} == 1 ]; then \
		echo "master_version_conf already exists, skipping"; \
	else \
		`which python3` generate_config_template.py master.yml master_version_conf.yml && echo "Generated master_version_conf.yml as comprehensive version configuration. Use it as template for config.yml.\nExecute mv master_version_conf.yml config.yml and customize config.yml accordingly"; \
	fi

# build CONFIG_NAME.pdf from CONFIG_NAME.text
pdf: ${CONFIG_NAME}.tex
	pdflatex ${CONFIG_NAME}.tex

# clean all the auxiliary files
clean:
	rm *.aux *.log *.out
