#!/bin/sh
"/home/sarthak/IDE/Pycharm/jre64/bin/java" -cp "/home/sarthak/IDE/Pycharm/plugins/git4idea/lib/git4idea-rt.jar:/home/sarthak/IDE/Pycharm/lib/xmlrpc-2.0.1.jar:/home/sarthak/IDE/Pycharm/lib/commons-codec-1.10.jar:/home/sarthak/IDE/Pycharm/lib/util.jar" org.jetbrains.git4idea.nativessh.GitNativeSshAskPassApp "$@"
