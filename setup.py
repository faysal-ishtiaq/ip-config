from setuptools import setup

setup(
    name='ip-config',
    version='0.1',
    install_requires=[
        'Click',
        'python-networkmanager'
    ],
    entry_points={
            'console_scripts': ['ip-config=ip_config:run']
    },
    url='https://github.com/faysal-ishtiaq/ip-config',
    license='MIT',
    author='Faysal Ishtiaq Rabby',
    author_email='f.i.rabby@gmail.com',
    description='A demo project to change ipv4 ip address on Red Hat, Debian, Arch Linux based distros'
)
