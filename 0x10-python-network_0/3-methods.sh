#!/bin/bash
# script that takes in a URL and displays all its acceptable HTTP methods
curl -sI "$1" | grep "Allow" | cut -d ' ' -f 2-
