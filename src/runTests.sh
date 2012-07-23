#!/bin/bash                                                                                                                                                    
# -*- coding: UTF8 -*-
REPERTOIRE_SCRIPT=`dirname $0`
REPERTOIRE_TEST="$REPERTOIRE_SCRIPT/test/python"
export PYTHONPATH="$REPERTOIRE_SCRIPT/main/python/"
ROUGE="[31;1m"
VERT="[32;1m"
JAUNE="[33;1m"

find -name "*.pyc" -exec rm {} \;
         
nosetests $REPERTOIRE_TEST
