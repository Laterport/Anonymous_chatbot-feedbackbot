from telebot import logger

def extract_id(text: str):
    """
    Extracts the username and ID from a string.
    """
    try:
        # Split the text by space and extract the username and ID
        username, user_id = text.split()[1][1:], text.split()[2][1:-1]
        # Convert the ID to an integer
        user_id = int(user_id)
    except (ValueError, IndexError) as e:
        # If there was an error, log it and return None
        logger.error(e)
        return None, None
    return username, user_id


