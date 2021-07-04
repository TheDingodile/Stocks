Traceback (most recent call last):
  File "main.py", line 17, in <module>
    from clean_data import get_data, read_data
  File "/zhome/ea/9/137501/Desktop/Stocks/Stocks/clean_data.py", line 1, in <module>
    import pandas as pd
ModuleNotFoundError: No module named 'pandas'

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 10015889: <Server_test4_0> in cluster <dcc> Exited

Job <Server_test4_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun Jul  4 13:17:11 2021
Job was executed on host(s) <n-62-20-4>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun Jul  4 13:17:12 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Stocks/Stocks/Utils> was used as the working directory.
Started at Sun Jul  4 13:17:12 2021
Terminated at Sun Jul  4 13:17:21 2021
Results reported at Sun Jul  4 13:17:21 2021

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

    CPU time :                                   1.30 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   17 sec.
    Turnaround time :                            10 sec.

The output (if any) is above this job summary.

torch.Size([12928, 274, 5])
torch.Size([11828, 274, 5])
torch.Size([11828, 24, 5]) torch.Size([11828, 250, 5])
tensor([-0.0319, -0.0698,  0.0980, -0.0526, -0.0037], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.2
trained 0.05 percent
trained 0.1 percent
trained 0.15 percent
trained 0.2 percent
tensor([ 0.0352, -0.0513, -0.0393, -0.1498, -0.0998], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1996
trained 0.25 percent
trained 0.3 percent
trained 0.35 percent
trained 0.4 percent
tensor([-0.0004, -0.0541, -0.0164, -0.1637, -0.1170], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.19920000000000002
trained 0.45 percent
trained 0.5 percent
trained 0.55 percent
trained 0.6 percent
tensor([ 0.0621,  0.0242, -0.1920, -0.3534, -0.4435], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1988
trained 0.65 percent
trained 0.7 percent
trained 0.75 percent
trained 0.8 percent
tensor([ 0.1146,  0.1065, -0.7837, -0.8587, -1.6077], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.19840000000000002
trained 0.85 percent
trained 0.9 percent
trained 0.95 percent
trained 1.0 percent
tensor([ 0.0921,  0.0596, -0.9382, -1.0258, -1.9377], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.198
trained 1.05 percent
trained 1.1 percent
trained 1.15 percent
trained 1.2 percent
tensor([ 0.0454, -0.0087, -0.8984, -1.0742, -2.0029], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1976
trained 1.25 percent
trained 1.3 percent
trained 1.35 percent
trained 1.4 percent
tensor([ 0.1373,  0.0458, -0.7394, -1.0485, -1.9308], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.19720000000000001
trained 1.45 percent
trained 1.5 percent
trained 1.55 percent
trained 1.6 percent
tensor([ 0.1337,  0.0965, -1.2100, -1.7547, -3.5273], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1968
trained 1.65 percent
trained 1.7 percent
trained 1.75 percent
trained 1.8 percent
tensor([ 0.1344,  0.0409, -0.7020, -1.1796, -2.4100], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.19640000000000002
trained 1.85 percent
trained 1.9 percent
trained 1.95 percent
trained 2.0 percent
tensor([ 0.6788,  0.2057, -0.1092, -0.1915, -0.4403], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.196
trained 2.05 percent
trained 2.1 percent
trained 2.15 percent
trained 2.2 percent
tensor([ 0.1867,  0.1022, -0.4593, -0.9414, -2.1305], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.19560000000000002
trained 2.25 percent
trained 2.3 percent
trained 2.35 percent
trained 2.4 percent
tensor([1.0574, 0.5082, 0.1957, 0.4124, 0.3683], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1952
trained 2.45 percent
trained 2.5 percent
trained 2.55 percent
trained 2.6 percent
tensor([ 0.1076,  0.0608, -0.3447, -0.8915, -2.3325], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1948
trained 2.65 percent
trained 2.7 percent
trained 2.75 percent
trained 2.8 percent
tensor([ 0.1092,  0.0759, -0.3603, -0.9990, -2.7226], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.19440000000000002
trained 2.85 percent
trained 2.9 percent
trained 2.95 percent
trained 3.0 percent
tensor([ 0.1708,  0.0843, -0.0574, -0.4790, -1.4414], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.194
trained 3.05 percent
trained 3.1 percent
trained 3.15 percent
trained 3.2 percent
tensor([ 0.1313,  0.0781, -0.0042, -0.4426, -1.4425], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.19360000000000002
trained 3.25 percent
trained 3.3 percent
trained 3.35 percent
trained 3.4 percent
tensor([ 0.0412,  0.0469,  0.0125, -0.5132, -1.9939], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1932
trained 3.45 percent
trained 3.5 percent
trained 3.55 percent
trained 3.6 percent
tensor([ 0.1185,  0.0821,  0.0761, -0.4784, -1.8974], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1928
trained 3.65 percent
trained 3.7 percent
trained 3.75 percent
trained 3.8 percent
tensor([ 1.9903,  1.0632,  0.4766,  0.5234, -0.3190], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.19240000000000002
trained 3.85 percent
trained 3.9 percent
trained 3.95 percent
trained 4.0 percent
tensor([ 0.4762,  0.2890,  0.2041, -0.1871, -1.2599], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.192
trained 4.05 percent
trained 4.1 percent
trained 4.15 percent
trained 4.2 percent
tensor([ 0.2396,  0.1423,  0.1005, -0.2532, -1.2857], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.19160000000000002
trained 4.25 percent
trained 4.3 percent
trained 4.35 percent
trained 4.4 percent
tensor([ 0.0075,  0.0112,  0.0254, -0.3652, -1.5466], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1912
trained 4.45 percent
trained 4.5 percent
trained 4.55 percent
trained 4.6 percent
tensor([ 0.2706,  0.1562,  0.1271, -0.1445, -0.7373], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.19080000000000003
trained 4.65 percent
trained 4.7 percent
trained 4.75 percent
trained 4.8 percent
tensor([ 0.3145,  0.1740,  0.1621, -0.1012, -0.6396], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1904
trained 4.85 percent
trained 4.9 percent
trained 4.95 percent
trained 5.0 percent
tensor([ 0.1680,  0.1099,  0.1441, -0.1382, -0.6913], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.19
trained 5.05 percent
trained 5.1 percent
trained 5.15 percent
trained 5.2 percent
tensor([ 2.2581,  1.2252,  0.5425,  0.8662, -0.1612], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.18960000000000002
trained 5.25 percent
trained 5.3 percent
trained 5.35 percent
trained 5.4 percent
tensor([ 0.3804,  0.2621,  0.3972,  0.1172, -0.4413], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1892
trained 5.45 percent
trained 5.5 percent
trained 5.55 percent
trained 5.6 percent
tensor([ 0.4618,  0.3782,  0.5685,  0.2265, -0.5912], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.18880000000000002
trained 5.65 percent
trained 5.7 percent
trained 5.75 percent
trained 5.8 percent
tensor([ 0.2806,  0.1865,  0.2655,  0.0322, -0.3706], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1884
trained 5.85 percent
trained 5.9 percent
trained 5.95 percent
trained 6.0 percent
tensor([ 1.7491,  1.2585,  0.7231,  0.6291, -0.5804], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.188
trained 6.05 percent
trained 6.1 percent
trained 6.15 percent
trained 6.2 percent
tensor([ 0.4873,  0.4886,  0.3527, -0.1857, -1.5458], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.18760000000000002
trained 6.25 percent
trained 6.3 percent
trained 6.35 percent
trained 6.4 percent
tensor([ 0.4650,  0.4282,  0.2779, -0.3417, -1.4236], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1872
trained 6.45 percent
trained 6.5 percent
trained 6.55 percent
trained 6.6 percent
tensor([ 0.2115,  0.2031,  0.0860, -0.5815, -1.7243], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.18680000000000002
trained 6.65 percent
trained 6.7 percent
trained 6.75 percent
trained 6.8 percent
tensor([4.5374, 3.1083, 1.9393, 2.7473, 1.3183], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1864
trained 6.85 percent
trained 6.9 percent
trained 6.95 percent
trained 7.0 percent
tensor([ 0.6154,  0.6193,  0.6525, -0.0964, -1.5425], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.186
trained 7.05 percent
trained 7.1 percent
trained 7.15 percent
trained 7.2 percent
tensor([ 1.7336,  1.4228,  1.0833,  0.6528, -0.6206], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.18560000000000001
trained 7.25 percent
trained 7.3 percent
trained 7.35 percent
trained 7.4 percent
tensor([ 0.4596,  0.3987,  0.5243,  0.1354, -0.4383], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1852
trained 7.45 percent
trained 7.5 percent
trained 7.55 percent
trained 7.6 percent
tensor([1.2582, 1.1445, 1.4420, 1.1143, 0.2276], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.18480000000000002
trained 7.65 percent
trained 7.7 percent
trained 7.75 percent
trained 7.8 percent
tensor([1.4622, 1.2962, 1.4767, 1.2881, 0.5475], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1844
trained 7.85 percent
trained 7.9 percent
trained 7.95 percent
trained 8.0 percent
tensor([ 0.9199,  0.8910,  0.9743,  0.5706, -0.2700], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.184
trained 8.05 percent
trained 8.1 percent
trained 8.15 percent
trained 8.2 percent
tensor([ 0.2056,  0.1954,  0.0863, -0.6078, -1.8689], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1836
trained 8.25 percent
trained 8.3 percent
trained 8.35 percent
trained 8.4 percent
tensor([ 0.2817,  0.2767,  0.2047, -0.4254, -1.5739], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1832
trained 8.45 percent
trained 8.5 percent
trained 8.55 percent
trained 8.6 percent
tensor([1.8068, 1.7076, 1.4243, 1.0867, 0.2826], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.18280000000000002
trained 8.65 percent
trained 8.7 percent
trained 8.75 percent
trained 8.8 percent
tensor([ 0.4812,  0.4804,  0.5435, -0.2481, -1.4188], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1824
trained 8.85 percent
trained 8.9 percent
trained 8.95 percent
trained 9.0 percent
tensor([2.1758, 2.0305, 1.7499, 1.6530, 1.1878], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.18200000000000002
trained 9.05 percent
trained 9.1 percent
trained 9.15 percent
trained 9.2 percent
tensor([1.1429, 1.1425, 1.2582, 0.9724, 0.5304], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1816
trained 9.25 percent
trained 9.3 percent
trained 9.35 percent
trained 9.4 percent
tensor([1.4147, 1.3546, 1.4345, 1.3222, 0.9565], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1812
trained 9.45 percent
trained 9.5 percent
trained 9.55 percent
trained 9.6 percent
tensor([ 0.4745,  0.4692,  0.4139, -0.0646, -0.7551], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.18080000000000002
trained 9.65 percent
trained 9.7 percent
trained 9.75 percent
trained 9.8 percent
tensor([2.8479, 2.5389, 2.1866, 2.4260, 2.0498], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1804
trained 9.85 percent
trained 9.9 percent
trained 9.95 percent
trained 10.0 percent
tensor([ 0.2135,  0.2016,  0.0614, -0.7202, -2.0215], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.18000000000000002
trained 10.05 percent
trained 10.1 percent
trained 10.15 percent
trained 10.2 percent
tensor([ 0.4178,  0.6113,  0.8457,  0.0245, -0.9428], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1796
trained 10.25 percent
trained 10.3 percent
trained 10.35 percent
trained 10.4 percent
tensor([0.8254, 0.9385, 1.0934, 0.6173, 0.0839], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.17920000000000003
trained 10.45 percent
trained 10.5 percent
trained 10.55 percent
trained 10.6 percent
tensor([2.2221, 2.0544, 1.9262, 1.9801, 1.7942], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.17880000000000001
trained 10.65 percent
trained 10.7 percent
trained 10.75 percent
trained 10.8 percent
tensor([1.2599, 1.2621, 1.3905, 1.1484, 0.9519], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1784
trained 10.85 percent
trained 10.9 percent
trained 10.95 percent
trained 11.0 percent
tensor([ 1.0820,  1.0965,  1.0835,  0.6385, -0.4128], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.17800000000000002
trained 11.05 percent
trained 11.1 percent
trained 11.15 percent
trained 11.2 percent
tensor([2.1482, 1.9981, 1.5474, 1.4099, 0.9140], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1776
trained 11.25 percent
trained 11.3 percent
trained 11.35 percent
trained 11.4 percent
tensor([ 0.1968,  0.2351,  0.0569, -0.7511, -2.1451], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.17720000000000002
trained 11.45 percent
trained 11.5 percent
trained 11.55 percent
trained 11.6 percent
tensor([ 0.6477,  0.6821,  0.5938,  0.0250, -1.1054], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1768
trained 11.65 percent
trained 11.7 percent
trained 11.75 percent
trained 11.8 percent
tensor([1.9824, 1.9518, 2.1337, 2.0492, 2.0047], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1764
trained 11.85 percent
trained 11.9 percent
trained 11.95 percent
trained 12.0 percent
tensor([2.7911, 2.7958, 2.9216, 2.9553, 2.9710], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.17600000000000002
trained 12.05 percent
trained 12.1 percent
trained 12.15 percent
trained 12.2 percent
tensor([2.6801, 2.5852, 2.4233, 2.3375, 2.1758], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1756
trained 12.25 percent
trained 12.3 percent
trained 12.35 percent
trained 12.4 percent
tensor([3.3240, 3.3604, 2.7615, 2.4003, 1.8303], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.17520000000000002
trained 12.45 percent
trained 12.5 percent
trained 12.55 percent
trained 12.6 percent
trained 12.65 percent
tensor([2.3803, 2.2401, 2.2435, 2.2171, 2.2090], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1748
trained 12.7 percent
trained 12.75 percent
trained 12.8 percent
trained 12.85 percent
tensor([2.5807, 2.5019, 1.8979, 1.5425, 0.9843], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1744
trained 12.9 percent
trained 12.95 percent
trained 13.0 percent
trained 13.05 percent
tensor([ 0.4720,  0.4753,  0.4209, -0.2884, -1.5984], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.17400000000000002
trained 13.1 percent
trained 13.15 percent
trained 13.2 percent
trained 13.25 percent
tensor([ 0.8259,  0.8071,  0.8440,  0.4418, -0.0737], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1736
trained 13.3 percent
trained 13.35 percent
trained 13.4 percent
trained 13.45 percent
tensor([2.7189, 2.6508, 2.3818, 2.1608, 1.8561], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.17320000000000002
trained 13.5 percent
trained 13.55 percent
trained 13.6 percent
trained 13.65 percent
tensor([ 1.5757,  1.7860,  1.0687,  0.2579, -0.7743], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1728
trained 13.7 percent
trained 13.75 percent
trained 13.8 percent
trained 13.85 percent
tensor([ 1.6075,  1.6208,  1.0222,  0.2641, -0.8004], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1724
trained 13.9 percent
trained 13.95 percent
trained 14.0 percent
trained 14.05 percent
tensor([ 0.7507,  0.7462,  0.8065, -0.0251, -1.4920], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.17200000000000001
trained 14.1 percent
trained 14.15 percent
trained 14.2 percent
trained 14.25 percent
tensor([2.8157, 2.6856, 2.5650, 2.4792, 2.4080], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1716
trained 14.3 percent
trained 14.35 percent
trained 14.4 percent
trained 14.45 percent
tensor([ 0.8095,  0.8279,  0.7902,  0.1925, -0.8588], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.17120000000000002
trained 14.5 percent
trained 14.55 percent
trained 14.6 percent
trained 14.65 percent
tensor([3.1799, 3.0534, 2.9219, 2.8030, 2.7899], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1708
trained 14.7 percent
trained 14.75 percent
trained 14.8 percent
trained 14.85 percent
tensor([1.8322, 1.8103, 1.8105, 1.4799, 0.9880], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1704
trained 14.9 percent
trained 14.95 percent
trained 15.0 percent
trained 15.05 percent
tensor([ 0.8354,  0.8467,  0.9118,  0.3690, -0.4031], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.17
trained 15.1 percent
trained 15.15 percent
trained 15.2 percent
trained 15.25 percent
tensor([2.3438, 2.2826, 2.3762, 2.1611, 1.9496], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1696
trained 15.3 percent
trained 15.35 percent
trained 15.4 percent
trained 15.45 percent
tensor([ 0.6376,  0.6299,  0.7052, -0.1297, -1.6315], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.16920000000000002
trained 15.5 percent
trained 15.55 percent
trained 15.6 percent
trained 15.65 percent
tensor([2.1866, 2.1332, 2.2683, 2.0984, 2.1150], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1688
trained 15.7 percent
trained 15.75 percent
trained 15.8 percent
trained 15.85 percent
tensor([3.0885, 3.0486, 2.6706, 2.3766, 1.9864], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1684
trained 15.9 percent
trained 15.95 percent
trained 16.0 percent
trained 16.05 percent
tensor([3.2708, 3.2755, 3.5347, 3.4609, 3.6462], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.168
trained 16.1 percent
trained 16.15 percent
trained 16.2 percent
trained 16.25 percent
tensor([ 2.2016,  1.9773,  1.4271,  0.8581, -0.0534], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.16760000000000003
trained 16.3 percent
trained 16.35 percent
trained 16.4 percent
trained 16.45 percent
tensor([2.8580, 2.8200, 3.0273, 2.9381, 3.0694], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.16720000000000002
trained 16.5 percent
trained 16.55 percent
trained 16.6 percent
trained 16.65 percent
tensor([ 0.8297,  0.8024,  0.8548,  0.2809, -0.5934], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1668
trained 16.7 percent
trained 16.75 percent
trained 16.8 percent
trained 16.85 percent
tensor([ 1.2656,  1.2513,  1.2956,  0.6061, -0.5400], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.16640000000000002
trained 16.9 percent
trained 16.95 percent
trained 17.0 percent
trained 17.05 percent
tensor([ 1.4121,  1.2554,  0.8363,  0.2068, -0.7062], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.166
trained 17.1 percent
trained 17.15 percent
trained 17.2 percent
trained 17.25 percent
tensor([ 0.8793,  0.8533,  0.9578,  0.4388, -0.3191], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.16560000000000002
trained 17.3 percent
trained 17.35 percent
trained 17.4 percent
trained 17.45 percent
tensor([2.9269, 2.9084, 2.6112, 2.2460, 1.8879], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1652
trained 17.5 percent
trained 17.55 percent
trained 17.6 percent
trained 17.65 percent
tensor([2.0061, 1.8884, 1.3685, 0.8669, 0.2043], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1648
trained 17.7 percent
trained 17.75 percent
trained 17.8 percent
trained 17.85 percent
tensor([7.8553, 7.6858, 7.4276, 7.7959, 7.7999], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.16440000000000002
trained 17.9 percent
trained 17.95 percent
trained 18.0 percent
trained 18.05 percent
tensor([ 1.6646,  1.4935,  0.9010,  0.3174, -0.4538], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.164
trained 18.1 percent
trained 18.15 percent
trained 18.2 percent
trained 18.25 percent
tensor([2.9221, 2.8118, 2.7464, 2.6169, 2.5270], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.16360000000000002
trained 18.3 percent
trained 18.35 percent
trained 18.4 percent
trained 18.45 percent
tensor([ 1.3193,  1.3181,  1.3506,  0.6832, -0.4557], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1632
trained 18.5 percent
trained 18.55 percent
trained 18.6 percent
trained 18.65 percent
tensor([1.5903, 1.5274, 1.6464, 1.3845, 1.1990], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1628
trained 18.7 percent
trained 18.75 percent
trained 18.8 percent
trained 18.85 percent
tensor([ 0.6139,  0.6576,  0.7360,  0.0238, -1.2026], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.16240000000000002
trained 18.9 percent
trained 18.95 percent
trained 19.0 percent
trained 19.05 percent
tensor([1.7633, 1.7424, 1.8057, 1.3935, 0.7944], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.162
trained 19.1 percent
trained 19.15 percent
trained 19.2 percent
trained 19.25 percent
tensor([1.6529, 1.6038, 1.6895, 1.3246, 0.8911], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.16160000000000002
trained 19.3 percent
trained 19.35 percent
trained 19.4 percent
trained 19.45 percent
tensor([3.7759, 3.6566, 3.5996, 3.5529, 3.5312], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1612
trained 19.5 percent
trained 19.55 percent
trained 19.6 percent
trained 19.65 percent
tensor([3.8359, 3.6963, 3.6216, 3.5229, 3.5362], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1608
trained 19.7 percent
trained 19.75 percent
trained 19.8 percent
trained 19.85 percent
tensor([4.6925, 4.5681, 4.4294, 4.3926, 4.4197], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.16040000000000001
trained 19.9 percent
trained 19.95 percent
trained 20.0 percent
trained 20.05 percent
tensor([ 1.1458,  1.1164,  1.1391,  0.5495, -0.4170], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.16
trained 20.1 percent
trained 20.15 percent
trained 20.2 percent
trained 20.25 percent
tensor([1.6411, 1.7125, 1.8562, 1.3775, 0.7069], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.15960000000000002
trained 20.3 percent
trained 20.35 percent
trained 20.4 percent
trained 20.45 percent
tensor([2.7574, 2.7052, 2.4892, 2.1539, 1.8170], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1592
trained 20.5 percent
trained 20.55 percent
trained 20.6 percent
trained 20.65 percent
tensor([ 0.8384,  0.8409,  0.8684,  0.1638, -1.1402], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1588
trained 20.7 percent
trained 20.75 percent
trained 20.8 percent
trained 20.85 percent
tensor([2.8086, 2.7846, 2.8526, 2.6615, 2.5271], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1584
trained 20.9 percent
trained 20.95 percent
trained 21.0 percent
trained 21.05 percent
tensor([3.3737, 3.3003, 3.3251, 3.2205, 3.2069], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.158
trained 21.1 percent
trained 21.15 percent
trained 21.2 percent
trained 21.25 percent
tensor([ 1.0309,  1.0559,  1.0306,  0.3729, -0.8324], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.15760000000000002
trained 21.3 percent
trained 21.35 percent
trained 21.4 percent
trained 21.45 percent
tensor([2.6738, 2.7467, 2.2992, 1.7673, 1.1240], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1572
trained 21.5 percent
trained 21.55 percent
trained 21.6 percent
trained 21.65 percent
tensor([1.5771, 1.5107, 1.6025, 1.2684, 0.9413], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1568
trained 21.7 percent
trained 21.75 percent
trained 21.8 percent
trained 21.85 percent
tensor([ 1.7919,  1.6249,  1.2023,  0.6993, -0.0156], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1564
trained 21.9 percent
trained 21.95 percent
trained 22.0 percent
trained 22.05 percent
tensor([2.2418, 2.0853, 1.6134, 1.1740, 0.5510], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.15600000000000003
trained 22.1 percent
trained 22.15 percent
trained 22.2 percent
trained 22.25 percent
tensor([ 1.6658,  1.6749,  1.6589,  1.0632, -0.0120], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.15560000000000002
trained 22.3 percent
trained 22.35 percent
trained 22.4 percent
trained 22.45 percent
tensor([4.8983, 4.9164, 5.0451, 5.0006, 5.1382], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1552
trained 22.5 percent
trained 22.55 percent
trained 22.6 percent
trained 22.65 percent
tensor([3.4623, 3.4417, 3.4917, 3.3825, 3.4876], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.15480000000000002
trained 22.7 percent
trained 22.75 percent
trained 22.8 percent
trained 22.85 percent
tensor([2.7768, 2.7909, 2.7893, 2.5412, 2.3085], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1544
trained 22.9 percent
trained 22.95 percent
trained 23.0 percent
trained 23.05 percent
tensor([9.1352, 8.8741, 8.7694, 8.8879, 8.9169], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.15400000000000003
trained 23.1 percent
trained 23.15 percent
trained 23.2 percent
trained 23.25 percent
tensor([4.5422, 4.6960, 4.5333, 4.2204, 3.5436], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.15360000000000001
trained 23.3 percent
trained 23.35 percent
trained 23.4 percent
trained 23.45 percent
tensor([2.6373, 2.6409, 2.6847, 2.3998, 2.1144], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1532
trained 23.5 percent
trained 23.55 percent
trained 23.6 percent
trained 23.65 percent
tensor([3.8493, 3.8081, 3.8638, 3.8007, 3.7777], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.15280000000000002
trained 23.7 percent
trained 23.75 percent
trained 23.8 percent
trained 23.85 percent
tensor([ 1.1637,  1.1732,  1.1525,  0.5454, -0.5301], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1524
trained 23.9 percent
trained 23.95 percent
trained 24.0 percent
trained 24.05 percent
tensor([1.7439, 1.7631, 1.7484, 1.2049, 0.3236], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.15200000000000002
trained 24.1 percent
trained 24.15 percent
trained 24.2 percent
trained 24.25 percent
tensor([ 0.7432,  0.7312,  0.7520,  0.0738, -1.0530], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1516
trained 24.3 percent
trained 24.35 percent
trained 24.4 percent
trained 24.45 percent
tensor([4.2936, 4.1478, 4.1500, 3.9994, 3.9529], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1512
trained 24.5 percent
trained 24.55 percent
trained 24.6 percent
trained 24.65 percent
tensor([3.9033, 3.9186, 4.1051, 3.9785, 4.1010], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.15080000000000002
trained 24.7 percent
trained 24.75 percent
trained 24.8 percent
trained 24.85 percent
tensor([3.2868, 3.1436, 2.8706, 2.7064, 2.5365], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1504
trained 24.9 percent
trained 24.95 percent
trained 25.0 percent
trained 25.05 percent
trained 25.1 percent
tensor([2.0160, 2.0662, 1.5410, 0.9683, 0.2457], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.15000000000000002
trained 25.15 percent
trained 25.2 percent
trained 25.25 percent
trained 25.3 percent
tensor([1.7910, 1.7860, 1.8085, 1.3317, 0.5800], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1496
trained 25.35 percent
trained 25.4 percent
trained 25.45 percent
trained 25.5 percent
tensor([1.4836, 1.4469, 1.4914, 1.0167, 0.3145], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1492
trained 25.55 percent
trained 25.6 percent
trained 25.65 percent
trained 25.7 percent
tensor([2.8982, 2.9977, 2.5420, 2.0425, 1.3768], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.14880000000000002
trained 25.75 percent
trained 25.8 percent
trained 25.85 percent
trained 25.9 percent
tensor([2.0679, 2.0272, 2.1120, 1.7881, 1.4604], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1484
trained 25.95 percent
trained 26.0 percent
trained 26.05 percent
trained 26.1 percent
tensor([4.9909, 4.9591, 5.0083, 4.8556, 4.7903], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.14800000000000002
trained 26.15 percent
trained 26.2 percent
trained 26.25 percent
trained 26.3 percent
tensor([2.4981, 2.4109, 1.9684, 1.5524, 1.0475], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1476
trained 26.35 percent
trained 26.4 percent
trained 26.45 percent
trained 26.5 percent
tensor([3.8992, 3.8427, 3.7195, 3.5258, 3.4107], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1472
trained 26.55 percent
trained 26.6 percent
trained 26.65 percent
trained 26.7 percent
tensor([6.2171, 6.3148, 6.2249, 6.1413, 5.8639], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1468
trained 26.75 percent
trained 26.8 percent
trained 26.85 percent
trained 26.9 percent
tensor([2.0112, 1.9677, 2.0371, 1.7039, 1.2809], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1464
trained 26.95 percent
trained 27.0 percent
trained 27.05 percent
trained 27.1 percent
tensor([3.0660, 2.8891, 2.7742, 2.5675, 2.3636], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.14600000000000002
trained 27.15 percent
trained 27.2 percent
trained 27.25 percent
trained 27.3 percent
tensor([1.9369, 1.9085, 1.9393, 1.5581, 1.1006], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1456
trained 27.35 percent
trained 27.4 percent
trained 27.45 percent
trained 27.5 percent
tensor([2.5485, 2.5015, 2.6045, 2.3857, 2.2910], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1452
trained 27.55 percent
trained 27.6 percent
trained 27.65 percent
trained 27.7 percent
tensor([8.4577, 8.4236, 8.3185, 8.3673, 8.3249], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1448
trained 27.75 percent
trained 27.8 percent
trained 27.85 percent
trained 27.9 percent
tensor([3.0541, 3.0444, 3.0964, 2.8899, 2.7308], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.14440000000000003
trained 27.95 percent
trained 28.0 percent
trained 28.05 percent
trained 28.1 percent
tensor([3.8081, 3.6831, 3.5327, 3.3895, 3.2815], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.14400000000000002
trained 28.15 percent
trained 28.2 percent
trained 28.25 percent
trained 28.3 percent
tensor([2.0261, 2.0069, 2.0371, 1.5998, 0.9123], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1436
trained 28.35 percent
trained 28.4 percent
trained 28.45 percent
trained 28.5 percent
tensor([2.7544, 2.6056, 2.0952, 1.7056, 1.0811], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1432
trained 28.55 percent
trained 28.6 percent
trained 28.65 percent
trained 28.7 percent
tensor([3.5581, 3.4893, 3.3349, 3.0804, 2.8551], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1428
trained 28.75 percent
trained 28.8 percent
trained 28.85 percent
trained 28.9 percent
tensor([1.2987, 1.2763, 1.3133, 0.7768, 0.0123], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.14240000000000003
trained 28.95 percent
trained 29.0 percent
trained 29.05 percent
trained 29.1 percent
tensor([8.6460, 8.6288, 8.6093, 8.6077, 8.6092], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.14200000000000002
trained 29.15 percent
trained 29.2 percent
trained 29.25 percent
trained 29.3 percent
tensor([1.7072, 1.7016, 1.7510, 1.2977, 0.6297], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1416
trained 29.35 percent
trained 29.4 percent
trained 29.45 percent
trained 29.5 percent
tensor([3.4888, 3.4598, 3.5412, 3.4168, 3.4476], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.14120000000000002
trained 29.55 percent
trained 29.6 percent
trained 29.65 percent
trained 29.7 percent
tensor([2.5867, 2.5701, 2.6861, 2.3992, 2.1454], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1408
trained 29.75 percent
trained 29.8 percent
trained 29.85 percent
trained 29.9 percent
tensor([2.4544, 2.4101, 2.4805, 2.2014, 1.8715], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.14040000000000002
trained 29.95 percent
trained 30.0 percent
trained 30.05 percent
trained 30.1 percent
tensor([2.0892, 2.0228, 2.1219, 1.8068, 1.4359], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.14
trained 30.15 percent
trained 30.2 percent
trained 30.25 percent
trained 30.3 percent
tensor([3.8805, 3.8446, 3.9717, 3.8513, 3.9074], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1396
trained 30.35 percent
trained 30.4 percent
trained 30.45 percent
trained 30.5 percent
tensor([ 0.9216,  0.9424,  0.9411,  0.2771, -0.8671], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.13920000000000002
trained 30.55 percent
trained 30.6 percent
trained 30.65 percent
trained 30.7 percent
tensor([2.6036, 2.5745, 2.6701, 2.4184, 2.1634], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1388
trained 30.75 percent
trained 30.8 percent
trained 30.85 percent
trained 30.9 percent
tensor([4.1598, 4.0868, 4.0623, 3.9053, 3.8062], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.13840000000000002
trained 30.95 percent
trained 31.0 percent
trained 31.05 percent
trained 31.1 percent
tensor([ 0.8596,  0.9237,  1.0029,  0.2890, -0.9198], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.138
trained 31.15 percent
trained 31.2 percent
trained 31.25 percent
trained 31.3 percent
tensor([2.4081, 2.3951, 2.0629, 1.7610, 1.2671], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1376
trained 31.35 percent
trained 31.4 percent
trained 31.45 percent
trained 31.5 percent
tensor([4.2457, 4.2137, 4.2506, 4.1814, 4.2984], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.13720000000000002
trained 31.55 percent
trained 31.6 percent
trained 31.65 percent
trained 31.7 percent
tensor([2.5454, 2.5191, 2.5775, 2.3138, 2.0356], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1368
trained 31.75 percent
trained 31.8 percent
trained 31.85 percent
trained 31.9 percent
tensor([8.5693, 8.5679, 8.5009, 8.5319, 8.4480], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.13640000000000002
trained 31.95 percent
trained 32.0 percent
trained 32.05 percent
trained 32.1 percent
tensor([3.1959, 3.1011, 2.8964, 2.6715, 2.3772], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.136
trained 32.15 percent
trained 32.2 percent
trained 32.25 percent
trained 32.3 percent
tensor([1.3341, 1.2989, 1.3672, 0.8619, 0.1031], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1356
trained 32.35 percent
trained 32.4 percent
trained 32.45 percent
trained 32.5 percent
tensor([6.2839, 6.3093, 6.3612, 6.2724, 6.2239], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.13520000000000001
trained 32.55 percent
trained 32.6 percent
trained 32.65 percent
trained 32.7 percent
tensor([3.0545, 3.0080, 2.5487, 2.1662, 1.5872], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.13480000000000003
trained 32.75 percent
trained 32.8 percent
trained 32.85 percent
trained 32.9 percent
tensor([4.5726, 4.4923, 4.4615, 4.2981, 4.1211], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.13440000000000002
trained 32.95 percent
trained 33.0 percent
trained 33.05 percent
trained 33.1 percent
tensor([9.0071, 9.2244, 9.1605, 9.2053, 9.0904], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.134
trained 33.15 percent
trained 33.2 percent
trained 33.25 percent
trained 33.3 percent
tensor([2.0099, 2.0734, 1.7662, 1.5221, 1.0769], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1336
trained 33.35 percent
trained 33.4 percent
trained 33.45 percent
trained 33.5 percent
tensor([1.5165, 1.5318, 1.5653, 1.0430, 0.2202], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1332
trained 33.55 percent
trained 33.6 percent
trained 33.65 percent
trained 33.7 percent
tensor([4.0788, 3.9518, 3.8386, 3.7168, 3.5912], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.13280000000000003
trained 33.75 percent
trained 33.8 percent
trained 33.85 percent
trained 33.9 percent
tensor([2.2763, 2.3486, 1.9465, 1.5380, 0.9460], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.13240000000000002
trained 33.95 percent
trained 34.0 percent
trained 34.05 percent
trained 34.1 percent
tensor([3.4761, 3.5465, 3.4877, 3.2959, 3.0225], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.132
trained 34.15 percent
trained 34.2 percent
trained 34.25 percent
trained 34.3 percent
tensor([2.4648, 2.4799, 2.2416, 2.0209, 1.5948], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1316
trained 34.35 percent
trained 34.4 percent
trained 34.45 percent
trained 34.5 percent
tensor([6.9153, 6.8906, 6.9178, 6.8615, 6.8139], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1312
trained 34.55 percent
trained 34.6 percent
trained 34.65 percent
trained 34.7 percent
tensor([4.0137, 3.8657, 3.7310, 3.5973, 3.4614], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.13080000000000003
trained 34.75 percent
trained 34.8 percent
trained 34.85 percent
trained 34.9 percent
tensor([2.0182, 2.0339, 2.0640, 1.6585, 1.0808], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.13040000000000002
trained 34.95 percent
trained 35.0 percent
trained 35.05 percent
trained 35.1 percent
tensor([4.7444, 4.7097, 4.7134, 4.5605, 4.4905], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.13
trained 35.15 percent
trained 35.2 percent
trained 35.25 percent
trained 35.3 percent
tensor([4.4602, 4.3585, 4.2462, 4.1442, 4.0363], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1296
trained 35.35 percent
trained 35.4 percent
trained 35.45 percent
trained 35.5 percent
tensor([8.4797, 8.4263, 8.3629, 8.3706, 8.2818], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1292
trained 35.55 percent
trained 35.6 percent
trained 35.65 percent
trained 35.7 percent
tensor([2.7854, 2.6245, 2.1280, 1.8131, 1.3301], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.12880000000000003
trained 35.75 percent
trained 35.8 percent
trained 35.85 percent
trained 35.9 percent
tensor([6.0875, 6.0183, 5.9980, 5.9039, 5.7908], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.12840000000000001
trained 35.95 percent
trained 36.0 percent
trained 36.05 percent
trained 36.1 percent
tensor([3.3179, 3.3075, 3.3826, 3.2122, 3.0844], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.128
trained 36.15 percent
trained 36.2 percent
trained 36.25 percent
trained 36.3 percent
tensor([2.3428, 2.3459, 2.3745, 2.0552, 1.5945], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1276
trained 36.35 percent
trained 36.4 percent
trained 36.45 percent
trained 36.5 percent
tensor([4.6754, 4.6589, 4.6517, 4.6235, 4.6921], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1272
trained 36.55 percent
trained 36.6 percent
trained 36.65 percent
trained 36.7 percent
tensor([3.7223, 3.7051, 3.7439, 3.6429, 3.6207], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.12680000000000002
trained 36.75 percent
trained 36.8 percent
trained 36.85 percent
trained 36.9 percent
tensor([4.6113, 4.6094, 4.6972, 4.6264, 4.6780], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1264
trained 36.95 percent
trained 37.0 percent
trained 37.05 percent
trained 37.1 percent
tensor([3.8768, 3.8344, 3.7613, 3.6047, 3.4460], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.126
trained 37.15 percent
trained 37.2 percent
trained 37.25 percent
trained 37.3 percent
tensor([2.8215, 2.8229, 2.8709, 2.6309, 2.3641], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.12560000000000002
trained 37.35 percent
trained 37.4 percent
trained 37.45 percent
trained 37.5 percent
trained 37.55 percent
tensor([3.4651, 3.3598, 2.9303, 2.6817, 2.3396], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1252
trained 37.6 percent
trained 37.65 percent
trained 37.7 percent
trained 37.75 percent
tensor([4.6065, 4.6267, 4.6224, 4.5720, 4.6546], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.12480000000000001
trained 37.8 percent
trained 37.85 percent
trained 37.9 percent
trained 37.95 percent
tensor([3.3688, 3.2764, 2.9263, 2.6998, 2.3858], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.12440000000000001
trained 38.0 percent
trained 38.05 percent
trained 38.1 percent
trained 38.15 percent
tensor([ 0.8893,  0.9216,  0.8988,  0.2820, -0.7097], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.12400000000000001
trained 38.2 percent
trained 38.25 percent
trained 38.3 percent
trained 38.35 percent
tensor([2.3633, 2.3576, 2.3973, 2.0744, 1.6395], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.12360000000000002
trained 38.4 percent
trained 38.45 percent
trained 38.5 percent
trained 38.55 percent
tensor([ 1.0706,  1.0873,  1.0787,  0.4633, -0.5155], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.12320000000000002
trained 38.6 percent
trained 38.65 percent
trained 38.7 percent
trained 38.75 percent
tensor([3.0016, 2.9392, 2.5474, 2.2471, 1.7729], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1228
trained 38.8 percent
trained 38.85 percent
trained 38.9 percent
trained 38.95 percent
tensor([2.5456, 2.4663, 1.9987, 1.6807, 1.2010], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.12240000000000001
trained 39.0 percent
trained 39.05 percent
trained 39.1 percent
trained 39.15 percent
tensor([2.2740, 2.2889, 2.3098, 1.8824, 1.2746], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.12200000000000001
trained 39.2 percent
trained 39.25 percent
trained 39.3 percent
trained 39.35 percent
tensor([3.7668, 3.6834, 3.3379, 3.1687, 2.9162], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.12160000000000001
trained 39.4 percent
trained 39.45 percent
trained 39.5 percent
trained 39.55 percent
tensor([2.6032, 2.5084, 2.0307, 1.6478, 1.0738], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.12120000000000002
trained 39.6 percent
trained 39.65 percent
trained 39.7 percent
trained 39.75 percent
tensor([3.1238, 3.0403, 2.8532, 2.7017, 2.3881], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1208
trained 39.8 percent
trained 39.85 percent
trained 39.9 percent
trained 39.95 percent
tensor([3.5127, 3.3961, 3.0559, 2.8284, 2.5239], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.12040000000000001
trained 40.0 percent
trained 40.05 percent
trained 40.1 percent
trained 40.15 percent
tensor([2.4375, 2.4422, 2.4533, 2.0766, 1.5234], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.12000000000000001
trained 40.2 percent
trained 40.25 percent
trained 40.3 percent
trained 40.35 percent
tensor([2.5378, 2.4085, 1.8884, 1.5132, 0.9141], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.11960000000000001
trained 40.4 percent
trained 40.45 percent
trained 40.5 percent
trained 40.55 percent
tensor([2.7626, 2.7498, 2.8461, 2.6126, 2.3467], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.11920000000000001
trained 40.6 percent
trained 40.65 percent
trained 40.7 percent
trained 40.75 percent
tensor([3.4187, 3.2972, 2.8558, 2.6214, 2.2649], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.11880000000000002
trained 40.8 percent
trained 40.85 percent
trained 40.9 percent
trained 40.95 percent
tensor([7.1715, 7.1450, 7.2778, 7.2054, 7.1698], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1184
trained 41.0 percent
trained 41.05 percent
trained 41.1 percent
trained 41.15 percent
tensor([2.5999, 2.5846, 2.3169, 2.1602, 1.7719], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.11800000000000001
trained 41.2 percent
trained 41.25 percent
trained 41.3 percent
trained 41.35 percent
tensor([5.0684, 4.9997, 4.9708, 4.8621, 4.7544], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.11760000000000001
trained 41.4 percent
trained 41.45 percent
trained 41.5 percent
trained 41.55 percent
tensor([3.1295, 3.1380, 3.1536, 2.9400, 2.6669], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.11720000000000001
trained 41.6 percent
trained 41.65 percent
trained 41.7 percent
trained 41.75 percent
tensor([3.4221, 3.2859, 3.0617, 2.8896, 2.5634], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.11680000000000001
trained 41.8 percent
trained 41.85 percent
trained 41.9 percent
trained 41.95 percent
tensor([2.5532, 2.4871, 2.0442, 1.7059, 1.0968], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.11640000000000002
trained 42.0 percent
trained 42.05 percent
trained 42.1 percent
trained 42.15 percent
tensor([2.8672, 2.8254, 2.4644, 2.1814, 1.7159], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.116
trained 42.2 percent
trained 42.25 percent
trained 42.3 percent
trained 42.35 percent
tensor([2.7992, 2.8463, 2.4557, 2.0709, 1.5292], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.11560000000000001
trained 42.4 percent
trained 42.45 percent
trained 42.5 percent
trained 42.55 percent
tensor([3.1294, 3.1453, 3.2442, 3.0269, 2.8134], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.11520000000000001
trained 42.6 percent
trained 42.65 percent
trained 42.7 percent
trained 42.75 percent
tensor([7.9163, 7.7791, 7.5421, 7.5059, 7.4480], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.11480000000000001
trained 42.8 percent
trained 42.85 percent
trained 42.9 percent
trained 42.95 percent
tensor([1.4125, 1.4267, 1.4754, 0.9846, 0.2347], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.11440000000000002
trained 43.0 percent
trained 43.05 percent
trained 43.1 percent
trained 43.15 percent
tensor([4.4916, 4.4957, 4.5963, 4.5256, 4.4568], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.11400000000000002
trained 43.2 percent
trained 43.25 percent
trained 43.3 percent
trained 43.35 percent
tensor([1.8724, 1.8905, 1.8136, 1.3827, 0.7325], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1136
trained 43.4 percent
trained 43.45 percent
trained 43.5 percent
trained 43.55 percent
tensor([2.8923, 2.8124, 2.4293, 2.1652, 1.7589], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.11320000000000001
trained 43.6 percent
trained 43.65 percent
trained 43.7 percent
trained 43.75 percent
tensor([ 1.0375,  1.0720,  1.0715,  0.5369, -0.2915], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.11280000000000001
trained 43.8 percent
trained 43.85 percent
trained 43.9 percent
trained 43.95 percent
tensor([3.7354, 3.6936, 3.2854, 3.0764, 2.8189], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.11240000000000001
trained 44.0 percent
trained 44.05 percent
trained 44.1 percent
trained 44.15 percent
tensor([2.7239, 2.7545, 2.2582, 1.8578, 1.2435], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.11200000000000002
trained 44.2 percent
trained 44.25 percent
trained 44.3 percent
trained 44.35 percent
tensor([3.0217, 3.0070, 3.1300, 2.9073, 2.6596], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1116
trained 44.4 percent
trained 44.45 percent
trained 44.5 percent
trained 44.55 percent
tensor([4.9959, 4.9710, 4.9643, 4.9595, 5.0058], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.11120000000000001
trained 44.6 percent
trained 44.65 percent
trained 44.7 percent
trained 44.75 percent
tensor([3.2016, 3.1849, 3.2414, 3.0488, 2.8533], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.11080000000000001
trained 44.8 percent
trained 44.85 percent
trained 44.9 percent
trained 44.95 percent
tensor([2.9209, 2.8366, 2.3682, 2.1147, 1.6748], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.11040000000000001
trained 45.0 percent
trained 45.05 percent
trained 45.1 percent
trained 45.15 percent
tensor([2.2233, 2.2284, 2.2798, 1.9467, 1.4965], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.11000000000000001
trained 45.2 percent
trained 45.25 percent
trained 45.3 percent
trained 45.35 percent
tensor([3.8549, 3.8856, 4.0274, 3.9395, 3.9047], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.10960000000000002
trained 45.4 percent
trained 45.45 percent
trained 45.5 percent
trained 45.55 percent
tensor([2.5675, 2.5963, 2.6934, 2.3550, 1.9577], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1092
trained 45.6 percent
trained 45.65 percent
trained 45.7 percent
trained 45.75 percent
tensor([9.1259, 9.1019, 8.8849, 8.8893, 8.8068], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.10880000000000001
trained 45.8 percent
trained 45.85 percent
trained 45.9 percent
trained 45.95 percent
tensor([4.8839, 4.8492, 4.8328, 4.7587, 4.6382], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.10840000000000001
trained 46.0 percent
trained 46.05 percent
trained 46.1 percent
trained 46.15 percent
tensor([ 0.9312,  0.9516,  0.9443,  0.3933, -0.4680], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.10800000000000001
trained 46.2 percent
trained 46.25 percent
trained 46.3 percent
trained 46.35 percent
tensor([ 1.2846,  1.3151,  1.2831,  0.7666, -0.0375], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.10760000000000002
trained 46.4 percent
trained 46.45 percent
trained 46.5 percent
trained 46.55 percent
tensor([4.0483, 4.0516, 4.0736, 4.0039, 3.9578], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.10720000000000002
trained 46.6 percent
trained 46.65 percent
trained 46.7 percent
trained 46.75 percent
tensor([5.7377, 5.7771, 5.7843, 5.7277, 5.6757], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1068
trained 46.8 percent
trained 46.85 percent
trained 46.9 percent
trained 46.95 percent
tensor([2.9061, 2.9285, 3.0477, 2.8276, 2.5662], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.10640000000000001
trained 47.0 percent
trained 47.05 percent
trained 47.1 percent
trained 47.15 percent
tensor([2.9097, 3.0361, 2.8329, 2.5939, 2.2845], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.10600000000000001
trained 47.2 percent
trained 47.25 percent
trained 47.3 percent
trained 47.35 percent
tensor([2.6521, 2.6736, 2.2670, 1.9769, 1.5090], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.10560000000000001
trained 47.4 percent
trained 47.45 percent
trained 47.5 percent
trained 47.55 percent
tensor([2.6763, 2.7471, 2.4894, 2.2199, 1.7879], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.10520000000000002
trained 47.6 percent
trained 47.65 percent
trained 47.7 percent
trained 47.75 percent
tensor([3.4525, 3.3977, 3.3659, 3.2793, 3.0711], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1048
trained 47.8 percent
trained 47.85 percent
trained 47.9 percent
trained 47.95 percent
tensor([6.0500, 6.0617, 6.0913, 6.0860, 6.0703], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1044
trained 48.0 percent
trained 48.05 percent
trained 48.1 percent
trained 48.15 percent
tensor([3.6320, 3.6370, 3.6091, 3.4749, 3.3393], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.10400000000000001
trained 48.2 percent
trained 48.25 percent
trained 48.3 percent
trained 48.35 percent
tensor([2.2489, 2.2464, 1.7644, 1.3405, 0.6711], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.10360000000000001
trained 48.4 percent
trained 48.45 percent
trained 48.5 percent
trained 48.55 percent
tensor([2.7055, 2.7288, 2.7618, 2.4918, 2.1426], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.10320000000000001
trained 48.6 percent
trained 48.65 percent
trained 48.7 percent
trained 48.75 percent
tensor([2.8697, 2.9265, 2.4950, 2.1415, 1.6001], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.10280000000000002
trained 48.8 percent
trained 48.85 percent
trained 48.9 percent
trained 48.95 percent
tensor([3.2920, 3.3288, 3.0338, 2.8330, 2.5169], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1024
trained 49.0 percent
trained 49.05 percent
trained 49.1 percent
trained 49.15 percent
tensor([3.7604, 3.6660, 3.3353, 3.1691, 2.9158], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.10200000000000001
trained 49.2 percent
trained 49.25 percent
trained 49.3 percent
trained 49.35 percent
tensor([4.9371, 4.9414, 5.0340, 5.0048, 4.9777], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.10160000000000001
trained 49.4 percent
trained 49.45 percent
trained 49.5 percent
trained 49.55 percent
tensor([2.9180, 2.9800, 2.8485, 2.7781, 2.4438], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.10120000000000001
trained 49.6 percent
trained 49.65 percent
trained 49.7 percent
trained 49.75 percent
tensor([3.6395, 3.6375, 3.6382, 3.4997, 3.3449], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.10080000000000001
trained 49.8 percent
trained 49.85 percent
trained 49.9 percent
trained 49.95 percent
trained 50.0 percent
tensor([3.2891, 3.3148, 3.3404, 3.1493, 2.9671], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.10040000000000002
trained 50.05 percent
trained 50.1 percent
trained 50.15 percent
trained 50.2 percent
tensor([2.5981, 2.6035, 2.6267, 2.3280, 1.9470], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.1
trained 50.25 percent
trained 50.3 percent
trained 50.35 percent
trained 50.4 percent
tensor([2.3244, 2.4258, 1.9764, 1.5117, 0.8317], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.09960000000000001
trained 50.45 percent
trained 50.5 percent
trained 50.55 percent
trained 50.6 percent
tensor([2.2276, 2.3080, 1.8874, 1.4692, 0.8009], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.09920000000000001
trained 50.65 percent
trained 50.7 percent
trained 50.75 percent
trained 50.8 percent
tensor([4.5593, 4.5344, 4.5430, 4.4494, 4.3887], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.09880000000000001
trained 50.85 percent
trained 50.9 percent
trained 50.95 percent
trained 51.0 percent
tensor([9.5860, 9.6555, 9.7166, 9.7443, 9.7481], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.09840000000000002
trained 51.05 percent
trained 51.1 percent
trained 51.15 percent
trained 51.2 percent
tensor([ 1.1810,  1.2095,  1.1869,  0.6407, -0.1507], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.09800000000000002
trained 51.25 percent
trained 51.3 percent
trained 51.35 percent
trained 51.4 percent
tensor([3.3245, 3.2418, 2.8337, 2.5878, 2.1843], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.0976
trained 51.45 percent
trained 51.5 percent
trained 51.55 percent
trained 51.6 percent
tensor([3.2753, 3.2909, 3.3468, 3.1636, 2.9342], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.09720000000000001
trained 51.65 percent
trained 51.7 percent
trained 51.75 percent
trained 51.8 percent
tensor([2.0088, 2.0124, 2.0276, 1.6395, 1.0726], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.09680000000000001
trained 51.85 percent
trained 51.9 percent
trained 51.95 percent
trained 52.0 percent
tensor([4.6624, 4.6658, 4.4880, 4.4381, 4.3569], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.09640000000000001
trained 52.05 percent
trained 52.1 percent
trained 52.15 percent
trained 52.2 percent
tensor([3.9303, 3.9481, 3.9935, 3.8637, 3.7253], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.09600000000000002
trained 52.25 percent
trained 52.3 percent
trained 52.35 percent
trained 52.4 percent
tensor([4.7396, 4.6467, 4.4033, 4.3436, 4.2182], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.0956
trained 52.45 percent
trained 52.5 percent
trained 52.55 percent
trained 52.6 percent
tensor([2.1006, 2.0818, 1.6320, 1.2201, 0.5622], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.0952
trained 52.65 percent
trained 52.7 percent
trained 52.75 percent
trained 52.8 percent
tensor([5.2955, 5.2400, 5.1810, 5.1047, 4.9867], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.09480000000000001
trained 52.85 percent
trained 52.9 percent
trained 52.95 percent
trained 53.0 percent
tensor([2.8024, 2.8266, 2.8403, 2.5651, 2.2217], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.09440000000000001
trained 53.05 percent
trained 53.1 percent
trained 53.15 percent
trained 53.2 percent
tensor([2.2151, 2.1880, 1.7477, 1.3661, 0.7660], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.09400000000000001
trained 53.25 percent
trained 53.3 percent
trained 53.35 percent
trained 53.4 percent
tensor([6.5504, 6.5371, 6.4986, 6.4838, 6.4122], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.09360000000000002
trained 53.45 percent
trained 53.5 percent
trained 53.55 percent
trained 53.6 percent
tensor([3.3720, 3.3800, 3.3024, 3.2169, 2.9406], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.0932
trained 53.65 percent
trained 53.7 percent
trained 53.75 percent
trained 53.8 percent
tensor([4.1951, 4.2099, 4.2652, 4.1623, 4.0735], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.09280000000000001
trained 53.85 percent
trained 53.9 percent
trained 53.95 percent
trained 54.0 percent
tensor([3.4405, 3.4280, 3.4725, 3.2933, 3.0713], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.09240000000000001
trained 54.05 percent
trained 54.1 percent
trained 54.15 percent
trained 54.2 percent
tensor([5.9923, 5.9965, 5.9829, 5.9729, 5.8588], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.09200000000000001
trained 54.25 percent
trained 54.3 percent
trained 54.35 percent
trained 54.4 percent
tensor([2.0087, 2.0212, 1.9826, 1.6084, 1.0297], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.09160000000000001
trained 54.45 percent
trained 54.5 percent
trained 54.55 percent
trained 54.6 percent
tensor([4.4593, 4.4695, 4.4525, 4.4015, 4.3329], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.09120000000000002
trained 54.65 percent
trained 54.7 percent
trained 54.75 percent
trained 54.8 percent
tensor([2.5036, 2.4062, 1.9110, 1.5231, 0.9356], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.0908
trained 54.85 percent
trained 54.9 percent
trained 54.95 percent
trained 55.0 percent
tensor([5.5168, 5.4554, 5.3639, 5.3039, 5.1749], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.09040000000000001
trained 55.05 percent
trained 55.1 percent
trained 55.15 percent
trained 55.2 percent
tensor([2.4063, 2.4991, 2.2437, 2.1079, 1.7716], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.09000000000000001
trained 55.25 percent
trained 55.3 percent
trained 55.35 percent
trained 55.4 percent
tensor([2.9641, 3.0476, 3.1221, 2.8338, 2.4691], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.08960000000000001
trained 55.45 percent
trained 55.5 percent
trained 55.55 percent
trained 55.6 percent
tensor([2.2250, 2.2501, 1.8911, 1.5279, 0.9005], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.08920000000000002
trained 55.65 percent
trained 55.7 percent
trained 55.75 percent
trained 55.8 percent
tensor([5.4229, 5.4059, 5.3987, 5.4001, 5.4201], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.08880000000000002
trained 55.85 percent
trained 55.9 percent
trained 55.95 percent
trained 56.0 percent
tensor([3.4870, 3.4862, 3.5056, 3.3188, 3.1086], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.0884
trained 56.05 percent
trained 56.1 percent
trained 56.15 percent
trained 56.2 percent
tensor([ 1.1893,  1.2101,  1.1935,  0.7025, -0.0336], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.08800000000000001
trained 56.25 percent
trained 56.3 percent
trained 56.35 percent
trained 56.4 percent
tensor([2.3914, 2.3882, 2.0643, 1.9342, 1.5684], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.08760000000000001
trained 56.45 percent
trained 56.5 percent
trained 56.55 percent
trained 56.6 percent
tensor([5.6534, 5.6907, 5.7530, 5.7597, 5.7679], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.08720000000000001
trained 56.65 percent
trained 56.7 percent
trained 56.75 percent
trained 56.8 percent
tensor([3.2382, 3.2572, 2.8786, 2.5370, 2.0986], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.08680000000000002
trained 56.85 percent
trained 56.9 percent
trained 56.95 percent
trained 57.0 percent
tensor([1.9548, 2.0289, 2.0758, 1.6213, 0.9961], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.0864
trained 57.05 percent
trained 57.1 percent
trained 57.15 percent
trained 57.2 percent
tensor([2.3028, 2.3054, 2.3464, 2.0321, 1.5523], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.08600000000000001
trained 57.25 percent
trained 57.3 percent
trained 57.35 percent
trained 57.4 percent
tensor([4.1608, 4.0801, 3.8358, 3.7507, 3.5461], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.08560000000000001
trained 57.45 percent
trained 57.5 percent
trained 57.55 percent
trained 57.6 percent
tensor([1.3530, 1.3869, 1.2833, 0.8207, 0.1168], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.08520000000000001
trained 57.65 percent
trained 57.7 percent
trained 57.75 percent
trained 57.8 percent
tensor([1.9432, 1.9498, 1.9152, 1.5412, 0.9814], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.08480000000000001
trained 57.85 percent
trained 57.9 percent
trained 57.95 percent
trained 58.0 percent
tensor([2.0398, 2.0736, 1.7313, 1.4157, 0.8698], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.08440000000000002
trained 58.05 percent
trained 58.1 percent
trained 58.15 percent
trained 58.2 percent
tensor([5.3019, 5.1932, 5.2062, 5.1229, 5.0536], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.084
trained 58.25 percent
trained 58.3 percent
trained 58.35 percent
trained 58.4 percent
tensor([3.3028, 3.3094, 3.2526, 3.1656, 2.9070], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.08360000000000001
trained 58.45 percent
trained 58.5 percent
trained 58.55 percent
trained 58.6 percent
tensor([3.0850, 3.0450, 2.5642, 2.2105, 1.6829], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.08320000000000001
trained 58.65 percent
trained 58.7 percent
trained 58.75 percent
trained 58.8 percent
tensor([5.4375, 5.3716, 5.2694, 5.2217, 5.0903], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.08280000000000001
trained 58.85 percent
trained 58.9 percent
trained 58.95 percent
trained 59.0 percent
tensor([3.3061, 3.1806, 2.7526, 2.4997, 2.0907], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.08240000000000001
trained 59.05 percent
trained 59.1 percent
trained 59.15 percent
trained 59.2 percent
tensor([1.6647, 1.6858, 1.6541, 1.2587, 0.6052], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.08200000000000002
trained 59.25 percent
trained 59.3 percent
trained 59.35 percent
trained 59.4 percent
tensor([1.9185, 1.9278, 1.9395, 1.5409, 0.9713], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.0816
trained 59.45 percent
trained 59.5 percent
trained 59.55 percent
trained 59.6 percent
tensor([2.5352, 2.5013, 2.1086, 1.7748, 1.2507], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.08120000000000001
trained 59.65 percent
trained 59.7 percent
trained 59.75 percent
trained 59.8 percent
tensor([4.2311, 4.2339, 4.3109, 4.2144, 4.1736], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.08080000000000001
trained 59.85 percent
trained 59.9 percent
trained 59.95 percent
trained 60.0 percent
tensor([3.8321, 3.8603, 3.6218, 3.4210, 3.1700], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.08040000000000001
trained 60.05 percent
trained 60.1 percent
trained 60.15 percent
trained 60.2 percent
tensor([3.1796, 3.2691, 3.2257, 3.2050, 2.9167], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.08000000000000002
trained 60.25 percent
trained 60.3 percent
trained 60.35 percent
trained 60.4 percent
tensor([4.2322, 4.1493, 3.8273, 3.6999, 3.5015], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.07960000000000002
trained 60.45 percent
trained 60.5 percent
trained 60.55 percent
trained 60.6 percent
tensor([ 0.9927,  0.9914,  0.9820,  0.5414, -0.2401], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.0792
trained 60.65 percent
trained 60.7 percent
trained 60.75 percent
trained 60.8 percent
tensor([2.4898, 2.4965, 2.1183, 1.7814, 1.2248], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.07880000000000001
trained 60.85 percent
trained 60.9 percent
trained 60.95 percent
trained 61.0 percent
tensor([3.4052, 3.4094, 3.4321, 3.2443, 2.9864], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.07840000000000001
trained 61.05 percent
trained 61.1 percent
trained 61.15 percent
trained 61.2 percent
tensor([6.0753, 6.0459, 6.0391, 5.9859, 5.9004], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.07800000000000001
trained 61.25 percent
trained 61.3 percent
trained 61.35 percent
trained 61.4 percent
tensor([2.6330, 2.6569, 2.3431, 2.0288, 1.5865], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.07760000000000002
trained 61.45 percent
trained 61.5 percent
trained 61.55 percent
trained 61.6 percent
tensor([2.8174, 2.8331, 2.8635, 2.5544, 2.1337], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.0772
trained 61.65 percent
trained 61.7 percent
trained 61.75 percent
trained 61.8 percent
tensor([4.4223, 4.2968, 4.1222, 4.0285, 3.8385], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.07680000000000001
trained 61.85 percent
trained 61.9 percent
trained 61.95 percent
trained 62.0 percent
tensor([5.4335, 5.3869, 5.2651, 5.2649, 5.2148], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.07640000000000001
trained 62.05 percent
trained 62.1 percent
trained 62.15 percent
trained 62.2 percent
tensor([1.9122, 1.9269, 1.9057, 1.5786, 1.0602], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.07600000000000001
trained 62.25 percent
trained 62.3 percent
trained 62.35 percent
trained 62.4 percent
tensor([3.0028, 3.0158, 3.0150, 2.7714, 2.4222], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.07560000000000001
trained 62.45 percent
trained 62.5 percent
trained 62.55 percent
trained 62.6 percent
trained 62.65 percent
tensor([ 1.0332,  1.0595,  1.0516,  0.5603, -0.2441], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.07520000000000002
trained 62.7 percent
trained 62.75 percent
trained 62.8 percent
trained 62.85 percent
tensor([4.8748, 4.8015, 4.6807, 4.6179, 4.4812], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.0748
trained 62.9 percent
trained 62.95 percent
trained 63.0 percent
trained 63.05 percent
tensor([5.6215, 5.5744, 5.4933, 5.4788, 5.4035], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.07440000000000002
trained 63.1 percent
trained 63.15 percent
trained 63.2 percent
trained 63.25 percent
tensor([3.4165, 3.3268, 2.8646, 2.5738, 2.1501], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.07400000000000001
trained 63.3 percent
trained 63.35 percent
trained 63.4 percent
trained 63.45 percent
tensor([2.9371, 2.9598, 2.6642, 2.4249, 2.0477], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.0736
trained 63.5 percent
trained 63.55 percent
trained 63.6 percent
trained 63.65 percent
tensor([6.1395, 6.1059, 6.0078, 6.0012, 5.8831], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.07320000000000002
trained 63.7 percent
trained 63.75 percent
trained 63.8 percent
trained 63.85 percent
tensor([6.8941, 6.9402, 7.0194, 6.9498, 6.9389], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.0728
trained 63.9 percent
trained 63.95 percent
trained 64.0 percent
trained 64.05 percent
tensor([4.5438, 4.5355, 4.5829, 4.5172, 4.4448], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.07240000000000002
trained 64.1 percent
trained 64.15 percent
trained 64.2 percent
trained 64.25 percent
tensor([8.1146, 8.7242, 8.4820, 8.4529, 8.3642], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.07200000000000001
trained 64.3 percent
trained 64.35 percent
trained 64.4 percent
trained 64.45 percent
tensor([5.8000, 5.7587, 5.6742, 5.6533, 5.5594], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.07160000000000002
trained 64.5 percent
trained 64.55 percent
trained 64.6 percent
trained 64.65 percent
tensor([4.3254, 4.2028, 3.8428, 3.7716, 3.5657], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.07120000000000001
trained 64.7 percent
trained 64.75 percent
trained 64.8 percent
trained 64.85 percent
tensor([5.1624, 5.1083, 4.9053, 4.9094, 4.8157], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.0708
trained 64.9 percent
trained 64.95 percent
trained 65.0 percent
trained 65.05 percent
tensor([4.7389, 4.7306, 4.7562, 4.7045, 4.6283], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.07040000000000002
trained 65.1 percent
trained 65.15 percent
trained 65.2 percent
trained 65.25 percent
tensor([2.4100, 2.5081, 2.3637, 2.3097, 2.0650], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.07
trained 65.3 percent
trained 65.35 percent
trained 65.4 percent
trained 65.45 percent
tensor([1.7720, 1.8132, 1.3983, 0.9854, 0.3739], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.06960000000000002
trained 65.5 percent
trained 65.55 percent
trained 65.6 percent
trained 65.65 percent
tensor([5.4449, 5.3951, 5.2147, 5.2282, 5.1769], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.06920000000000001
trained 65.7 percent
trained 65.75 percent
trained 65.8 percent
trained 65.85 percent
tensor([2.7064, 2.7150, 2.7303, 2.4213, 1.9781], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.0688
trained 65.9 percent
trained 65.95 percent
trained 66.0 percent
trained 66.05 percent
tensor([2.3205, 2.3148, 2.2944, 2.0038, 1.5736], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.06840000000000002
trained 66.1 percent
trained 66.15 percent
trained 66.2 percent
trained 66.25 percent
tensor([3.4172, 3.4128, 3.3972, 3.2196, 3.0012], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.068
trained 66.3 percent
trained 66.35 percent
trained 66.4 percent
trained 66.45 percent
tensor([4.1646, 4.0873, 3.7395, 3.5861, 3.3491], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.06760000000000002
trained 66.5 percent
trained 66.55 percent
trained 66.6 percent
trained 66.65 percent
tensor([6.6615, 7.0382, 6.7720, 6.6286, 6.4030], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.06720000000000001
trained 66.7 percent
trained 66.75 percent
trained 66.8 percent
trained 66.85 percent
tensor([7.5518, 7.5782, 7.6336, 7.6311, 7.5954], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.0668
trained 66.9 percent
trained 66.95 percent
trained 67.0 percent
trained 67.05 percent
tensor([3.9688, 3.8835, 3.7600, 3.6696, 3.4677], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.06640000000000001
trained 67.1 percent
trained 67.15 percent
trained 67.2 percent
trained 67.25 percent
tensor([4.0683, 4.0553, 4.1206, 3.9586, 3.8525], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.066
trained 67.3 percent
trained 67.35 percent
trained 67.4 percent
trained 67.45 percent
tensor([3.5393, 3.5514, 3.6334, 3.4185, 3.1861], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.06560000000000002
trained 67.5 percent
trained 67.55 percent
trained 67.6 percent
trained 67.65 percent
tensor([4.6580, 4.6603, 4.6551, 4.6118, 4.5725], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.06520000000000001
trained 67.7 percent
trained 67.75 percent
trained 67.8 percent
trained 67.85 percent
tensor([2.2847, 2.2901, 2.2968, 1.9932, 1.5666], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.06480000000000002
trained 67.9 percent
trained 67.95 percent
trained 68.0 percent
trained 68.05 percent
tensor([5.3790, 5.3860, 5.3678, 5.3995, 5.3420], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.06440000000000001
trained 68.1 percent
trained 68.15 percent
trained 68.2 percent
trained 68.25 percent
tensor([4.5012, 4.4990, 4.5508, 4.4558, 4.3786], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.064
trained 68.3 percent
trained 68.35 percent
trained 68.4 percent
trained 68.45 percent
tensor([3.9049, 3.9337, 3.7218, 3.5779, 3.3299], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.06360000000000002
trained 68.5 percent
trained 68.55 percent
trained 68.6 percent
trained 68.65 percent
tensor([5.1033, 5.1164, 4.9322, 4.9274, 4.8627], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.0632
trained 68.7 percent
trained 68.75 percent
trained 68.8 percent
trained 68.85 percent
tensor([4.6325, 4.6216, 4.6719, 4.6025, 4.5246], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.06280000000000002
trained 68.9 percent
trained 68.95 percent
trained 69.0 percent
trained 69.05 percent
tensor([9.0549, 9.1272, 9.1116, 9.1751, 9.1714], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.06240000000000001
trained 69.1 percent
trained 69.15 percent
trained 69.2 percent
trained 69.25 percent
tensor([2.4947, 2.4983, 2.5157, 2.2169, 1.8521], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.062
trained 69.3 percent
trained 69.35 percent
trained 69.4 percent
trained 69.45 percent
tensor([3.5472, 3.5529, 3.5113, 3.3551, 3.1512], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.061600000000000016
trained 69.5 percent
trained 69.55 percent
trained 69.6 percent
trained 69.65 percent
tensor([2.3140, 2.2700, 1.7891, 1.3915, 0.7919], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.061200000000000004
trained 69.7 percent
trained 69.75 percent
trained 69.8 percent
trained 69.85 percent
tensor([2.5793, 2.5939, 2.6274, 2.3087, 1.9015], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.06080000000000002
trained 69.9 percent
trained 69.95 percent
trained 70.0 percent
trained 70.05 percent
tensor([2.1068, 2.1601, 1.7657, 1.3989, 0.8621], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.06040000000000001
trained 70.1 percent
trained 70.15 percent
trained 70.2 percent
trained 70.25 percent
tensor([3.6786, 3.6101, 3.2092, 2.9571, 2.6749], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.06
trained 70.3 percent
trained 70.35 percent
trained 70.4 percent
trained 70.45 percent
tensor([5.2973, 5.2272, 5.1553, 5.1026, 5.0020], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.059600000000000014
trained 70.5 percent
trained 70.55 percent
trained 70.6 percent
trained 70.65 percent
tensor([2.8152, 2.8120, 2.5087, 2.1928, 1.7103], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.0592
trained 70.7 percent
trained 70.75 percent
trained 70.8 percent
trained 70.85 percent
tensor([2.5027, 2.5554, 2.4259, 2.3668, 2.1196], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.05880000000000002
trained 70.9 percent
trained 70.95 percent
trained 71.0 percent
trained 71.05 percent
tensor([ 0.7748,  0.8194,  0.7827,  0.3292, -0.3434], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.05840000000000001
trained 71.1 percent
trained 71.15 percent
trained 71.2 percent
trained 71.25 percent
tensor([2.8247, 2.8520, 2.8841, 2.6042, 2.2242], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.058000000000000024
trained 71.3 percent
trained 71.35 percent
trained 71.4 percent
trained 71.45 percent
tensor([3.3774, 3.4032, 3.4176, 3.2093, 2.9293], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.05760000000000001
trained 71.5 percent
trained 71.55 percent
trained 71.6 percent
trained 71.65 percent
tensor([4.7501, 4.7608, 4.8003, 4.7455, 4.7043], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.0572
trained 71.7 percent
trained 71.75 percent
trained 71.8 percent
trained 71.85 percent
tensor([4.6239, 4.5473, 4.3513, 4.2821, 4.1388], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.05680000000000002
trained 71.9 percent
trained 71.95 percent
trained 72.0 percent
trained 72.05 percent
tensor([2.2303, 2.2384, 2.2178, 1.9033, 1.4125], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.056400000000000006
trained 72.1 percent
trained 72.15 percent
trained 72.2 percent
trained 72.25 percent
tensor([2.2167, 2.2186, 2.1877, 1.8559, 1.3711], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.05600000000000002
trained 72.3 percent
trained 72.35 percent
trained 72.4 percent
trained 72.45 percent
tensor([7.3768, 7.3802, 7.3817, 7.3648, 7.3205], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.05560000000000001
trained 72.5 percent
trained 72.55 percent
trained 72.6 percent
trained 72.65 percent
tensor([ 0.9242,  0.9470,  0.9003,  0.4825, -0.1531], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.0552
trained 72.7 percent
trained 72.75 percent
trained 72.8 percent
trained 72.85 percent
tensor([5.4949, 5.5276, 5.5518, 5.5439, 5.5318], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.054800000000000015
trained 72.9 percent
trained 72.95 percent
trained 73.0 percent
trained 73.05 percent
tensor([5.0766, 5.0380, 4.9119, 4.8700, 4.7639], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.054400000000000004
trained 73.1 percent
trained 73.15 percent
trained 73.2 percent
trained 73.25 percent
tensor([5.9880, 6.0151, 5.9740, 5.9976, 5.9610], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.05400000000000002
trained 73.3 percent
trained 73.35 percent
trained 73.4 percent
trained 73.45 percent
tensor([3.0910, 3.0577, 2.7017, 2.4191, 2.0106], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.05360000000000001
trained 73.5 percent
trained 73.55 percent
trained 73.6 percent
trained 73.65 percent
tensor([2.2352, 2.2392, 2.2199, 1.9200, 1.4194], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.0532
trained 73.7 percent
trained 73.75 percent
trained 73.8 percent
trained 73.85 percent
tensor([2.5356, 2.5455, 2.2542, 2.1807, 1.8830], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.052800000000000014
trained 73.9 percent
trained 73.95 percent
trained 74.0 percent
trained 74.05 percent
tensor([ 0.8253,  0.8601,  0.8102,  0.3953, -0.2493], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.0524
trained 74.1 percent
trained 74.15 percent
trained 74.2 percent
trained 74.25 percent
tensor([4.3766, 4.3113, 4.0362, 3.9267, 3.7965], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.05200000000000002
trained 74.3 percent
trained 74.35 percent
trained 74.4 percent
trained 74.45 percent
tensor([2.7687, 2.8941, 2.6066, 2.2703, 1.7988], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.05160000000000001
trained 74.5 percent
trained 74.55 percent
trained 74.6 percent
trained 74.65 percent
tensor([7.1698, 7.1817, 7.1036, 7.1153, 7.0567], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.05120000000000002
trained 74.7 percent
trained 74.75 percent
trained 74.8 percent
trained 74.85 percent
tensor([3.1489, 3.1238, 2.7726, 2.5086, 2.0977], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.05080000000000001
trained 74.9 percent
trained 74.95 percent
trained 75.0 percent
trained 75.05 percent
trained 75.1 percent
tensor([5.3666, 5.3391, 5.2628, 5.2188, 5.1314], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.0504
trained 75.15 percent
trained 75.2 percent
trained 75.25 percent
trained 75.3 percent
tensor([5.5095, 5.4759, 5.4201, 5.4274, 5.3932], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.05000000000000002
trained 75.35 percent
trained 75.4 percent
trained 75.45 percent
trained 75.5 percent
tensor([1.7658, 1.7778, 1.7716, 1.3807, 0.8274], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.049600000000000005
trained 75.55 percent
trained 75.6 percent
trained 75.65 percent
trained 75.7 percent
tensor([1.8368, 1.8547, 1.8226, 1.4978, 0.9994], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.04920000000000002
trained 75.75 percent
trained 75.8 percent
trained 75.85 percent
trained 75.9 percent
tensor([2.6223, 2.6033, 2.2553, 1.9855, 1.5949], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.04880000000000001
trained 75.95 percent
trained 76.0 percent
trained 76.05 percent
trained 76.1 percent
tensor([5.5089, 5.5183, 5.3390, 5.3539, 5.2691], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.0484
trained 76.15 percent
trained 76.2 percent
trained 76.25 percent
trained 76.3 percent
tensor([6.0260, 6.0522, 5.9883, 5.9480, 5.8684], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.048000000000000015
trained 76.35 percent
trained 76.4 percent
trained 76.45 percent
trained 76.5 percent
tensor([4.1312, 4.1478, 4.2004, 4.0640, 3.9511], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.0476
trained 76.55 percent
trained 76.6 percent
trained 76.65 percent
trained 76.7 percent
tensor([5.5183, 5.4338, 5.3666, 5.3156, 5.1959], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.04720000000000002
trained 76.75 percent
trained 76.8 percent
trained 76.85 percent
trained 76.9 percent
tensor([2.7595, 2.7630, 2.7536, 2.4683, 2.0984], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.04680000000000001
trained 76.95 percent
trained 77.0 percent
trained 77.05 percent
trained 77.1 percent
tensor([2.3942, 2.4025, 2.3910, 2.0640, 1.6153], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.046400000000000025
trained 77.15 percent
trained 77.2 percent
trained 77.25 percent
trained 77.3 percent
tensor([4.9088, 4.8596, 4.7630, 4.7210, 4.6406], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.04600000000000001
trained 77.35 percent
trained 77.4 percent
trained 77.45 percent
trained 77.5 percent
tensor([7.6890, 7.7431, 7.7798, 7.7934, 7.7770], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.0456
trained 77.55 percent
trained 77.6 percent
trained 77.65 percent
trained 77.7 percent
tensor([5.9336, 5.9749, 5.9368, 5.8676, 5.8047], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.04520000000000002
trained 77.75 percent
trained 77.8 percent
trained 77.85 percent
trained 77.9 percent
tensor([4.2386, 4.2038, 4.0103, 3.9082, 3.6875], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.044800000000000006
trained 77.95 percent
trained 78.0 percent
trained 78.05 percent
trained 78.1 percent
tensor([3.4498, 3.4199, 3.1343, 2.9276, 2.6636], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.04440000000000002
trained 78.15 percent
trained 78.2 percent
trained 78.25 percent
trained 78.3 percent
tensor([5.6614, 5.5718, 5.4046, 5.4629, 5.3221], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.04400000000000001
trained 78.35 percent
trained 78.4 percent
trained 78.45 percent
trained 78.5 percent
tensor([3.6595, 3.6649, 3.5107, 3.4805, 3.2436], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.0436
trained 78.55 percent
trained 78.6 percent
trained 78.65 percent
trained 78.7 percent
tensor([2.2278, 2.2446, 2.2394, 1.8959, 1.3951], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.043200000000000016
trained 78.75 percent
trained 78.8 percent
trained 78.85 percent
trained 78.9 percent
tensor([3.1299, 3.1340, 3.1433, 2.8929, 2.6436], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.042800000000000005
trained 78.95 percent
trained 79.0 percent
trained 79.05 percent
trained 79.1 percent
tensor([3.9886, 3.9975, 3.9885, 3.8465, 3.7243], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.04240000000000002
trained 79.15 percent
trained 79.2 percent
trained 79.25 percent
trained 79.3 percent
tensor([5.1964, 5.1627, 5.0296, 4.9570, 4.8106], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.04200000000000001
trained 79.35 percent
trained 79.4 percent
trained 79.45 percent
trained 79.5 percent
tensor([4.6092, 4.6306, 4.3736, 4.2103, 4.0291], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.0416
trained 79.55 percent
trained 79.6 percent
trained 79.65 percent
trained 79.7 percent
tensor([2.9319, 3.0202, 2.8569, 2.6712, 2.4437], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.041200000000000014
trained 79.75 percent
trained 79.8 percent
trained 79.85 percent
trained 79.9 percent
tensor([7.4610, 7.4911, 7.5234, 7.4988, 7.5014], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.0408
trained 79.95 percent
trained 80.0 percent
trained 80.05 percent
trained 80.1 percent
tensor([2.0388, 2.0481, 2.0503, 1.6955, 1.1442], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.04040000000000002
trained 80.15 percent
trained 80.2 percent
trained 80.25 percent
trained 80.3 percent
tensor([3.0553, 3.0620, 3.0789, 2.8142, 2.5015], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.04000000000000001
trained 80.35 percent
trained 80.4 percent
trained 80.45 percent
trained 80.5 percent
tensor([9.1974, 9.1800, 9.1909, 9.1737, 9.2033], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.039600000000000024
trained 80.55 percent
trained 80.6 percent
trained 80.65 percent
trained 80.7 percent
tensor([2.4274, 2.4336, 2.4160, 2.1244, 1.7233], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.03920000000000001
trained 80.75 percent
trained 80.8 percent
trained 80.85 percent
trained 80.9 percent
tensor([6.3388, 6.3976, 6.3689, 6.3501, 6.2822], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.0388
trained 80.95 percent
trained 81.0 percent
trained 81.05 percent
trained 81.1 percent
tensor([2.9954, 3.0638, 3.1072, 2.8227, 2.4415], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.03840000000000002
trained 81.15 percent
trained 81.2 percent
trained 81.25 percent
trained 81.3 percent
tensor([2.6250, 2.6380, 2.2652, 1.9351, 1.4954], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.038000000000000006
trained 81.35 percent
trained 81.4 percent
trained 81.45 percent
trained 81.5 percent
tensor([2.6706, 2.6899, 2.4045, 2.0761, 1.5858], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.03760000000000002
trained 81.55 percent
trained 81.6 percent
trained 81.65 percent
trained 81.7 percent
tensor([5.1165, 5.1328, 5.1393, 5.1186, 5.1043], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.03720000000000001
trained 81.75 percent
trained 81.8 percent
trained 81.85 percent
trained 81.9 percent
tensor([4.7656, 4.6873, 4.5612, 4.5114, 4.3590], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.0368
trained 81.95 percent
trained 82.0 percent
trained 82.05 percent
trained 82.1 percent
tensor([3.1294, 3.0432, 2.6095, 2.3253, 1.9136], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.036400000000000016
trained 82.15 percent
trained 82.2 percent
trained 82.25 percent
trained 82.3 percent
tensor([3.1693, 3.1835, 3.1966, 2.9899, 2.7146], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.036000000000000004
trained 82.35 percent
trained 82.4 percent
trained 82.45 percent
trained 82.5 percent
tensor([2.2292, 2.3172, 2.3811, 2.0149, 1.5227], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.03560000000000002
trained 82.55 percent
trained 82.6 percent
trained 82.65 percent
trained 82.7 percent
tensor([2.0851, 2.2040, 1.8692, 1.4883, 0.8768], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.03520000000000001
trained 82.75 percent
trained 82.8 percent
trained 82.85 percent
trained 82.9 percent
tensor([3.7684, 3.7799, 3.8222, 3.6588, 3.4259], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.0348
trained 82.95 percent
trained 83.0 percent
trained 83.05 percent
trained 83.1 percent
tensor([3.3310, 3.2784, 3.1844, 3.1322, 2.9257], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.034400000000000014
trained 83.15 percent
trained 83.2 percent
trained 83.25 percent
trained 83.3 percent
tensor([1.2260, 1.2632, 1.2430, 0.8301, 0.1336], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.034
trained 83.35 percent
trained 83.4 percent
trained 83.45 percent
trained 83.5 percent
tensor([2.6785, 2.6873, 2.6947, 2.3996, 2.0331], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.03360000000000002
trained 83.55 percent
trained 83.6 percent
trained 83.65 percent
trained 83.7 percent
tensor([2.2192, 2.2266, 2.2159, 1.8893, 1.4416], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.03320000000000001
trained 83.75 percent
trained 83.8 percent
trained 83.85 percent
trained 83.9 percent
tensor([4.2772, 4.1838, 4.0267, 3.9125, 3.7482], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.032800000000000024
trained 83.95 percent
trained 84.0 percent
trained 84.05 percent
trained 84.1 percent
tensor([3.7458, 3.8001, 3.8705, 3.6384, 3.4432], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.03240000000000001
trained 84.15 percent
trained 84.2 percent
trained 84.25 percent
trained 84.3 percent
tensor([3.9924, 4.0522, 4.0967, 3.9199, 3.7043], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.032
trained 84.35 percent
trained 84.4 percent
trained 84.45 percent
trained 84.5 percent
tensor([3.0430, 3.0169, 2.6541, 2.3676, 1.9720], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.03160000000000002
trained 84.55 percent
trained 84.6 percent
trained 84.65 percent
trained 84.7 percent
tensor([2.1233, 2.1898, 1.8825, 1.6006, 1.1959], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.031200000000000006
trained 84.75 percent
trained 84.8 percent
trained 84.85 percent
trained 84.9 percent
tensor([6.1117, 6.0933, 6.0371, 6.0110, 5.9689], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.030800000000000022
trained 84.95 percent
trained 85.0 percent
trained 85.05 percent
trained 85.1 percent
tensor([6.9958, 6.9533, 6.8043, 6.8352, 6.8108], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.03040000000000001
trained 85.15 percent
trained 85.2 percent
trained 85.25 percent
trained 85.3 percent
tensor([3.4973, 3.5034, 3.5362, 3.3158, 3.1284], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.03
trained 85.35 percent
trained 85.4 percent
trained 85.45 percent
trained 85.5 percent
tensor([1.7654, 1.7671, 1.7378, 1.4226, 0.9273], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.029600000000000015
trained 85.55 percent
trained 85.6 percent
trained 85.65 percent
trained 85.7 percent
tensor([2.0394, 2.0408, 1.6492, 1.2107, 0.5344], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.029200000000000004
trained 85.75 percent
trained 85.8 percent
trained 85.85 percent
trained 85.9 percent
tensor([2.7444, 2.7689, 2.4130, 2.1905, 1.8289], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.02880000000000002
trained 85.95 percent
trained 86.0 percent
trained 86.05 percent
trained 86.1 percent
tensor([5.9831, 5.9827, 5.9607, 5.9691, 5.9269], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.02840000000000001
trained 86.15 percent
trained 86.2 percent
trained 86.25 percent
trained 86.3 percent
tensor([4.4863, 4.4506, 4.3927, 4.2952, 4.1699], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.028000000000000025
trained 86.35 percent
trained 86.4 percent
trained 86.45 percent
trained 86.5 percent
tensor([1.4283, 1.4529, 1.4501, 1.0293, 0.3589], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.027600000000000013
trained 86.55 percent
trained 86.6 percent
trained 86.65 percent
trained 86.7 percent
tensor([3.6529, 3.6029, 3.2551, 3.0112, 2.6881], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.027200000000000002
trained 86.75 percent
trained 86.8 percent
trained 86.85 percent
trained 86.9 percent
tensor([1.2148, 1.2185, 1.2173, 0.7949, 0.1758], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.026800000000000018
trained 86.95 percent
trained 87.0 percent
trained 87.05 percent
trained 87.1 percent
tensor([ 0.9350,  0.9478,  0.8926,  0.5394, -0.1044], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.026400000000000007
trained 87.15 percent
trained 87.2 percent
trained 87.25 percent
trained 87.3 percent
tensor([4.5401, 4.5346, 4.2989, 4.1686, 3.9889], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.026000000000000023
trained 87.35 percent
trained 87.4 percent
trained 87.45 percent
trained 87.5 percent
trained 87.55 percent
tensor([2.0668, 2.0513, 1.5900, 1.1173, 0.4445], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.02560000000000001
trained 87.6 percent
trained 87.65 percent
trained 87.7 percent
trained 87.75 percent
tensor([5.6925, 5.6684, 5.5949, 5.6045, 5.5115], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.0252
trained 87.8 percent
trained 87.85 percent
trained 87.9 percent
trained 87.95 percent
tensor([4.9234, 4.8914, 4.8041, 4.7317, 4.6215], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.024800000000000016
trained 88.0 percent
trained 88.05 percent
trained 88.1 percent
trained 88.15 percent
tensor([5.7699, 5.7400, 5.6328, 5.6311, 5.5462], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.024400000000000005
trained 88.2 percent
trained 88.25 percent
trained 88.3 percent
trained 88.35 percent
tensor([1.4057, 1.4242, 1.4183, 0.9813, 0.3033], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.02400000000000002
trained 88.4 percent
trained 88.45 percent
trained 88.5 percent
trained 88.55 percent
tensor([2.1930, 2.2060, 2.1873, 1.8509, 1.3876], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.02360000000000001
trained 88.6 percent
trained 88.65 percent
trained 88.7 percent
trained 88.75 percent
tensor([3.5604, 3.5681, 3.5616, 3.3693, 3.1511], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.0232
trained 88.8 percent
trained 88.85 percent
trained 88.9 percent
trained 88.95 percent
tensor([4.8460, 4.7898, 4.5632, 4.4470, 4.2974], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.022800000000000015
trained 89.0 percent
trained 89.05 percent
trained 89.1 percent
trained 89.15 percent
tensor([3.0976, 3.1107, 2.8257, 2.6014, 2.3268], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.022400000000000003
trained 89.2 percent
trained 89.25 percent
trained 89.3 percent
trained 89.35 percent
tensor([4.2098, 4.1675, 3.8983, 3.7209, 3.5505], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.02200000000000002
trained 89.4 percent
trained 89.45 percent
trained 89.5 percent
trained 89.55 percent
tensor([3.7556, 3.7836, 3.7104, 3.6338, 3.5087], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.021600000000000008
trained 89.6 percent
trained 89.65 percent
trained 89.7 percent
trained 89.75 percent
tensor([5.1626, 5.1138, 4.8829, 4.8245, 4.6800], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.021200000000000024
trained 89.8 percent
trained 89.85 percent
trained 89.9 percent
trained 89.95 percent
tensor([4.7672, 4.7676, 4.7987, 4.6770, 4.6230], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.020800000000000013
trained 90.0 percent
trained 90.05 percent
trained 90.1 percent
trained 90.15 percent
tensor([5.5403, 5.5007, 5.4702, 5.4305, 5.3845], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.0204
trained 90.2 percent
trained 90.25 percent
trained 90.3 percent
trained 90.35 percent
tensor([1.6668, 1.6726, 1.6653, 1.3037, 0.7594], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.020000000000000018
trained 90.4 percent
trained 90.45 percent
trained 90.5 percent
trained 90.55 percent
tensor([ 1.0851,  1.1255,  1.1122,  0.6547, -0.1018], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.019600000000000006
trained 90.6 percent
trained 90.65 percent
trained 90.7 percent
trained 90.75 percent
tensor([3.8998, 3.9038, 3.9201, 3.7316, 3.5007], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.019200000000000023
trained 90.8 percent
trained 90.85 percent
trained 90.9 percent
trained 90.95 percent
tensor([4.7806, 4.7237, 4.4937, 4.4336, 4.2855], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.01880000000000001
trained 91.0 percent
trained 91.05 percent
trained 91.1 percent
trained 91.15 percent
tensor([5.4742, 5.4437, 5.3536, 5.3012, 5.2061], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.0184
trained 91.2 percent
trained 91.25 percent
trained 91.3 percent
trained 91.35 percent
tensor([3.5127, 3.5305, 3.5600, 3.3363, 3.0333], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.018000000000000016
trained 91.4 percent
trained 91.45 percent
trained 91.5 percent
trained 91.55 percent
tensor([6.1598, 6.1971, 6.1717, 6.1687, 6.0951], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.017600000000000005
trained 91.6 percent
trained 91.65 percent
trained 91.7 percent
trained 91.75 percent
tensor([6.1300, 6.1048, 6.0358, 6.0352, 5.9616], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.01720000000000002
trained 91.8 percent
trained 91.85 percent
trained 91.9 percent
trained 91.95 percent
tensor([6.0965, 6.0569, 6.0144, 5.9586, 5.8810], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.01680000000000001
trained 92.0 percent
trained 92.05 percent
trained 92.1 percent
trained 92.15 percent
tensor([1.9622, 1.9797, 1.9770, 1.6084, 1.0210], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.016399999999999998
trained 92.2 percent
trained 92.25 percent
trained 92.3 percent
trained 92.35 percent
tensor([3.8435, 3.8335, 3.7402, 3.6725, 3.4832], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.016000000000000014
trained 92.4 percent
trained 92.45 percent
trained 92.5 percent
trained 92.55 percent
tensor([2.2360, 2.2339, 1.8193, 1.4403, 0.9135], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.015600000000000003
trained 92.6 percent
trained 92.65 percent
trained 92.7 percent
trained 92.75 percent
tensor([2.9327, 2.9546, 2.7412, 2.4924, 2.2189], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.015200000000000019
trained 92.8 percent
trained 92.85 percent
trained 92.9 percent
trained 92.95 percent
tensor([1.3272, 1.3355, 1.3220, 0.8917, 0.1611], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.014800000000000008
trained 93.0 percent
trained 93.05 percent
trained 93.1 percent
trained 93.15 percent
tensor([4.3493, 4.4486, 4.3258, 4.2807, 4.1100], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.014400000000000024
trained 93.2 percent
trained 93.25 percent
trained 93.3 percent
trained 93.35 percent
tensor([5.3857, 5.3446, 5.2511, 5.2353, 5.1743], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.014000000000000012
trained 93.4 percent
trained 93.45 percent
trained 93.5 percent
trained 93.55 percent
tensor([4.7508, 4.6717, 4.5763, 4.4858, 4.3527], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.013600000000000001
trained 93.6 percent
trained 93.65 percent
trained 93.7 percent
trained 93.75 percent
tensor([4.3323, 4.2411, 3.9310, 3.7758, 3.5013], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.013200000000000017
trained 93.8 percent
trained 93.85 percent
trained 93.9 percent
trained 93.95 percent
tensor([3.6747, 3.6914, 3.6938, 3.4888, 3.2456], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.012800000000000006
trained 94.0 percent
trained 94.05 percent
trained 94.1 percent
trained 94.15 percent
tensor([2.5535, 2.5913, 2.3352, 2.1446, 1.9083], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.012400000000000022
trained 94.2 percent
trained 94.25 percent
trained 94.3 percent
trained 94.35 percent
tensor([5.8402, 5.8802, 5.6807, 5.6552, 5.5594], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.01200000000000001
trained 94.4 percent
trained 94.45 percent
trained 94.5 percent
trained 94.55 percent
tensor([2.3637, 2.3780, 2.4026, 2.0682, 1.5666], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.0116
trained 94.6 percent
trained 94.65 percent
trained 94.7 percent
trained 94.75 percent
tensor([5.6017, 5.6067, 5.5166, 5.4857, 5.3962], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.011200000000000015
trained 94.8 percent
trained 94.85 percent
trained 94.9 percent
trained 94.95 percent
tensor([3.6738, 3.6824, 3.7229, 3.5049, 3.3361], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.010800000000000004
trained 95.0 percent
trained 95.05 percent
trained 95.1 percent
trained 95.15 percent
tensor([3.1916, 3.2108, 3.0498, 2.9667, 2.8062], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.01040000000000002
trained 95.2 percent
trained 95.25 percent
trained 95.3 percent
trained 95.35 percent
tensor([3.6076, 3.6334, 3.6145, 3.3987, 3.1565], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.010000000000000009
trained 95.4 percent
trained 95.45 percent
trained 95.5 percent
trained 95.55 percent
tensor([5.6859, 5.7504, 5.5377, 5.4775, 5.4968], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.01
trained 95.6 percent
trained 95.65 percent
trained 95.7 percent
trained 95.75 percent
tensor([4.0614, 4.0289, 3.8462, 3.7304, 3.5743], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.01
trained 95.8 percent
trained 95.85 percent
trained 95.9 percent
trained 95.95 percent
tensor([4.8157, 4.8325, 4.8577, 4.8013, 4.7273], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.01
trained 96.0 percent
trained 96.05 percent
trained 96.1 percent
trained 96.15 percent
tensor([4.8147, 4.8164, 4.7190, 4.6170, 4.4896], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.01
trained 96.2 percent
trained 96.25 percent
trained 96.3 percent
trained 96.35 percent
tensor([6.9724, 7.0218, 6.9565, 6.9056, 6.8617], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.01
trained 96.4 percent
trained 96.45 percent
trained 96.5 percent
trained 96.55 percent
tensor([6.6295, 6.6328, 6.5544, 6.5721, 6.4894], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.01
trained 96.6 percent
trained 96.65 percent
trained 96.7 percent
trained 96.75 percent
tensor([5.0121, 4.9563, 4.8402, 4.7734, 4.6540], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.01
trained 96.8 percent
trained 96.85 percent
trained 96.9 percent
trained 96.95 percent
tensor([4.2347, 4.2576, 4.2490, 4.1327, 3.9702], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.01
trained 97.0 percent
trained 97.05 percent
trained 97.1 percent
trained 97.15 percent
tensor([3.6824, 3.7219, 3.7025, 3.5031, 3.2776], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.01
trained 97.2 percent
trained 97.25 percent
trained 97.3 percent
trained 97.35 percent
tensor([6.2441, 6.2476, 6.1626, 6.1718, 6.0843], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.01
trained 97.4 percent
trained 97.45 percent
trained 97.5 percent
trained 97.55 percent
tensor([4.2437, 4.2642, 4.2546, 4.1424, 3.9840], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.01
trained 97.6 percent
trained 97.65 percent
trained 97.7 percent
trained 97.75 percent
tensor([2.0404, 2.0511, 2.0514, 1.6546, 1.0956], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.01
trained 97.8 percent
trained 97.85 percent
trained 97.9 percent
trained 97.95 percent
tensor([3.9713, 4.0096, 3.8667, 3.7692, 3.6200], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.01
trained 98.0 percent
trained 98.05 percent
trained 98.1 percent
trained 98.15 percent
tensor([1.8883, 1.9020, 1.8903, 1.5047, 0.9976], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.01
trained 98.2 percent
trained 98.25 percent
trained 98.3 percent
trained 98.35 percent
tensor([2.0763, 2.1584, 1.8304, 1.6783, 1.5381], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.01
trained 98.4 percent
trained 98.45 percent
trained 98.5 percent
trained 98.55 percent
tensor([3.2632, 3.2702, 3.2357, 2.9942, 2.6725], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.01
trained 98.6 percent
trained 98.65 percent
trained 98.7 percent
trained 98.75 percent
tensor([4.5355, 4.5493, 4.5232, 4.4045, 4.3088], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.01
trained 98.8 percent
trained 98.85 percent
trained 98.9 percent
trained 98.95 percent
tensor([4.8198, 4.8401, 4.8247, 4.7737, 4.7133], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.01
trained 99.0 percent
trained 99.05 percent
trained 99.1 percent
trained 99.15 percent
tensor([1.4779, 1.5057, 1.4968, 1.1065, 0.4416], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.01
trained 99.2 percent
trained 99.25 percent
trained 99.3 percent
trained 99.35 percent
tensor([5.8575, 5.8823, 5.8453, 5.8097, 5.7417], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.01
trained 99.4 percent
trained 99.45 percent
trained 99.5 percent
trained 99.55 percent
tensor([3.9531, 3.9411, 3.6562, 3.4806, 3.2341], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.01
trained 99.6 percent
trained 99.65 percent
trained 99.7 percent
trained 99.75 percent
tensor([2.5578, 2.4849, 2.0676, 1.6759, 1.1729], device='cuda:0',
       dtype=torch.float64, grad_fn=<SelectBackward>)
eps at 0.01
trained 99.8 percent
trained 99.85 percent
trained 99.9 percent
trained 99.95 percent
trained 100.0 percent

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 10015891: <Server_test4_0> in cluster <dcc> Done

Job <Server_test4_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun Jul  4 13:20:24 2021
Job was executed on host(s) <n-62-20-4>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun Jul  4 13:20:25 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Stocks/Stocks/Utils> was used as the working directory.
Started at Sun Jul  4 13:20:25 2021
Terminated at Sun Jul  4 14:02:30 2021
Results reported at Sun Jul  4 14:02:30 2021

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

    CPU time :                                   2098.70 sec.
    Max Memory :                                 2726 MB
    Average Memory :                             2498.62 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               13658.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   2584 sec.
    Turnaround time :                            2526 sec.

The output (if any) is above this job summary.

