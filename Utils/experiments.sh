#!/bin/sh
mkdir ../outputs/Server_test7/
mkdir ../outputs/Server_test7/Markdown
bsub -o "../outputs/Server_test7/Markdown/Server_test7_0.md" -J "Server_test7_0" -env MYARGS="-name Server_test7-0 -hours 0.05 -num 0" < submit_gpu.sh
