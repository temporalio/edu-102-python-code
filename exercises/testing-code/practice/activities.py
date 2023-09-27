import logging
from temporalio import activity
import aiohttp
from shared import TranslationActivityInput, TranslationActivityOutput


class TranslationActivities:
    def __init__(self, session):
        self.session = session
        logging.basicConfig(level=logging.DEBUG)

    @activity.defn
    async def translate_term(
        self, input: TranslationActivityInput
    ) -> TranslationActivityOutput:
        logging.info(f"translate_term Activity invoked with input: {input}")
        url = f"http://localhost:9999/translate?term={input.term}&lang={input.language_code}"

        async with self.session.get(url) as response:
            if response.status != 200:
                error_message = await response.text()
                raise Exception(error_message)
            response_json = await response.json()
            response = TranslationActivityOutput(**response_json)
            logging.debug(
                f"translate_term completed successfully with the result: {input.term} was translated to {input.language_code}: {response.translation}"
            )
            return response
