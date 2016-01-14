MathLing Reading Group Website
==============================

This repository holds the Pelican source files for the MathLing Reading Group website.
These are simple markdown files that are automatically converted into HTML via the Python-based [Pelican](http://docs.getpelican.com/) and then uploaded to Github with [ghp-import](https://github.com/davisp/ghp-import).


System Requirements
-------------------

1.  Recent version of Python2.

1.  Pelican 3.6 or higher.
    Under Linux, this might already be in your repository.
    
    - In Debian Jessie you have to activate the backports repository to get a recent version.
    - In Ubuntu 14.04 (LTS) you'll need to find a ppa or use the Mac/Windows method.
    - On OSX and Windows (and Linux, if necessary) you can install Pelican via Python's package manager pip.

    ~~~~~
    pip install pelican
    ~~~~~

1.  The ghp-import script.
    Again you can install it via pip

    ~~~~~
    pip install ghp-import
    ~~~~~

    or use your package manager if you're on Linux.


File Structure
--------------

Once you've cloned the repository, you'll see a couple of files and folders.
The most important ones are:

- *content*: the markdown files for the website
- *output*: the actual website generated by Pelican
- *pelicanconf.py*: contains various settings for site creation; do not change unless you know what you're doing
- *publishconf.py*: allows you to override certain settings in the final creation phase; do not change unless you know what you're doing
- *Makefile*: set of instructions for building the website


Workflow
--------

Creating a new announcement is easy.

1.  Go to the folder *content* and then the folder for the current semester (e.g. *2016-Spring*).
1.  Create a new markdown file.
1.  Make sure the markdown file starts with a well-formed header with the first three lines consisting of `Title:`, `Author:`, and `Date:` (in format YYYY-MM-DD), followed by an empty line.

To test things locally before you upload them, you have to

1.  open a terminal and navigate to the root folder of the repository (the one with *pelicanconf.py*),
1.  run `make devserver`, and
1.  open a browser and load [http://localhost:8000](http://localhost:8000).

If everything is fine, run `make stopserver` to end the testing phase.
Now only two things remain:

1.  upload the website by running `make github`, and
1.  sync the source files to the repository:
    - `git add .`
    - `git commit`
    - `git push origin master`
