import logging


def create_logger(namespace: str, class_log: str):
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s | %(levelname)-8s | "
        "%(module)s:%(funcName)s:%(lineno)d - %(message)s",
    )
    log = logging.getLogger(f"{namespace} - {class_log} --- ")
    return log
