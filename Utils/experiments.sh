#!/bin/sh
mkdir ../outputs/Server_test4/
mkdir ../outputs/Server_test4/Markdown
bsub -o "../outputs/Server_test4/Markdown/Server_test4_0.md" -J "Server_test4_0" -env MYARGS="-name Server_test4-0 -hours 1 -num 0" < submit_gpu.sh
