Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:25:58) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #!/usr/bin/env python
import subprocess
import os
from optparse import OptionParser
import hashlib

user_keyVal = []

def hash_username(self, username):
    return hash(self.username)

def make_secret(self, hashed_user): 
    user_keyVal += hash_username
    user_keyVal += hashlib.sha224(hash_username(self.hashed_user)).hexdigest()
    if(user_keyVal.length == 1) {
        print("Success!")
    }

def main():
    usage = "usage: python %prog [options] arg"
    parser = OptionParser(usage)
    parser.add_option("-u", "--user", dest="user", type=int,
                                        help="Enter username to hash")
    (options, args) = parser.parse_args()

    if (options.user is None):
        subprocess.call("python %prog --help", shell=True)
    else:
        make_secret(options.user)
        print(user_keyVal)
        
if _name_ == "_main_":
        main()
exit()