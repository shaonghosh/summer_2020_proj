from setuptools import setup

setup(name='readXML',
      version='0.1.0',
      packages=['readXML'],
      entry_points={
          'console_scripts': [
              'read-xml = readXML.readinj:main'
          ]
      },
      )
