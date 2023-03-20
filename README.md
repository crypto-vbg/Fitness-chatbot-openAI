# Fitness Coach Chatbot
This is a Python chatbot that can help you with your fitness goals. It can suggest personalized exercise routines, diet plans, and provide helpful fitness tips.

## Requirements
To run this chatbot, you will need to have the following installed:

    1. Python 3.6 or higher
    2. Streamlit
    3. OpenAI API key

**To install Streamlit, you can run the following command:**
    `pip install streamlit`

## Running the Chatbot
To run the chatbot, you will need to set your OpenAI API key. You can do this by setting it as a secret in Streamlit. Once you have set your API key, you can run the chatbot by running the following command:

`streamlit run fitness_chatbot.py`
This will start the chatbot in your web browser. You can then interact with the chatbot by clicking on the buttons for exercise routine, diet plan, or fitness tips, and following the prompts. The chatbot will generate a response based on your input and display it in the chat history.

You can view the chat history by scrolling down the page. The chat history includes both the user's input and the chatbot's generated response.

## Notes
    1. The chatbot uses OpenAI's text-davinci-002 model to generate responses, which can take some time to complete. Please be patient while waiting for a response.
    2. The chatbot stores the chat history in the session state, which means that the chat history will be lost if you close the chatbot window. If you want to save the chat history, you can copy and paste it into a text document.
