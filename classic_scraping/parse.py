from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
    "5. **answers in the user's language:** reply in the user's language unless explicitly asked to reply in another language"
)

model = OllamaLLM(model="mistral-nemo")


def parse_with_ollama(dom_chunks, parse_description, store_interaction=False):
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model

    parsed_results = []

    with open("store_LLM_interaction.txt", 'w') as file:
        pass # on vide le contenu du fichier

    for i, chunk in enumerate(dom_chunks, start=1):
        response = chain.invoke(
            {"dom_content": chunk, "parse_description": parse_description}
        )

        if store_interaction:
            with open("store_LLM_interaction.txt", "a") as file:
                file.write(f"\nInteraction {i} of {len(dom_chunks)}\n"
                           f"INPUT: chunk, {chunk}\n"
                           f"parse_description, {parse_description}\n"
                           f"OUTPUT: {response}")

        print(f"Parsed batch: {i} of {len(dom_chunks)}")
        parsed_results.append(response)

    return "\n".join(parsed_results)
