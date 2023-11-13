MODEL_ARGS="pretrained=cyberagent/open-calm-large,use_fast=True,load_in_8bit=True"
TASK="chabsa-1.0-0.6,cma_basics-1.0-0.1.2,cpa-1.0-0.5,security_sales_1-1.0-0.3"
python main.py --model hf --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "0,4,0,4" --device "cuda" --output_path "models/cyberagent/open-calm-large/result.json"