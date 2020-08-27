#!/usr/bin/env python3

import polyinterface
import sys
import os
import json
import glob
import time
import datetime
from subprocess import call
import os,subprocess
import json
import requests
from collections import defaultdict

from  Messana import MessanaCtrl

LOGGER = polyinterface.LOGGER

if __name__ == "__main__":

    try:
        LOGGER.info('Starting Messana Controller')
        polyglot = polyinterface.Interface('Messana_Control')
        polyglot.start()
        control = MessanaController(polyglot)
        control.runForever()
    except (KeyboardInterrupt, SystemExit):
        sys.exit(0)
