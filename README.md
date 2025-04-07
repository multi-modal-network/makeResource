# 制作资源文件

## Python依赖

protobuf

## 命令

### 单文件

```bash
python buildResourceSingle.py --ctx-json context.json --tofino-bin tofino.bin  --bfrt-json bfrt.json --output basic_tna.bin -p basic_tna
```

### 多文件

在目标文件夹下批量生成资源文件

```
input文件夹结构
root
|--[p4name]
   |--[p4name].pb.txt
   |--[p4name].tofino
      |--bfrt.json
      |--pipe
         |--context.json
         |--tofino.bin
```

参数

* input 目标文件夹
* output (可选)输出文件夹，没有该参数则原地生成

  `python buildResourceDir.py --input p4src --output out`
