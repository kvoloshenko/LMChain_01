import openai

def marketing_text(user_input, temp=0.9):
    openai.api_type = "open_ai"
    openai.api_base = "http://localhost:1234/v1"
    openai.api_key = "no need anymore"

    system_content = """
    Ты старательный помощник.
    """

    messages = [
        {"role": "system", "content": system_content},
        {"role": "user", "content": user_input}
    ]


    completion = openai.ChatCompletion.create(
        model='no need anymore',
        messages=messages,
        temperature=temp
    )


    answer = completion.choices[0].message.content
    print(answer)  # query result
    return answer

if __name__ == '__main__':
    topic ="инновационная экологически чистая кофейная чашка"
    ans = marketing_text(topic)
    print(ans)