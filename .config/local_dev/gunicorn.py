daemon = False
chdir = '/srv/amanda_clone/app'
bind = 'unix:/run/amanda_clone.sock'
accesslog = '/var/log/gunicorn/amanda_clone-access.log'
errorlog = '/var/log/gunicorn/amanda_clone-error.log'
capture_output = True