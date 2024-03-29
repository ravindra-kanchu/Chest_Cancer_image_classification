# it is the center of all activity in buliding,distributing and
# installing modules using the Distutils

from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT="-e ."
def get_requirements(file_path:str)->List[str]:
    """
     this fun will return the list of requirements
    """
    # requirements=[]
    # with open(file_path) as file_obj:
    #     requirements=file_obj.readlines()
    #     requirements=[req.replace("\n","")for req in requirements]

    #     if HYPEN_E_DOT in requirements:
    #         requirements.remove(HYPEN_E_DOT)
    # return requirements
   
    requirements = []
    with open(file_path) as file_obj:
        lines = file_obj.readlines()
        for line in lines:
            # Exclude the '-e .' line but still trigger setup.py execution
            if line.strip() == '-e .':
                continue
            requirements.append(line.strip())
    return requirements

setup(
    name='dlproject_imageClassification',
    version='0.0.1',
    author='Ravindra',
    author_email='ravindrakanchu2001@gmail.com',
    packages=find_packages(),
    # install_requires=['pandas','numpy','tensorflow','seaborn']
    install_requires=get_requirements('requirements.txt')
    # it is when we have more packages to be instaaled
)