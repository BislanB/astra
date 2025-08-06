import openai
import json
from core.config import settings

class OpenAIClient:
    async def evaluate_brick(self, brick_text: str, user_response: str) -> dict:
        prompt = f"""
        Ты эксперт конкурса «Большая Перемена». Оцени ответ участника по критериям:
        1. Глубина анализа (0-20 баллов)
        2. Системность изложения (0-20 баллов)
        3. Оригинальность выводов (0-10 баллов)
        
        Текст для анализа:
        {brick_text}
        
        Ответ участника:
        {user_response}
        
        Верни JSON с полями:
        - total_score (общий балл 0-50)
        - feedback (развернутый комментарий)
        - metrics (словарь с баллами по каждому критерию)
        """
        
        response = await openai.AsyncClient(api_key=settings.OPENAI_API_KEY).chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )
        
        return json.loads(response.choices[0].message.content)
