#!/bin/bash
<<Description

	Removes existing virtual environment and creates new virtual environment,
	installing the required packages.
	
	Usage:
			bash newenv.sh
	
Description

# Install virtualenv if it is not already
echo NEW ENV: Installing/updating virtualenv...
pip install virtualenv

# Delete existing virtual environment (include, lib, scripts, tcl folders)
echo NEW ENV: Removing files...
rm -rf Lib Include Scripts tcl

# Create new virtual environment
echo NEW ENV: Creating new environment...
virtualenv "$cd"

# Install the required packages
echo NEW ENV: Installing required packages...
source Scripts/activate
pip install --upgrade pip
pip install -r requirements.txt

# Environment setup
echo NEW ENV: Done creating new environment.

# Check to make sure environment is set up correctly
echo NEW ENV: Checking environment configuration...
python env_check.py
echo NEW ENV: Done.

# Deactivating virtual env
deactivate