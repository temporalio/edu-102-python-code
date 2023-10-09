# Exercise 3: Testing the Translation Workflow
During this exercise, you will

* Run a unit test provided for the `translate_term` Activity
* Develop and run your own unit test for the `translate_term` Activity
* Write assertions for a Workflow test 
* Uncover, diagnose, and fix a bug in the Workflow Definition
* Observe the time-skipping feature in the Workflow test environment

Make your changes to the code in the `practice` subdirectory (look for 
`TODO` comments that will guide you to where you should make changes to 
the code). If you need a hint or want to verify your changes, look at 
the complete version in the `solution` subdirectory.

## Prerequisite: Ensure the Microservice is running and your Virtual Environment is activated
If you haven't already started the Translation Microservice used by this exercise, 
do so in a separate terminal.

**Note: If you're using the Gitpod environment to run this exercise you can
skip this step. An instance of the Microservice is already running in your
environment**

### Activate the Virtual Environment
1. Ensure that the virtual environment you setup at the beginning of the
course is activated as detailed in the course [README](../../README.md#setup-your-python-virtual-environment)

### Start the Microservice
1. Navigate to the `utilities` directory at the root level of the course
2. Change directories into the `microservice` directory
   1. `cd utilities/microservice`
3. Run the microservice
   1. `python microservice.py`

## Part A: Running a Test

We have provided a unit test for the `translate_term` Activity
to get you started. This test verifies that the Activity correctly 
translates the term "Hello" to German. Take a moment to study the 
test, which you'll find in the `test_activities.py` file in the `tests` directory.
Since the test runs the Activity, which in turn calls the microservice to do 
the translation, you'll begin by starting that.
 
1. Run the `python -m pytest` command to execute the provided test

## Part B: Add another test case for the Activity

In the previous step you verified that running `translate_term` for Hello was
invoking properly. Now it is time to test if Goodbye is also working. 

1. Edit the `test_activities.py` file
2. Copy the tuple in the `pytest.mark.parametrize` list and paste it into the 
    list, effectively creating a second entry to test the method on.
3. Change the term for the `TranslationActivityInput` object in this second 
    tuple from `Hello` to `Goodbye` 
4. Change the language code for the `TranslationActivityInput` object in this 
    second tuple from `de` (German) to `lv` (Latvian)
5. Change the translation for the `TranslationActivityOutput` object in this second
    tuple from `Hallo` to `Ardievu`
6. Run the `python -m pytest` command to verify that the method was tested twice
    and that the test completed successfully.

## Part C: Test the Activity with Invalid Input

In addition to verifying that your code behaves correctly when used as 
you intended, it is sometimes also helpful to verify its behavior with 
unexpected input. The example below does this, testing that the Activity 
returns the appropriate error when called with an invalid language code. 

```python
@pytest.mark.asyncio
async def test_failed_translate_activity_bad_language_code():
    with pytest.raises(Exception) as e:
        input = TranslationActivityInput("goodbye", "xq")
        async with aiohttp.ClientSession() as session:
            activity_environment = ActivityEnvironment()
            activities = TranslationActivities(session)
            await activity_environment.run(activities.translate_term, input)
    assert "Invalid language code" in str(e)
```

Take a moment to study this code, and then continue with the 
following steps:

1. Edit the `test_activities.py` file
2. Copy the entire `test_failed_translate_acivity_bad_language_code` function
   provided above and paste it at the bottom of the `test_activities.py` file 
4. Save the changes
5. Run `python -m pytest` again to run this new test, in addition to the others


## Part D: Test a Workflow Definition

1. Edit the `test_workflow.py` file
4. Add assertions for the following conditions
   * The `hello_message` field in the result is `Bonjour, Pierre`
   * The `goodbye_message` field in the result is `Au revoir, Pierre`
5. Save your changes
6. Run `python -m pytest`. This will fail, due to a bug in the Workflow Definition.
7. Find and fix the bug in the Workflow Definition
8. Run the `python -m pytest` command again to verify that you fixed the bug

There are two things to note about this test.

First, the test completes in under a second, even though the Workflow 
Definition contains a `await asyncio.sleep(15)` call that adds a 15-second delay 
to the Workflow Execution. This is because of the time-skipping feature
provided by the test environment.

Second, calls to `RegisterActivity` near the top of the test indicate 
that the Activity Definitions are executed as part of this Workflow 
test. As you learned, you can test your Workflow Definition in isolation 
from the Activity implementations by using mocks. The optional exercise 
that follows provides an opportunity to try this for yourself.


### This is the end of the exercise.


## (Optional) Using Mock Activities in a Workflow Test

If you have time and would like an additional challenge, 
continue with the following steps.

1. Make a copy of the existing Workflow Test by running 
    `cp test_workflow.py test_workflow_with_mocks.py`
2. Edit the `test_workflow_with_mocks.py` file
3. Add the following imports 
    ```python
    from temporalio import activity
    from shared import (
        TranslationWorkflowInput,
        TranslationActivityInput,
        TranslationActivityOutput,
    )
    ```
4. Create a new async function to mock your Activity.
    1. Name it `translate_term_mocked_french` and decorate it with 
    `@activity.defn(name="translate_term")`. The function should take `TranslationActivityInput`
    2. In the body of your new mocked Activity, write an if statement that returns
    a new `TranslationActivityOutput` object containing `Bonjour` if the term
    that was passed in via the `TranslationActivityInput` was `hello`. Otherwise
    return a new `TranslationActivityObject` containing `Au revoir`.
    3. The full mocked Activity is shown below:
    ```python
    @activity.defn(name="translate_term")
    async def translate_term_mocked_french(input: TranslationActivityInput):
      if input.term == "hello":
          return TranslationActivityOutput("Bonjour")
      else:
          return TranslationActivityOutput("Au revoir")
    ```
4. Delete the context manager and the creation of a `TranslationActivites` object,
    these are now unnecessary due to the use of a mocked Activity.
    ```python
    async with aiohttp.ClientSession() as session:
        activities = TranslationActivities(session)
    ```
    Once deleted realign your Python code properly now that a scope has been
    removed.
5. In the Worker creation, replace the statement `activities=[activities.translate_term],`
    with `activities=[translate_term_mocked_french],`
6. Save your changes
7. Run `python -m pytest` to run the tests
