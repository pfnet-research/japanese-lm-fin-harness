MODEL_ARGS="pretrained=karakuri-ai/karakuri-lm-7b-apm-v0.2,dtype=bfloat16"
TASK="chabsa-1.0-0.3,cma_basics-1.0-0.3,cpa_audit-1.0-0.3,fp2-1.0-0.3,security_sales_1-1.0-0.3"
python main.py --model vllm --model_args $MODEL_ARGS --tasks $TASK --num_fewshot 0 --output_path "models/karakuri-ai/karakuri-lm-7b-apm-v0.2/result-1.0-0.3.json"
# a100-80gb: 1
# a30-24gb: 1
# v100-32gb: 0
# v100-16gb: 0
