# Motivation for the Changes

As I wrote more resumes for different company, even for different slightly different positions in the same company, I found it hard to maintain a sole copy that all the resumes originates from. And this leads to inconsistency in my different resume.

In order to make the content of resume consistent, I separate the version configuration, which is resume version specific for some purpose, from the master copy. In this way, all my generated pdfs can be updated whenever I made modifications to the master copy, and of course, most of the time, I will just need to update specific one.

## Before V1.0

I love to use structured format, like Markdown and LaTeX, to present my notes and article. So I choose Sourabh Bajaj's template. And I modified the original template to fit USC's requirements of better resume on VMock.

Also, I have set up personal resume website: <https://www.iwktd.com/> to let others know me comprehensively instead of one-page resume.

So I have the demand to share the same information across different repository and use YAML as the language to organize my information.

Thanks to [Firfi's PR](https://github.com/sb2nov/resume/pull/46), I integrated the GitHub Actions into this repository, so that you no longer need to install the environment or Docker in your computer!