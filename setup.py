from setuptools import setup

with open("README.md", "r") as f:
  readme = f.read()

setup(
  name = 'Python.js',
  packages = ['PyJS', 'PyJS.modules'],
  version = '1.0.8',
  license='MIT',
  description = 'A python library for people who prefer JavaScript\'s way of handling things.',
  author = 'Nemika',
  author_email = 'nemika@bytestobits.dev',
  url = 'https://github.com/Nemika-Haj/PyJS',
  download_url = 'https://github.com/Nemika-Haj/PyJS/archive/0.1.tar.gz',
  keywords = ['pyjs', 'javascript', 'python', 'js', 'py.js', "python.js", "python js"],
  long_description=readme,
  long_description_content_type="text/markdown",
  install_requires=[
          'forbiddenfruit',
      ],
  classifiers=[
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9'
  ],
)