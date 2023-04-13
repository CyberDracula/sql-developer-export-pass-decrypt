import argparse
from argparse import RawTextHelpFormatter

from decryptUtil import decrypt


# argument logic
parser = argparse.ArgumentParser(description='This script will help you decrypt passwords saved in the json/xml exported by Oracle SQL Developer. This is not a brute force tool, you still need to know the password used to export the file', formatter_class=RawTextHelpFormatter)
parser.add_argument('-e', help='Targeted encrypted password (found in json file)',type=str,required=True,dest='encryptedPass')
parser.add_argument('-p', help='Password used to export the file.', type=str,required=True,dest='secret')
args = parser.parse_args()

d = decrypt(args.encryptedPass, args.secret)
if d:
    print("[+++] Decrypted password: %s" % d)