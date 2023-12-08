#!/bin/bash


# install cairo
if [[ "$OSTYPE" == "darwin"* ]]
then
    brew install cairo pango

fi

pip install -r requirements.txt
