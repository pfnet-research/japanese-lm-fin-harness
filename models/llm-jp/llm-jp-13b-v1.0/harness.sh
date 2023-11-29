MODEL_ARGS="pretrained=llm-jp/llm-jp-13b-v1.0,trust_remote_code=True"
TASK="chabsa-1.0-0.2,cma_basics-1.0-0.6,cpa_audit-1.0-0.2.1,security_sales_1-1.0-0.5,fp2-1.0-0.1"
python main.py --model hf-causal-experimental --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "4,1,4,4,2" --no_cache --output_path "models/llm-jp/llm-jp-13b-v1.0/result.json"
# Estimated results: chabsa:0.8124120360919906,cma_basics:0.39473684210526316,cpa_audit:0.19095477386934673,security_sales_1:0.49122807017543857,fp2:0.2926315789473684
