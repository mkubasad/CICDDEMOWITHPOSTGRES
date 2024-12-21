sudo systemctl stop nginx
sudo systemctl stop gunicorn
sudo systemctl stop gunicorn.socket
sudo systemctl daemon-reload
sudo systemctl start gunicorn
sudo systemctl start nginx
