try:
    from subprocess import check_output
except ImportError:
    import subprocess
    def check_output(cmd):
        return subprocess.Popen(cmd, stdout=subprocess.PIPE).communicate()[0]
import shlex
import os
import getpass

fedmsg_repo = "https://github.com/rossdylan/fedmsg.git"
tahrir_repo = "https://github.com/ralphbean/tahrir.git"
pypi_packages = [
        'virtualenv',
        'virtualenvwrapper'
]

distro_packages = [
        'mysql',
        'mysql-python',
        'git',
        'zeromq',
        'zeromq-devel',
]
def runSudoCommand(command):
    return runCommand("echo {0} | sudo -S {1}".format(
    getpass.getpass("Enter password; "),
    command
    ))

def runCommand(command):
    return check_output(shlex.split(command))

def installPYPIPackages():
    print runSudoCommand("pip install " + " ".join(pypi_packages))

def installDistroPackages():
    print runSudoCommand("yum install " + " ".join(distro_packages))

def createVirtualEnvs():
    print runCommand("source /usr/bin/virtualenvwrapper.sh")

    print runCommand("rmvirtualenv tahrir")
    print runCommand("rmvirtualenv fedmsg")

    print runCommand("mkvirtualenv tahrir")
    print runCommand("mkvirtualenv fedmsg")

    print runCommand("deactivate")

def installFedmsg():
    print runCommand("git clone {0}".format(fedmsg_repo))
    top_dir = os.getcwd()
    os.chdir("fedmsg")
    print runCommand("git checkout fedbadges")
    print runCommand("workon fedmsg")
    print runCommand("python setup.py install")
    print runCommand("deactivate")
    os.chdir(top_dir)

def installTahrir():
    print runCommand("git clone {0}".format(tahrir_repo))
    top_dir = os.getcwd()
    os.chdir("tahrir")
    print runCommand("git checkout develop")
    print runCommand("workon tahrir")
    print runCommand("python setup.py install")
    print runCommand("deactivate")
    os.chdir(top_dir)

def quickstart():
    installPYPIPackages()
    installDistroPackages()
    createVirtualEnvs()
    installFedmsg()
    installTahrir()

if __name__ == "__main__":
    quickstart()
