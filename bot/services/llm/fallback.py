class RuleBasedEvaluator:
    def evaluate(self, user_response: str) -> dict:
        # Простая эвристическая оценка
        word_count = len(user_response.split())
        score = min(word_count, 50)  # максимум 50 баллов
        
        return {
            "total_score": score,
            "feedback": "Оценено по базовым правилам (без ИИ)",
            "metrics": {
                "depth": score // 3,
                "system": score // 3,
                "originality": score // 3
            }
        }