from distutils.core import setup

setup(name='cool story bot',
      version='1.0',
      description='Twitter bot that finds random information on the web and tweets it.',
      author='Coady LaCroix',
      author_email='cool-story-bot@gmail.com',
      url='',
      packages=['cool_story_bot'],
      requires=[
          'wikipedia',
          'twitter'
      ],
      classifiers=[
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5'
      ],
      )
