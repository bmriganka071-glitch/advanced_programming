

import re
from typing import Final

from exceptions import InvalidEmailError, UnderageError


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

_EMAIL_PATTERN: Final[str] = (
    r"^[a-zA-Z0-9._%+\-]+"   # local part  (identifier)
    r"@"                       # literal @
    r"[a-zA-Z0-9.\-]+"        # domain name
    r"\.[a-zA-Z]{2,}$"        # dot + TLD (≥ 2 letters)
)

MINIMUM_AGE: Final[int] = 18




class RegistrationService:
   

    def __init__(self) -> None:
        # Compile the regex once at construction time.
        self._email_regex: re.Pattern[str] = re.compile(_EMAIL_PATTERN)

  
        assert self._email_regex is not None, (
            "RegistrationService invariant violated: "
            "email regex failed to compile — cannot process registrations."
        )

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def register_user(self, email: str, age: int) -> bool:
       
        self._validate_email(email)
        self._validate_age(age)

        return True

    # ------------------------------------------------------------------
    # Private helpers
    # ------------------------------------------------------------------

    def _validate_email(self, email: str) -> None:
        """Raise InvalidEmailError for null/empty or badly formatted email."""

        # 1. Null / empty guard
        if email is None or not email.strip():
            raise InvalidEmailError(
                email=str(email),
                reason="email must not be null or empty",
            )

        # 2. Regex format check
        if not self._email_regex.fullmatch(email.strip()):
            raise InvalidEmailError(
                email=email,
                reason=(
                    "email must contain a valid identifier, "
                    "an '@' symbol, and a domain name "
                    "(e.g. user@example.com)"
                ),
            )

    def _validate_age(self, age: int) -> None:
        """Raise UnderageError when applicant is below minimum age."""

        if age < MINIMUM_AGE:
            raise UnderageError(age=age)
