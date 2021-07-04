folders = ['', 'Markdown']
file = open('Utils/experiments.sh', 'w')
file.write('#!/bin/sh\n')



def createFolders(name):
    for folder in folders:
        file.write(f"mkdir ../outputs/{name}/{folder}\n")


def genExperiments(name, n=1, cpu=False, **params):
    createFolders(name)
    for i in range(n):
        params['num'] = i
        file.write(f'bsub -o "../outputs/{name}/Markdown/{name}_{i}.md" -J "{name}_{i}" -env MYARGS="-name {name}-{i} {" ".join(f"-{name} {value}" for name, value in params.items())}" < submit_{"cpu" if cpu else "gpu"}.sh\n')

genExperiments("Server_test3", hours=10)
file.close()
