"""
RegistrationServiceTest
=======================
Pytest suite for the user-onboarding validation module.

Test lifecycle
--------------
* A shared ``@pytest.fixture`` (``service``) creates a fresh
  ``RegistrationService`` instance before every test — the Python
  equivalent of JUnit 5's ``@BeforeEach``.

Coverage
--------
✔ Successful registrations (valid email + age ≥ 18)
✔ InvalidEmailError  – null / empty / whitespace email
✔ InvalidEmailError  – malformed email (missing @, missing TLD, etc.)
✔ UnderageError      – age < 18 (boundary: 17, 0, negative)
✔ Boundary value     – age == 18 must succeed
✔ Error message      – dynamic messages carry the offending values
"""

import sys
import os

# Allow imports from the same package directory regardless of cwd.
sys.path.insert(0, os.path.dirname(__file__))

import pytest

from exceptions import InvalidEmailError, UnderageError
from registration_service import RegistrationService


# ---------------------------------------------------------------------------
# Shared fixture  (replaces @BeforeEach)
# ---------------------------------------------------------------------------

@pytest.fixture
def service() -> RegistrationService:
    """
    Provide a freshly constructed RegistrationService for every test.
    Mirrors the role of a JUnit 5 @BeforeEach setup method.
    """
    return RegistrationService()


# ---------------------------------------------------------------------------
# 1. Successful registration tests
# ---------------------------------------------------------------------------

class TestSuccessfulRegistration:
    """Happy-path scenarios that must return True."""

    def test_valid_email_and_adult_age(self, service: RegistrationService):
        assert service.register_user("alice@example.com", 25) is True

    def test_minimum_legal_age_boundary(self, service: RegistrationService):
        """Age == 18 is the exact boundary — must succeed."""
        assert service.register_user("bob@domain.org", 18) is True

    def test_email_with_subdomain(self, service: RegistrationService):
        assert service.register_user("user@mail.company.co", 30) is True

    def test_email_with_plus_addressing(self, service: RegistrationService):
        assert service.register_user("user+tag@example.com", 22) is True

    def test_email_with_dots_in_local_part(self, service: RegistrationService):
        assert service.register_user("first.last@example.io", 40) is True

    def test_email_with_digits(self, service: RegistrationService):
        assert service.register_user("user123@domain123.com", 19) is True


# ---------------------------------------------------------------------------
# 2. InvalidEmailError tests
# ---------------------------------------------------------------------------

class TestInvalidEmailError:
    """Malformed or absent email addresses must raise InvalidEmailError."""

    # --- Null / empty guards ---

    def test_none_email_raises(self, service: RegistrationService):
        with pytest.raises(InvalidEmailError):
            service.register_user(None, 25)  # type: ignore[arg-type]

    def test_empty_string_raises(self, service: RegistrationService):
        with pytest.raises(InvalidEmailError):
            service.register_user("", 25)

    def test_whitespace_only_raises(self, service: RegistrationService):
        with pytest.raises(InvalidEmailError):
            service.register_user("   ", 25)

    # --- Regex format failures ---

    def test_missing_at_symbol_raises(self, service: RegistrationService):
        with pytest.raises(InvalidEmailError):
            service.register_user("invalidemail.com", 25)

    def test_missing_domain_raises(self, service: RegistrationService):
        with pytest.raises(InvalidEmailError):
            service.register_user("user@", 25)

    def test_missing_tld_raises(self, service: RegistrationService):
        with pytest.raises(InvalidEmailError):
            service.register_user("user@domain", 25)

    def test_missing_local_part_raises(self, service: RegistrationService):
        with pytest.raises(InvalidEmailError):
            service.register_user("@domain.com", 25)

    def test_double_at_symbol_raises(self, service: RegistrationService):
        with pytest.raises(InvalidEmailError):
            service.register_user("user@@domain.com", 25)

    def test_spaces_inside_email_raises(self, service: RegistrationService):
        with pytest.raises(InvalidEmailError):
            service.register_user("user @domain.com", 25)

    # --- Dynamic error message ---

    def test_error_message_contains_offending_email(
        self, service: RegistrationService
    ):
        bad_email = "not-an-email"
        with pytest.raises(InvalidEmailError) as exc_info:
            service.register_user(bad_email, 25)
        assert bad_email in str(exc_info.value)

    def test_exception_inherits_from_value_error(
        self, service: RegistrationService
    ):
        """InvalidEmailError must be a subclass of ValueError (checked-style)."""
        with pytest.raises(ValueError):
            service.register_user("bad", 25)


# ---------------------------------------------------------------------------
# 3. UnderageError tests
# ---------------------------------------------------------------------------

class TestUnderageError:
    """Applicants younger than 18 must raise UnderageError."""

    def test_age_17_raises(self, service: RegistrationService):
        with pytest.raises(UnderageError):
            service.register_user("teen@example.com", 17)

    def test_age_zero_raises(self, service: RegistrationService):
        with pytest.raises(UnderageError):
            service.register_user("baby@example.com", 0)

    def test_negative_age_raises(self, service: RegistrationService):
        with pytest.raises(UnderageError):
            service.register_user("ghost@example.com", -5)

    def test_age_just_below_minimum_raises(self, service: RegistrationService):
        """17 is strictly below the 18 boundary."""
        with pytest.raises(UnderageError):
            service.register_user("almostlegal@example.com", 17)

    # --- Dynamic error message ---

    def test_error_message_contains_offending_age(
        self, service: RegistrationService
    ):
        with pytest.raises(UnderageError) as exc_info:
            service.register_user("young@example.com", 16)
        assert "16" in str(exc_info.value)

    def test_exception_inherits_from_runtime_error(
        self, service: RegistrationService
    ):
        """UnderageError must be a subclass of RuntimeError (unchecked-style)."""
        with pytest.raises(RuntimeError):
            service.register_user("young@example.com", 15)

    # --- Exception attributes ---

    def test_underage_error_carries_age_attribute(
        self, service: RegistrationService
    ):
        with pytest.raises(UnderageError) as exc_info:
            service.register_user("kid@example.com", 10)
        assert exc_info.value.age == 10

    def test_invalid_email_error_carries_email_attribute(
        self, service: RegistrationService
    ):
        bad = "notvalid"
        with pytest.raises(InvalidEmailError) as exc_info:
            service.register_user(bad, 25)
        assert exc_info.value.email == bad


# ---------------------------------------------------------------------------
# 4. Interaction / priority tests
# ---------------------------------------------------------------------------

class TestValidationOrder:
    """Email is validated before age; ensure exception priority is correct."""

    def test_bad_email_takes_priority_over_underage(
        self, service: RegistrationService
    ):
        """Both inputs are invalid; InvalidEmailError should fire first."""
        with pytest.raises(InvalidEmailError):
            service.register_user("not-an-email", 15)
