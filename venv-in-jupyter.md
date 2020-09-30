# Using venv in Jupyter notebook

```bash
python -m venv <venv-name>
source <venv-name>/bin/activate
pip install jupyter
ipython kernel install --user --<venv-name>
jupyter notebook
```