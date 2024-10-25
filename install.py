import pip

def install_package(package_name):
    pip.main(['install', package_name])

# Example of installing a package
install_package('requests')

import requests
print(requests.get('https://api.github.com').json())

