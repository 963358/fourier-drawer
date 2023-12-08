#!/bin/bash

# only supports mac/windows... linux users can figure it out themselves !

if [[ "$OSTYPE" == "darwin"* ]]
then
    brew install $(cat mac-install.txt)
fi

pip install -r requirements.txt

