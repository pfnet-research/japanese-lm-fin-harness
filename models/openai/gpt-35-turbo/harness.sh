TASK="chabsa,cma_basics,cpa_audit,security_sales_1,fp2"
python open_ai.py --model gpt-35-turbo --tasks $TASK --num_fewshot 0 --output_path "models/openai/gpt-35-turbo/result.json"
# azure 2023-03-15-preview 