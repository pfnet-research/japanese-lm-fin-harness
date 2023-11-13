MODEL_ARGS="pretrained=cyberagent/open-calm-3b,use_fast=True,load_in_8bit=True"
TASK="chabsa-1.0-0.1,cma_basics-1.0-0.5,cpa-1.0-0.4,security_sales_1-1.0-0.2.1"
python main.py --model hf --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "4,3,2,3" --device "cuda" --output_path "models/cyberagent/open-calm-3b/result.json"