#!/bin/bash
# sends POST request to passed URL and displays response body
 curl -d "email:test@gmail.com, subject:I will always be here for the PLD" -X POST "$1"
