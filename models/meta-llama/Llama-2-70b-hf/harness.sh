MODEL_ARGS="pretrained=meta-llama/Llama-2-70b-hf,load_in_8bit=True"
TASK="chabsa,cma_basics-1.0-0.2.1,cpa_audit,security_sales_1-1.0-0.1.2,fp2-1.0-0.1"
python main.py --model hf --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "0,0,0,0,0" --device "cuda" --output_path "models/meta-llama/Llama-2-70b-hf/result.json"
# Estimated results: chabsa:0.540504500939955,cma_basics:0.47368421052631576,cpa_audit:0.1884422110552764,security_sales_1:0.5614035087719298,fp2:0.32
