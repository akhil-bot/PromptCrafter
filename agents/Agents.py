from termcolor import colored
from models.openai_models import get_open_ai, get_open_ai_json
from models.ollama_models import OllamaModel, OllamaJSONModel
from models.vllm_models import VllmJSONModel, VllmModel
from models.groq_models import GroqModel, GroqJSONModel
from models.claude_models import ClaudModel, ClaudJSONModel
from models.gemini_models import GeminiModel, GeminiJSONModel
from states.state import AgentGraphState
from prompts.prompts import Prompts
prompts = Prompts()

class Agent:
    def __init__(self, state: AgentGraphState, model=None, server=None, temperature=0, model_endpoint=None, stop=None,
                 guided_json=None):
        self.state = state
        self.model = model
        self.server = server
        self.temperature = temperature
        self.model_endpoint = model_endpoint
        self.stop = stop
        self.guided_json = guided_json

    def get_llm(self, json_model=True):
        if self.server == 'openai':
            return get_open_ai_json(model=self.model, temperature=self.temperature) if json_model else get_open_ai(
                model=self.model, temperature=self.temperature)
        if self.server == 'ollama':
            return OllamaJSONModel(model=self.model, temperature=self.temperature) if json_model else OllamaModel(
                model=self.model, temperature=self.temperature)
        if self.server == 'vllm':
            return VllmJSONModel(
                model=self.model,
                guided_json=self.guided_json,
                stop=self.stop,
                model_endpoint=self.model_endpoint,
                temperature=self.temperature
            ) if json_model else VllmModel(
                model=self.model,
                model_endpoint=self.model_endpoint,
                stop=self.stop,
                temperature=self.temperature
            )
        if self.server == 'groq':
            return GroqJSONModel(
                model=self.model,
                temperature=self.temperature
            ) if json_model else GroqModel(
                model=self.model,
                temperature=self.temperature
            )
        if self.server == 'claude':
            return ClaudJSONModel(
                model=self.model,
                temperature=self.temperature
            ) if json_model else ClaudModel(
                model=self.model,
                temperature=self.temperature
            )
        if self.server == 'gemini':
            return GeminiJSONModel(
                model=self.model,
                temperature=self.temperature
            ) if json_model else GeminiModel(
                model=self.model,
                temperature=self.temperature
            )

    def update_state(self, key, value):
        self.state = {**self.state, key: value}

class PromptWriterAgent(Agent):
    def invoke(self, task, prompt="", feedback=None):

        prompt_writer_prompt = prompts.prompt_writer_prompt.format(
            )

        messages = [
            {"role": "system", "content": prompt_writer_prompt},
            {"role": "user", "content": f"Task, Goal, or Current Prompt:\n{task}"}
        ]

        llm = self.get_llm(json_model=False)
        ai_msg = llm.invoke(messages)
        response = ai_msg.content

        self.update_state("prompt_writer_response", response)
        print(colored(f"PromptWriter 👩🏿‍💻: {response}", 'cyan'))
        return self.state
    

class PromptReviewerAgent(Agent):
    def invoke(self, task="", prompt_writer_response="", prompt="", feedback=None):
        print(f"Task: {task}")
        print(f"PromptWriterResponse: {prompt_writer_response}")
        print(f"Prompt: {prompt}")
        prompt_reviewer_prompt = prompts.prompt_reviewer_prompt.replace("{task}", task).replace("{promptGenerated}", prompt_writer_response[0].content)

        messages = [
            {"role": "system", "content": prompt_reviewer_prompt},
        ]

        llm = self.get_llm(json_model=False)
        ai_msg = llm.invoke(messages)
        response = ai_msg.content

        self.update_state("prompt_reviewer_response", response)
        print(colored(f"PromptReviewer 👩🏿‍💻: {response}", 'cyan'))
        return self.state

class EndNodeAgent(Agent):
    def invoke(self):
        self.update_state("end_chain", "end_chain")
        return self.state
    
