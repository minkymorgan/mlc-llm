
👉 Instruction - https://github.com/mlc-ai/mlc-llm/issues/71 
- for web https://github.com/mlc-ai/web-llm#instructions-for-local-deployment
- for ios https://github.com/mlc-ai/mlc-llm/blob/main/ios/README.md

1. Install dependencies
> ```sh pip install -r requirements.txt ```

2. Prepare python env
> ```sudo conda create --name myenv python=3.8```

> ```conda activate myenv```

3. Install TVM
- try to install using manual  https://pyshine.com/How-to-install-TVM-in-MacOS/ (I clone via: `git clone --recursive https://github.com/mlc-ai/relax  tvm`  )
- or try to install via  https://tlcpack.ai/


'dist/models/dolly-v2-3b'
RedPajama-INCITE-Instruct-3B-v1

python3 build.py --model dolly-v2-3b --dtype float16 --target iphone --quantization-mode int3 --quantization-sym --quantization-storage-nbit 16 --max-seq-len 768
python3 build.py --model RedPajama-INCITE-Instruct-3B-v1 --dtype float16 --target iphone --quantization-mode int3 --quantization-sym --quantization-storage-nbit 16 --max-seq-len 768

# target auto
python3 build.py --model RedPajama-INCITE-Instruct-3B-v1 --dtype float16 --target auto --quantization-mode int3 --quantization-sym --quantization-storage-nbit 16 --max-seq-len 768

python3 build.py --model RedPajama-INCITE-Instruct-3B-v1 --dtype float16 --target metal_x86_64 --quantization-mode int4 --quantization-sym


## from project issues
python3 build.py --model vicuna-v1-7b --dtype float16 --target auto --quantization-mode int3 --quantization-sym --quantization-storage-nbit 16 --max-seq-len 768
python build.py --model dolly-v2-3b --use-cache 0 --dtype float16 --quantization-mode int4 --quantization-sym
