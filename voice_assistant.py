import os
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs.conversational_ai.conversation import Conversation
from elevenlabs.conversational_ai.default_audio_interface import DefaultAudioInterface
from elevenlabs.types import ConversationConfig

# --- Load environment ---
load_dotenv()
AGENT_ID = os.getenv("AGENT_ID")
API_KEY = os.getenv("API_KEY")

# --- User + Context ---
user_name = "hariharan"
schedule = "complete the project you are working on. complete the project before August 30"

prompt = f"You are a helpful assistant. Your interlocutor has the following schedule: {schedule}."
first_message = f"Hello {user_name}, how can I help you today?"

conversation_override = {
    "agent": {
        "prompt": {"prompt": prompt},
        "first_message": first_message,
    },
}

# --- Config with user_id ---
config = ConversationConfig(
    conversation_config_override=conversation_override,
    extra_body={},
    dynamic_variables={},
    user_id="hariharan",  # <-- Added here
)

# --- Client + Conversation ---
client = ElevenLabs(api_key=API_KEY)

def print_agent_response(response):
    print(f"Agent: {response}")

def print_interrupted_response(original, corrected):
    print(f"Agent interrupted, truncated response: {corrected}")

def print_user_transcript(transcript):
    print(f"User: {transcript}")

conversation = Conversation(
    client,
    AGENT_ID,
    config=config,
    requires_auth=True,
    audio_interface=DefaultAudioInterface(),
    callback_agent_response=print_agent_response,
    callback_agent_response_correction=print_interrupted_response,
    callback_user_transcript=print_user_transcript,
)

# --- Run session ---
conversation.start_session()
