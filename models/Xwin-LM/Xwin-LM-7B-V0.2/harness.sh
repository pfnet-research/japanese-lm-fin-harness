MODEL_ARGS="pretrained=Xwin-LM/Xwin-LM-7B-V0.2,use_accelerate=True,device_map_option=auto"
TASK="chabsa,cma_basics-1.0-0.1,cpa_audit-1.0-0.5,security_sales_1-1.0-0.2,fp2-1.0-0.2"
python main.py --model hf-causal-experimental --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "0,0,2,3,2" --no_cache --output_path "models/Xwin-LM/Xwin-LM-7B-V0.2/result.json"
# Estimated results: chabsa:0.8278564128248398,cma_basics:0.42105263157894735,cpa_audit:0.1984924623115578,security_sales_1:0.5087719298245614,fp2:0.2926315789473684
