#!/bin/sh
mkdir ../outputs/Server_test6/
mkdir ../outputs/Server_test6/Markdown
bsub -o "../outputs/Server_test6/Markdown/Server_test6_0.md" -J "Server_test6_0" -env MYARGS="-name Server_test6-0 -hours 0.05 -num 0" < submit_gpu.sh
