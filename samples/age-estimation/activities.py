import urllib.parse
import json
from temporalio import activity

from models import EstimatorResponse


class AgeEstimationActivities:
    def __init__(self, session):
        self.session = session

    @activity.defn
    async def retrieve_estimate(self, name: str) -> EstimatorResponse:
        url = f"https://api.agify.io/?name={urllib.parse.quote(name)}"

        async with self.session.get(url) as response:
            response.raise_for_status()
            response_json = await response.json()
            response = EstimatorResponse(**response_json)
            return response
