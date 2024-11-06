@echo off

cls

title Preparando Ambiente

echo Criando ambiente virtual...
python -m venv venv

echo Ativando ambiente virtual...
call venv\Scripts\activate

echo Instalando requirements...
pip install -r requirements.txt >NUL

echo Ambiente pronto para uso!