import pathlib

req_file = tdu.expandPath(ipar.ExtPython.Pyreqs)
install_target = tdu.expandPath(ipar.ExtPython.Target)
install_script_path = pathlib.Path(install_target).parents[0]

win_file = install_script_path / 'dep_install.cmd'
mac_file = install_script_path / 'dep_install.sh'

# windows template
win_txt = '''
:: update pip
python -m pip install --user --upgrade pip


:: install from requirements file
py -3.9 -m pip install -r "{reqs}" --target="{target}"
'''

#mac template
mac_txt = '''
#!/bin/bash

dep=$(dirname "$0")
pythonDir=/python

# change current directory to where the script is run from
dirname "$(readlink -f "$0")"

#fix up pip with python3
curl https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py

#update dependencies
#make sure pip is up to date
python3 -m pip install --user --upgrade pip

#install requirements
python3 -m pip install -r "{reqs}" --target="{target}"
'''

formatted_win_txt = win_txt.format(reqs=req_file, target=install_target)
formatted_mac_txt = win_txt.format(reqs=req_file, target=install_target)

#print(formatted_win_txt)
#print(formatted_mac_txt)

with open(str(win_file), "w+") as win_script:
	win_script.write(formatted_win_txt)

with open(str(mac_file), "w+") as mac_script:
	mac_script.write(formatted_mac_txt)