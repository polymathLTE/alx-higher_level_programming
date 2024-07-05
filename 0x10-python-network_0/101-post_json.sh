#!/bin/bash
# script sends POST request with provided JSON file and URL
curl -s -X POST -d "$2" "$1"
