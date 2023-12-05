# Methods

After V1.0, there are two parts to configure:

* `master.yml`: the master copy of all your resume information. It should be comprehensive, because all your different versions of resume is based on it.
* `master_version_conf.yml`: sample for a version of the resume based on `master.yml`. It should be specific for a purpose, e.g., a kind of position or a position in specific company.
    * It should **be generated** with `make gen_vc` and get modified accordingly.
    * Refer to [Version Configuration format](./format.md#version-configuration). A sample for version configuration is `config.yml` and `config.pdf`.
    * `make CONFIG_NAME=general build` can build the `general.pdf` with `general.yml`, which is a version configuration, and `master.yml`

There are three ways to generate PDF:

* Install TeX command line tool and Use YAML to maintain content
    * Local machine (Recommend for initial start)
    * In docker (Easiest to make another version)
        1. Read General Steps
        2. Refer to [Compiler using Docker](#compile-using-docker) and RUN
        3. You get the `config.pdf`
* GitHub Action does everything except filling version configuration `config.yml` and `master.yml`. (Recommend for other version configuration)

## General Steps

1. Refer to [practical guide](../README.md#practical-guide) to know the structure and available keys in YAML
2. Write your master copy `master.yml` accordingly by referring to `master.yml` and output `master.pdf`.
3. Generate your comprehensive version configuration, e.g., `master_version_conf.yml`, by `make gen_vc` or `python generate_config_template.py [master.yml] [version_conf.yml]`.
4. Compile and get the `master_version_conf.pdf` from the version configuration `master_version_conf.yml`.
    * Compile with `make CONFIG_NAME=general build` for version configuration `general.yml`

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

And then, continue with the [General Step4](#general-steps).

## GitHub Action (2-commit)

Steps:

1. Fork this repository.
2. Learn the format of YAML: [Simple Guide](https://www.cloudbees.com/blog/yaml-tutorial-everything-you-need-get-started).
3. Read the short [Practical Guide](#practical-guide) for `master.yml` to know the most-used structures.
4. Refer to [Master Format](./format.md#masteryml-master-format), study the structures by looking at `master.pdf` and `master.yml` side by side.
    * [Online Lint](https://www.yamllint.com/) if you need.
5. Commit it to the repository for your `master_version_conf.yml`.
6. ~~Then make a cup of tea.~~ Wait for the GitHub Actions to complete. Link example: <https://github.com/Karl-Han/resume/actions>
7. Get the `master_version_conf.pdf` in the repository! Your new Resume! You are all set!
8. Rename and modify the `master_version_conf.yml`, e.g., `config.yml`, by referring to [Version Configuration format](./format.md#version-configuration).
9. Modify `CONFIG_NAME`, e.g., `config`, in Makefile to change the target version configuration and commit it again.

## Docker Image

> It downloads 2 GB data and takes more than 5 minutes. Total size of image is about 4.75 GB.

After going through everything in [General Steps](#general-steps). Execute the followings in the repository directory:

```sh
docker build -t latex .
docker run --rm -i -v "$PWD":/data latex make
```

Then you will get the `config.pdf` with version configuration `config.yml`!

## [Deprecated] Overleaf

Get started quickly using [Sourabh Bajaj's Overleaf](https://www.overleaf.com/latex/templates/software-engineer-resume/gqxmqsvsbdjf) template.

## Appendix
