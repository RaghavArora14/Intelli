# Intelli
<p>
<a href="https://github.com/intelligentnode/Intelli/blob/release-documentation/LICENSE" alt="licenses tag">
    <img src="https://img.shields.io/github/license/intelligentnode/Intelli?style=flat-square" />
</a>

<a href="https://discord.gg/VYgCh2p3Ww" alt="Join our Discord community">
    <img src="https://img.shields.io/badge/Discord-join%20us-5865F2?style=flat-square&logo=discord&logoColor=white" />
</a>

</p>

A framework for creating chatbots and AI agent workflows. It enables seamless integration with multiple AI models, including OpenAI, LLaMA, deepseek, Stable Diffusion, and Mistral, through a unified access layer.


```bash
pip install intelli
```

# Latest changes
- Support llama.cpp & GGUF models for fast inference.
- Add deepseek and Llama3 integration [doc](https://docs.intellinode.ai/docs/python/chatbot/nvidia-chat).
- Add offline speech2text Whisper [doc](https://docs.intellinode.ai/docs/python/offline-chatbot/whisper).
- Add Anthropic claude 3.5 as a chatbot provider.
- Add KerasAgent to load open source models offline.

For detailed instructions, refer to [intelli documentation](https://docs.intellinode.ai/docs/python).

# Code Examples

## Create Chatbot
Switch between multiple chatbot providers without changing your code.

```python
from intelli.function.chatbot import Chatbot
from intelli.model.input.chatbot_input import ChatModelInput

def call_chatbot(provider, model=None, api_key='YOUR_API_KEY'):
    # prepare common input 
    input = ChatModelInput("You are a helpful assistant.", model)
    input.add_user_message("What is the capital of France?")

    # creating chatbot instance
    openai_bot = Chatbot(api_key, provider)
    response = openai_bot.chat(input)

    return response

# call openai
call_chatbot("openai", "gpt-4")

# call mistralai
call_chatbot("mistral", "mistral-medium")

# call claude3
call_chatbot(ChatProvider.ANTHROPIC, "claude-3-sonnet-20240229")

# Call NVIDIA Deepseek.
call_chatbot(ChatProvider.NVIDIA, "deepseek-ai/deepseek-r1")

# call google gemini
call_chatbot("gemini")
```

## Chat With Docs
Chat with your docs using multiple LLMs. To connect your data, visit the [IntelliNode App](https://app.intellinode.ai/), start a project using the Document option, upload your documents or images, and copy the generated One Key. This key will be used to connect the chatbot to your uploaded data.

```python
# creating chatbot with the intellinode one key
bot = Chatbot(YOUR_OPENAI_API_KEY, "openai", {"one_key": YOUR_ONE_KEY})

input = ChatModelInput("You are a helpful assistant.", "gpt-3.5-turbo")
input.add_user_message("What is the procedure for requesting a refund according to the user manual?")

response = bot.chat(input)
```

## Generate Images
Use the image controller to generate arts from multiple models with minimum code change:
```python
from intelli.controller.remote_image_model import RemoteImageModel
from intelli.model.input.image_input import ImageModelInput

# model details - change only two words to switch
provider = "openai"
model_name = "dall-e-3"

# prepare the input details
prompts = "cartoonishly-styled solitary snake logo, looping elegantly to form both the body of the python and an abstract play on data nodes."
image_input = ImageModelInput(prompt=prompt, width=1024, height=1024, model=model_name)

# call the model openai/stability
wrapper = RemoteImageModel(your_api_key, provider)
results = wrapper.generate_images(image_input)
```

## Create AI Flows
You can create a flow of tasks executed by different AI models. Here's an example of creating a blog post flow:
- ChatGPT agent to write a post.
- Google gemini agent to write image description.
- Stable diffusion to generate images.

```python
from intelli.flow.agents.agent import Agent
from intelli.flow.tasks.task import Task
from intelli.flow.sequence_flow import SequenceFlow
from intelli.flow.input.task_input import TextTaskInput
from intelli.flow.processors.basic_processor import TextProcessor

# define agents
blog_agent = Agent(agent_type='text', provider='openai', mission='write blog posts', model_params={'key': YOUR_OPENAI_API_KEY, 'model': 'gpt-4'})
copy_agent = Agent(agent_type='text', provider='gemini', mission='generate description', model_params={'key': YOUR_GEMINI_API_KEY, 'model': 'gemini'})
artist_agent = Agent(agent_type='image', provider='stability', mission='generate image', model_params={'key': YOUR_STABILITY_API_KEY})

# define tasks
task1 = Task(TextTaskInput('blog post about electric cars'), blog_agent, log=True)
task2 = Task(TextTaskInput('Generate short image description for image model'), copy_agent, pre_process=TextProcessor.text_head, log=True)
task3 = Task(TextTaskInput('Generate cartoon style image'), artist_agent, log=True)

# start sequence flow
flow = SequenceFlow([task1, task2, task3], log=True)
final_result = flow.start()
```

To build async AI flows with multiple paths, refer to the [flow tutorial](https://doc.intellinode.ai/docs/python/flows/async-flow).

# Pillars
- **The wrapper layer** provides low-level access to the latest AI models.
- **The controller layer** offers a unified input to any AI model by handling the differences.
- **The function layer** provides abstract functionality that extends based on the app's use cases. 
- **Flows**: create a flow of ai agents working toward user tasks.
