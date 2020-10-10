#!/usr/bin/env python3
# coding: utf-8
# Veni Sancte Spiritus

# This code is under public domain.

import os
import argparse
import logging
import re


logging.basicConfig(
    format="[%(levelname)s]: %(message)s", level=logging.INFO)


parser = argparse.ArgumentParser(description="get plugins used by Jenkins job")
parser.add_argument("--jenkinshome", metavar="/tmp/jenkins-usage/jenkinsBackup",
                    help="Jenkins home location (default: {})".format(
                        os.getcwd()), default=os.getcwd())

arguments = parser.parse_args()

alreadyadded = []
pluginsalreadyadded = {}

for root, subFolders, files in os.walk(os.path.join(
        arguments.jenkinshome, "jobs")):
    if 'config.xml' in files:
        with open(os.path.join(root, 'config.xml'), 'r') as fin:
            for lines in fin:
                if 'plugin=' in lines:
                    before_keyword, keyword, after_keyword = lines.partition(
                        'plugin=')
                    jobname = os.path.basename(root)
                    plugin = re.sub(r'"(.+)@([0-9.]+)"/?>\n?',
                                    r'\1 ver. \2', after_keyword)

                    if [jobname, plugin] not in alreadyadded:
                        logging.info("{}: {}".format(jobname, plugin))

                         #   if plugin not in pluginsalreadyadded:
                          #      pluginsalreadyadded[plugin] = []

                          #  pluginsalreadyadded[plugin].append(jobname)

                        alreadyadded.append([jobname, plugin])

for root, subFolder, files in os.walk(os.path.join(
        arguments.jenkinshome, "plugins")):
    if "MANIFEST.MF" in files:
        with open(os.path.join(root, "MANIFEST.MF")) as fon:
            name = None
            version = None
            for line in fon:
                if "Extension-Name: " in line:
                    beforekyw, kyw, name = line.partition("Extension-Name: ")
                    # clean the string
                    name = re.search(r'(\w+)', name).group(0)
                elif "Plugin-Version: " in line:
                    beforekyw, kyw, version = line.partition(
                        "Plugin-Version: ")
                    version = re.sub(r'\n', '', version)
                    # clean the string
                    version = re.search(r'(.+)', version).group(0)
            logging.info("{} ver. {}".format(name, version))
