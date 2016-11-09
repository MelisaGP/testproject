#Universidad Icesi 
#Curso: Sistemas Operativos 
#Estudiante: Melisa 
#Parcial de sistemas operativos 2
#Tema: Integración continua, Pruebas unitarias a servicios web

Enable network interfaces at boot (nat, bridge)

Update server date 

```sh
yum install ntp ntpdate ntp-doc
chkconfig ntpd on
ntpdate pool.ntp.org
/etc/init.d/ntpd start
```

***(Optional)*** You can configure additional parameters for ntd in the configuration file

```sh
vi /etc/ntp.conf
```

Instalo las siguientes dependencias

```sh
yum install java-1.7.0-openjdk
yum install wget -y
yum install git -y
sudo wget -O /etc/yum.repos.d/jenkins.repo http://pkg.jenkins-ci.org/redhat/jenkins.repo
sudo rpm --import https://jenkins-ci.org/redhat/jenkins-ci.org.key
sudo yum install jenkins
```

Inicio el servidor de Jnekins,  abro el puerto 8080 para probar y reinicio el iptables
```sh
chkconfig jenkins on
service jenkins start
vi /etc/sysconfig/iptables
-A INPUT -m state --state NEW -m tcp -p tcp --dport 8080 -j ACCEPT
service iptables restart
```

Install Python package manager and virtualenv package

```sh
wget https://bootstrap.pypa.io/get-pip.py
python get-pip.py
pip install virtualenv
```

Give user jenkins temporary permissions to use a console while preparing the virtualenvironment for the project. Save file changes with **esc, :x**

```sh
vi /etc/passwd
hago el cambio de jenkins a /bin/bash
```

Create a virtual environment for the project

```sh
su jenkins
mkdir /var/lib/jenkins/.virtualenvs
cd /var/lib/jenkins/.virtualenvs
virtualenv testproject
. testproject/bin/activate
```

***(Optional)*** You can specify the Python version for using in the environment
```sh
virtualenv -p /usr/bin/python3.0 <path/to/new/virtualenv/>
```

Install requirements for the project in the virtualenv

```sh
pip install xmlrunner
pip install unittest2
pip install pytest
pip install pytest-cov
pip install flask
```

Export dependencies for the project. You must have your virtual environment activated. In a project, you must provide the requeriments file to your developing team

```sh
pip freeze > requirements.txt
```

## Configure Jenkins through website

Get the ip address of the server and open it in a browser

http://192.168.56.101:8080

If jenkins stuck on the loading screen, go into the server console and restart jenkins service. Follow
the wizard configurations. Select the suggested plugins option, also install github plugin, cobertura plugin, html publisher plugin. You can install more plugins later (manage jenkins -> manage plugins)

Create a free-style project with the name **testproject**. Use the configurations as show in the graphics below

![][1]

If the installation was correct, you can see jenkins reports

![][2]

![][3]

If you also want to show coberture tests use the following configuration

![][4]

Instalo el ambiente
```sh
wget https://bootstrap.pypa.io/get-pip.py
python get-pip.py
pip install virtualenv
```

Create a user and a folder for your projects

```sh
adduser developer
passwd developer
su developer
mkdir ~/projects
mkdir ~/virtualenvs
```

Create the environment for the project, activate it and install requeriments

```sh
cd ~/virtualenvs
virtualenv testproject
. testproject/bin/activate
```

Get the requirements file from your devops engineer, and install dependencies on the testproject virtual environment

```sh
pip install -r requirements
```

Clono el repositorio que voy a utilizar, en este caso es el del profesor del curso

```sh
git clone https://github.com/d4n13lbc/testproject.git
```


[1]: images/jenkins_configuration_icesi.png
[2]: images/jenkins_ok.png
[3]: images/jenkins_console.png
[4]: images/jenkins_configuration_coverage_icesi.png

<!---
#Respuestas
set -e = termina inmediatamente si algun comando produce un error
python -m = permite ejecutar un modulo como script
instalar violations plugin
-->
