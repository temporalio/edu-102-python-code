# Optional: Using Classes for Data

In this example, you will see how dataclasses are used to represent input
and output data of Workflow and Activity Definitions.

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

## Part A: Observing the Use of Dataclasses in Workflows

This sample provides an improved version of the translation Workflow used in
Temporal 101. The Workflow follows the best practice of using objects to represent
input parameters and return values.

Look at the code in the `shared.py` file to see how the objects are defined for
the Workflows and Activities. After this, look at the `workflow.py` file to see
how these values are passed in and used in the Workflow code. Finally, look at
`starter.py` to see how the input parameters are created and passed into the Workflow.

## Part B: Observing the Use of Dataclasses in Activities

Now let's take a look at how we used objects to represent input and output data
in Activity definitions.

Take a look at the `activities.py` file to see how the `translate_term` method
takes in the `TranslationActivityInput` dataclass as an input parameter. Also
notice how that method returns a `TranslationActivityOutput` object for the output.

## Part C: Run the Translation Workflow

To run the workflow

1. In one terminal, start the Worker by running `python worker.py`
2. In another terminal, execute the Workflow by running `python starter.py Mason fr`
   (replace `Mason` with your first name), which should display customized greeting and farewell messages in French.

It's common for a single Workflow Definition to be executed multiple times,
each time using a different input. Feel free to experiment with this by specifying
a different language code when starting the Workflow. The translation service
currently supports the following languages:

- `de`: German
- `es`: Spanish
- `fr`: French
- `lv`: Latvian
- `mi`: Maori
- `sk`: Slovak
- `tr`: Turkish
- `zu`: Zulu

### This is the end of the exercise.
