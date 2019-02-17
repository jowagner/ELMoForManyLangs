#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# (C) 2019 Dublin City University
# All rights reserved. This material may not be
# reproduced, displayed, modified or distributed without the express prior
# written permission of the copyright holder.

import h5py
import sys

token_rep = h5py.File(sys.argv[1], 'r')

for key in token_rep.keys():
    print(key)

