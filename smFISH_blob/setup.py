#!/usr/bin/env python

############################################
# File Name : setup
#
# Purpose :
#
# Creation Date : 12-01-2015
#
# Last Modified : Fri Jan 16 15:43:22 2015
#
# Created By : ahaber
#
# Usage : 
############################################



from distutils.core import setup

setup(name='detect_cells',
      version='0.0',
      description='Simple blob/contour detection for smFISH quantification',
      author='Adam Haber',
      author_email='ahaber@broadinstitute.org',
      packages=['smFISH_blob'],
      entry_points={
                  'console_scripts':
                  ['smFISH_blob = smFISH_blob.main:main']
        },
        install_requires=['numpy','argparse'],
     )
