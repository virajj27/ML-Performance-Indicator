from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    given in requirements.txt file
    '''
    with open(file_path,'r') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
    
        if  HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name  = 'MlProject',
    version = '0.0.1',
    author = 'Viraj',
    author_email = 'virajpadale27@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)