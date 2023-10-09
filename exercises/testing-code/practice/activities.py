from shared import TranslationActivityInput, TranslationActivityOutput
from temporalio import activity


class TranslationActivities:
    def __init__(self, session):
        self.session = session

    @activity.defn
    async def translate_term(
        self, input: TranslationActivityInput
    ) -> TranslationActivityOutput:
        activity.logger.info(f"translate_term Activity invoked with input: {input}")
        url = f"http://localhost:9999/translate?term={input.term}&lang={input.language_code}"

        async with self.session.get(url) as response:
            if response.status != 200:
                error_message = await response.text()
                raise Exception(error_message)
            response_json = await response.json()
            response = TranslationActivityOutput(**response_json)
            activity.logger.debug(
                f"translate_term completed successfully with the result: {input.term} was translated to {input.language_code}: {response.translation}"
            )
            return response
