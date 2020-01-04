#!/usr/bin/python3
# Script to compress using .tgz
import os
from fabric import api
from datetime import datetime


def do_pack():
    """Function to create a task to web_static

    Returns: path of .tgz or None
    """
    with api.settings(warn_only=True):
        isdir = os.path.isdir("versions")
        if not isdir:
            mkdir = api.local("mkdir versions")
            if mkdir.failed:
                return None
        sfx = datetime.now().strftime("%Y%m%d%M%S")
        path = "versions/web_static_{:s}.tgz".format(sfx)
        tar = api.local("tar -cvzf {:s} web_static".format(path))
        if tar.failed:
            return None
        size = os.stat(path).st_size
        print("wb_static packed: {} -> {}Bytes".format(path, size))
        return path
