from flask import Flask, render_template, request
from translator import translate_text
from rag_chain import retrieve_context, generate_response
from langdetect import detect

app = Flask(__name__)
context = ""

@app.route("/", methods=["GET", "POST"])
def index():
    global context
    user_input = ""
    response = ""

    if request.method == "POST":
        if "clear" in request.form:
            context = ""
            return render_template("index.html", user_input="", response="")

        user_input = request.form["message"]
        lang = request.form.get("language", "en")

        try:
            # Step 1: Translate input to English
            if lang == "hi":
                translated_input = translate_text(user_input.strip(), src_lang="hin_Deva", tgt_lang="eng_Latn")
            elif lang == "mr":
                translated_input = translate_text(user_input.strip(), src_lang="mar_Deva", tgt_lang="eng_Latn")
            else:
                translated_input = user_input

            # Step 2: Get context + AI response
            docs_context, citations = retrieve_context(translated_input)
            raw_response = generate_response(translated_input, docs_context)

            # Step 3: Translate back to original language
            if lang == "hi":
                translated = translate_text(raw_response, src_lang="eng_Latn", tgt_lang="hin_Deva")
                response = translated if translated.strip() else raw_response
            elif lang == "mr":
                translated = translate_text(raw_response, src_lang="eng_Latn", tgt_lang="mar_Deva")
                response = translated if translated.strip() else raw_response
            else:
                response = raw_response

            # Step 4: Add references only if available
            if citations and "unable to answer" not in raw_response.lower():
                response += "\n\n🔖 संदर्भ / References:\n" + "\n".join(f"📄 {ref}" for ref in citations)

            context += f"\nUser: {user_input}\nAI: {response}"

        except Exception as e:
            response = f"⚠️ Error: {e}"

    return render_template("index.html", user_input=user_input, response=response)

if __name__ == "__main__":
    print("🌐 Running at http://127.0.0.1:5000")
    app.run(debug=True)
