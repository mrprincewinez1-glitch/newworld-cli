

import textwrap

from newworld_cli import format_brief


def test_format_brief():
    # Arrange: define sample inputs for the brief generator
    business = "Test Business"
    repetitive_task = "Test Task"
    workflow_trigger = "client request"
    desired_outcome = "improved efficiency"

    # CHANGED: expected output is dedented so indentation from this test file doesn't affect comparison
    expected_output = textwrap.dedent(
        """
        Business: Test Business
        Repetitive Task: Test Task
        Workflow Trigger: client request
        Desired Outcome: improved efficiency
        Category: High automation potential
        Automation Hypothesis: when client request, the Test Task will be automated for Test Business to achieve improved efficiency and improve client experience.
        """
    ).strip()

    # CHANGED: normalize the actual output the same way before comparing
    actual_output = textwrap.dedent(
        format_brief(business, repetitive_task, workflow_trigger, desired_outcome)
    ).strip()

    # Assert: verify the generated brief matches the expected content exactly
    assert actual_output == expected_output
