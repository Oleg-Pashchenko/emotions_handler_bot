import dataclasses
import datetime


@dataclasses.dataclass
class CreationInfo:
    creator_name: str
    creator_id: int
    creation_date: datetime.date


@dataclasses.dataclass
class Story:
    id: int
    text: str
    story_date: datetime.date
    attachments: list[str]
    creation_info: CreationInfo


@dataclasses.dataclass
class Blog:
    id: int
    creation_info: CreationInfo
    stories: list[Story]

