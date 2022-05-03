"""
VARIABLES
"""
WEEKS_IN_MONTH = 4
VAT_MULTIPLIER = 1.2 # 20% VAT
WEEKLY_RENT_MIN = 2500 # in pennies (£1 = 100p)
WEEKLY_RENT_MAX = 200000
MONTHLY_RENT_MIN = 11000
MONTHLY_RENT_MAX = 866000
MIN_MEMBERSHIP_FEE = 12000

"""
ORGANISATION UNIT
"""
class OrganisationUnitConfig:
    def __init__(self, has_fixed_membership_fee: bool, fixed_membership_fee: int):
        self.has_fixed_membership_fee = has_fixed_membership_fee
        self.fixed_membership_fee = fixed_membership_fee

class OrganisationUnit:
    def __init__(self, name: str, OrganisationUnitConfig: OrganisationUnitConfig = None):
        self.name = name
        self.config = OrganisationUnitConfig

class ClientUnit(OrganisationUnit):
    def __init__(self, name: str, OrganisationUnitConfig: OrganisationUnitConfig):
        super().__init__(name, OrganisationUnitConfig)

class DivisionUnit(OrganisationUnit):
    def __init__(self, name: str, OrganisationUnitConfig: OrganisationUnitConfig, ClientUnit: ClientUnit):
        super().__init__(name, OrganisationUnitConfig)
        self.parent = ClientUnit

class AreaUnit(OrganisationUnit):
    def __init__(self, name: str, OrganisationUnitConfig: OrganisationUnitConfig, DivisionUnit: DivisionUnit):
        super().__init__(name, OrganisationUnitConfig)
        self.parent = DivisionUnit

class BranchUnit(OrganisationUnit):
    def __init__(self, name: str, OrganisationUnitConfig: OrganisationUnitConfig, AreaUnit: AreaUnit):
        super().__init__(name, OrganisationUnitConfig)
        self.parent = AreaUnit 

"""
MAIN
"""    
def calculate_membership_fee(rent_amount: int, rent_period: str, organisation_unit: OrganisationUnit) -> int:
    """
    Calculate the membership fee for a given organisation unit.
    """

    # Check if rent period is valid
    if rent_period != "month" and rent_period != "week":
        raise ValueError ("Rent Period is not valid.")

    # Check if min/max rent amount criteria is met
    if rent_period == "week":
        if rent_amount < WEEKLY_RENT_MIN or rent_amount > WEEKLY_RENT_MAX:
            raise ValueError ("Rent Amount is not valid.")
    if rent_period == "month":
        if rent_amount < MONTHLY_RENT_MIN or rent_amount > MONTHLY_RENT_MAX:
            raise ValueError ("Rent Amount is not valid.")

    # Calculate membership fee
    config = get_config(organisation_unit)
    has_fixed_membership_fee = config.has_fixed_membership_fee
    fixed_membership_fee = config.fixed_membership_fee

    if has_fixed_membership_fee:
        return int(fixed_membership_fee * VAT_MULTIPLIER)
    else:
        if rent_period == "month":
            membership_fee = (rent_amount / WEEKS_IN_MONTH)
        else:
            membership_fee = rent_amount
    # Minimum membership fee
    if membership_fee < MIN_MEMBERSHIP_FEE:
        membership_fee = MIN_MEMBERSHIP_FEE
    # VAT
    membership_fee = membership_fee * VAT_MULTIPLIER
    return int(membership_fee)
 
def get_config(organisation_unit: OrganisationUnit):
    """
    Get the configuration for a given organisation unit.
    """
    if organisation_unit.config == None:
        if organisation_unit.parent == None:
            raise Exception ("No configuration found.")
        else:
            return get_config(organisation_unit.parent)
    else:
        return organisation_unit.config