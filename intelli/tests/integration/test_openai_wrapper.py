import unittest
from wrappers.openai_wrapper import OpenAIWrapper
import os
import base64
from io import BytesIO
from dotenv import load_dotenv
load_dotenv()

class TestOpenAIWrapper(unittest.TestCase):

    def setUp(self):
        self.api_key = os.getenv('OPENAI_API_KEY')
        self.openai = OpenAIWrapper(self.api_key)
    """
    def test_generate_chat_text(self):
        params = {
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "system", "content": "You are a helpful assistant."}]
        }
        
        result = self.openai.generate_chat_text(params)
        print('ChatGPT Result:\n', result, '\n')
        # assert
        self.assertTrue("choices" in result)
    
    def test_generate_images(self):
        params = {
            "prompt": "teddy writing a blog in times square",
            "n": 1,
            "size": "1024x1024",
            "quality": "standard",
            "model": "dall-e-3"
        }
        
        result = self.openai.generate_images(params)
        print('Image Model Result:\n', result['data'][0]['url'], '\n')
        self.assertTrue("data" in result)
    
    def test_get_embeddings(self):
        params = {
            "input": "IntelliNode provide lightning-fast access to the latest deep learning models",
            "model": "text-embedding-3-small",
        }
        result = self.openai.get_embeddings(params)
        print('Embeddings Sample Result:\n', result['data'][0]['embedding'][:3], '\n')
        self.assertTrue("data" in result)

    def test_list_fine_tuning_data(self):
        result = self.openai.list_fine_tuning_data()
        print('List Fine Tuning Count:\n', len(result['data']), '\n')
        self.assertTrue(isinstance(result, dict))
    

    def test_upload_file(self):
        # Make sure the file path is correct and accessible from the test execution context
        file_path = '../temp/training_data.jsonl'
        purpose = "fine-tune"  # Purpose as defined in the call and ensuring param use matches method signature

        result = self.openai.upload_file(file_path, purpose)
        print('Upload File Result:\n', result, '\n')
        self.assertTrue("id" in result)
    """
    def test_vision_image_to_text(self):

        file_path = '../temp/test_image_desc.png'
        
        with open(file_path, "rb") as image_file:
            image_data = base64.b64encode(image_file.read()).decode('utf-8')

        params = {
            "model": "gpt-4-vision-preview",
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "What's in this image?"
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/png;base64,{image_data}"
                            }
                        }
                    ]
                }
            ],
            "max_tokens": 300
        }

        result = self.openai.image_to_text(params)
        value = result['choices'][0]['message']['content']

        print('Vision Sample Result:\n', value[:50], '\n')

        self.assertTrue(len(value) > 0)

if __name__ == "__main__":
    unittest.main()