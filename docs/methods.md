 Methods

After V1.0, there are two parts to configure:

* `master.yml`: the master copy of all your resume information. It should be comprehensive, because all your different versions of resume is based on it.
* `config.yml`: sample for a version of the resume. It should be specific for a purpose, e.g., a kind of position or a position in specific company.
    * It should be generated with `python generate_config_template.py` and get modified accordingly.
    * `make CONFIG_NAME=general build` can build the `general.pdf` with `general.yml` and `master.yml`

There are three ways to generate PDF:

* GitHub Action does everything except filling `config.yml` and `master.yml` (MOST convenient)
* Install TeX command line tool and Use YAML to maintain content
    * In docker (Easiest to Start)
        1. Read General Steps
        2. Refer to [config.yaml format](./format.md#configyml-format)
        3. Modify `config.yaml` accordingly
        4. Refer to [Compiler using Docker](#compile-using-docker) and RUN
        5. You get the `config.pdf`
    * Local machine

## General Steps

1. Refer to [practical guide](../README.md#practical-guide) to know the structure and available keys in YAML
2. Write your master copy `master.yml` accordingly by referring to `master.yml` and output `config.pdf`
3. Generate your comprehensive version, e.g., `config.yml`, by `python generate_config_template.py [master.yml] [version_conf.yml]`.
4. Compile and get the `config.pdf` from the version configuration.
    * Compile with `make CONFIG_NAME=general build` for version configuration file `general.yml`

## GitHub Action

Steps:

1. Fork this repository.
2. Learn the format of YAML: [Simple Guide](https://www.cloudbees.com/blog/yaml-tutorial-everything-you-need-get-started).
3. Read the short [Practical Guide](#practical-guide) for `master.yml` to know the most-used structures.
4. Refer to [Master Format](./format.md#masteryml-master-format), study the structures by looking at `config.pdf` and `config.yml` side by side.
5. Modify `config.yml` with your content and make sure `config.yml` is syntactically correct.
    * [Online Lint](https://www.yamllint.com/) if you need.
6. Commit it to the repository.
7. ~~Then make a cup of tea.~~ Wait for the GitHub Actions to complete. Link example: <https://github.com/Karl-Han/resume/actions>
8. Get the `config.pdf` in the repository! Your new Resume! You are all set!

## Docker Image

> It downloads 2 GB data and takes more than 5 minutes. Total size of image is about 4.75 GB.

Execute the followings in the repository directory:

```sh
docker build -t latex .
docker run --rm -i -v "$PWD":/data latex make
```

Then you will get the `config.pdf`!

## Local TeX Tools

Requirements: TeX command line tool, Makefile, python3.6+
I would recommend you to use BasicTeX with homebrew: <https://tex.stackexchange.com/questions/307483/setting-up-basictex-homebrew>

Python package requirements: `python3 -m pip install -r requirements.txt`

If you are prompted for extra packages, for example in `BasicTeX`, you have to download the following packages:

```shell
sudo tlmgr install preprint
sudo tlmgr install titlesec
sudo tlmgr install marvosym
sudo tlmgr install enumitem
sudo tlmgr install babel-english
```

And then, execute `make`, then you are all set!

## [Deprecated] Overleaf

Get started quickly using [Sourabh Bajaj's Overleaf](https://www.overleaf.com/latex/templates/software-engineer-resume/gqxmqsvsbdjf) template.

## Appendix
