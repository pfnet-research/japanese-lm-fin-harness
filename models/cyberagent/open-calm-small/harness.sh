MODEL_ARGS="pretrained=cyberagent/open-calm-small,use_fast=True"
TASK="chabsa-1.0-0.1,cma_basics-1.0-0.3,cpa_audit-1.0-0.1.2,security_sales_1-1.0-0.1.2,fp2-1.0-0.2.1"
python main.py --model hf-causal-experimental --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "0,3,2,2,2" --no_cache --output_path "models/cyberagent/open-calm-small/result.json"
# Estimated results: chabsa:0.5028373177536112,cma_basics:0.34210526315789475,cpa_audit:0.19095477386934673,security_sales_1:0.49122807017543857,fp2:0.27578947368421053
