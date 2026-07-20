import textwrap


def main():
    business = input("Enter the name of the business: ")
    while not business:
        business = input("Business name cannot be empty. Please enter the name of the business: ")
    repetitive_task = input("Enter the repetitive task to automate: ")
    while not repetitive_task:
        repetitive_task = input("Repetitive task cannot be empty. Please enter the repetitive task to automate: ")
    workflow_trigger = input("What workflow starts the task? ")
    while not workflow_trigger:
        workflow_trigger = input("Workflow trigger cannot be empty. Please enter the workflow that starts the task: ")
    desired_outcome = input("What is the desired outcome of the task? ")
    while not desired_outcome:
        desired_outcome = input("Desired outcome cannot be empty. Please enter the desired outcome of the task: ")
    brief = format_brief(business, repetitive_task, workflow_trigger, desired_outcome)
    print(textwrap.dedent(brief))
    return brief

def format_brief(business, repetitive_task, workflow_trigger, desired_outcome):
    hypothesis = f"when {workflow_trigger}, the {repetitive_task} will be automated for {business} to achieve {desired_outcome}."
    if any(keyword in workflow_trigger for keyword in ["client", "someone", "request", "submit", "approval"]):
        category = "High automation potential"
        hypothesis = f"when {workflow_trigger}, the {repetitive_task} will be automated for {business} to achieve {desired_outcome} and improve client experience."
    elif any(keyword in workflow_trigger for keyword in ["logged", "added", "notified"]):
        category = "Medium automation potential"
    else:
        category = "Low automation potential"
    brief = f"""
    Business: {business}
    Repetitive Task: {repetitive_task}
    Workflow Trigger: {workflow_trigger}
    Desired Outcome: {desired_outcome}
    Category: {category}
    Automation Hypothesis: {hypothesis}
    """
    return brief


if __name__ == "__main__":
    main()