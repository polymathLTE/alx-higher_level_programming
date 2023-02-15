#!/bin/bash

rm *~

find . -type f -name "*.py" -exec chmod u+x {} \;
find . -type f -name "*~" -delete
