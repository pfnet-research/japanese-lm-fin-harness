MODEL_ARGS="pretrained=cyberagent/calm2-7b-chat,use_fast=True,load_in_8bit=True"
TASK="chabsa-1.0-0.2,cma_basics-1.0-0.1,cpa-1.0-0.2,security_sales_1-1.0-0.3"
python main.py --model hf --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "4,4,4,3" --device "cuda" --output_path "models/cyberagent/calm2-7b-chat/result.json"