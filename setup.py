from setuptools import setup

setup(name='YTtoMp3',
      version='0.1',
      description='tool to download mp3 from youtube videos',
      url='https://github.com/jacopo-cavallo/YTtoMp3',
      author='jacopo cavallo',
      author_email='jacopo.cavallo@protonmail.com',
      license='GPL',
      packages=['YTtoMp3'],
      install_requires=['pytube',],
      zip_safe=False)
