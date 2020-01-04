#!/usr/bin/python3
"""Decompress and deploy to the servers"""
import os
from fabric import api, decorators
from fabric.contrib import files
from datetime import datetime


api.env.hosts = ["holberton1", "holberton3"]
api.env.hosts = ["35.229.67.166", "35.196.11.70"]
api.env.user = "ubuntu"
api.env.key_filename = "~/.ssh/holberton"


def deploy():
    """Wrapper to pack and move to servers"""
    return do_deploy(do_pack())


@decorators.runs_once
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


def do_deploy(archive_path):
    """Function move the path to the servers

    Args:
        archive_path (str): path of the .tgz file
    Returns: True on success, False otherwise
    """
    if not os.path.isfile(archive_path):
        return False
    with api.cd("/tmp"):
        basename = os.path.basename(archive_path)
        root, ext = os.path.splitext(basename)
        opath = "/data/web_static/releases/{}".format(root)
        try:
            ppath = api.put(archive_path)
            if files.exists(opath):
                api.run("rm -rdf {}".format(opath))
            api.run("mkdir -p {}".format(opath))
            api.run("tar -xzf {} -C {}".format(ppath[0], opath))
            api.run("rm -f {}".format(ppath[0]))
            api.run("mv -u {}/web_static/* {}".format(opath, opath))
            api.run("rm -rf {}/web_static".format(opath))
            api.run("rm -rf /data/web_static/current")
            api.run("ln -s {} /data/web_static/current".format(opath))
            print("New version deployed!")
        except:
            return False
        else:
            return True

