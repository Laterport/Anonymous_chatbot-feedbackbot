# Anonymous chatbot (feedbackbot)

This chatbot allows you to communicate with other users and displays the sender's username and user ID. It also
enables you to reply anonymously on behalf of the bot. This version is based on
an [existing chatbot](https://github.com/coder2020official/feedbackbot), but the original version does not show the
sender's information, only their ID. If you need additional functionality, you can try modifying the chatbot yourself to
meet your requirements. The token is now stored in the .env file instead of config.py.

##### To use the chatbot, follow these simple setup steps:

* Specify your ID in `models\users_model.py`
* Specify your Telegram token in the `.env`
* Install the required packages listed in the `requirements.txt file` file using the command `pip install -r 
  requirements.txt`
