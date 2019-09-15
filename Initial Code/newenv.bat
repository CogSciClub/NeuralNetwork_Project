@echo off
rem ***********************************************************************
rem Removes existing virtual environment and creates new virtual environment,
rem installing the required packages.
rem 
rem Usage:
rem 		newenv
rem
rem ***********************************************************************

:: Install virtualenv if it is not already
echo NEW ENV: Installing/updating virtualenv...
pip install virtualenv

:: Delete existing virtual environment (include, lib, scripts, tcl folders)
echo NEW ENV: Removing files...
RMDIR /S /Q Lib
RMDIR /S /Q Include
RMDIR /S /Q Scripts
RMDIR /S /Q tcl

:: Create new virtual environment
echo NEW ENV: Creating new environment...
virtualenv "%cd%"

:: Install the required packages
echo NEW ENV: Installing required packages...
call Scripts\activate.bat
pip install --upgrade pip
pip install -r requirements.txt

:: Environment setup
echo NEW ENV: Done creating new environment.

:: Check to make sure environment is set up correctly
echo NEW ENV: Checking environment configuration...
python env_check.py
echo NEW ENV: Done.

:: Deactivating virtual env
call Scripts\deactivate.bat