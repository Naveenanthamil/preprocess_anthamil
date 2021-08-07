import setuptools

with open('Readme.md','r') as file:
	long_description=file.read()


setuptools.setup(
	name='preprocess_anthamil',version='0.0.1',author='naveen_anthamil',author_email='mail2naveen1202@gmail.com',
	description='This is preprocessing package',long_description=long_description,
	long_description_content_type='text/markdown',
	packages=setuptools.find_packages,
	classifier=['programming  Language::python::3','licence :: OSI Aproved ::MIT License',
	"operating system :: OS Independent"],
	python_requires='>=3.5's
