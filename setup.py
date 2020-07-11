
from setuptools import setup, find_packages
setup(
    name='coral-enviro',
    version='1.0',
    description='API and Demo Application for Coral Environmental Sensor Board',
    author='Coral Team',
    author_email='coral-support@google.com',
    url="https://coral.withgoogle.com/",
    license='Apache 2',
    packages=['coral.enviro'],
    include_package_data=True,
    install_requires=[
        'luma.oled>=2.3.2',
        'spidev',
        'coral-cloudiot',
    ],
    python_requires='>=3.5.3',
)
