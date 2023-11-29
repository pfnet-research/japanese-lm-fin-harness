MODEL_ARGS="pretrained=stabilityai/japanese-stablelm-base-alpha-7b,trust_remote_code=True,tokenizer=novelai/nerdstash-tokenizer-v1"
TASK="chabsa-1.0-0.1,cma_basics-1.0-0.3,cpa_audit-1.0-0.2.1,security_sales_1-1.0-0.6,fp2-1.0-0.3"
python main.py --model hf-causal-experimental --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "4,1,3,2,2" --no_cache --output_path "models/stabilityai/japanese-stablelm-base-alpha-7b/result.json"
# Estimated results: chabsa:0.7874460036446005,cma_basics:0.34210526315789475,cpa_audit:0.19095477386934673,security_sales_1:0.5087719298245614,fp2:0.30736842105263157
