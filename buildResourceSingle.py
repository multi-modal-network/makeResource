import argparse
import json
import genResource as res

def getArgsParser():
    parser = argparse.ArgumentParser(description='Build resource file for the project')
    parser.add_argument('--ctx-json',help='path to the context json file', required=True,action='store')
    parser.add_argument('--tofino-bin',help='path to the tofino binary file', required=True,action='store')
    parser.add_argument('--bfrt-json',help='path to the bfrt json file', required=True,action='store')
    parser.add_argument('--output','-o',help='path to the output resource file', required=True,action='store')
    parser.add_argument('--p4-name','-p',help='name of the p4 program', required=True,action='store')
    return parser




def main():
    parser = getArgsParser()
    args = parser.parse_args()
    res.buildResource(args.ctx_json, args.tofino_bin, args.bfrt_json, args.output, args.p4_name)
    
if "__main__" == __name__:
    main()