#!/usr/bin/env python

# setup.py.in.distutils
#
# Copyright 2012, 2013 Brandon Invergo <brandon@invergo.net>
#
# Copying and distribution of this file, with or without modification,
# are permitted in any medium without royalty provided the copyright
# notice and this notice are preserved.  This file is offered as-is,
# without any warranty.


from distutils.core import setup
import platform


if platform.system() == 'Linux':
    doc_dir = '/usr/local/share/doc/'
else:
    try:
        from win32com.shell import shellcon, shell
        homedir = shell.SHGetFolderPath(0, shellcon.CSIDL_APPDATA, 0, 0)
        appdir = ''
        doc_dir = os.path.join(homedir, appdir)
    except:
        pass

long_desc = \
"""
"""

setup(name='',
      version='',
      author='',
      author_email='',
      maintainer='',
      maintainer_email='',
      url='',
      description="""""",
      long_description=long_desc,
      download_url='',
      classifiers=[''],
      platforms=[''],
      license='',
      requires=[''],
      provides=[''],
      obsoletes=[''],
      packages=[],
      py_modules=[],
      scripts=[],
      data_files=[(doc_dir, ['COPYING', 'README'])],
      package_data={},
      ext_modules=[],
     )
