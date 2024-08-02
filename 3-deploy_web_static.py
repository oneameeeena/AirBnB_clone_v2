#!/usr/bin/python3
"""
Fabric script based on the file 1-pack_web_static.py that distributes an
archive to the web servers
"""

from fabric.api import put, run, env
from os.path import exists
env.hosts = ['54.89.109.87', '100.25.190.21']


def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False
        
        try:
            file_n = archive_path.split("/")[-1]
            no_ext = file_n.split(".")[0]
            path = "/data/web_static/releases/"
        
        # Upload the archive to the /tmp/ directory of the server
        put(archive_path, '/tmp/')
        
        # Create the directory where the release will be unpacked
        run('mkdir -p {}{}/'.format(path, no_ext))
        
        # Unpack the archive
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))
        
        # Remove the archive from the /tmp/ directory
        run('rm /tmp/{}'.format(file_n))
        
        # Move the contents of the web_static folder to the parent folder
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        
        # Remove the now empty web_static folder
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        
        # Remove the current symbolic link
        run('rm -rf /data/web_static/current')
        
        # Create a new symbolic link to the new release
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        
         return True
         except Exception as e:
            print(f"Error: {e}")
        return False

