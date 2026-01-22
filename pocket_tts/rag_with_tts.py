from dotenv import load_dotenv
import scipy.io.wavfile

from llama_index.llms.groq import Groq
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings

from pocket_tts import TTSModel


def main() -> None:
    load_dotenv()

    # --- TTS (Pocket-TTS) ---
    tts_model = TTSModel.load_model()  # pyright: ignore[reportAttributeAccessIssue]
    voice_state = tts_model.get_state_for_audio_prompt(
        # Pocket-TTS README uses an HF voice file URL like this. [page:0]
        # "hf://kyutai/tts-voices/alba-mackenna/casual.wav"
        # You can also use:
        "alba" 
        # - "./some_audio.wav" (local wav for voice cloning)
    )

    # --- LlamaIndex setup ---
    llm = Groq(model="moonshotai/kimi-k2-instruct-0905")
    embed = HuggingFaceEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")

    Settings.llm = llm
    Settings.embed_model = embed

    documents = SimpleDirectoryReader("data").load_data()
    index = VectorStoreIndex.from_documents(documents)
    query_engine = index.as_query_engine()

    # --- Ask once, reuse response ---
    resp = query_engine.query("What is the population ?")
    text = resp.response if hasattr(resp, "response") else str(resp) # pyright: ignore[reportAttributeAccessIssue]

    print(text)

    # --- Generate speech from the response text ---
    audio = tts_model.generate_audio(voice_state, text)

    # Audio is a 1D torch tensor containing PCM data. [page:0]
    scipy.io.wavfile.write("output.wav", tts_model.sample_rate, audio.numpy())


if __name__ == "__main__":
    main()
