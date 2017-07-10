import os
from codecs import open
from setuptools import find_packages, setup

version = '0.0.1'

here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README file
with open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


test_requires = [
    'py>=1.4.26',
    'pyflakes==1.1.0',
    'pytest>=3.0.7',
    'pytest-cache>=1.0',
    'pytest-cov>=2.1.0',
    'pytest-flakes>=1.0.1',
    'pytest-isort==0.1.0',
    'pytest-pep8>=1.0.6',
    'coverage>=4.0',
    'pep8>=1.6.2',
    'tox',
    'tox-pyenv',
]

setup(
    name='draw',
    version=version,
    description='Draw devops against humanity sentence.',
    long_description=long_description,
    keywords=['devops against humanity', 'cards against humanity'],
    url='https://github.com/lenarother/draw-devops-against-humanity/',
    author='Magdalena Rother',
    author_email='rother.magdalena@gmail.com',
    license='MIT',
    packages=find_packages(exclude=[
        'tests*'
    ]),
    package_data={'': ['LICENSE.txt', 'README.rst'],
                  'data': ['devops_against_humanity.csv']},
    data_files=[('.', ['LICENSE.txt', 'README.rst']),
                ('data', ['data/devops_against_humanity.csv'])],
    include_package_data=True,
    extras_require={
        'tests': test_requires,
    },
    tests_require=test_requires,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Command Line',
        'Intended Audience :: Developers',
        'Topic :: DevOps',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
