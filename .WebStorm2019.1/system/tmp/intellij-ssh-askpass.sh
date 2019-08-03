#!/bin/sh
"/home/sarthak/IDE/webstorm/jre64/bin/java" -cp "/home/sarthak/IDE/webstorm/plugins/git4idea/lib/git4idea-rt.jar:/home/sarthak/IDE/webstorm/lib/xmlrpc-2.0.1.jar:/home/sarthak/IDE/webstorm/lib/commons-codec-1.10.jar:/home/sarthak/IDE/webstorm/lib/util.jar" org.jetbrains.git4idea.nativessh.GitNativeSshAskPassApp "$@"
