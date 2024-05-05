MODEL_ARGS="pretrained=mosaicml/mpt-30b-instruct,trust_remote_code=True,dtype=bfloat16"
TASK="chabsa-1.0-0.6,cma_basics-1.0-0.6,cpa_audit-1.0-0.6,fp2-1.0-0.6,security_sales_1-1.0-0.6"
python main.py --model vllm --model_args $MODEL_ARGS --tasks $TASK --num_fewshot 0 --output_path "models/mosaicml/mpt-30b-instruct/result-1.0-0.6.json"
# a100-80gb: 1
# a30-24gb: 0
# v100-32gb: 0
# v100-16gb: 0
