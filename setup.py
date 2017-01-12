from setuptools import setup

setup(name='2016-pycon-tutorial-sguberman',
      version='0.1a',
      description='test stuff for pycon tutorial',
      py_modules=['wordcount_lib'],
      scripts=['wordcount'],
      setup_requires=[
          'pytest-runner',
      ],
      tests_require=[
          'pytest',
      ],
)
