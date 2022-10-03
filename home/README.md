# Guide

## How to run locally?
---

### Create virtual environment
```
python -m venv env
```

### Install requirements
```
pip install -r requirements.txt
```

### Start server
```
python manage.py runserver
```

## How to use tailwind css?
---

### Install node.js' npm
- For mac:
  ```
  brew install node
  ```
- For linux:
  ```
  sudo apt install npm
  ```
- For windows visit [this site](https://nodejs.org/en/download/)

### Configure `tugas-tengah-semester/settings.py`
- For mac/linux: Just ignore this step
- For windows uncomment this section
  ```
  # NPM_BIN_PATH = "C:\\Program Files\\nodejs\\npm.cmd"
  ```

### Install tailwind in venv
```
python manage.py tailwind install
```

### Start tailwind development env
```
python manage.py tailwind start
```