from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_path = "facebook/nllb-200-distilled-600M"

# Allow downloading from internet if model not present
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSeq2SeqLM.from_pretrained(model_path)

# Language code mapping
lang_code_to_id = {
    "eng_Latn": tokenizer.convert_tokens_to_ids("__eng_Latn__"),
    "hin_Deva": tokenizer.convert_tokens_to_ids("__hin_Deva__"),
    "mar_Deva": tokenizer.convert_tokens_to_ids("__mar_Deva__"),
}

def translate_text(text, src_lang="hin_Deva", tgt_lang="eng_Latn"):
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    inputs["forced_bos_token_id"] = lang_code_to_id[tgt_lang]

    outputs = model.generate(
        **inputs,
        max_length=512,
        num_beams=4,
        early_stopping=True
    )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
