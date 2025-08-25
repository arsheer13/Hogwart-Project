from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_path = "facebook/nllb-200-distilled-600M"
AutoTokenizer.from_pretrained(model_path)
AutoModelForSeq2SeqLM.from_pretrained(model_path)

print("✅ NLLB model downloaded and cached for offline use.")
