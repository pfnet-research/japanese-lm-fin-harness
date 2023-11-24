MODEL_ARGS="pretrained=cyberagent/calm2-7b-chat,use_fast=True,load_in_8bit=True"
TASK="chabsa-1.0-0.2,cma_basics-1.0-0.1.2,cpa_audit,security_sales_1-1.0-0.1.2,fp2-1.0-0.2.1"
python main.py --model hf --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "0,0,0,0,0" --device "cuda" --output_path "models/cyberagent/calm2-7b-chat/result.json"
# Estimated results: chabsa:0.528650869198983,cma_basics:0.2631578947368421,cpa_audit:0.1708542713567839,security_sales_1:0.49122807017543857,fp2:0.27578947368421053
