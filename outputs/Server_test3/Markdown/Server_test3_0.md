Traceback (most recent call last):
  File "main.py", line 17, in <module>
    from clean_data import get_data, read_data
  File "/zhome/ea/9/137501/Desktop/Stocks/Stocks/clean_data.py", line 1, in <module>
    import pandas as pd
ModuleNotFoundError: No module named 'pandas'

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 10015602: <Server_test3_0> in cluster <dcc> Exited

Job <Server_test3_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun Jul  4 03:27:49 2021
Job was executed on host(s) <n-62-20-5>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun Jul  4 03:27:50 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Stocks/Stocks/Utils> was used as the working directory.
Started at Sun Jul  4 03:27:50 2021
Terminated at Sun Jul  4 03:27:54 2021
Results reported at Sun Jul  4 03:27:54 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=16G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 1440
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $MYARGS


------------------------------------------------------------

Exited with exit code 1.

Resource usage summary:

    CPU time :                                   1.21 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   68 sec.
    Turnaround time :                            5 sec.

The output (if any) is above this job summary.

