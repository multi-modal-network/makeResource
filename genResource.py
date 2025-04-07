import bf_pb2


def buildResource(ctx_json, tofino_bin, bfrt_json, output, p4_name):
    with open(ctx_json,'rb') as ctx,open(tofino_bin,'rb') as bin,open(bfrt_json,'rb') as bfrt , open(output,'wb') as out:
         # 创建 BfPipelineConfig 实例
         pipelineConfig = bf_pb2.BfPipelineConfig()
         
         # 设置 p4 程序名称
         pipelineConfig.p4_name = p4_name
         
         # 设置 bfruntime 信息
         pipelineConfig.bfruntime_info = bfrt.read()
         
         # 创建 Profile 对象
         profile = bf_pb2.BfPipelineConfig.Profile()
         profile.profile_name = "pipe"  # 使用 p4_name 作为 profile_name
         profile.context = ctx.read()    # 设置 context 数据
         profile.binary = bin.read()     # 设置二进制数据
         profile.pipe_scope.extend([0,1,2,3])  # 添加默认的 pipe scope (通常为0)
         
         # 将 Profile 添加到 pipelineConfig 的 profiles 列表中
         pipelineConfig.profiles.append(profile)
         
         # 输出构建信息
         print(f"Building resource for P4 program: {p4_name}")
         print(f"Context file size: {len(profile.context)} bytes")
         print(f"Binary file size: {len(profile.binary)} bytes")
         print(f"BfRuntime info size: {len(pipelineConfig.bfruntime_info)} bytes")
         
         # 序列化 pipelineConfig 并写入输出文件
         serialized = pipelineConfig.SerializeToString()
         out.write(serialized)
         print(f"Resource file written to {output} ({len(serialized)} bytes)")