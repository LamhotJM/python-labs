# Python Labs
pip install MySQL-connector-python
pip install ConfigParser


python3 -m venv env
source ./env/bin/activate 

/usr/local/mysql/bin/mysql -u root -p

ALTER USER 'root3'@'localhost'
IDENTIFIED WITH mysql_native_password BY 'root3';


ALTER USER 'root3'@'localhost'
IDENTIFIED WITH caching_sha2_password BY 'root3';


python fetchone.py 
