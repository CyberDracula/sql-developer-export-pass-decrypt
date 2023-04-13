import os
import sys
import argparse
from argparse import RawTextHelpFormatter
import json

from decryptUtil import decrypt
from prettytable import PrettyTable

class SmartFormatter(argparse.HelpFormatter):

    def _split_lines(self, text, width):
        if text.startswith('R|'):
            return text[2:].splitlines()  
        # this is the RawTextHelpFormatter._split_lines
        return argparse.HelpFormatter._split_lines(self, text, width)

# argument logic
parser = argparse.ArgumentParser(description='This script will help you decrypt passwords saved in the json/xml exported by Oracle SQL Developer. \nYou still need to know the password used to export the file.\nA brute force attack will be added but the time/resource cost is as expected ... so don\'t make any expectations from this.', formatter_class=RawTextHelpFormatter)
parser.add_argument('-e', help='Targeted encrypted password (found in json file)',type=str,required=True,dest='encryptedPass')
parser.add_argument('-p', help='Password used to export the file.', type=str,required=True,dest='secret')
parser.add_argument('-f', help='File path (relative/absolute)', type=str,required=True,dest='path')
parser.add_argument('-o', help='Output table to a file path', type=str,dest='outputPath')
args = parser.parse_args()


try:
    if os.path.isfile(args.path):
        print('File to be decrypted: ' + args.path)
        f = open(args.path)
        jsonFile = json.loads(f.read())
        if not jsonFile['connections']:
            raise Exception('"connections" not found in given file or empty!')
        
        tb = PrettyTable()
        tb.field_names = ['ConnName','connType','hostname','port','serviceName','customUrl','user','pass']

        for con in jsonFile['connections']:
            c = con['info']
            if c.get('password'):
                p = decrypt(c.get('password'), args.secret)
            else:
                p = 'None'
            tb.add_row([c.get('ConnName'),c.get('OracleConnectionType'),c.get('hostname'),c.get('port'),c.get('serviceName'),c.get('customUrl'),c.get('user'),p])

        # print result
        print(tb)

        # save to a file if needed
        if args.outputPath:
            fw = open(args.outputPath,'a')
            fw.write(str(tb))
            fw.close()
        f.close()

    else: raise Exception('File not found')
except Exception as e:
    print('Error: ' + str(e))