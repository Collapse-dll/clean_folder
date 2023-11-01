from setuptools import setup, find_packages

setup(name='clean',
      version='0.1.1',
      packages=find_packages(),
      entry_points = {'console_scripts': ['clean = clean_folder.clean:main']},
      author='Saitov Mykyta'
      )