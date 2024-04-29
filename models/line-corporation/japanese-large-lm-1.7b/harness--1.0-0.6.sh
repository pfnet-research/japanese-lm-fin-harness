MODEL_ARGS="pretrained=line-corporation/japanese-large-lm-1.7b,trust_remote_code=True,dtype=float16"
    TASK="chabsa-1.0-0.6,cma_basics-1.0-0.6,cpa_audit-1.0-0.6,fp2-1.0-0.6,security_sales_1-1.0-0.6"
    python main.py --model vllm --model_args $MODEL_ARGS --tasks $TASK --num_fewshot 0 --output_path "models/line-corporation/japanese-large-lm-1.7b/result--1.0-0.6.json"
    # a100-80gb: 0
    # a30-24gb: 0
    # v100-32gb: 0
    # v100-16gb: 0
    