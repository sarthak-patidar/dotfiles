#!/bin/sh
"/home/sarthak/IDE/Phpstorm/jre64/bin/java" -cp "/home/sarthak/IDE/Phpstorm/plugins/git4idea/lib/git4idea-rt.jar:/home/sarthak/IDE/Phpstorm/lib/xmlrpc-2.0.1.jar:/home/sarthak/IDE/Phpstorm/lib/commons-codec-1.10.jar:/home/sarthak/IDE/Phpstorm/lib/util.jar" org.jetbrains.git4idea.nativessh.GitNativeSshAskPassApp "$@"
