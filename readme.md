# Python Membership Fee Coding Challenge

## Exercise description 
1. Implement a function: ```def calculate_membership_fee(rent_amount, rent_period, organisation_unit) -> 
int``` 
2. Define the model to represent the organisation structure. Resulting model should include the OrganisationUnit type. 

## Data model (feel free to adjust the model) 
1. OrganisationUnit 
    - name: String 
    - config: OrganisationUnitConfig 
    - Any other fields you'd find useful to represent the organisation structure 
2. OrganisationUnitConfig 
    - has_fixed_membership_fee: Boolean 
    - fixed_membership_fee_amount: Integer 

## Requirements for calculate_membership_fee 
1. Input 
    - rent_amount: Integer - rent amount between 1-int.max 
    - rent_period: String - [‘month’, ‘week’] 
    - organisation_unit: OrganisationUnit - branch instance of organisation unit 
2. Validation 
    - rent input - function should throw or return an error when the rent amount is 
outside of the range: 
        - Minimum rent amount is £25 per week or £110 per month 
        - Maximum rent amount is £2000 per week or £8660 per month 
3. Assumptions 
    - VAT is 20% 
    - Monetary amounts are stored in pence [int] 
4. Membership fee calculation rules (in order, from least to most important): 
    - Membership fee is equal to one week of rent + VAT 
    - Minimum membership fee is £120 + VAT - if the rent is lower than £120 the 
membership fee stays at £120 + VAT
    - If the organisation unit has a config object and fixed_membership_fee is true override previous rules and the membership fee should be equal to the fixed_membership_fee_amount. If the passed organisation unit doesn’t have a config recursively check parents until you find configuration object (ie branch doesn’t have a config check area, area doesn’t have a config check division)
6. Output 
    - Membership fee: Integer 
