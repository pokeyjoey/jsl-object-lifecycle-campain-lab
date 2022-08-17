from campaign import Campaign

def test_initialize_campaign():
    campaign = Campaign(800)
    assert type(campaign) == Campaign

def test_initialize_campaign_sets_property():
    campaign = Campaign(800)
    assert campaign.budget == 800

def test_initialize_converts_string_to_floats():
    campaign = Campaign("800")
    assert type(campaign.budget) == float

def test_sets_revenue_earned():
    campaign = Campaign("800")
    campaign.set_revenue(1000)
    assert campaign.revenue == 1000

def test_profit():
    campaign = Campaign("800")
    campaign.set_revenue(1000)
    campaign.profit()

def test_average_revenue_per_customer():
    campaign = Campaign(800)
    campaign.set_revenue(1000)
    campaign.set_customers_acquired(20)
    assert campaign.average_revenue_per_customer() == 50

def test_breakeven_customer_number():
    campaign = Campaign(800)
    campaign.set_revenue(1000)
    campaign.set_customers_acquired(20)
    campaign.breakeven_customer_number() == 16
