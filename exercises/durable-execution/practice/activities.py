from shared import TranslationActivityInput, TranslationActivityOutput
from temporalio import activity


class TranslationActivities:
    def __init__(self, session):
        self.session = session

    @activity.defn
    async def translate_term(
        self, input: TranslationActivityInput
    ) -> TranslationActivityOutput:
        # TODO Add a logging message using the activity logger at the info level
        # stating that the activity has been invoked. Be sure to include the input
        url = f"http://localhost:9999/translate?term={input.term}&lang={input.language_code}"

        async with self.session.get(url) as response:
            if response.status != 200:
                error_message = await response.text()
                raise RuntimeError(error_message)
            response_json = await response.json()
            response = TranslationActivityOutput(**response_json)
            # TODO Add a logging message using the activity logger at the debug
            # level stating that the activity completed successfully. Include
            # the term, language_code and result in your message
            return response
