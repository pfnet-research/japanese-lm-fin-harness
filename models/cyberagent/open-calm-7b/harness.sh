MODEL_ARGS="pretrained=cyberagent/open-calm-7b,use_fast=True"
TASK="chabsa,cma_basics,cpa_audit-1.0-0.2,security_sales_1-1.0-0.2.1,fp2-1.0-0.3"
python main.py --model hf-causal-experimental --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "1,2,2,3,2" --no_cache --output_path "models/cyberagent/open-calm-7b/result.json"
# Estimated results: chabsa:0.6289289231057371,cma_basics:0.34210526315789475,cpa_audit:0.20100502512562815,security_sales_1:0.5263157894736842,fp2:0.2736842105263158
