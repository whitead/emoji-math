import io
import os
import re

from setuptools import find_packages
from setuptools import setup


def read(filename):
    filename = os.path.join(os.path.dirname(__file__), filename)
    text_type = type(u'')
    with io.open(filename, mode='r', encoding='utf-8') as fd:
        return re.sub(text_type(r':[a-z]+:`~?(.*?)`'), text_type(r'``\1``'), fd.read())


setup(
    name='emath',
    version='1.0',
    url='https://github.com/whitead/emoji-math',
    license='MIT',

    author='Andrew D White',
    author_email='andrew.white@rochester.edu',

    description='Emoji Mathematics',
    long_description=read('README.md'),

    packages=find_packages(),

    install_requires=['numpy', 'pandas', 'click'],

        entry_points={
        'console_scripts': [
            'emoji-math = emath.main:app',
        ]
        }
)
