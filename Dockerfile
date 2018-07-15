FROM httpd:2.4.33

ARG APACHE_ROOT="/usr/local/apache2"

# Install alpine packages
RUN apt-get update
RUN apt-get install -y libapache2-mod-wsgi-py3 python3-pip git
RUN pip3 install --upgrade pip

COPY requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt

# Create folder for Apache daemon processes (req'd)
RUN mkdir -p /var/run/apache2/wsgi

# Add custom httpd.conf elements
COPY httpd.conf /tmp/httpd.conf
RUN /bin/sh -c "cat /tmp/httpd.conf >> /usr/local/apache2/conf/httpd.conf"

# Copy snake files
RUN mkdir -p /var/www
COPY snakes /var/www/snakes
