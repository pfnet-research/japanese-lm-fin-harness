MODEL_ARGS="pretrained=line-corporation/japanese-large-lm-3.6b,trust_remote_code=True,load_in_8bit=True"
TASK="chabsa-1.0-0.1,cma_basics-1.0-0.2.1,cpa_audit-1.0-0.4,security_sales_1-1.0-0.6,fp2-1.0-0.2"
python main.py --model hf --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "0,0,0,0,0" --device "cuda" --output_path "models/line-corporation/japanese-large-lm-3.6b/result.json"
# Estimated results: chabsa:0.4331385988479779,cma_basics:0.2894736842105263,cpa_audit:0.17336683417085427,security_sales_1:0.47368421052631576,fp2:0.25263157894736843
