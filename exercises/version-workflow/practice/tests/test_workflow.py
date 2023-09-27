import pytest
from temporalio.client import WorkflowHistory

from workflow import LoanProcessingWorkflow

from temporalio.worker import Replayer


@pytest.mark.asyncio
async def test_successful_replay():
    with open("tests/history_for_original_execution.json", "r") as fh:
        history = fh.read()
    replayer = Replayer(workflows=[LoanProcessingWorkflow])
    await replayer.replay_workflow(
        WorkflowHistory.from_json("loan-processing-workflow-customer-a100", history)
    )
