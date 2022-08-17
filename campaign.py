class Campaign:

    def __init__(self, budget):
        self.budget = float(budget)
        self.revenue = None
        self.customers_acquired = None

    def set_revenue(self, revenue):
        self.revenue = float(revenue)

    def profit(self):
        return self.revenue - self.budget

    def set_customers_acquired(self, customers_acquired):
        self.customers_acquired = customers_acquired

    def average_revenue_per_customer(self):
        return self.revenue / self.customers_acquired

    def breakeven_customer_number(self):
        return self.budget / self.average_revenue_per_customer()
