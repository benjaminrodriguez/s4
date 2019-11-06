from subprocess import run, PIPE
x = run(["ls", "-l", "/dev/null", "/dev/net/tcp"],
        stdout=PIPE, stderr=PIPE)

print('Sans .decode:\n-------------')
print('stdout: {}\nstderr: {}\n'.format(x.stdout, x.stderr))
print('Avec .decode:\n-------------')
print('stdout: {}\nstderr: {}\n'.format(x.stdout.decode('ascii'),
                                        x.stderr.decode('utf8')))
