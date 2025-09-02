from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_path = "facebook/nllb-200-distilled-600M"

tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSeq2SeqLM.from_pretrained(model_path)

lang_code_to_id = {
    "eng_Latn": tokenizer.convert_tokens_to_ids("__eng_Latn__"),
    "hin_Deva": tokenizer.convert_tokens_to_ids("__hin_Deva__"),
    "mar_Deva": tokenizer.convert_tokens_to_ids("__mar_Deva__"),
}

def translate_text(text, src_lang="hin_Deva", tgt_lang="eng_Latn"):
    tokenizer.src_lang = src_lang
    encoded = tokenizer(text, return_tensors="pt")
    generated_tokens = model.generate(**encoded, forced_bos_token_id=lang_code_to_id[tgt_lang])
    return tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)[0]
