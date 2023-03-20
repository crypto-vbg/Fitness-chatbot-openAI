import openai 
import streamlit as st

# pip install streamlit-chat  
from streamlit_chat import message

openai.api_key = st.secrets["api_secret"]

# Define the prompts and responses for the fitness chatbot
prompts = {
    "Exercise routine": "Sure! Please tell me your fitness goals and current fitness level, and I'll suggest a personalized exercise routine for you.",
    "Diet plan": "Of course! What kind of diet plan are you looking for?",
    "Fitness tips": "Absolutely! What kind of fitness tips would you like to know?"
}

responses = {
    "Exercise routine": "Based on your fitness goals and current fitness level, I suggest doing the following exercises...",
    "Diet plan": "For a healthy diet plan, you should consider eating the following foods...",
    "Fitness tips": "Here are some fitness tips that might be helpful for you...",
}

def generate_response(prompt):
    completions = openai.Completion.create(
        engine = "text-davinci-002",
        prompt = prompt,
        max_tokens = 1024,
        n = 1,
        stop = None,
        temperature=0.5,
    )
    message = completions.choices[0].text
    return message 

#Creating the chatbot interface
st.title("Fitness Coach Chatbot")

# Storing the chat
if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

# We will get the user's input by calling the get_text function
def get_text(prompt):
    input_text = st.text_input("You: ", prompts[prompt], key="input")
    return input_text

# Determine the intent of the user's request and generate an appropriate response
if st.button("Exercise routine"):
    user_input = get_text("Exercise routine")
    output = generate_response(user_input)
    st.session_state.past.append(user_input)
    st.session_state.generated.append(responses["Exercise routine"])
elif st.button("Diet plan"):
    user_input = get_text("Diet plan")
    output = generate_response(user_input)
    st.session_state.past.append(user_input)
    st.session_state.generated.append(responses["Diet plan"])
elif st.button("Fitness tips"):
    user_input = get_text("Fitness tips")
    output = generate_response(user_input)
    st.session_state.past.append(user_input)
    st.session_state.generated.append(responses["Fitness tips"])

# Display the chat history and the generated responses
for i in range(len(st.session_state['generated'])-1, -1, -1):
    message(st.session_state["generated"][i], key=str(i))
    message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')

if st.session_state['generated']:
    message(st.session_state['generated'][-1], key='current')