# svnContribution.py
#     Calculate numbers of lines each people committed
# in a svn repository.

########################################
# CONFIG
########################################
exts = ['.c', '.h','m','mm','.txt']
svnCommand = r'svn blame -x -w %s'

########################################
# GLOBLAL
########################################
import os
import re
pattObj  = re.compile('^\s*\d*\s*(\S*)\s*.*$')
allAuthors = {}

########################################
# BLAME
########################################
def fileProc(path):
    from os import popen
    thisAuthors = {}
    pipe = os.popen(svnCommand % path)
    #text = pipe.read()
    for text in pipe.readlines():
        matchObj = pattObj.match(text[0:-1])
        if allAuthors.has_key(matchObj.group(1)):
            allAuthors[ matchObj.group(1) ] += 1
        else:
            allAuthors[ matchObj.group(1) ] = 1
        if thisAuthors.has_key(matchObj.group(1)):
            thisAuthors[ matchObj.group(1) ] += 1
        else:
            thisAuthors[ matchObj.group(1) ] = 1
        pipe.close
    print 'Authors: ', thisAuthors
    
########################################
# SEARCH
########################################
from os.path import basename, isdir, join
from os import listdir
def walkIn(path, depth=0):
    #prefix = depth* '| ' + '-'
    if(isdir(path)):
        #print prefix, basename(path)
        for item in listdir(path):
            walkIn(os.path.join(path, item), depth + 1)
    else:
        #print prefix, basename(path)
        if os.path.splitext(path)[1] in exts:
            print path
            fileProc(path)
    
########################################
# MAIN
########################################
if __name__ == '__main__':
    from os.path import isdir
    root = raw_input('Root directory: [.] ')
    if root == '': root = '.'
    if not os.path.isdir(root):
        raise 'What you entered is not a path.'

    print 'Searching...'
    walkIn(root, 0)

    print '  Result'
    print '----------'
    for Author in allAuthors.keys():
        print Author, allAuthors[Author]
