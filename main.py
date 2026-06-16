

import fitz

def load_policy():

    pdf = fitz.open("policy.pdf")

    text = ""

    for page in pdf:
        text += page.get_text()

    pdf.close()

    return text

def search_policy():

    policy_text = load_policy

    policy_text = policy_text.lower()
    question = question.lower()

    if "casual leave" in question:
        return extract_line(policy_text, "casual leave")

    elif "annual leave" in question:
        return extract_line(policy_text, "annual leave")

    elif "remote work" in question:
        return extract_line(policy_text, "remote work")

    elif "office hours" in question:
        return extract_line(policy_text, "office hours")

    else:
        return None


def ai_agent(question):

    print("\n----- AI AGENT STARTED -----")

    # Goal
    print("Goal: Answer the user's question.")

    # Planning
    print("Planning: Search the company policy file.")

    # Tool Selection
    print("Tool Selected: PDF File Search Tool")

    # Action
    result = search_policy(question)

    # Observation
    print("Observation:", result)

    # Decision
    if result:
        print("Decision: Information found.")
        return result
    else:
        print("Decision: Information not found.")
        return "Sorry, I could not find that information in the company policy."


while True:

    user_question = input("\nYou: ")

    if user_question.lower() == "exit":
        print("\nAgent: Goodbye!")
        break

    answer = ai_agent(user_question)

    print("\nAgent:", answer)
    

