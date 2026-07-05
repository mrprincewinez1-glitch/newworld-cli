import textwrap


def main():
    business = input("Enter the name of the business: ")
    repetitive_task = input("Enter the repetitive task to automate: ")
    workflow_trigger = input("What workflow starts the task? ")
    desired_outcome = input("What is the desired outcome of the task? ")
    brief = format_brief(business, repetitive_task, workflow_trigger, desired_outcome)
    print(textwrap.dedent(brief))
    return brief

def format_brief(business, repetitive_task, workflow_trigger, desired_outcome):
    hypothesis = f" when {workflow_trigger}, the {repetitive_task} will be automated for {business} to achieve {desired_outcome}."
    brief = f"""
    Business: {business}
    Repetitive Task: {repetitive_task}
    Workflow Trigger: {workflow_trigger}
    Desired Outcome: {desired_outcome}
    Automation Hypothesis: {hypothesis}
    """
    return brief


if __name__ == "__main__":
    main()