#!/usr/bin/env python
#coding=utf-8

import cgitb
cgitb.enable()
from original import *
from printChannels import channels_operation


sp_id = get_formData('which_sp')    
channels_operation(sp_id[0])
    
    