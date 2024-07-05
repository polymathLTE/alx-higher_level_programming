#!/bin/bash
# this script retrieves the byte size of a HTTP response
curl -s "$1" | wc -c
