CONFIG_NAME ?= config
DATE := $(shell date -u +%Y%m%d)

.PHONY: pre-build build

pre-build:
ifneq (${CONFIG_NAME}, config)
	$(info "defined CONFIG_NAME") 
endif


build: ${CONFIG_NAME}.yml preamble.tex pre-build
	`which python3` conf2tex.py ${CONFIG_NAME}.yml ${CONFIG_NAME}.tex
	pdflatex ${CONFIG_NAME}.tex
	`which python3` pdf2png.py ${CONFIG_NAME}

pdf: ${CONFIG_NAME}.tex
	pdflatex ${CONFIG_NAME}.tex

clean:
	rm *.aux *.log *.out
