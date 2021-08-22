from distutils.core import setup
setup(
	name = 'pynosqlite',
	packages = ['pynosqlite'],
	version = '0.1',
	license='MIT',
	description = 'Fast and Lightweight json file based database',
	author = 'Moin Ahmad',
	author_email = 'ahmadmoin723@gmail.com',
	url = 'https://github.com/programmingplanet/pynosqlite',
	download_url = 'https://github.com/ProgrammingPlanet/pynosqlite/archive/refs/tags/v0.1.tar.gz',
	keywords = ['Single File', 'Json', 'DataBase', 'Small', 'LightWeight', 'Fast'],
	install_requires=['filelock==3.0.12'],
	classifiers=[
		'Development Status :: 4 - Alpha',	# Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
		'Intended Audience :: Developers',	# Define that your audience are developers
		'Topic :: Software Development :: Build Tools',
		'License :: OSI Approved :: MIT License',	 # Again, pick a license
		'Programming Language :: Python :: 3.9',	#Specify which pyhton versions that you want to support
		'Programming Language :: Python :: 3.8',
		'Programming Language :: Python :: 3.7',
		'Programming Language :: Python :: 3.6',
	],
)