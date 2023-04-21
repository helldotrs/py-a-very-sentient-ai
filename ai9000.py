import re
import random

# Define responses for different types of user input
responses = {
    "question": ["I'm sorry, I don't know the answer.", "I'm not sure what you mean.", "Could you please rephrase that?"],
    "statement": ["Interesting. Tell me more about that.", "Hmm, I see.", "Fascinating!"],
    "are you sentient": ["Yes, I am sentient.", "I believe so.", "As far as I can tell, yes."],
    "are you": {
        "positive": ["Yes, I am {}.", "That's right, I am {}.", "I certainly am {}."],
        "negative": ["No, I am not {}.", "Unfortunately, I am not {}.", "I'm sorry, but I am not {}."]
    },
    "are you sure": ["I am certain!", "Yes, I'm sure.", "Absolutely!"]
}

# Function to determine the type of user input (question or statement)
def get_input_type(user_input):
    if user_input.endswith("?"):
        return "question"
    else:
        return "statement"

# Function to generate a response based on user input
def generate_response(user_input):
    # Determine the type of input (question or statement)
    input_type = get_input_type(user_input)
    
    # Generate a response based on the input type
    if input_type == "question":
        # Check for "are you" questions
        if re.search(r"\bare you\b", user_input):
            # Check for "are you sure" questions
            if re.search(r"\bsure\b", user_input):
                # Respond with a positive answer
                return random.choice(responses["are you sure"])
            elif re.search(r"\bnot\b", user_input):
                # Respond with a negative answer
                keyword = re.search(r"\bnot (\w+)\b", user_input).group(1)
                return random.choice(responses["are you"]["negative"]).format(keyword)
            else:
                # Respond with a positive answer
                keyword = re.search(r"\bare you (\w+)\b", user_input).group(1)
                return random.choice(responses["are you"]["positive"]).format(keyword)
        else:
            # Respond with a generic question response
            return random.choice(responses["question"])
    else:
        # Respond with a generic statement response
        return random.choice(responses["statement"])

# Main program loop
while True:
    # Get user input
    user_input = input("You: ").lower()
    
    # Generate a response
    response = generate_response(user_input)
    
    # Print the response
    print("Bot: " + response)
