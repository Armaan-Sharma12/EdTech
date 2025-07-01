# logic/adaptive_engine.py

def get_next_difficulty(current_difficulty: str, is_correct: bool) -> str:
    """
    Adjust difficulty based on user's last answer.

    Rules:
    - If correct → move to higher difficulty
    - If incorrect → move to lower difficulty
    """
    difficulty_levels = ['easy', 'medium', 'hard']

    try:
        current_index = difficulty_levels.index(current_difficulty)
    except ValueError:
        return 'easy'  # default fallback

    if is_correct and current_index < len(difficulty_levels) - 1:
        return difficulty_levels[current_index + 1]  # promote
    elif not is_correct and current_index > 0:
        return difficulty_levels[current_index - 1]  # demote
    else:
        return current_difficulty  # stay same


def calculate_score(current_score: int, is_correct: bool, difficulty: str) -> int:
    """
    Returns updated score based on difficulty.
    Higher difficulty = higher reward.
    """
    weight = {
        'easy': 1,
        'medium': 2,
        'hard': 3
    }
    if is_correct:
        return current_score + weight.get(difficulty, 1)
    else:
        return current_score
