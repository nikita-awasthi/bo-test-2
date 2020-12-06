# !/usr/bin/env python3
# encoding: utf-8

"""
custom wakatime installation script
"""

from __future__ import print_function

import os
import sys
import subprocess
from os.path import expanduser

__author__ = 'Gaurav Tolani'


def implement_sequential_steps():
    """
    Implements steps required for custom wakatime installation
    Steps-
    1. install pip using python2
    2. install requests[security] pip package
    3. copy the requests[security] name to wakatime required packages directory
    4. replace original wakatime api.py file with new api.py file
    5. add blueoptima proxy certificates at wakatime directory
    :return:
    """
    # OS specific path setting
    # default_python_version = '.'.join(str(sys.version).split()[0].split('.')[:2])
    wakatime_dir_path = []
    site_packages_path = subprocess.check_output('python -m site --user-site', shell=True).rstrip()
    # print(site_packages_path)
    for dirpath, dirnames, filenames in os.walk(site_packages_path):
        for each_dir in dirnames:
            each_dir_str = each_dir.decode("utf-8")
            if each_dir_str == 'wakatime':
                # print('found')
                for dirpath_wk, dirnames_wk, filenames_wk in os.walk(os.path.join(site_packages_path, each_dir)):
                    # print('1', dirnames_wk)
                    # print('2', dirpath_wk)
                    # print('3', filenames_wk)
                    for each_file_name in filenames_wk:
                        if each_file_name.decode("utf-8") == 'api.py':
                            wakatime_dir_path.append(os.path.join(site_packages_path, each_dir).decode("utf-8"))

    if os.name == 'posix':
        wakatime_dir_path.append(os.path.join(expanduser("~"), '.wakatime/wakatime-master/wakatime'))
    else:
        print('Identified OS - Windows')
        print('This script is not written for windows OS. Please contact gaurav.tolani@blueoptima.com')
        # wakatime_dir_path = os.path.expanduser("C:\Users\sahoosu\AppData\Roaming\WakaTime\wakatime-master\wakatime")

    wakatime_dir_path = list(set(wakatime_dir_path))
    print(wakatime_dir_path)
    print('Executing steps...')
    try:
        # os.system('curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py')
        # os.system('python get-pip.py')
        # print('step 1: success')

        # os.system('pip install requests[security]')
        # print('step 2: success')
        print('executing step 1')
        requests_package_path = os.path.join(os.path.split(os.path.abspath(__file__))[0], 'requests/')
        for each_path in wakatime_dir_path:
            os.system("cp -r {} {}packages/".format(requests_package_path, str(each_path)+'/'))
        # print('step 1: success')

        print('executing step 2')
        api_py_path = os.path.join(os.path.split(os.path.abspath(__file__))[0], 'api.py')
        for each_path in wakatime_dir_path:
            os.system("cp {} {}".format(str(api_py_path), str(each_path)+'/'))
        # print('step 2: success')

        print('executing step 3')
        api_py_path = os.path.join(os.path.split(os.path.abspath(__file__))[0], 'ca-certificates.crt')
        for each_path in wakatime_dir_path:
            os.system("cp {} {}".format(str(api_py_path), str(each_path)+'/'))
        # print('step 3: success')

        return True

    except Exception as e:
        print("Error installing custom wakatime api. Error: {}".format(str(e)))
        return False


if __name__ == '__main__':
    install_status = implement_sequential_steps()
    if install_status:
        print('custom wakatime successfully installed!')
    else:
        print('Issue installing custom wakatime. Contact gaurav.tolani@blueoptima.com')
