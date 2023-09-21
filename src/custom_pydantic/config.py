from pydantic import ConfigDict

BaseConfigDict = ConfigDict(
    validate_default=True,
    extra="forbid",
)

BaseFrozenConfigDict = ConfigDict(
    validate_default=True,
    extra="forbid",
    frozen=True,
)
