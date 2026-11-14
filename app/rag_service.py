def retrieve_context(question):
    with open("data/knowledge.txt", "r", encoding="utf-8") as file:
        return file.read()


def generate_answer(question):
    context = retrieve_context(question)

    return {
        "context": context,
        "answer": f"FastAPI response for: {question}"
    }