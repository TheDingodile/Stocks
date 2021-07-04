#!/bin/sh
mkdir ../outputs/Server_test2/
mkdir ../outputs/Server_test2/Markdown
bsub -o "../outputs/Server_test2/Markdown/Server_test2_0.md" -J "Server_test2_0" -env MYARGS="-name Server_test2-0 -hours 10 -num 0" < submit_gpu.sh
