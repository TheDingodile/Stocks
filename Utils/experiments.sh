#!/bin/sh
mkdir ../outputs/Server_test3/
mkdir ../outputs/Server_test3/Markdown
bsub -o "../outputs/Server_test3/Markdown/Server_test3_0.md" -J "Server_test3_0" -env MYARGS="-name Server_test3-0 -hours 10 -num 0" < submit_gpu.sh
