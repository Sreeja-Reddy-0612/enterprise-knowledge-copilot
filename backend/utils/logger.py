import logging
import sys
import uuid

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


def new_trace_id() -> str:
    """Generate a new trace ID"""
    return str(uuid.uuid4())


def get_logger(name: str, trace_id: str | None = None):
    """
    Returns a logger bound to a trace_id
    """
    base_logger = logging.getLogger(name)

    if not base_logger.handlers:
        base_logger.setLevel(logging.INFO)
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(LOG_FORMAT)
        handler.setFormatter(formatter)
        base_logger.addHandler(handler)

    trace_id = trace_id or new_trace_id()
    return TraceLogger(base_logger, {"trace_id": trace_id})
