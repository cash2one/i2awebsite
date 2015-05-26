from __future__ import with_statement
import datetime
import time
from fabric.api import local, run, cd, put, sudo, env, show, prefix

env.disable_known_hosts = True

def _deploy(remote_dir, svn_rev, postfix):
    svn_rev = svn_rev or str(int(time.time()))
    remote_dir = remote_dir if remote_dir[-1] != '/' else remote_dir[:-1]
    postfix = '-'.join(remote_dir.split('/')) + postfix
 
    with show('debug'):
        local('tar czf /tmp/webapp' + postfix + '.tar.gz * --exclude="*.svn"')
 
    with cd(remote_dir):
        dirname = 'r-%s' % svn_rev
        sudo('rm -rf %s; mkdir %s' % (dirname, dirname))
        put('/tmp/webapp' + postfix + '.tar.gz', '/tmp/')
        sudo('tar xmzf /tmp/webapp' + postfix + '.tar.gz -C %s/%s' % (remote_dir, dirname))

        sudo('rm -rf webapp')
        sudo('cp -Rp %s webapp' % dirname)
        sudo('chown -R www-data: webapp')
        sudo('echo "%s" > webapp/VERSION' % svn_rev)

def deploy(remote_dir, svn_rev='', nfs=False):
    """
    Deploy the app to PROD
    """
    _deploy(remote_dir, svn_rev, '-prod')
    with show('debug'):
        with cd(remote_dir + '/webapp'):
            sudo('chmod +x manage.py')
            with prefix('source /opt/virtualenv/i2awebsite/bin/activate'):
                sudo('./manage.py collectstatic --noinput')
    sudo('service i2awebsite restart')
    return

