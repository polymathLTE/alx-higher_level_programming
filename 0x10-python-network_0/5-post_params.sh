#!/bin/bash
# sends POST request to passed URL and displays response body
curl -s -d "email=test@gmail.com&subject=I will always be here for PLD" -X POST "$1"
