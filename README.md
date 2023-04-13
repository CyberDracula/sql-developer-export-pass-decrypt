# SQL Developer Tool - Decrypt exported connection passwords

This should work from `SQL Developer` 18+ (if you try it on lower versions please let me know, never test it :) )

Sometimes you need a password for `SQL Developer` a solution will be to use [Show Me password](http://show-me-password.tomecode.com/) extension, but from what i tested it no longer works for version above 19.
This tool will work by exporting all the connections from `SQL Developer` to a `json` (of course with passwords included). The only thing you need to remember is the key (`secret`) you used to generate the exported file!

==Passwords are AES-CBC encrypted without the `secret` you can't 'hack' them (KPA included)==

## Tools

- `decrypt.py` -> most basic tool, you just give the encrypted password string and the `secret` and it will return the decrypted value
- `decryptJson.py`
    * This will decrypt all the exported `json` file. The output will be a table with all connections details user and decrypted password. You still need to know the `secret` used for the exported `json`.
    * **SOON** you can choose to `brute force` the decryption if the `secret` is unknown (this will be paintfull to wait ... but if you got time and resources .... :) )

## How to

### Install it

`pip install -r requirements.txt`

### Run it

Both scripts have helpers inluded if you run `python tool_file -h`