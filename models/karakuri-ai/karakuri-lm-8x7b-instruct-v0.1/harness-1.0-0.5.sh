MODEL_ARGS="pretrained=karakuri-ai/karakuri-lm-8x7b-instruct-v0.1,dtype=bfloat16,tensor_parallel_size=2"
TASK="chabsa-1.0-0.5,cma_basics-1.0-0.5,cpa_audit-1.0-0.5,fp2-1.0-0.5,security_sales_1-1.0-0.5"
python main.py --model vllm --model_args $MODEL_ARGS --tasks $TASK --num_fewshot 0 --output_path "models/karakuri-ai/karakuri-lm-8x7b-instruct-v0.1/result-1.0-0.5.json"
# a100-80gb: 2
# a30-24gb: 0
# v100-32gb: 0
# v100-16gb: 0
