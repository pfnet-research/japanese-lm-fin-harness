MODEL_ARGS="pretrained=Xwin-LM/Xwin-LM-13B-V0.2,use_accelerate=True,device_map_option=auto"
TASK="chabsa-1.0-0.1,cma_basics,cpa_audit-1.0-0.1.2,security_sales_1-1.0-0.2,fp2-1.0-0.2"
python main.py --model hf-causal-experimental --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "4,1,2,3,2" --no_cache --output_path "models/Xwin-LM/Xwin-LM-13B-V0.2/result.json"
# Estimated results: chabsa:0.8810678047800047,cma_basics:0.5263157894736842,cpa_audit:0.22110552763819097,security_sales_1:0.5263157894736842,fp2:0.30736842105263157
