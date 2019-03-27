from setuptools import setup, find_packages

setup(
    name='ip-config',
    version='0.1',
    python_requires='>=3.6',
    install_requires=[
        'Click',
        'python-networkmanager'
    ],
    packages=find_packages(),
    entry_points={
            'console_scripts': ['ip-config=src.ip_config:run']
    },
    url='https://github.com/faysal-ishtiaq/ip-config',
    license='MIT',
    author='Faysal Ishtiaq Rabby',
    author_email='f.i.rabby@gmail.com',
    description='A demo project to change ipv4 ip address on Red Hat, Debian, Arch Linux based distros'
)
