def get_header() -> dict:
    import random

    from data_stars.settings import USER_AGENT

    random_idx = random.randint(0, len(USER_AGENT) - 1)
    user_agent = {'user-agent': USER_AGENT[random_idx]}
    return user_agent
