#!/usr/bin/env python3.7
import logging
from logging.handlers import TimedRotatingFileHandler
import os

import asyncio
import iterm2

ITERM_PATH = "/Users/philiphouse/Library/Application Support/iTerm2"
LOGGING_DIR = "logs"
VERSION = "0.1"

path = os.path.join(ITERM_PATH, LOGGING_DIR)
if not os.path.exists(path):
    os.mkdir(path)

logger = logging.getLogger("it2-{}".format(VERSION))
logger.setLevel(logging.DEBUG)

handler = TimedRotatingFileHandler(
    os.path.join(path, "session.log"),
    when="midnight",
)
handler.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)


async def main(connection):
    """
    This long running iTerm2 daemon logs commands, status's sessions, etc.
    :param connection: iTerm2 connection obj
    """
    app = await iterm2.async_get_app(connection)

    async def monitor(session_id):
        """
        Monitor a session for commands, log them out.
        :param session_id: str
        """
        session = app.get_session_by_id(session_id)
        logger.info("new session: %s", session_id)
        if not session:
            logger.warning("No session with id: %s", session_id)
            return

        modes = [
            iterm2.PromptMonitor.Mode.PROMPT,
            iterm2.PromptMonitor.Mode.COMMAND_START,
            iterm2.PromptMonitor.Mode.COMMAND_END,
        ]
        async with iterm2.PromptMonitor(connection, session_id, modes=modes) as mon:
            while True:
                # blocks until a status changes, new prompt, command starts, command finishes
                mode, info = await mon.async_get()
                if mode == iterm2.PromptMonitor.Mode.COMMAND_START:
                    logger.info("session-%s-command: %s", session_id, info)
                elif mode == iterm2.PromptMonitor.Mode.COMMAND_END:
                    logger.info("session-%s-status: %s", session_id, info)

    await iterm2.EachSessionOnceMonitor.async_foreach_session_create_task(app, monitor)

# This instructs the script to run the "main" coroutine and to keep running even after it returns.
iterm2.run_forever(main)
