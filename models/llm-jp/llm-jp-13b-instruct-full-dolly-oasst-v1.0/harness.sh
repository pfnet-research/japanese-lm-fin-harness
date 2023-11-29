MODEL_ARGS="pretrained=llm-jp/llm-jp-13b-instruct-full-dolly-oasst-v1.0,trust_remote_code=True"
TASK="chabsa-1.0-0.5,cma_basics-1.0-0.2,cpa_audit-1.0-0.1,security_sales_1-1.0-0.2.1,fp2-1.0-0.3"
python main.py --model hf-causal-experimental --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "3,3,2,2,2" --no_cache --output_path "models/llm-jp/llm-jp-13b-instruct-full-dolly-oasst-v1.0/result.json"
# Estimated results: chabsa:0.8323006259801777,cma_basics:0.39473684210526316,cpa_audit:0.19597989949748743,security_sales_1:0.49122807017543857,fp2:0.2736842105263158
