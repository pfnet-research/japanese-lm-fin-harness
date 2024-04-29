MODEL_ARGS="pretrained=llm-jp/llm-jp-13b-instruct-full-jaster-dolly-oasst-v1.0,trust_remote_code=True,dtype=float16"
    TASK="chabsa-1.0-0.2,cma_basics-1.0-0.2.1,cpa_audit-1.0-0.2.1,fp2-1.0-0.2.1,security_sales_1-1.0-0.2.1"
    python main.py --model vllm --model_args $MODEL_ARGS --tasks $TASK --num_fewshot 0 --output_path "models/llm-jp/llm-jp-13b-instruct-full-jaster-dolly-oasst-v1.0/result--1.0-0.2.1.json"
    # a100-80gb: 0
    # a30-24gb: 0
    # v100-32gb: 0
    # v100-16gb: 0
    