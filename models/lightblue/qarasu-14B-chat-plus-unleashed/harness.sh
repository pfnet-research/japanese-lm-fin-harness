MODEL_ARGS="pretrained=lightblue/qarasu-14B-chat-plus-unleashed,trust_remote_code=True"
TASK="chabsa-1.0-0.1,cma_basics-1.0-0.1.2,cpa_audit-1.0-0.3,security_sales_1-1.0-0.2.1,fp2-1.0-0.1.2"
python main.py --model hf-causal-experimental --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "4,3,0,2,4" --no_cache --output_path "models/lightblue/qarasu-14B-chat-plus-unleashed/result.json"
# Estimated results: chabsa:0.896868503735033,cma_basics:0.5789473684210527,cpa_audit:0.20351758793969849,security_sales_1:0.631578947368421,fp2:0.3157894736842105
