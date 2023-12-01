from dataclasses import dataclass

TASK_QUEUE_NAME = "translation-tasks"


@dataclass
class TranslationWorkflowInput:
    name: str
    language_code: str


@dataclass
class TranslationWorkflowOutput:
    hello_message: str
    goodbye_message: str


@dataclass
class TranslationActivityInput:
    term: str
    language_code: str


@dataclass
class TranslationActivityOutput:
    translation: str
