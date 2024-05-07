MODEL_ARGS="pretrained=line-corporation/japanese-large-lm-1.7b,trust_remote_code=True,dtype=float16"
TASK="chabsa-1.0-0.5,cma_basics-1.0-0.5,cpa_audit-1.0-0.5,fp2-1.0-0.5,security_sales_1-1.0-0.5"
python main.py --model vllm --model_args $MODEL_ARGS --tasks $TASK --num_fewshot 0 --output_path "models/line-corporation/japanese-large-lm-1.7b/result-1.0-0.5.json"
# a100-80gb: 1
# a30-24gb: 1
# v100-32gb: 1
# v100-16gb: 1
