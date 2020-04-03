#automate the task of creating a custom HTTP header response
exec { 'HTTP Configuration':
  command  => "apt-get update && apt-get -y install nginx && echo -e 'Holberton School' > sudo /var/www/html/index.html && sed -i '/listen 80 default_server;/a rewrite ^/redirect_me https://facebook.com permanent;' /etc/nginx/sites-available/default && sed -i '22i add_header X-Served-By $hostname;' /etc/nginx/nginx.conf && service nginx start",
  provider => 'shell',
}
