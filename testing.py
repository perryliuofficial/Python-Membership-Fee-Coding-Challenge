import unittest
from main import DivisionUnit, OrganisationUnitConfig, AreaUnit, BranchUnit, ClientUnit, calculate_membership_fee, get_config

class test_calculate_membership_fee(unittest.TestCase):
    def setUp(self) -> None:
        self.client = ClientUnit("Client", OrganisationUnitConfig(False,0))
        self.divisionA = DivisionUnit("Division A", OrganisationUnitConfig(False, 0), self.client)
        self.divisionB = DivisionUnit("Division B", OrganisationUnitConfig(True, 0), self.client)
        self.areaA = AreaUnit("Area A", OrganisationUnitConfig(True, 45000), self.divisionA)
        self.areaB = AreaUnit("Area B", OrganisationUnitConfig(False, 0), self.divisionA)
        self.areaC = AreaUnit("Area C", OrganisationUnitConfig(True, 45000), self.divisionB)
        self.areaD = AreaUnit("Area D", OrganisationUnitConfig(False, 0), self.divisionB)
        self.branchA = BranchUnit("Branch A", None, self.areaA)
        self.branchB = BranchUnit("Branch B", OrganisationUnitConfig(False,0), self.areaA)
        self.branchC = BranchUnit("Branch C", OrganisationUnitConfig(False,0), self.areaA)
        self.branchD = BranchUnit("Branch D", None, self.areaA)
        self.branchE = BranchUnit("Branch E", OrganisationUnitConfig(False, 0), self.areaB)
        self.branchF = BranchUnit("Branch F", OrganisationUnitConfig(False, 0), self.areaB)
        self.branchG = BranchUnit("Branch G", OrganisationUnitConfig(False, 0), self.areaB)
        self.branchH = BranchUnit("Branch H", OrganisationUnitConfig(False, 0), self.areaB)
        self.branchI = BranchUnit("Branch I", OrganisationUnitConfig(False, 0), self.areaC)
        self.branchJ = BranchUnit("Branch J", OrganisationUnitConfig(False, 0), self.areaC)
        self.branchK = BranchUnit("Branch K", OrganisationUnitConfig(True, 25000), self.areaC)
        self.branchL = BranchUnit("Branch L", OrganisationUnitConfig(False, 0), self.areaC)
        self.branchM = BranchUnit("Branch M", None, self.areaD)
        self.branchN = BranchUnit("Branch N", OrganisationUnitConfig(False, 0), self.areaD)
        self.branchO = BranchUnit("Branch O", OrganisationUnitConfig(False, 0), self.areaD)
        self.branchP = BranchUnit("Branch P", OrganisationUnitConfig(False, 0), self.areaD)

    def test_calculate_membership_success(self):
        self.assertEqual(calculate_membership_fee(rent_amount=2600, rent_period="week", organisation_unit=self.branchA), 54000)
        self.assertEqual(calculate_membership_fee(rent_amount=2600, rent_period="week", organisation_unit=self.branchB), 14400)
        
    def test_calculate_membership_failure(self):
        self.assertRaises(ValueError, calculate_membership_fee, rent_amount=2600, rent_period="weeka", organisation_unit=self.branchM)
        self.assertRaises(ValueError, calculate_membership_fee, rent_amount=2600, rent_period="months", organisation_unit=self.branchM)
        self.assertRaises(ValueError, calculate_membership_fee, rent_amount=2400, rent_period="week", organisation_unit=self.branchM)
        self.assertRaises(ValueError, calculate_membership_fee, rent_amount=200100, rent_period="week", organisation_unit=self.branchM)

    def test_get_config_with_branchA_success(self):
        configResult = get_config(self.branchA)
        self.assertEqual(configResult.has_fixed_membership_fee, True)
        self.assertEqual(configResult.fixed_membership_fee, 45000)

if __name__ == "__main__":
    unittest.main()