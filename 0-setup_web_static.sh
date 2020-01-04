#!/usr/bin/env bash
# Script to prepare a server
sudo apt-get update
OUTPUT="$(apt-cache policy nginx | grep Installed)"
if [[ $OUTPUT == *"(none)"* ]]
then
    sudo apt-get install -y nginx
fi
DIR1="./data"
DIR2="./data/web_static"
DIR3="./data/web_static/releases"
DIR4="./data/web_static/releases/test"
FILE1="./data/web_static/releases/test/index.html"
DIRNAME=""
FILENAME=""
SYMLINK="./data/web_static/current"
USER="ubuntu"
GROUP="ubuntu"
if [ ! -d $DIR1 ]
then
    DIRNAME="$(echo $DIR1 | cut -c3-)"
    mkdir "$DIRNAME"
fi
if [ ! -d $DIR2 ]
then
    DIRNAME="$(echo $DIR2 | cut -c3-)"
    mkdir "$DIRNAME"
fi
if [ ! -d $DIR3 ]
then
    DIRNAME="$(echo $DIR3 | cut -c3-)"
    mkdir "$DIRNAME"
fi
if [ ! -d $DIR4 ]
then
    DIRNAME="$(echo $DIR4 | cut -c3-)"
    mkdir "$DIRNAME"
fi
if [ ! -f $FILE1 ]
then
    FILENAME="$(echo $FILE1 | cut -c3-)"
    touch "$DIRNAME"
    echo "<marquee>Holberton School</marquee>" | sudo tee "$DIRNAME"
fi
if [ -L $SYMLINK ]
then
    rm $SYMLINK
    ln -sf $DIR4 $SYMLINK
else
    ln -sf $DIR4 $SYMLINK
fi
echo "Adding the ownership to $USER to the folder $DIR1"
chown -hR "$USER":"$GROUP" "$DIR1"
service nginx restart
exit 0
