# find all the packages available in the entire directory where the application is being setup.
from setuptools import find_packages, setup
## to recognise the output of get_requirements() as a list ()
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        ## list comprehension to replace \n with "". 
        ## when each line is read from requirements.txt file, \n is also recorded, hence this line of code to avoid it.
        requirements=[req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements



## metadata of the entire project
setup(
name = 'mlproject',
version ='0.0.1',
author='V. Arun Kumar',
author_email="arunkv2198@gmail.com",
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)
