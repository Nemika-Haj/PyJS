from distutils.core import setup
setup(
  name = 'PyJS',
  packages = ['PyJS'],
  version = '0.1',
  license='MIT',
  description = 'A library to create your own madlibs game!',
  author = 'Nemika',
  author_email = 'nemika@bytestobits.dev',
  url = 'https://github.com/Nemika-Haj/PyJS',
  download_url = 'https://github.com/Nemika-Haj/PyJS/archive/0.1.tar.gz',
  keywords = ['pyjs', 'javascript', 'python', 'js'],
  long_description="README.md",
  long_description_content_type="text/md",
  install_requires=[
          'forbiddenfruit',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha'
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