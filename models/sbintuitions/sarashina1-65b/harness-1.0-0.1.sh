MODEL_ARGS="pretrained=sbintuitions/sarashina1-65b,dtype=float16,tensor_parallel_size=4"
TASK="chabsa-1.0-0.1,cma_basics-1.0-0.1,cpa_audit-1.0-0.1,fp2-1.0-0.1,security_sales_1-1.0-0.1"
python main.py --model vllm --model_args $MODEL_ARGS --tasks $TASK --num_fewshot 0 --output_path "models/sbintuitions/sarashina1-65b/result-1.0-0.1.json"
# a100-80gb: 4
# a30-24gb: 0
# v100-32gb: 8
# v100-16gb: 0
