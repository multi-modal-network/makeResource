import argparse
import json
import bf_pb2

def getArgsParser():
    parser = argparse.ArgumentParser(description='Build resource file for the project')
    parser.add_argument('--ctx-json',help='path to the context json file', required=True,action='store')
    parser.add_argument('--tofino-bin',help='path to the tofino binary file', required=True,action='store')
    parser.add_argument('--bfrt-json',help='path to the bfrt json file', required=True,action='store')
    parser.add_argument('--output','-o',help='path to the output resource file', required=True,action='store')
    parser.add_argument('--p4-name','-p',help='name of the p4 program', required=True,action='store')
    return parser


def buildResource(ctx_json, tofino_bin, bfrt_json, output, p4_name):
    with open(ctx_json,'rb') as ctx,open(tofino_bin,'rb') as bin,open(bfrt_json,'rb') as bfrt , open(output,'wb') as out :
         pipelineConfig = bf_pb2.BfPipelineConfig()
         
         # 设置 p4 程序名称
         pipelineConfig.p4_name = p4_name
         
         # 设置 bfruntime 信息
         pipelineConfig.bfruntime_info = bfrt.read()
         
         # 创建 Profile
         profile = pipelineConfig.Profile()
         profile.profile_name = p4_name  # 设置配置文件名称
         profile.context = ctx.read()   # 读取 context.json 文件内容
         profile.binary = bin.read()    # 读取 tofino.bin 文件内容
         
         # 将 Profile 添加到 pipelineConfig
         pipelineConfig.profiles.append(profile)
         
         # 序列化 pipelineConfig 并写入输出文件
         out.write(pipelineConfig.SerializeToString())

def main():
    parser = getArgsParser()
    args = parser.parse_args()
    buildResource(args.ctx_json, args.tofino_bin, args.bfrt_json, args.output, args.p4_name)
    
if "__main__" == __name__:
    main()