MODEL_ARGS="pretrained=stabilityai/japanese-stablelm-instruct-alpha-7b,trust_remote_code=True,load_in_8bit=True,tokenizer=novelai/nerdstash-tokenizer-v1"
TASK="chabsa-1.0-0.6,cma_basics-1.0-0.1.2,cpa_audit-1.0-0.4,security_sales_1-1.0-0.6,fp2-1.0-0.1"
python main.py --model hf --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "0,0,0,0,0" --device "cuda" --output_path "models/abeja/abeja-gpt-neox-japanese-2.7b/result.json"
# Estimated results: chabsa:0.48073918949212296,cma_basics:0.2894736842105263,cpa_audit:0.18090452261306533,security_sales_1:0.5263157894736842,fp2:0.2631578947368421
