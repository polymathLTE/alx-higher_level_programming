#!/bin/bash
# script that sends HTTP request and displays only the status code
curl -sI "$1" | grep HTTP | cut -d " " -f 2
