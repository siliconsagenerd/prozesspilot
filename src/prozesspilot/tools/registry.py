"""Tool registry."""

from __future__ import annotations

from collections.abc import Awaitable, Callable
from dataclasses import dataclass, field
from typing import Any


@dataclass
class Tool:
    name: str
    description: str
    fn: Callable[..., Awaitable[Any]]
    input_schema: dict = field(default_factory=dict)


class ToolRegistry:
    def __init__(self) -> None:
        self._tools: dict[str, Tool] = {}

    def register(self, tool: Tool) -> None:
        self._tools[tool.name] = tool

    def get(self, name: str) -> Tool:
        if name not in self._tools:
            raise KeyError(f"unknown tool {name}")
        return self._tools[name]

    def names(self) -> list[str]:
        return list(self._tools.keys())

    async def call(self, name: str, **kwargs) -> Any:
        return await self._tools[name].fn(**kwargs)

    def describe(self) -> list[dict]:
        return [{"name": t.name, "description": t.description} for t in self._tools.values()]


registry = ToolRegistry()