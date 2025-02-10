# Code Repository for Temporal 102 (Python)

This repository provides code used for exercises and demonstrations
included in the Python version of the
[Temporal 102](https://learn.temporal.io/courses/temporal_102)
training course.

It's important to remember that the example code used in this course was designed to support learning a specific aspect of Temporal, not to serve as a ready-to-use template for implementing a production system.

For the exercises, make sure to run `temporal server start-dev --ui-port 8080 --db-filename clusterdata.db` in one terminal to start the Temporal server. For more details on this command, please refer to the `Setting up a Local Development Environment` chapter in the course. Note: If you're using the Gitpod environment to run this exercise, you can skip this step.

## Hands-On Exercises

| Directory Name                | Exercise                                            |
| :---------------------------- | :-------------------------------------------------- |
| `exercises/durable-execution` | [Exercise 1](exercises/durable-execution/README.md) |
| `exercises/testing-code`      | [Exercise 2](exercises/testing-code/README.md)      |
| `exercises/debug-activity`    | [Exercise 3](exercises/debug-activity/README.md)    |

## Examples for Self-Study

| Directory Name                                  | Description                                                                                                     |
| :---------------------------------------------- | :-------------------------------------------------------------------------------------------------------------- |
| `samples/age-estimation`                        | [Calls a remote API to estimate the age of a person given their name](samples/age-estimation)                   |
| `samples/using-dataclasses-as-input-and-output` | [Demonstrate how data classes are passed in as input and output](samples/using-dataclasses-as-input-and-output) |

## Reference

The following links provide additional information that you may find helpful as you work through this course.

- [General Temporal Documentation](https://docs.temporal.io/)
- [Temporal Python SDK Documentation](https://python.temporal.io/)
- [Python Language Documentation](https://docs.python.org/3/)
- [Python Packaging and Virtual Environment Documentation](https://packaging.python.org/en/latest/tutorials/installing-packages/#creating-virtual-environments)
- [GitPod Documentation: Troubleshooting](https://www.gitpod.io/docs/troubleshooting)

### Setup Your Python Virtual Environment

All Python libraries for this course should be installed in a virtual environment.
If you are running these exercises in the course's GitPod environment, there
is a virtual environment already setup for you and you can skip this section.
(Be certain that you are running Python 3.7+. If you system has)

1. Open a terminal window in the environment and change directories to the root directory of the
   `edu-102-python-code` repository
2. Run the following command to create a virtual environment

```
$ python3 -m venv env
```

3. Activate the virtual environment

**Linux/Mac**:

```
$ source env/bin/activate
```

**Windows**:

```
$ env\Scripts\activate
```

Once the environment is active you should see `(env)` prepended to your prompt similar
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

**Linux/Mac**:

```
$ source env/bin/activate
```

**Windows**:

```
$ env\Scripts\activate
```

However, the packages are already installed, so there is no need to run pip again.

## Exercise Environment for this Course

You can launch an exercise environment for this course using Gitpod or Codeanywhere:

### 🌐 Gitpod


[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/temporalio/edu-102-python-code)

### 🌍 Codeanywhere
[![Open in Codeanywhere](https://codeanywhere.com/img/open-in-codeanywhere-btn.svg)](https://app.codeanywhere.com/#https://github.com/temporalio/edu-102-python-code)

Alternatively, you can follow
[these instructions](https://learn.temporal.io/getting_started/python/dev_environment/) to
set up your own Temporal Cluster with Docker Compose, which you can use as an
exercise environment.
