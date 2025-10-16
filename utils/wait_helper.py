from typing import Callable
from config.settings import TIMEOUT


class WaitHelper:
    """
    대기 전략 - 명시적, 조건부 대기
    """

    def __init__(self, page, timeout: int = TIMEOUT) -> None:
        self.page = page
        self.timeout = timeout

    async def wait_for_url_change(self, expected_url: str) -> None:
        await self.page.wait_for_url(expected_url, timeout=self.timeout)

    async def wait_for_element_visible(self, selector: str) -> None:
        await self.page.wait_for_selector(selector, state="visible", timeout=self.timeout)

    async def wait_for_text_in_page(self, text: str) -> None:
        await self.page.wait_for_selector(f"text={text}", timeout=self.timeout)

    async def wait_for_network_idle(self) -> None:
        await self.page.wait_for_load_state("networkidle", timeout=self.timeout)

    async def wait_for_load_state(self, state: str = "load") -> None:
        await self.page.wait_for_load_state(state, timeout=self.timeout)

    async def wait_custom_condition(self, condition_func: Callable[[], bool], timeout: int | None = None) -> None:
        from asyncio import sleep

        max_ms = timeout or self.timeout
        elapsed = 0
        step = 0.1
        while elapsed < max_ms / 1000:
            if await condition_func():
                return
            await sleep(step)
            elapsed += step
        raise TimeoutError("Custom condition timed out")
