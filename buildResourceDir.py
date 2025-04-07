import argparse
import json
import genResource as res
import os

def getArgsParser():
    parser = argparse.ArgumentParser(description='Build resource file for the project')
    parser.add_argument('--input',help='path to the input Dir', required=True,action='store')
    parser.add_argument('--output','-o',help='path to the output Dir', required=False,action='store')
    return parser

def getSubDirs(inputDir,prefix='tofino'):
    subDirs = []
    p4Name = []
    for root, dirs, files in os.walk(inputDir):
        for dir in dirs:
            if dir.startswith(prefix):
                subDirs.append(os.path.join(root, dir))
                p4Name.append(dir)
    return subDirs,p4Name

def buildResourceDir(inputDir,outputDir):
    subDirs,p4Name = getSubDirs(inputDir)
    for i in range(len(subDirs)):
        tofinoPath = os.path.join(subDirs[i], f'{p4Name[i]}.tofino')
        pipePath = os.path.join(tofinoPath, 'pipe')
        ctxJson = os.path.join(pipePath,'context.json')
        tofinoBin = os.path.join(pipePath, 'tofino.bin')
        bfrtJson = os.path.join(tofinoPath, 'bfrt.json')
        outputSubDir = os.path.join(outputDir, p4Name[i])
        os.makedirs(outputSubDir, exist_ok=True)
        output = os.path.join(outputSubDir, f'{p4Name[i]}.bin')
        ##复制subDirs中的p4Name[i].pb.txt到outputSubDir
        p4pbtxt = os.path.join(subDirs[i], f'{p4Name[i]}.pb.txt')
        if os.path.exists(p4pbtxt):
            with open(p4pbtxt, 'r') as f:
                p4txtContent = f.read()
            with open(os.path.join(outputSubDir, f'{p4Name[i]}.pb.txt'), 'w') as f:
                f.write(p4txtContent)
        ##print(ctxJson, tofinoBin, bfrtJson, output, p4Name[i])
        res.buildResource(ctxJson, tofinoBin, bfrtJson, output, p4Name[i])

def buildResourceDir(inputDir):
    subDirs,p4Name = getSubDirs(inputDir)
    for i in range(len(subDirs)):
        tofinoPath = os.path.join(subDirs[i], f'{p4Name[i]}.tofino')
        pipePath = os.path.join(tofinoPath, 'pipe')
        ctxJson = os.path.join(pipePath,'context.json')
        tofinoBin = os.path.join(pipePath, 'tofino.bin')
        bfrtJson = os.path.join(tofinoPath, 'bfrt.json')
        output = os.path.join(subDirs[i], f'{p4Name[i]}.bin')
        print(ctxJson, tofinoBin, bfrtJson, output, p4Name[i])
        #res.buildResource(ctxJson, tofinoBin, bfrtJson, output, p4Name[i])


def main():
    parser = getArgsParser()
    args = parser.parse_args()
    if args.output:
        os.makedirs(args.output, exist_ok=True)
        buildResourceDir(args.input, args.output)
    else: 
        buildResourceDir(args.input)
   
    
if "__main__" == __name__:
    main()