# Code Repository for Temporal 102 (Python)
This repository provides code used for exercises and demonstrations
included in the Python version of the 
[Temporal 102](https://learn.temporal.io/courses/temporal_102) 
training course.


## Hands-On Exercises

Directory Name                     | Exercise
:--------------------------------- | :-------------------------------------------------------
`exercises/using-data-classes`     | [Exercise 1](exercises/using-classes/README.md)
`exercises/durable-execution`      | [Exercise 2](exercises/durable-execution/README.md)
`exercises/testing-code`           | [Exercise 3](exercises/testing-code/README.md)
`exercises/debug-activity`         | [Exercise 4](exercises/debug-activity/README.md)
`exercises/version-workflow`       | [Exercise 5](exercises/version-workflow/README.md)


## Examples for Self-Study
Directory Name                         | Description
:------------------------------------- | :----------------------------------------------------------------------------------
`samples/age-estimation`               | [Calls a remote API to estimate a given name](samples/age-estimation)


## Reference
The following links provide additional information that you may find helpful as you work through this course.
* [General Temporal Documentation](https://docs.temporal.io/)
* [Temporal Python SDK Documentation](https://python.temporal.io/)
* [Python Language Documentation](https://docs.python.org/3/)
* [GitPod Documentation: Troubleshooting](https://www.gitpod.io/docs/troubleshooting)

### Setup Your Python Virtual Environment

All Python libraries for this course should be installed in a virtual environment.
If you are running these exercises in the course's GitPod environment, there
is a virtual environment already setup for you and you can skip this section.

1. Open a terminal window in the environment and change directories to the root directory of the
`edu-102-python-code` repository
2. Run the following command to create a virtual environment

```
$ python -m venv env
```

3. Activate the virtual environment

```
$ source env/bin/activate
```

Once the environment is active you should see `(env)` prepended to your bash prompt similar
to below

```
(env) $
```

4. Install the necessary packages into the virtual environment

```
python -m pip install -r requirements.txt
```

5. For every new terminal you open, you will need to activate the environment using
the following command

```
$ source env/bin/activate
```

However, the packages are already installed, so there is no need to run pip again.


## Exercise Environment for this Course
You can launch an exercise environment for this course in GitPod by 
clicking the button below:

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/temporalio/edu-102-python-code)

Alternatively, you can follow 
[these instructions](https://learn.temporal.io/getting_started/python/dev_environment/) to 
set up your own Temporal Cluster with Docker Compose, which you can use as an 
exercise environment.
