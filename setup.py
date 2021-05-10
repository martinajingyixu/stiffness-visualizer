"""
Setup of core python codebase
Author: Jingyi Xu / Michael Danielczuk / Jeff Mahler
"""
from setuptools import setup

requirements = [
    'trimesh[easy]',            # mesh processing
    'pyrender',                 # visualization
    'numpy',                    # array handing
    'matplotlib',               # visualization
    'argparse',                 # load args
]

exec(open('stiffness-visualizer/version.py').read())

setup(
    name='stiffness-visualizer',
    version = __version__,
    description = 'Stiffness Visualizer',
    long_description = 'Visualize an object stiffness map.',
    author = 'Jingyi Xu',
    author_email = 'jingyi.xu@tum.de',
    license = 'Creative Commons Public License',
    url = 'https://github.com/martinajingyixu/stiffness-visualizer.git',
    keywords = 'robotics grasping visualization',
    classifiers = [
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: Creative Commons Public License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Natural Language :: English',
        'Topic :: Scientific/Engineering'
    ],
    packages = ['stiffness-visualizer'],
    install_requires = requirements,
)
