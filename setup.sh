#!/bin/bash

# only supports mac/windows... linux users can figure it out themselves !

if [[ "$OSTYPE" == "darwin"* ]]
then
    brew install $(mac-install.txt)
else

pip install -r requirements.txt

fi
