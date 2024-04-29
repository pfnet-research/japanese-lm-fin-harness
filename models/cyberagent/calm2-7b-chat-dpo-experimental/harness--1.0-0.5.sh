MODEL_ARGS="pretrained=cyberagent/calm2-7b-chat-dpo-experimental,use_fast=True,dtype=bfloat16"
    TASK="chabsa-1.0-0.5,cma_basics-1.0-0.5,cpa_audit-1.0-0.5,fp2-1.0-0.5,security_sales_1-1.0-0.5"
    python main.py --model vllm --model_args $MODEL_ARGS --tasks $TASK --num_fewshot 0 --output_path "models/cyberagent/calm2-7b-chat-dpo-experimental/result--1.0-0.5.json"
    # a100-80gb: 0
    # a30-24gb: 0
    # v100-32gb: 0
    # v100-16gb: 0
    