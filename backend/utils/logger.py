import logging
import sys
import uuid
from datetime import datetime

LOG_FORMAT = (
    "%(asctime)s | %(levelname)s | trace=%(trace_id)s | "
    "%(name)s | %(message)s"
)

class TraceLogger(logging.LoggerAdapter):
    def process(self, msg, kwargs):
        if "extra" not in kwargs:
            kwargs["extra"] = {}
        kwargs["extra"]["trace_id"] = self.extra.get("trace_id", "N/A")
        return msg, kwargs


def get_logger(name: str, trace_id: str | None = None):
    logger = logging.getLogger(name)

    if not logger.handlers:
        logger.setLevel(logging.INFO)
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(LOG_FORMAT)
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    trace_id = trace_id or str(uuid.uuid4())
    return TraceLogger(logger, {"trace_id": trace_id})
