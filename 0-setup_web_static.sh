#!/usr/bin/env bash
# Script that sets up web servers for the deployment of web_static

# Update and install Nginx
sudo apt-get update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'

# Create required directories
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

# Create a test HTML file
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership to the ubuntu user
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

# Restart Nginx to apply changes
sudo service nginx restart

