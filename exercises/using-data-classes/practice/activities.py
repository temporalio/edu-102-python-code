import urllib.parse

import aiohttp
from shared import TranslationActivityInput, TranslationActivityOutput
from temporalio import activity


class TranslationActivities:
    def __init__(self, session: aiohttp.ClientSession):
        self.session = session

    # TODO Replace the last two parameters with the data class you defined as input
    # TODO Replace the type hit (str) with the name of the data class you defined as output
    @activity.defn
    async def translate_term(self, input_term: str, language_code: str) -> str:
        # TODO Change the parameters used in the URL to the appropriate fields from
        # your input data class
        base = f"http://localhost:9999/translate"
        url = f"{base}?term={urllib.parse.quote(input.term)}&lang={input.language_code}"

        async with self.session.get(url) as response:
            response.raise_for_status()

            # TODO return the Activity output object here instead of
            # just a string
            return await response.text()
