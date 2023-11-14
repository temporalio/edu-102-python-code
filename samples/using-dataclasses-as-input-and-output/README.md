# Optional Exercise: Using Classes for Data

During this exercise, you will

- Define classes to represent input and output of an Activity Definition
- Update the Activity and Workflow code to use these classes
- Run the Workflow to ensure that it works as expected

Make your changes to the code in the `practice` subdirectory (look for `TODO` comments that will guide you to where you should make changes to the code). If you need a hint or want to verify your changes, look at the complete version in the `solution` subdirectory.

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

## Part A: Define the Activity Data Classes

This exercise provides an improved version of the translation Workflow used in Temporal 101. The Workflow has already been updated to follow the best practice of using classes to represent input parameters and return values. You'll apply what you've learned to do the same for the Activity.

Before continuing with the steps below, take at the code in the `shared.py` file to see how the dataclasses are defined for the Workflow. After this, look at the `workflow.py` file to see how these values are passed in and used in the Workflow code. Finally, look at the `starter.py` file to see how the input parameters are created and passed into the Workflow.

Once you're ready to implement something similar for the Activity, continue with the steps below:

1. Edit the shared.py
   1. Define a Data Class called `TranslationActivityInput` to be used as an input parameter
      1. Define a field named `term` of type `str`
      1. Define a field named `language_code` of type `str`
   2. Define a Data Class called `TranslationActivityOutput` to be used for the result
      1. Define a field named `translation` of type `str`
   3. Save your changes

## Part B: Use the Data Classes in Your Activity

Now that you have defined the class, you must update the Activity code to use them.

1. Edit the `activities.py` file
2. Replace the last two input parameters in the `translate_term` method with the Data Class you defined as input
3. Replace the first type hint (`str`) in the `translate_term` method with the name of the Data Class you defined as output
4. At the end of the method, create a `TranslationActivityOutput` object and populate its `translation` field with the `content` variable, which holds the translation returned in the microservice call.
5. Return the object created in the previous step
6. Save your changes

## Part C: Update the Workflow Code

You've now updated the Activity code to use the classes. The next step is to update the Workflow code to use these classes where it passes input to the Activity and access its return value.

1. Edit the `workflow.py` file
   1. Add a new line to define a `TranslationActivityInput` object, populating it with the two fields
      (term and language code) currently passed as input to the first `execute_activity_method` call
   2. Change that `execute_activity_method` call to use the object as input instead of the two parameters it now uses
   3. Update the `hello_message` string so that it is based on the `translation` field from the Activity output object
2. Repeat the previous three steps for the second call to `execute_activity_method`, which translates "Goodbye"
3. Save your changes

## Part D: Run the Translation Workflow

Now that you've made the necessary changes, it's time to run the Workflow to ensure that it works as expected.

1. In another terminal, start the Worker by running `python worker.py`
2. In another terminal, execute the Workflow by running `python starter.py Mason fr` (replace `Mason` with your first name), which should display customized greeting and farewell messages in French.

If your code didn't work as expected, go back and double-check your changes, possibly comparing them to the code in the `solution` directory.

It's common for a single Workflow Definition to be executed multiple times, each time using a different input. Feel free to experiment with this by specifying a different language code when starting the Workflow. The translation service currently supports the following languages:

- `de`: German
- `es`: Spanish
- `fr`: French
- `lv`: Latvian
- `mi`: Maori
- `sk`: Slovak
- `tr`: Turkish
- `zu`: Zulu

### This is the end of the exercise.
