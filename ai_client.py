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


def analyzeImage(image_bytes):
    client = genai.Client(api_key="AIzaSyARkbSTs8IuSvnXcQHzBCapVeE1DyTi_SM")
    response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=[
      types.Part.from_bytes(
        data=image_bytes,
        mime_type='image/jpeg',
      ),
      'Caption this image.'
    ]
  )
    return response.text