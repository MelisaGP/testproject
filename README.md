#Universidad Icesi 
#Curso: Sistemas Operativos 
#Estudiante: Melisa 
#Parcial de sistemas operativos 2
#Tema: Integración continua, Pruebas unitarias a servicios web

Enable network interfaces at boot (nat, bridge)

Modifico el servidor

```sh
yum install ntp ntpdate ntp-doc
chkconfig ntpd on
ntpdate pool.ntp.org
/etc/init.d/ntpd start
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

Instalo el paquete de Python para el entorno virtual

```sh
wget https://bootstrap.pypa.io/get-pip.py
python get-pip.py
pip install virtualenv
```

```sh
vi /etc/passwd
hago el cambio de jenkins a /bin/bash
```

Hice la creación de un ambiente virtual y lo activé

```sh
su jenkins
mkdir /var/lib/jenkins/.virtualenvs
cd /var/lib/jenkins/.virtualenvs
virtualenv testproject
. testproject/bin/activate
```
Copio lo realizado en el parcial 1 en un nuevo directorio llamado parcial_2
```sh
cp -r /home/filesystem_user parcial_2
```

Install requirements for the project in the virtualenv

```sh
pip install xmlrunner
pip install unittest2
pip install pytest
pip install pytest-cov
pip install flask
```


Para la apertura de jenkins de el servidor, lo abro con la dirección ip y el puerto abierto

http://127.0.0.1:8080

Hago las instalaciones 
Instalo el ambiente
```sh
wget https://bootstrap.pypa.io/get-pip.py
python get-pip.py
pip install virtualenv
```

Creo un usuario y un folder para el proyecto

```sh
adduser developer
passwd developer
su developer
mkdir ~/projects
mkdir ~/virtualenvs
```

Get the requirements file from your devops engineer, and install dependencies on the testproject virtual environment

```sh
pip install -r requirements
```

Clono el repositorio que voy a utilizar, en este caso es el del profesor del curso

```sh
git clone https://github.com/d4n13lbc/testproject.git

Forked from d4n13lbc/testproject
```


