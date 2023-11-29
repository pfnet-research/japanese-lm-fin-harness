MODEL_ARGS="pretrained=lmsys/vicuna-7b-v1.5-16k"
TASK="chabsa,cma_basics-1.0-0.1.2,cpa_audit,security_sales_1,fp2-1.0-0.2.1"
python main.py --model hf-causal-experimental --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "0,1,0,1,3" --no_cache --output_path "models/lmsys/vicuna-7b-v1.5-16k/result.json"
# Estimated results: chabsa:0.8478277116584707,cma_basics:0.39473684210526316,cpa_audit:0.19597989949748743,security_sales_1:0.5263157894736842,fp2:0.2905263157894737
