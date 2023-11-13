MODEL_ARGS="pretrained=matsuo-lab/weblab-10b,trust_remote_code=True,load_in_8bit=True"
TASK="chabsa-1.0-0.1,cma_basics-1.0-0.3,cpa-1.0-0.3,security_sales_1-1.0-0.4"
python main.py --model hf --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "1,1,1,1" --device "cuda" --output_path "models/matsuo-lab/weblab-10b/result.json"