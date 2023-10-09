import urllib.parse

import aiohttp
from shared import TranslationActivityInput, TranslationActivityOutput
from temporalio import activity


class TranslationActivities:
    def __init__(self, session: aiohttp.ClientSession):
        self.session = session

    @activity.defn
    async def translate_term(
        self, input: TranslationActivityInput
    ) -> TranslationActivityOutput:
        base = f"http://localhost:9999/translate"
        url = f"{base}?term={urllib.parse.quote(input.term)}&lang={input.language_code}"

        async with self.session.get(url) as response:
            response.raise_for_status()
            response_json = await response.json()
            response = TranslationActivityOutput(**response_json)
            return response
