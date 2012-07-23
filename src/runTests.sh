#!/bin/bash                                                                                                                                                    
# -*- coding: UTF8 -*-
REPERTOIRE_SCRIPT=`dirname $0`
REPERTOIRE_TEST="$REPERTOIRE_SCRIPT/test/python"
export PYTHONPATH="$REPERTOIRE_SCRIPT/main/python/"

find . -name "*.pyc" -exec rm {} \;
         
nosetests $REPERTOIRE_TEST
