# Using venv in Jupyter notebook

For UNIX based systems -

```bash
python3 -m venv <venv-name>
source <venv-name>/bin/activate
pip install jupyter
ipython kernel install --user --<venv-name>
jupyter notebook
```

For Windows -

```bash
python -m venv <venv-name>
cd <venv-name>/Scripts
activate
cd ..
cd ..
pip install jupyter
ipython kernel install --user --<venv-name>
jupyter notebook
```

Create a new notebook from New > \<venv-name>

Check the location of activated python environment in the new created notebook -

For UNIX based systems -

```bash
!which python
```

For Windows -

```bash
!where python
```