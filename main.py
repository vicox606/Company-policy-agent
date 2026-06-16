company_policy = {
    "casual leave": "Employees receive 12 casual leaves annually.",
    "annual leave": "Employees receive 20 annual leaves annually.",
    "remote work": "Employees are allowed to work remotely 3 days per week.",
    "office hours": "Office working hours are 9:00 AM to 6:00 PM."
}

def search_policy(questions):
    questions = questions.lower()

    for topic in company_policy:
        if topic in question:
            return company_policy[topic]

        return None

def ai_agent(question):

    # Goal
    print("Goal: Answer the user's question.")

    # Planning
    print("Planning: Search the company policy database.")

    # Tool Selection
    print("Tool Selected: Policy Search Tool")

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

    user_question = input("\n you : ")

    if user_question.lower() == "exit":
        print("GoodBye")
        break

    answer = ai_agent(user_question)
    print("\nAgent:", answer)

def load_policy():
    with open("policy.txt","r") as file:
        data = file.read()

        return data

        
    
