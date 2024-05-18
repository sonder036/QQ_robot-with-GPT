from __future__ import annotations

import abc
import typing

from ..core import app, entities as core_entities
from . import entities


_stage_classes: dict[str, PipelineStage] = {}


def stage_class(name: str):

    def decorator(cls):
        _stage_classes[name] = cls
        return cls
    
    return decorator


class PipelineStage(metaclass=abc.ABCMeta):
    """流水线阶段
    """

    ap: app.Application

    def __init__(self, ap: app.Application):
        self.ap = ap

    async def initialize(self):
        """初始化
        """
        pass

    @abc.abstractmethod
    async def process(
        self,
        query: core_entities.Query,
        stage_inst_name: str,
    ) -> typing.Union[
        entities.StageProcessResult,
        typing.AsyncGenerator[entities.StageProcessResult, None],
    ]:
        """处理
        """
        raise NotImplementedError
