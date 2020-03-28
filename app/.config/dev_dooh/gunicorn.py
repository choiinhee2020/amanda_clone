daemon = False
chdir = '/srv/amanda/app'
bind = 'unix:/run/amanda.sock'
accesslog = '/var/log/gunicorn/amanda-access.log'
errorlog = '/var/log/gunicorn/amanda-error.log'
capture_output = True