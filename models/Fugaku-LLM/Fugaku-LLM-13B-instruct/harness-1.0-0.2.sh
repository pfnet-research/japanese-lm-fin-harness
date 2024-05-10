MODEL_ARGS="pretrained=Fugaku-LLM/Fugaku-LLM-13B-instruct,dtype=bfloat16"
TASK="chabsa-1.0-0.2,cma_basics-1.0-0.2,cpa_audit-1.0-0.2,fp2-1.0-0.2,security_sales_1-1.0-0.2"
python main.py --model hf --model_args $MODEL_ARGS --tasks $TASK --num_fewshot 0 --output_path "models/Fugaku-LLM/Fugaku-LLM-13B-instruct/result-1.0-0.2.json"
# a100-80gb: 1
# a30-24gb: 0
# v100-32gb: 0
# v100-16gb: 0
