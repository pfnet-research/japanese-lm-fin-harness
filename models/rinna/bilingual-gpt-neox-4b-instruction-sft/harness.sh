MODEL_ARGS="pretrained=rinna/bilingual-gpt-neox-4b-instruction-sft"
TASK="chabsa-1.0-0.2,cma_basics-1.0-0.4,cpa_audit-1.0-0.1.2,security_sales_1-1.0-0.3,fp2-1.0-0.1"
python main.py --model hf-causal-experimental --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "1,2,2,1,2" --no_cache --output_path "models/rinna/bilingual-gpt-neox-4b-instruction-sft/result.json"
# Estimated results: chabsa:0.7827312888727447,cma_basics:0.34210526315789475,cpa_audit:0.19095477386934673,security_sales_1:0.49122807017543857,fp2:0.28210526315789475
