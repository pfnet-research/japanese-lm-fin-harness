MODEL_ARGS="pretrained=stabilityai/japanese-stablelm-instruct-alpha-7b-v2,trust_remote_code=True,load_in_8bit=True,tokenizer=novelai/nerdstash-tokenizer-v1"
TASK="chabsa-1.0-0.6,cma_basics-1.0-0.3,cpa_audit-1.0-0.3,security_sales_1-1.0-0.6,fp2-1.0-0.1"
python main.py --model hf --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "0,0,0,0,0" --device "cuda" --output_path "models/stabilityai/japanese-stablelm-instruct-alpha-7b-v2/result.json"
# Estimated results: chabsa:0.47157023874113624,cma_basics:0.34210526315789475,cpa_audit:0.18341708542713567,security_sales_1:0.5263157894736842,fp2:0.2694736842105263
