#!/bin/bash
<<Description

	Removes existing virtual environment and creates new virtual environment,
	installing the required packages.
	
	Usage:
			bash newenv.sh
	
Description

# Delete existing virtual environment (include, lib, scripts, tcl folders)
echo NEW ENV: Removing files...
rm -rf Lib Include Scripts tcl

# Create new virtual environment
echo NEW ENV: Creating new environment...
virtualenv "$cd"

# Install the required packages
echo NEW ENV: Installing required packages...
source Scripts/activate
pip install -r requirements.txt
deactivate

# Script finished
echo NEW ENV: Done creating new environment.