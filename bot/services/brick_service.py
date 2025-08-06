import logging
from bot.services.llm.openai_client import OpenAIClient
from bot.services.llm.fallback import RuleBasedEvaluator

logger = logging.getLogger(__name__)

class BrickService:
    def __init__(self):
        self.openai_client = OpenAIClient()
        self.fallback_evaluator = RuleBasedEvaluator()
    
    async def evaluate_response(self, brick_text: str, user_response: str):
        try:
            return await self.openai_client.evaluate_brick(
                brick_text, user_response
            )
        except Exception as e:
            logger.error(f"Ошибка оценки через OpenAI: {e}")
            return self.fallback_evaluator.evaluate(user_response)