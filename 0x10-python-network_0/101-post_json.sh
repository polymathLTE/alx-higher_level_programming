#!/bin/bash
# script sends POST request with provided JSON file and URL
curl -s -H "Content-Type: application/json" -X POST -d @"$2" "$1"
