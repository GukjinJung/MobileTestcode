import logging
import os
from datetime import datetime
from config.settings import LOG_DIR
from config.constants import DATE_FORMAT


class LoggerSetup:
    """
    로깅 설정 - 파일, 콘솔 로깅 제공
    """

    @staticmethod
    def setup_logger(name: str, log_file: str | None = None) -> logging.Logger:
        os.makedirs(LOG_DIR, exist_ok=True)
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)
        logger.propagate = False

        if not log_file:
            timestamp = datetime.now().strftime(DATE_FORMAT)
            log_file = os.path.join(LOG_DIR, f"test_{timestamp}.log")

        if not any(isinstance(h, logging.FileHandler) for h in logger.handlers):
            fh = logging.FileHandler(log_file, encoding="utf-8")
            fh.setLevel(logging.INFO)
            formatter = logging.Formatter(
                fmt="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S",
            )
            fh.setFormatter(formatter)
            logger.addHandler(fh)

        if not any(isinstance(h, logging.StreamHandler) for h in logger.handlers):
            ch = logging.StreamHandler()
            ch.setLevel(logging.INFO)
            ch.setFormatter(
                logging.Formatter("%(asctime)s [%(levelname)s] %(name)s - %(message)s")
            )
            logger.addHandler(ch)

        return logger

    @staticmethod
    def log_info(logger: logging.Logger, message: str) -> None:
        logger.info(message)

    @staticmethod
    def log_error(logger: logging.Logger, message: str) -> None:
        logger.error(message)

    @staticmethod
    def log_debug(logger: logging.Logger, message: str) -> None:
        logger.debug(message)

    @staticmethod
    def log_screenshot(logger: logging.Logger, screenshot_path: str) -> None:
        logger.info(f"Screenshot saved: {screenshot_path}")
