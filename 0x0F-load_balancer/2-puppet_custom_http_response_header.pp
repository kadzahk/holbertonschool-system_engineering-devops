# 2. Add a custom HTTP header with Puppet
exec { 'HTTP_header_Puppet':
  command  => 'sudo apt-get -y update;
               sudo apt-get -y install nginx;
               echo "Hello World!" > /var/www/html/index.nginx-debian.html;
               service nginx start;
               sudo chmod 777 /etc/nginx;
               sudo chmod 777 /etc/nginx/nginx.conf;
               sudo sed -i "/sendfile on;/ a add_header X-Served-By $HOSTNAME;" /etc/nginx/nginx.conf;
               sudo service nginx restart',
  provider => 'shell',
}
