MODEL_ARGS="pretrained=rinna/japanese-gpt-neox-3.6b-instruction-sft-v2,load_in_8bit=True"
TASK="chabsa-1.0-0.2,cma_basics-1.0-0.2.1,cpa_audit-1.0-0.2,security_sales_1-1.0-0.4,fp2-1.0-0.2.1"
python main.py --model hf --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "0,0,0,0,0" --device "cuda" --output_path "models/rinna/japanese-gpt-neox-3.6b-instruction-sft-v2/result.json"
# Estimated results: chabsa:0.5021521943414035,cma_basics:0.3157894736842105,cpa_audit:0.1934673366834171,security_sales_1:0.49122807017543857,fp2:0.28210526315789475
