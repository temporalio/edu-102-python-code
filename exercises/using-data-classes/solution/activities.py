from temporalio import activity

from shared import TranslationActivityInput, TranslationActivityOutput


class TranslationActivities:
    def __init__(self, session):
        self.session = session

    @activity.defn
    async def translate_term(
        self, input: TranslationActivityInput
    ) -> TranslationActivityOutput:
        url = f"http://localhost:9999/translate?term={input.term}&lang={input.language_code}"

        async with self.session.get(url) as response:
            response.raise_for_status()
            response_json = await response.json()
            response = TranslationActivityOutput(**response_json)
            return response
