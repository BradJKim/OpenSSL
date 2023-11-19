#!/bin/bash

openssl rsautl -encrypt -inkey keys/cguti_public.key -pubin -in files/file.txt -out files/encrypted_file.txt
