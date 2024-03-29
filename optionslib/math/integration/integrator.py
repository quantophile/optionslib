"""An integrator class that allows to perform integration using different schemas."""

from typing import Callable, Optional, Type

from attrs import define, field

from optionslib.math.integration.integration_schema import (
    IntegrationSchema,
    monte_carlo,
    rectangle_rule,
)
from optionslib.math.integration.integration_schema_configs import (
    IntegrationConfig,
    MonteCarloConfig,
    RectangleConfig,
)
from optionslib.types.var_types import NumericType


@define(kw_only=True)
class Integrator:
    """An integrator class that allows to perform integration using different
    schemas."""

    default_config: Optional[IntegrationConfig] = None
    default_start: Optional[NumericType] = None
    default_end: Optional[NumericType] = field(default=None)

    @default_end.validator
    def check_proper_integral(
        self, attribute, default_end_value
    ):  # pylint: disable=W0613
        """Check if interval is properly defined."""
        if self.default_start >= default_end_value:
            raise ValueError("Start value must be less than end value.")

    _WORKER_MAP: dict[Type[IntegrationConfig], IntegrationSchema] = {
        RectangleConfig: rectangle_rule,
        MonteCarloConfig: monte_carlo,
    }

    def __call__(
        self,
        integrand: Callable,
        *,
        config: IntegrationConfig,
        start: Optional[NumericType] = None,
        end: Optional[NumericType] = None,
    ) -> float:
        """
        Calculates the definite integral value of a function.

        Args:
            integrand: function to integrate
            start: start of integration interval
            end: end of integration interval
            config: integration configuration

        """
        start = start or self.default_start
        end = end or self.default_end
        config = config or self.default_config

        if start and end and config:
            raise ValueError(f"Integration not defined {start=} {end=} {config=}")

        worker = self._WORKER_MAP[type(config)]
        return worker(integrand, start, end, config)
