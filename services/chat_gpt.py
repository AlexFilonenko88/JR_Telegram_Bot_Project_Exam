from openai import AsyncOpenAI, BadRequestError


class ChatGptService:
    def __init__(self, api_key: str):
        self.client = AsyncOpenAI(api_key=api_key)

    async def ask(self, user_text: str, role_text: str):
        response = await self.client.chat.completions.create(
            model = 'gpt-4o-mini',
            messages=[
                {
                    'role':'system',
                    'content': role_text,
                },
                {
                    'role': 'user',
                    'content': user_text,
                },
            ],
            max_tokens = 700,
            temperature = 0.4,
        )
        answer = response.choices[0].message.content

        return answer


    async def generate_image(self, prompt: str):
        try:
            response = await self.client.images.generate(
                model="gpt-image-1",
                prompt=prompt,
                size="1024x1024"
            )

            return response.data[0].b64_json

        except BadRequestError as e:
            if 'billing' in str(e):
                print(f"Ошибка при генерации изображения: {e}")
                return None
            raise