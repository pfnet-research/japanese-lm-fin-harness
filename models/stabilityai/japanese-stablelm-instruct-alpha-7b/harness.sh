MODEL_ARGS="pretrained=stabilityai/japanese-stablelm-instruct-alpha-7b,trust_remote_code=True,tokenizer=novelai/nerdstash-tokenizer-v1"
TASK="chabsa-1.0-0.1,cma_basics-1.0-0.3,cpa_audit-1.0-0.1.2,security_sales_1-1.0-0.6,fp2-1.0-0.3"
python main.py --model hf-causal-experimental --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "4,1,2,0,2" --no_cache --output_path "models/stabilityai/japanese-stablelm-instruct-alpha-7b/result.json"
# Estimated results: chabsa:0.7893571104043616,cma_basics:0.34210526315789475,cpa_audit:0.1934673366834171,security_sales_1:0.5263157894736842,fp2:0.3031578947368421
