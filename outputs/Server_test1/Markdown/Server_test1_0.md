YHELLO

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 10015513: <Server_test1_0> in cluster <dcc> Done

Job <Server_test1_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sat Jul  3 21:00:29 2021
Job was executed on host(s) <n-62-20-5>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sat Jul  3 21:00:30 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Stocks/Stocks/Utils> was used as the working directory.
Started at Sat Jul  3 21:00:30 2021
Terminated at Sat Jul  3 21:00:31 2021
Results reported at Sat Jul  3 21:00:31 2021

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

Successfully completed.

Resource usage summary:

    CPU time :                                   0.25 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   111 sec.
    Turnaround time :                            2 sec.

The output (if any) is above this job summary.

YHELLO

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 10015515: <Server_test1_0> in cluster <dcc> Done

Job <Server_test1_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sat Jul  3 21:08:43 2021
Job was executed on host(s) <n-62-20-5>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sat Jul  3 21:08:44 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Stocks/Stocks/Utils> was used as the working directory.
Started at Sat Jul  3 21:08:44 2021
Terminated at Sat Jul  3 21:08:45 2021
Results reported at Sat Jul  3 21:08:45 2021

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

Successfully completed.

Resource usage summary:

    CPU time :                                   0.26 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   1 sec.
    Turnaround time :                            2 sec.

The output (if any) is above this job summary.

Traceback (most recent call last):
  File "main.py", line 19, in <module>
    train.train()
  File "/zhome/ea/9/137501/Desktop/Stocks/Stocks/Train_trader.py", line 16, in train
    all_data = torch.load(data).to(device=device) #yo
  File "/zhome/ea/9/137501/Desktop/Stocks/project-env/lib/python3.8/site-packages/torch/serialization.py", line 594, in load
    with _open_file_like(f, 'rb') as opened_file:
  File "/zhome/ea/9/137501/Desktop/Stocks/project-env/lib/python3.8/site-packages/torch/serialization.py", line 230, in _open_file_like
    return _open_file(name_or_buffer, mode)
  File "/zhome/ea/9/137501/Desktop/Stocks/project-env/lib/python3.8/site-packages/torch/serialization.py", line 211, in __init__
    super(_open_file, self).__init__(open(name, mode))
FileNotFoundError: [Errno 2] No such file or directory: 'DayliData.pt'

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 10015596: <Server_test1_0> in cluster <dcc> Exited

Job <Server_test1_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun Jul  4 02:59:28 2021
Job was executed on host(s) <n-62-20-5>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun Jul  4 02:59:29 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Stocks/Stocks/Utils> was used as the working directory.
Started at Sun Jul  4 02:59:29 2021
Terminated at Sun Jul  4 02:59:38 2021
Results reported at Sun Jul  4 02:59:38 2021

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

    CPU time :                                   1.33 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   100 sec.
    Turnaround time :                            10 sec.

The output (if any) is above this job summary.

