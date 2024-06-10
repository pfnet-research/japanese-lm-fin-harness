MODEL_ARGS="pretrained=Qwen/Qwen2-72B-Instruct,dtype=bfloat16,tensor_parallel_size=4"
TASK="chabsa,cma_basics,cpa_audit,fp2,security_sales_1"
python main.py --model hf --model_args $MODEL_ARGS --tasks $TASK --num_fewshot 0 --output_path "models/Qwen/Qwen2-72B-Instruct/result-default.json"
# a100-80gb: 4
# a30-24gb: 0
# v100-32gb: 0
# v100-16gb: 0
