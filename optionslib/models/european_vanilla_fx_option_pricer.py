from datetime import date

from optionslib.market.discounting_curve import DiscountingCurve
from optionslib.market.european_vanilla_fx_option import EuropeanVanillaFxOption
from optionslib.market.fx_volatility_surface import FxVolatilitySurface
from optionslib.models.black_calculator import BlackCalculator
from optionslib.types.enums import (
    FxVanillaEuropeanOptionQuoteConvention,
    DeltaConvention,
)


## A pricer for European Vanilla FX Options that uses the `BlackCalculator`
class EuropeanVanillaFxOptionPricer:
    def __init__(
        self,
        valuationDate: date,
        europeanVanillaFxOption: EuropeanVanillaFxOption,
        fxSpot: float,
        foreignDiscountingCurve: DiscountingCurve,
        domesticDiscountingCurve: DiscountingCurve,
        fxVolatilitySurface: FxVolatilitySurface,
    ):
        self.fxVolatilitySurface = fxVolatilitySurface
        self.sigma = self.fxVolatilitySurface.volatility(self.K, self.T)
        self.blackCalculator = BlackCalculator(
            valuationDate,
            europeanVanillaFxOption,
            fxSpot,
            foreignDiscountingCurve,
            domesticDiscountingCurve,
            self.sigma,
        )

    ## Returns the forward contract strike F(0,T)
    def atTheMoneyForward(self):
        return self.blackCalculator.atTheMoneyForward()

    def dPlus(self):
        return self.blackCalculator.d_plus()

    def dMinus(self):
        return self.blackCalculator.d_minus()

    def value(
        self,
        quoteConvention: FxVanillaEuropeanOptionQuoteConvention = FxVanillaEuropeanOptionQuoteConvention.DOMESTIC_PER_UNIT_OF_FOREIGN,
    ):
        return self.blackCalculator.value(quoteConvention)

    def delta(self, deltaConvention: DeltaConvention = DeltaConvention.PIPS_SPOT_DELTA):
        return self.blackCalculator.delta(deltaConvention)

    def analyticGamma(self):
        return self.blackCalculator.analyticGamma()

    def analyticTheta(self):
        return self.blackCalculator.analyticTheta()

        return theta

    def vega(self):
        return self.blackCalculator.vega()

    def vanna(self):
        return self.blackCalculator.vanna()

    def volga(self):
        return self.blackCalculator.volga()
