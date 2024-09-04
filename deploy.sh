#!/bin/bash

cd /var/www/flaskapp

# Ativar o ambiente virtual
source venv/bin/activate

# Atualizar o repositório
git pull origin main

# Instalar dependências
pip install -r requirements.txt

# Rodar testes (substitua com seu comando de teste se houver)
# python -m unittest discover

# Reiniciar o Apache para aplicar as alterações
sudo systemctl restart apache2
