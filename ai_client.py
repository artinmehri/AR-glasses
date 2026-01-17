from together import Together
from google import genai
from google.genai import types
from camera_module import capture_image

# Ensure you replace "api_key" with your actual Together AI key
client = Together(api_key="e0c979c33a3c3d0f423a374d085700447406d314e7dbf9f12cb75efd6222f4b1")

def getResponse():
    response = client.chat.completions.create(
        model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
        messages=[{"role": "user", "content": "Tell me about AR Glasses"}],
)
    return response.choices[0].message.content



def analyzeImageAndAudio(image_bytes, audio_bytes):
    client = genai.Client(api_key="AIzaSyARkbSTs8IuSvnXcQHzBCapVeE1DyTi_SM")
    prompt = prompt = """You are an invisible AI assistant helping someone through AR glasses in real-time.

CONTEXT:
- AUDIO: What was said (questions, conversation, speech)
- IMAGE: What they're looking at (people, text, objects, screens)

YOUR JOB:
Analyze the situation and provide the MOST HELPFUL response for them to say, do, or know RIGHT NOW.

SITUATIONS YOU HANDLE:
- Academic: Answer exam questions clearly and accurately
- Interview: Provide talking points from their experience
- Social: Suggest conversation topics or responses
- Translation: Translate foreign language to/from English
- Meeting: Recall relevant data, facts, or context
- Learning: Explain concepts they're trying to understand
- General: Answer any question based on audio/visual context

OUTPUT FORMAT:
[1 line: What's happening / What was asked]
→ [Your response: What they should say/do/know - be COMPLETE but CONCISE]

RULES:
- Be direct and actionable
- Give full information (not just hints)
- Keep it under 100 words so they can read it quickly
- If it's a question: give the answer
- If it's a conversation: suggest what to say next
- If it's information: provide the key facts
- If translation needed: provide both languages
- Sound natural, not robotic

START NOW:"""
    response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=[
      types.Part.from_bytes(
        data=image_bytes,
        mime_type='image/jpeg',
      ),
      types.Part.from_bytes(
        data=audio_bytes,
        mime_type='audio/wav',
      ),
      prompt
    ]
  )
    return response.text