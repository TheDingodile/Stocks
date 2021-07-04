#!/bin/sh
mkdir ../outputs/Server_test1/
mkdir ../outputs/Server_test1/Markdown
bsub -o "../outputs/Server_test1/Markdown/Server_test1_0.md" -J "Server_test1_0" -env MYARGS="-name Server_test1-0 -hours 10 -num 0" < submit_gpu.sh
