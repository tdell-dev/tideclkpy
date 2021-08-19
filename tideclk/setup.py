from distutils.core import setup

setup(name='tideclk',
      version='1.0.0',
      description='Tide Infographic for Raspi4',
      author='Uiblr',
      author_email='uibler@github.com',
      url='https://www.github.com/uiblr/tideclk',
      packages=['tideclk'],
      install_requires=['requests','numpy','matplotlib'],
      entry_points={
          'console_scripts': [
              'tideclk = tideclk.console:main',
              ],
          }
      )
