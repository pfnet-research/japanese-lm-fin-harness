MODEL_ARGS="pretrained=cyberagent/open-calm-1b,use_fast=True,load_in_8bit=True"
TASK="chabsa,cma_basics-1.0-0.1.2,cpa-1.0-0.6,security_sales_1-1.0-0.1"
python main.py --model hf --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "4,1,0,0" --device "cuda" --output_path "models/cyberagent/open-calm-1b/result.json"