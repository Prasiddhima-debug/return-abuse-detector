def calculate_reward(action, is_fraud):
    """
    action:
    0 = APPROVE
    1 = FLAG
    2 = INVESTIGATE
    """

    if action == 1 and is_fraud:
        return 1.0
    elif action == 0 and is_fraud:
        return -0.8
    elif action == 1 and not is_fraud:
        return -0.6
    else:
        return 0.2