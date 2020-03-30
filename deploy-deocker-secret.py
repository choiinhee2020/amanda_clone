#!/usr/bin/env python
import os
import subprocess
from pathlib import Path

DOCKER_IMAGE_TAG = 'johnkdo2020/amanda_clone'
DOCKER_OPTIONS = [
    ('--rm', ''),
    ('-it', ''),
    # background로 실행하는 옵션 추가
    ('-d', ''),
    ('-p', '80:80'),
    ('-p', '443:443'),
    ('--name', 'amanda_clone'),

    # Let's Encrypt volume
    ('-v', '/etc/letsencrypt:/etc/letsencrypt'),
]
USER = 'ubuntu'
HOST = '52.78.95.18'
TARGET = f'{USER}@{HOST}'
HOME = str(Path.home())
IDENTITY_FILE = os.path.join(HOME, '.ssh', 'amantha.pem')
SOURCE = os.path.join(HOME, 'projects', 'fastcampus', 'project_with_team', 'personal-projects', 'amanda_clone')

SECRETS_FILE = os.path.join(SOURCE, 'secrets.json')

def run(cmd, ignore_error=False):
    process = subprocess.run(cmd, shell=True)
    if not ignore_error:
        process.check_returncode()


def ssh_run(cmd, ignore_error=False):
    run(f"ssh -o StrictHostKeyChecking=no -i {IDENTITY_FILE} {TARGET} -C {cmd}", ignore_error=ignore_error)


# 1. 호스트에서 도커 이미지 build, push
def local_build_push():
    run(f'poetry export -f requirements.txt > requirements.txt')
    run(f'sudo docker build -t {DOCKER_IMAGE_TAG} .')
    run(f'sudo docker push {DOCKER_IMAGE_TAG}')


# 서버 초기설정
def server_init():
    ssh_run(f'sudo apt update')
    ssh_run(f'sudo DEBIAN_FRONTEND=noninteractive apt dist-upgrade -y')
    ssh_run(f'sudo apt -y install docker.io')


# 2. 실행중인 컨테이너 종료, pull, run
def server_pull_run():
    ssh_run(f'sudo docker stop amanda_clone', ignore_error=True)
    ssh_run(f'sudo docker pull {DOCKER_IMAGE_TAG}')
    ssh_run('sudo docker run {options} {tag} /bin/bash'.format(
        options=' '.join([
            f'{key} {value}' for key, value in DOCKER_OPTIONS
        ]),
        tag=DOCKER_IMAGE_TAG,
    ))


# 3. Host에서 EC2로 secrets.json을 전송, EC2에서 Container로 다시 전송
def copy_secrets():
    run(f'scp -i {IDENTITY_FILE} {SECRETS_FILE} {TARGET}:/tmp', ignore_error=True)
    ssh_run(f'sudo docker cp /tmp/secrets.json amanda_clone:/srv/amanda_clone')

# 4. Container에서 collectstatic, supervisor실행
def server_cmd():
    ssh_run(f'sudo docker exec amanda_clone /usr/sbin/nginx -s stop', ignore_error=True)
    ssh_run(f'sudo docker exec amanda_clone python manage.py collectstatic --noinput')
    ssh_run(f'sudo docker exec -it -d amanda_clone '
           f'supervisord -c /srv/amanda_clone/.config/local_dev/supervisord.conf -n')
    # ssh_run(f'sudo docker exec -it -d amanda_clone '
    #        f'supervisord -c /srv/amanda_clone/.config/dev_dooh/supervisord.conf -n')



if __name__ == '__main__':
    try:
        print('aa')
        local_build_push()
        server_init()
        server_pull_run()
        copy_secrets()
        server_cmd()
        print('bb')
    except subprocess.CalledProcessError as e:
        print('deploy-docker-secrets Error!')
        print(' cmd:', e.cmd)
        print(' returncode:', e.returncode)
        print(' output:', e.output)
        print(' stdout:', e.stdout)
        print(' stderr:', e.stderr)











