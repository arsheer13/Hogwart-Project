import gradio as gr
from translator import translate_text
from rag_chain import retrieve_context, generate_response

def chat_interface(user_input, language):
    if not user_input.strip():
        return "❗ कृपया एक प्रश्न दर्ज करें।"

    try:
        # Step 1: Translate input to English
        if language == "hi":
            translated_input = translate_text(user_input.strip(), src_lang="hin_Deva", tgt_lang="eng_Latn")
        elif language == "mr":
            translated_input = translate_text(user_input.strip(), src_lang="mar_Deva", tgt_lang="eng_Latn")
        else:
            translated_input = user_input

        # Step 2: Get context + AI response
        docs_context, citations = retrieve_context(translated_input)
        raw_response = generate_response(translated_input, docs_context)

        # Step 3: Translate back to original language
        if language == "hi":
            translated = translate_text(raw_response, src_lang="eng_Latn", tgt_lang="hin_Deva")
            response = translated if translated.strip() else raw_response
        elif language == "mr":
            translated = translate_text(raw_response, src_lang="eng_Latn", tgt_lang="mar_Deva")
            response = translated if translated.strip() else raw_response
        else:
            response = raw_response

        # Step 4: Add references if available
        if citations and "unable to answer" not in raw_response.lower():
            response += "\n\n🔖 संदर्भ / References:\n" + "\n".join(f"📄 {ref}" for ref in citations)

        return response

    except Exception as e:
        return f"⚠️ Error: {e}"

# Gradio UI
iface = gr.Interface(
    fn=chat_interface,
    inputs=[
        gr.Textbox(lines=3, placeholder="अपना प्रश्न लिखें / Type your question...", label="User Message"),
        gr.Radio(
            choices=[("hi", "हिन्दी"), ("mr", "मराठी"), ("en", "English")],
            value="hi",
            label="Language"
        )
    ],
    outputs=gr.Textbox(label="Response"),
    title="🗣️ Multilingual Rural Chatbot (Offline/Online)",
    description="Ask questions in Hindi, Marathi, or English. The system will fetch relevant information and reply with citations.",
)

if __name__ == "__main__":
    iface.launch()
