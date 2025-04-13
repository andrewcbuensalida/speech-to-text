Use https://github.com/yt-dlp/yt-dlp.git to download audio from Youtube URL first.

## Create a virtual environment

```bash
python -m venv .venv
```

Activate the virtual environment (mac/linux):

```bash
source .venv/bin/activate
```

For Windows
```bash
.venv\Scripts\activate.bat
```

In the future, to deactivate venv
```bash
.venv\Scripts\deactivate.bat 
```

## Install dependencies. This is not needed if doing a pip install in the notebook
pip install -r requirements.txt

## To save dependencies into requirements.txt
pip freeze > requirements.txt

## To create a pull request using github cli
`gh pr create --base dev`

## Start the app with
`python main.py`