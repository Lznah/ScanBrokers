from setuptools import setup

with open('README.rst') as f:
    long_description = ''.join(f.readlines())

setup(
    name='scanbrokers',
    version='0.1',
    description='A webserver in Flask, that operates with historal data of Czech real estate agents, gathered from Sreality.',
    packages=find_packages(),
    author='Petr Hanzl',
    long_description_content_type='text/x-rst',
    author_email='hanzlpe@icloud.com',
    license='MIT',
    keywords='analytics sreality real estate flask',
    url='https://github.com/Lznah/ScanBrokers/',
    package_data={
        'scanbrokers': [
            '/templates/*.html.j2'
        ]
    },
    zip_safe=False,
    install_requires=[
        'flask',
        'flask_httpauth'
    ],
    classifiers=[
        'Framework :: Flask',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
    ],
)
