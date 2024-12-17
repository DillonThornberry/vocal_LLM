import torch
from tts import TTS
from transformers import AutoTokenizer, AutoModelForCausalLM

class LLM:

    def __init__(self):
        # Define the model name
        model_name = "meta-llama/Llama-3.2-3B-Instruct"

        # Load the tokenizer
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)

        # Load the model and move it to GPU
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        print("device:", self.device)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype=torch.float16,  # Use FP16 for GPU efficiency
            device_map="auto"          # Automatically allocate model layers across GPUs
        )

        print("model loaded")

        # Load preprompt.txt and append to prompt
        with open("./preprompts/preprompt.txt", "r") as file:
            self.context = file.read() + "\n"

        print("preprompt loaded into context")


    def generate(self, prompt):
        # Example prompt
        self.context += "<|start_header_id|>user<|end_header_id|>\n"
        self.context += prompt + "<|eot_id|>" + "\n"

        print("Prompt:", prompt) 

        # Tokenize the input and move it to the correct device
        inputs = self.tokenizer(self.context, return_tensors="pt").to(self.device)
        l = inputs['input_ids'].shape[1]
        
        # Generate text
        outputs = self.model.generate(
            **inputs,
            max_new_tokens=100,       # Limit the output length
            temperature=0.7,      # Control randomness in generation
            top_p=0.9,            # Nucleus sampling
            num_return_sequences=1  # Generate one response
        )

        # Decode and print the output
        response = self.tokenizer.decode(outputs[0][l:], skip_special_tokens=True)
        print("Response:")
        print(response)

        self.context += "<|start_header_id|>assistant<|end_header_id|>\n"
        self.context += response + "<|eot_id|>" + "\n"

        return response


def main():
    llm = LLM()
    tts = TTS()

    while True:
        prompt = input("Enter a prompt: ")
        response = llm.generate(prompt)
        tts.say(response)


if __name__ == "__main__":
    main()