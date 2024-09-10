@echo off

python -m pip install --upgrade pip

python -m venv venv

call venv\Scripts\activate

pip install -r requirements.txt

echo Ambiente configurado. Agora, rode o script usando: venv\Scripts\activate e python index.py
