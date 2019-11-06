import paramiko
import sys

hostname = '10.20.0.1'
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.WarningPolicy)
username, password = 'root', 'root'

old_stderr = sys.stderr
sys.stderr = open('/dev/null', 'w')
client.connect(hostname, username=username, password=password)
sys.stderr = old_stderr

stdin, stdout, stderr = client.exec_command('id')
print('{}{}'.format(stdout.read().decode('utf8'),
                    stderr.read().decode('utf8')))

stdin, stdout, stderr = client.exec_command('ls -lAh')
print('{}{}'.format(stdout.read().decode('utf8'),
                    stderr.read().decode('utf8')))

