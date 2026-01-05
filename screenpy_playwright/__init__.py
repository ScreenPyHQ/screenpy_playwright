"""
                              ScreenPy Playwright.

                                                                      FADE IN:

INT. SITEPACKAGES DIRECTORY

ScreenPy Playwright is an extension for ScreenPy which enables Actors to use
the Playwright browser automation tool.

:copyright: (c) 2019-2026 by Perry Goy.
:license: MIT, see LICENSE for more details.
"""

from . import abilities, actions, questions, resolutions
from .abilities import *  # noqa: F403
from .actions import *  # noqa: F403
from .exceptions import NoPageError, TargetingError
from .protocols import PageObject
from .questions import *  # noqa: F403
from .resolutions import *  # noqa: F403
from .target import Target

__all__ = [
    "NoPageError",
    "PageObject",
    "Target",
    "TargetingError",
]

__all__ += abilities.__all__ + actions.__all__ + questions.__all__ + resolutions.__all__
