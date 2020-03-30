daemon = False
chdir = '/srv/amanda_clone/app'
bind = 'unix:/run/amanda_clone.sock'
accesslog = '/var/log/gunicorn/amanda-access.log'
errorlog = '/var/log/gunicorn/amanda-error.log'
capture_output = True
