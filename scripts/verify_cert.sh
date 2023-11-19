#!/bin/bash

openssl req -text -in yourdomain.csr -out verify.csr -verify
