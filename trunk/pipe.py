import threading
import sys
import popen2

class Piper(threading.Thread):

    def __init__(self, readPipe, output):
        threading.Thread.__init__(self)

        if not isinstance(readPipe, file):
            raise TypeError, "readPipe parameter must be of File type"
        #if not isinstance(output, file):
        #    raise TypeError, "output parameter must be of File type"

        self.readPipe = readPipe
        self.output = output
        self.toStop = False

    def run(self):
        print "Running"
        while not self.toStop and not self.readPipe.closed:
            read = self.readPipe.readline()
            self.output.write(read)
            self.output.flush()
        print "Stopped"

    def stop(self):
        self.toStop = True


if __name__ == "__main__":
    r, w = popen2.popen4('python -u')
    piper = Piper(r, sys.stdout)
    piper.start()
    w.write("print 'Hello!'\r\n")
    w.flush()
    w.write("print 'Goodbye!'\r\n")
    w.flush()
    import time; time.sleep(2)
    w.close()
    #import time; time.sleep(3)
    #r.close()
    piper.stop()