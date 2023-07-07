from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in customizations/__init__.py
from customizations import __version__ as version

setup(
	name="customizations",
	version=version,
	description="Ts",
	author="Ts",
	author_email="ts@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
