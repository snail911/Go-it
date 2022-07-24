from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='0.0.1',
    description='My long code',
    url='https://github.com/snail911/Go-it',
    author='Yakiv KLymenko',
    author_email='yasha1311@gmail.com',
    license='Go-IT',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['clean-folder = useful.some_code.clean: create_folders',
                                      'clean-folder = useful.some_code.clean: sort_files',
                                      'clean-folder = useful.some_code.clean: new_names',
                                      'clean-folder = useful.some_code.clean: extract_archives',
                                      'clean-folder = useful.some_code.clean: del_empty_dirs']})