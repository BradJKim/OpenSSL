#!/bin/bash

openssl rsautl -decrypt -inkey keys/brad_priv.key -in files/encrypted_file.txt > files/file_decrypted.txt
