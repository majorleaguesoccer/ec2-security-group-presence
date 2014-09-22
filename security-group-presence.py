import time, sys, signal

def sighandler(signum, frame):
    print 'signal handler called with signal: %s ' % signum
    sys.exit() # make sure you add this so the main thread exits as well.

def main(argv=None):
    signal.signal(signal.SIGTERM, sighandler) # so we can handle kill gracefully
    signal.signal(signal.SIGINT, sighandler) # so we can handle ctrl-c
    print "in  main looping"

if __name__ == '__main__':
    main(sys.argv)
    while 1:  # this will force your main thread to live until you terminate it.
       print "outside of  main looping"
       time.sleep(100)
