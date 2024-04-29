MODEL_ARGS="pretrained=google/gemma-2b,dtype=bfloat16"
TASK="chabsa-1.0-0.2,cma_basics-1.0-0.2.1,cpa_audit-1.0-0.2.1,fp2-1.0-0.2.1,security_sales_1-1.0-0.2.1"
python main.py --model vllm --model_args $MODEL_ARGS --tasks $TASK --num_fewshot 0 --output_path "models/google/gemma-2b/result-1.0-0.2.1.json"
# a100-80gb: 1
# a30-24gb: 1
# v100-32gb: 0
# v100-16gb: 0
