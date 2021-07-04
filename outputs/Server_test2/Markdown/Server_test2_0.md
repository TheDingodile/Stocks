Traceback (most recent call last):
  File "main.py", line 17, in <module>
    from clean_data import get_data, read_data
  File "/zhome/ea/9/137501/Desktop/Stocks/Stocks/clean_data.py", line 1, in <module>
    import pandas as pd
ModuleNotFoundError: No module named 'pandas'

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 10015600: <Server_test2_0> in cluster <dcc> Exited

Job <Server_test2_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun Jul  4 03:23:28 2021
Job was executed on host(s) <n-62-20-5>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun Jul  4 03:23:29 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Stocks/Stocks/Utils> was used as the working directory.
Started at Sun Jul  4 03:23:29 2021
Terminated at Sun Jul  4 03:23:34 2021
Results reported at Sun Jul  4 03:23:34 2021

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

    CPU time :                                   1.29 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   61 sec.
    Turnaround time :                            6 sec.

The output (if any) is above this job summary.

Traceback (most recent call last):
  File "main.py", line 17, in <module>
    from clean_data import get_data, read_data
  File "/zhome/ea/9/137501/Desktop/Stocks/Stocks/clean_data.py", line 1, in <module>
    import pandas as pd
ModuleNotFoundError: No module named 'pandas'

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 10015601: <Server_test2_0> in cluster <dcc> Exited

Job <Server_test2_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun Jul  4 03:26:32 2021
Job was executed on host(s) <n-62-20-5>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun Jul  4 03:26:33 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Stocks/Stocks/Utils> was used as the working directory.
Started at Sun Jul  4 03:26:33 2021
Terminated at Sun Jul  4 03:26:36 2021
Results reported at Sun Jul  4 03:26:36 2021

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

    CPU time :                                   1.20 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   61 sec.
    Turnaround time :                            4 sec.

The output (if any) is above this job summary.

