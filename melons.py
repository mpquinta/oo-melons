"""Classes for melon orders."""

class AbstractMelonOrder:
    """A base class that other Melon Orders inherit from"""

    def __init__(self, species, qty, country_code=None):
        """Initialize melon order attributes."""

        self.species = species.lower()
        self.qty = qty
        self.country_code = country_code
        self.shipped = False


    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        if self.species == "christmas melon":
            base_price = base_price * 1.5
        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
      
    order_type = "domestic"
    tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17

    def get_total(self):
        if self.qty < 10:
            total = super().get_total() + 3
        
        return total

class GovernmentMelonOrder(AbstractMelonOrder):
    tax = 0
    passed_inspection = False

    def mark_inspection(self):
        self.passed_inspection = True
