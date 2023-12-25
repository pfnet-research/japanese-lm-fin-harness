MODEL_ARGS="pretrained=rinna/nekomata-14b,trust_remote_code=True"
TASK="chabsa-1.0-0.3,cma_basics,cpa_audit-1.0-0.1,security_sales_1,fp2-1.0-0.1"
python main.py --model hf-causal-experimental --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "3,3,0,3,4" --no_cache --output_path "models/rinna/nekomata-14b/result.json"
# Estimated results: chabsa:0.8970016027440977,cma_basics:0.631578947368421,cpa_audit:0.25125628140703515,security_sales_1:0.6842105263157895,fp2:0.42947368421052634
