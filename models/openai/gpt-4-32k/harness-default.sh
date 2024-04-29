TASK="chabsa,cma_basics,cpa_audit,security_sales_1,fp2"
python open_ai.py --model gpt-4-32k --tasks $TASK --num_fewshot 0 --output_path "models/openai/gpt-4-32k/result.json"
# azure 0613: Data up to Sep 2021