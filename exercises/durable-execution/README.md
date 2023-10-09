# Exercise 2: Observing Durable Execution
During this exercise, you will

* Create Workflow and Activity loggers 
* Add logging statements to the code
* Add a Timer to the Workflow Definition
* Launch two Workers and run the Workflow
* Kill one of the Workers during Workflow Execution and observe that the remaining Worker completes the execution

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

## Part A: Add Logging to the Workflow Code

1. Edit the `workflow.py` file
2. Add a new line in the `run` method to log a message at the info level
    1. It should mention that the Workflow method has been invoked
    2. It should also include the variables passes as input
3. Before each call to `execute_activity_method`, log a message at Debug level
    1. This should should identify the word being translated
    2. It should also include the language code passed as input
4. Save your changes


## Part B: Add Logging to the Activity Code

1. Edit the `activities.py` file
2. Insert a logging statement in the `run` method `info` level, so you'll know 
    when the Activity is invoked.
    1. Include the term being translated and the language code
3. Near the bottom of the method, use the `debug` level to log the successful translation
	1. Include the translated term as a name-value pair
4. Save your changes

## Part C: Configure the Log Level

1. Edit the `worker.py` file
2. Uncomment the import for `import logging` (this allows you to set the log level)
3. Set your logging level to `logging.INFO` as the first line in the `main` function.

## Part D: Add a Timer to the Workflow
You will now add a Timer between the two Activity calls in the Workflow Definition, which will make it easier to observe durable execution in the next section.

1. After the statement where `hello_message` is defined, but before the statement where
   `goodbye_input` is defined, add a new statement that logs the message `Sleeping between translation calls` at the `info` level.
2. Just after the new log statement, use `await asyncio.sleep(10)` to set a Timer for 10 seconds


## Part E: Observe Durable Execution
It is typical to run Temporal applications using two or more Worker processes. Not only do additional Workers allow the application to scale, it also increases availability since another Worker can take over if a Worker crashes during Workflow Execution. You'll see this for yourself now and will learn more about how Temporal achieves this as you continue through the course.

Before proceeding, make sure that there are no Workers running for this or any previous exercise. Also, please read through all of these instructions before you begin, so that you'll know when and how to react.

1. In one terminal, start the Worker by running `python worker.py`
2. In another terminal, start a second Worker by running `python worker.py`
3. In another terminal, execute the Workflow by running `python starter.py Stanislav sk` (replace `Stanislav` with your first name) 
4. Observe the output in the terminal windows used by each worker. 
5. As soon as you see a log message in one of the Worker terminals indicating that it has started the Timer, press Ctrl-C in that window to kill that Worker process.
6. Switch to the terminal window for the other Worker process. Within a few seconds, you should observe new output, indicating that it has resumed execution of the Workflow.
7. Once you see log output indicating that translation was successful, switch back to the terminal window where you started the Workflow. 

After the final step, you should see the translated Hello and Goodbye messages, which confirms that Workflow Execution completed successfully despite the original Worker being killed.

Since you added logging code to the Workflow and Activity code, take a moment to look at what you see in the terminal windows for each Worker and think about what took place. You may also find it helpful to look at this Workflow Execution in the Web UI.

The microservice for this exercise logs each successful translation, and if you look at its terminal window, you will see that the service only translated Hello (the first Activity) once, even though the Worker was killed after this translation took place. In other words, Temporal did not re-execute the completed Activity when it restored the state of the Workflow Execution. 

### This is the end of the exercise.
