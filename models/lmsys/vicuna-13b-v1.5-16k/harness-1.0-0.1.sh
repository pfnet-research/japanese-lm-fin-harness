MODEL_ARGS="pretrained=lmsys/vicuna-13b-v1.5-16k,dtype=float16"
TASK="chabsa-1.0-0.1,cma_basics-1.0-0.1,cpa_audit-1.0-0.1,fp2-1.0-0.1,security_sales_1-1.0-0.1"
python main.py --model vllm --model_args $MODEL_ARGS --tasks $TASK --num_fewshot 0 --output_path "models/lmsys/vicuna-13b-v1.5-16k/result-1.0-0.1.json"
# a100-80gb: 1
# a30-24gb: 0
# v100-32gb: 0
# v100-16gb: 0
