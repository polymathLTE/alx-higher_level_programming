#!/bin/bash
# bash script takes URL as argument and sends GET request
curl -H "X-School-User-Id: 98" -X GET "$1"
