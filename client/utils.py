from g4f.client import Client


def process_query(query):
    client = Client()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Hello"}],
    )
    return response.to_json()
