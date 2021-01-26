from setuptools import setup

setup(
    name='scanbrokers',
    packages=['scanbrokers'],
    author='Petr Hanzl',
    author_email='hanzlpe@icloud.com',
    license='MIT',
    url='https://github.com/Lznah/ScanBrokers/',
    include_package_data=True,
    install_requires=[
        'flask',
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
)
