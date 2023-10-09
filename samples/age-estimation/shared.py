from dataclasses import dataclass

TASK_QUEUE_NAME = "testing-estimate-age-tasks"
WORKFLOW_ID = "testing-estimate-age-example"


@dataclass
class EstimatorResponse:
    age: int
    count: int
    name: str
