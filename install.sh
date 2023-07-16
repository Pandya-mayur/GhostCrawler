#!/bin/bash
mkdir -p tmp_build 
# Makes directory for dependencies and executable to be installed

mkdir -p tmp_dist

pip install pyinstaller 

# Creates executable file and sends dependences to the recently created directories
pyinstaller --onefile --workpath ./tmp_build --distpath ./tmp_dist GhostCrawler.py

# Puts the executable in the current directory
mv tmp_dist/GhostCrawler . 

# Removes both directories and unneeded file
rm -r tmp_build tmp_dist
rm GhostCrawler.spec
