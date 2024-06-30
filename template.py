import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s] : %(message)s:')

projectName="Yoga_Pose_Classifier"

list_of_files=[
    f"src/{projectName}/__init__.py",
    f"src/{projectName}/components/__init__.py",
    f"src/{projectName}/utils/__init__.py",
    f"src/{projectName}/config/__init__.py",
    f"src/{projectName}/entity/__init__.py",
    f"src/{projectName}/pipline/__init__.py",
    f"src/{projectName}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/experiment.py"
    ]


for filePath in list_of_files:
    filePath=Path(filePath)
    dirname,filename=os.path.split(filePath)
    
    if dirname !="":
        os.makedirs(dirname,exist_ok=True)
        logging.info(f"Creating Directories: {dirname} for file: {filename}")
        
    if(not os.path.exists(filePath) or (os.path.getsize(filePath)==0)):
        with open(filePath,'w') as file:
            pass
        logging.info(f"Creating Empty File: {filename}")
    
    else:
        logging.info(f"{filename} is already exists")
        