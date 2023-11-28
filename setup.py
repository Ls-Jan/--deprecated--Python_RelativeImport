from setuptools import setup


description='Module relative import'
try:
    with open('README.md','r',encoding='utf-8') as f:
        long_description = f.read()
except Exception as e:
    long_description = description

setup(name='RelativeImport',
      version='1.1',
      description=description,
      long_description=long_description,
      long_description_content_type='text/markdown',
      python_requires=">=3.5.0",
      url='http://github.com/ls-jan/Python_RelativeImport',
      author='Ls_Jan',
      author_email='1990317049@qq.com',
      license='MIT Licence',
      packages=['RelativeImport'],
      platforms = 'any',
      zip_safe=False)

