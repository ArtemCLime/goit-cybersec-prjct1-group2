from setuptools import setup, find_namespace_packages

setup(name='bot_assistant',
      version='1',
      description='Address book bot assistant',
      url='https://github.com/ArtemCLime/goit-cybersec-prjct1-group2',
      author='DataDefenders',
      license='MIT',
      packages=find_namespace_packages(),
      install_requires=['rich', 'pytest'],
      entry_points={'console_scripts': ['bot-assistant = bot_assistant.source:main']}
)