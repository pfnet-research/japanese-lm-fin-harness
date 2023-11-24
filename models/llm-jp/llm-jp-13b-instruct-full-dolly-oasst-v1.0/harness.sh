MODEL_ARGS="pretrained=llm-jp/llm-jp-13b-instruct-full-dolly-oasst-v1.0,trust_remote_code=True,load_in_8bit=True"
TASK="chabsa-1.0-0.6,cma_basics-1.0-0.1.2,cpa_audit-1.0-0.2,security_sales_1-1.0-0.2.1,fp2-1.0-0.2.1"
python main.py --model hf --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "0,0,0,0,0" --device "cuda" --output_path "models/llm-jp/llm-jp-13b-instruct-full-dolly-oasst-v1.0/result.json"
# Estimated results: chabsa:0.535014896010781,cma_basics:0.3157894736842105,cpa_audit:0.16080402010050251,security_sales_1:0.47368421052631576,fp2:0.24842105263157896
