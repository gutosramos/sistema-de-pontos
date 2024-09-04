#!/bin/bash
cd /var/www/flaskapp
git pull origin main
source /var/www/flaskapp/venv/bin/activate
pip install -r requirements.txt
sudo systemctl restart apache2
