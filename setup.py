#!/usr/bin/env python
# Learn more: https://github.com/EchoShoot/Sheen/setup.py

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='sheen',
    version='0.1.2',
    description='Pythonic cross-platform colored terminal text [support 16/256 colors]',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Yaowu Zhang',
    author_email='BiarFordlander@gmail.com',
    url='https://github.com/EchoShoot/Sheen',
    packages=['sheen'],
    license='MIT',
    include_package_data=True,
    zip_safe=False,
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Terminals"
    ],
    install_requires=[],
)
