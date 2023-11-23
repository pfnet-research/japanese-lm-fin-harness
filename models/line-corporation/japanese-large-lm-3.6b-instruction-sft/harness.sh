MODEL_ARGS="pretrained=line-corporation/japanese-large-lm-3.6b-instruction-sft,trust_remote_code=True,load_in_8bit=True"
TASK="chabsa,cma_basics-1.0-0.4,cpa_audit-1.0-0.1,security_sales_1-1.0-0.5,fp2"
python main.py --model hf --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "0,0,0,0,0" --device "cuda" --output_path "models/abeja/abeja-gpt-neox-japanese-2.7b/result.json"
# Estimated results: chabsa:0.38328305599425344,cma_basics:0.2894736842105263,cpa_audit:0.17839195979899497,security_sales_1:0.47368421052631576,fp2:0.2968421052631579
