#!/usr/bin/env bash
# Script to prepare a server
sudo apt-get update
sudo apt-get install -y nginx
mkdir -p -m=755 /data/web_static/{releases/test,shared} || exit 0
echo "<marquee>Holberton School</marquee>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/current
chown -hR ubuntu:ubuntu /data
INFO='\\rlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;}'
sed -i "37i $INFO" /etc/nginx/sites-available/default
service nginx restart
exit 0
