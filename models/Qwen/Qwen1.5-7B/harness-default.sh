MODEL_ARGS="pretrained=Qwen/Qwen1.5-7B,trust_remote_code=True,dtype=bfloat16"
TASK="chabsa,cma_basics,cpa_audit,fp2,security_sales_1"
python main.py --model vllm --model_args $MODEL_ARGS --tasks $TASK --num_fewshot 0 --output_path "models/Qwen/Qwen1.5-7B/result-default.json"
# a100-80gb: 1
# a30-24gb: 0
# v100-32gb: 0
# v100-16gb: 0
