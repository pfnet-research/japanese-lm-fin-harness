MODEL_ARGS="pretrained=stabilityai/japanese-stablelm-base-gamma-7b,trust_remote_code=True,tokenizer=novelai/nerdstash-tokenizer-v1,dtype=bfloat16"
TASK="chabsa-1.0-0.4,cma_basics-1.0-0.4,cpa_audit-1.0-0.4,fp2-1.0-0.4,security_sales_1-1.0-0.4"
python main.py --model vllm --model_args $MODEL_ARGS --tasks $TASK --num_fewshot 0 --output_path "models/stabilityai/japanese-stablelm-base-gamma-7b/result-1.0-0.4.json"
# a100-80gb: 1
# a30-24gb: 0
# v100-32gb: 0
# v100-16gb: 0
