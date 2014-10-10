#!/usr/bin/python
# the source code was referenced from http://whatwant.tistory.com/578

import os

# if this file is executed in command line, then __name__ == __main__

if __name__ == "__main__":
    print "__file__ = " + __file__
    print "os.path.dirname(__file__) = " + os.path.dirname(__file__)
    print "\n"
    print "os.path.realpath(__file__) = " + os.path.realpath(__file__)
    print (
        "os.path.realpath(or.path.dirname(__file__)) = " + 
        os.path.realpath(os.path.dirname(__file__))
    )
    
    print "os.getcwd() = " + os.getcwd()
    print (
        "os.path.basename(os.path.realpath(__file__)) = " +
        os.path.basename(os.path.realpath(__file__))
    )
    print (
        "os.path.abspath(os.path.realpath(__file__)) = " +
        os.path.abspath(os.path.realpath(__file__))
    )
    print (
        "os.path.dirname(os.path.dirname(__file__)) = " +
        os.path.dirname(os.path.dirname(__file__))
    )
    
    print (
        "os.path.realpath('../' + or.path.dirname(__file__)) = " + 
        os.path.realpath('../' + os.path.dirname(__file__))
    )
 

