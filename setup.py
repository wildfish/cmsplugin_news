from setuptools import setup, find_packages

setup(
    name='cmsplugin-news',
    version='0.3b',
    description='This is a news app/plugin for the django-cms 2',
    author='Harro van der Klauw',
    author_email='hvdklauw@gmail.com',
    url='https://github.com/azizmb/cmsplugin-news',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    include_package_data=True,
    zip_safe=False,
)
