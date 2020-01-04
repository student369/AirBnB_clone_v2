#!/usr/bin/python3
"""Deploy the archive with Fabric"""
import os
from fabric import api
from fabric.contrib import files


api.env.hosts = ["35.229.67.166", "35.196.11.70"]
api.env.user = "ubuntu"
api.env.key_filename = "~/.ssh/holberton"


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
            api.run("ln -sf {} /data/web_static/current".format(opath))
            print("New version deployed!")
        except:
            return False
        else:
            return True
