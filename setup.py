from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
        requirements=[]
        with open(file_path) as file_obj:
                requirements=file_obj.readlines()
                requirements=[req.replace("\n","") for req in requirements]

                #below code is for remove the error that are comming when we run the 
                #requiremt.txt file for make pacakge with (-e .)that is liker of setupfile and it generates error
                #so we igone this with the help by making constant and with the help of removing from the file by below code
                if HYPEN_E_DOT in requirements:
                        requirements.remove(HYPEN_E_DOT)
                return requirements


setup(
    name='DiamondPricePredictio',
    version='0.0.1',
    author='Raj kumar',
    author_email="rajkr8369@gmail.com",
    #install_requires=['pandas','numpy'] #this is install the library that are mension in list
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()
)

