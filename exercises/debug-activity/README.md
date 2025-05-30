# Exercise 3: Debugging and Fixing an Activity Failure

During this exercise, you will

- Start a Worker and run a basic Workflow for processing a pizza order
- Use the Web UI to find details about the execution
- Diagnose and fix a latent bug in the Activity Definition
- Test and deploy the fix
- Verify that the Workflow now completes successfully

Make your changes to the code in the `practice` subdirectory (look for
`TODO` comments that will guide you to where you should make changes to
the code). If you need a hint or want to verify your changes, look at
the complete version in the `solution` subdirectory.

## Prerequisite: Ensure Your Virtual Environment is activated

If you haven't already started the Translation Microservice used by this exercise,
do so in a separate terminal by navigating to `utilities/microservice`
and running `python microservice.py`.

### Activate the Virtual Environment

1. Ensure that the virtual environment you setup at the beginning of the
   course is activated as detailed in the course [README](../../README.md#setup-your-python-virtual-environment)

## Part A: Run the Workflow

In this part of the exercise, you will start two Workers and run the
provided Workflow. We recommend that you do not look at the code yet,
since the next part of this exercise will ask you to determine what it
does by using the Web UI to interpret the Event History.

1. Change to the `exercises/debug-activity/practice` directory
2. Start a Worker by running `python worker.py`
3. In another terminal window, run the above command to start another Worker.
4. In another terminal window, run `python starter.py` to start the Workflow

## Part B: Interpret Workflow Execution by Using the Web UI

Open the Web UI and navigate to the detail page for the Workflow
Execution you just ran, which has the Workflow Type `PizzaWorkflow`
and Workflow ID `pizza-workflow-order-XD001`.

If the detail page still shows a status of Running, wait a few seconds
and refresh the page. Once the page shows a status of Completed, use
what you've learned about the Event History, try to answer the
following questions:

1. Did it use sticky execution for all Workflow Tasks following the
   first one?
   - Hint: It's possible to determine this without expanding any of the
     Events in the Web UI, but you may also check the `WorkflowTaskScheduled` Events for confirmation.
2. What is the Activity Type for the first Activity executed?
3. Which of the 2 Workers started execution of the first Activity?
   - Was it the one running in your first terminal or the second?
   - Did the same Worker complete execution of this Activity?
4. Following execution of the first Activity, which of the following
   happened next?
   - A) Another Activity was executed
   - B) A Timer was started
   - C) Workflow Execution failed due to an error
   - D) Workflow Execution completed successfully
5. What was the duration specified for the Timer used to delay execution?
   - Hint: this is shown as a timeout in the relevant Event
6. Find the Event associated with the Worker completing execution of
   the `get_distance` Activity
   - What is the ID for this Event?
   - What is the ID of the Event logged when this Activity was started
     by the Worker?
   - What is the ID of the Event logged when this Activity was scheduled
     by the Cluster?
7. Can you find the input data supplied as a parameter to the
   `get_distance` Activity?
8. Can you find the output data returned as output from the
   `get_distance` Activity?
9. What was the Maximum Interval value for the Retry Policy used to
   execute the `send_bill` Activity?
10. What was the Start-to-Close Timeout value used when executing
    the `send_bill` Activity?

Take a moment to switch to the Compact view, and if one of the rows in the
table is expanded, click to collapse it. Do you find that this view makes
it easier to see the Activities and Timer that ran during the execution?

Click "Expand All" at the top of this table. Do you find
that this helps you to correlate Events related to the Activities and Timer?

Since the Web UI remembers the current view, be sure to click "Collapse All"
and switch back to the History view before continuing.

## Part C: Finding an Activity Bug

The pizza shop is running a special this month, offering a $5 discount
on all orders over $30. One of your co-workers has already implemented
the business logic for this, although the order for the Workflow you
just ran was only $27, not enough to qualify for the discount.

Note that the code models prices in cents (for example, $27 is represented
as 2700) in order to avoid the problems that occur when a computer program
uses floating point numbers to represent currency.

1. Edit the `shared` file, which creates the input data and starts
   the Workflow
   - Lines 78-79 create and populate dataclass objects (`pizza1` and `pizza2`)
     representing pizzas, which are then added to an array named `pizza_list` used
     in the `PizzaOrder` dataclass used as input to the Workflow.
2. Create and populate another Pizza object, named `pizza3`, representing a third
   pizza added to the order. It should have the following values:
   - Description: "Medium, with extra cheese"
   - Price: 1300
3. Add `pizza3` to the `pizza_list` list
4. Save the changes and close the editor
5. Restart both workers
6. Submit this pizza order by starting the Workflow: `python starter.py`

Although the Workflow _should_ complete within a few seconds, you will
probably find that it never does, so open the Web UI and look at the
detail page for this execution to determine why it hasn't finished.
Do this before continuing with the next part of the exercise.

## Part D: Fixing the Activity Bug

You should have observed that the `send_bill` Activity is failing with an
error that indicates it was supplied with an invalid (negative) charge
amount. Click the **Pending Activities** tab near the top of the screen
to display information about the failure and retries in a more convenient
layout.

1. Run `python -m pytest`. You should observe that all tests pass.
   - Unfortunately, the co-worker who implemented the code to apply a
     discount did not write a test case for it.
     Deploying the untested code is what led to this failure, but
     writing a test now will help you to verify the fix.
2. Open the `test_activities.py` file in the editor
3. Add a new test by copying the existing `test_send_bill_typical_order`
   function and renaming the new function as `test_send_bill_applies_discount`,
   and then make the following changes to it:
   - Change the `description` to `5 large cheese pizzas`
   - Change the `amount` to `6500` ($65)
   - Change the comment next to the `amount` field to say
     `amount qualifies for discount`
   - Change the expected price in the `assert` statement that checks `confirmation.amount`
     to `6000`, which is the $65 amount minus the $5 discount.
4. Save the changes and close the editor
5. Run `python -m pytest`. Since you have not yet fixed the bug, the test will fail.
6. Open the `activities.py` file in the editor and find where the `send_bill`
   Activity is defined.
7. Examine the code where the discount is applied. Once you spot the bug,
   fix it.
8. Save your changes and close the editor

Make sure the bug is fixed before continuing to the next part. Since
you wrote a test case for this, you can verify that it's fixed by
running `python -m pytest` again.

## Part E: Deploying and Verifying the Fix

1. Press Ctrl-C in both terminal windows used to run the Workers.
   Since Workers cache the code, the changes won't take effect until
   they have been restarted. Do not press Ctrl-C in the terminal used
   to start the Workflow.
2. Start both Workers by running `python worker.py` in their respective
   terminals.
3. Click the **History** tab near the top of the detail page in the Web UI
4. Click the toggle button labeled **Auto refresh** near the upper-right
   portion of the screen. This will refresh the page every 15 seconds.
5. The Maximum Interval for the Retry Policy used to execute this Activity
   is set to 10 seconds, so you should observe that the Workflow Execution
   status soon changes from **Running** to **Completed**.

An order processing Workflow is probably more likely to apply a discount
in the Workflow code, rather than in an Activity, since that is typically
not prone to failure and unlikely to affect whether the Workflow executes
in a deterministic manner. This exercise implemented it in the Activity,
since you can deploy a fix to Activity code without a risk of causing a
non-deterministic error. As you learned earlier in this course, there are also ways to safely
deploy changes to Workflow Definitions.

### This is the end of the exercise.
