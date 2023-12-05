# Methods

There are three ways to generate PDF:

* GitHub Action does everything except filling `config.yml` (MOST convenient)
* Modify Overleaf directly
* Install TeX command line tool and Use YAML to maintain content
    * In docker (Easiest to Start)
        1. Read General Steps
        2. Refer to [config.yaml format](#configyml-format)
        3. Modify `config.yaml` accordingly
        4. Refer to [Compiler using Docker](#compile-using-docker) and RUN
        5. You get the `config.pdf`
    * Local machine 

## General Steps

1. Refer to [practical guide](../README.md#practical-guide) to know the structure and available keys in YAML
2. Modify `config.yml` accordingly by reading `config.pdf` 
3. Compile and get the `config.pdf` from `config.yml`

Except `make`, please refer to `Makefile` to know other instructions.

## GitHub Action
Steps: 
1. Fork this repository.
2. Learn the format of YAML: [Simple Guide](https://www.cloudbees.com/blog/yaml-tutorial-everything-you-need-get-started).
3. Read the short [Practical Guide](#practical-guide) for `config.yml` to know the most-used structures.
4. Refer to [config.yml format](#configyml-format), study the structures by looking at `config.pdf` and `config.yml` side by side. 
5. Modify `config.yml` with your content and make sure `config.yml` is syntactically correct.
  * [Online Lint](https://www.yamllint.com/) if you need.
6. Commit it to the repository. 
7. ~~Then make a cup of tea.~~ Wait for the GitHub Actions to complete. Link example: https://github.com/Karl-Han/resume/actions
8. Get the `config.pdf` in the repository! Your new Resume! You are all set!

## Overleaf

Get started quickly using [Sourabh Bajaj's Overleaf](https://www.overleaf.com/latex/templates/software-engineer-resume/gqxmqsvsbdjf) template.

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

If you need extra packages, for example in `BasicTeX`, you have to download the following packages:
```shell
sudo tlmgr install preprint
sudo tlmgr install titlesec
sudo tlmgr install marvosym
sudo tlmgr install enumitem
```

And then, execute `make`, then you are all set!
