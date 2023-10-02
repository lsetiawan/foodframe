from distutils.core import setup
setup(
  name = 'foodframe',
  packages = ['foodframe'],
  version = '0.0.1',
  license='MIT',
  description = 'Standardize. Analyze. Impact.',
  author = 'Tushar Dalmia, Annie K. Lamar',
  author_email = 'kalamar@stanford.edu',
  url = 'https://github.com/annieklamar/foodframe',
  download_url = 'https://github.com/annieklamar/foodframe/archive/v_001.tar.gz',
  keywords = ['Food', 'foodbanks', 'nutrition', 'feeding america', 'hei'],
  install_requires=[
          'pandas'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Researchers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)