# Pip install and save to requirements.txt

Upon installing a package in a Python virtual environment (python3-venv), it doesn't automatically save that package to a requirements file (unlike npm which saves installed packeges in the package.json file). Here is a simple bash script (and a batch script for Windows systems) that will install the package via pip and will save that package name (and other installed packages in that virtual environment) in a requirements.txt file.

For example, to install the [python requests](https://requests.readthedocs.io/en/master/) module - 

```bash
sh pi.sh requests
```

Or in Windows systems -

```bash
pi.bat requests
```