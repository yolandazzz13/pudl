"""Metadata and operational constants."""
import datetime
from collections.abc import Callable

import pandas as pd
import pyarrow as pa
import sqlalchemy as sa
from sqlalchemy.dialects.sqlite import DATETIME as SQLITE_DATETIME

FIELD_DTYPES_PANDAS: dict[str, str] = {
    "string": "string",
    "number": "float64",
    "integer": "Int64",
    "boolean": "boolean",
    "date": "datetime64[s]",
    "datetime": "datetime64[s]",
    "year": "datetime64[s]",
}
"""Pandas data type by PUDL field type (Data Package `field.type`)."""

FIELD_DTYPES_PYARROW: dict[str, pa.lib.DataType] = {
    "boolean": pa.bool_(),
    "date": pa.date32(),
    "datetime": pa.timestamp("ms", tz="UTC"),
    "integer": pa.int32(),
    "number": pa.float32(),
    "string": pa.string(),
    "year": pa.int32(),
}

FIELD_DTYPES_SQL: dict[str, type] = {
    "boolean": sa.Boolean,
    "date": sa.Date,
    # Ensure SQLite's string representation of datetime uses only whole seconds:
    "datetime": SQLITE_DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d %(hour)02d:%(minute)02d:%(second)02d"
    ),
    "integer": sa.Integer,
    "number": sa.Float,
    "string": sa.Text,
    "year": sa.Integer,
}
"""SQLAlchemy column types by PUDL field type (Data Package `field.type`)."""

CONSTRAINT_DTYPES: dict[str, type] = {
    "string": str,
    "integer": int,
    "year": int,
    "number": float,
    "boolean": bool,
    "date": datetime.date,
    "datetime": datetime.datetime,
}
"""Python types for field constraints by PUDL field type (Data Package `field.type`)."""

LICENSES: dict[str, dict[str, str]] = {
    "cc-by-4.0": {
        "name": "CC-BY-4.0",
        "title": "Creative Commons Attribution 4.0",
        "path": "https://creativecommons.org/licenses/by/4.0",
    },
    "us-govt": {
        "name": "other-pd",
        "title": "U.S. Government Works",
        "path": "https://www.usa.gov/government-works",
    },
}
"""License attributes."""

PERIODS: dict[str, Callable[[pd.Series], pd.Series]] = {
    "year": lambda x: pd.Series(x.to_numpy().astype("datetime64[Y]")),
    "quarter": lambda x: x.apply(
        pd.tseries.offsets.QuarterBegin(startingMonth=1).rollback
    ),
    "month": lambda x: pd.Series(x.to_numpy().astype("datetime64[M]")),
    "date": lambda x: pd.Series(x.to_numpy().astype("datetime64[D]")),
}
"""Functions converting datetimes to period start times, by time period."""

CONTRIBUTORS: dict[str, dict[str, str]] = {
    "catalyst-cooperative": {
        "title": "Catalyst Cooperative",
        "email": "pudl@catalyst.coop",
        "path": "https://catalyst.coop",
        "role": "publisher",
        "organization": "Catalyst Cooperative",
    },
    "zane-selvans": {
        "title": "Zane Selvans",
        "email": "zane.selvans@catalyst.coop",
        "path": "https://amateurearthling.org",
        "role": "wrangler",
        "organization": "Catalyst Cooperative",
        "orcid": "0000-0002-9961-7208",
    },
    "christina-gosnell": {
        "title": "Christina Gosnell",
        "email": "christina.gosnell@catalyst.coop",
        "role": "contributor",
        "organization": "Catalyst Cooperative",
    },
    "steven-winter": {
        "title": "Steven Winter",
        "email": "steven.winter@catalyst.coop",
        "role": "contributor",
        "organization": "Catalyst Cooperative",
    },
    "alana-wilson": {
        "title": "Alana Wilson",
        "email": "alana.wilson@catalyst.coop",
        "role": "contributor",
        "organization": "Catalyst Cooperative",
    },
    "karl-dunkle-werner": {
        "title": "Karl Dunkle Werner",
        "email": "karldw@berkeley.edu",
        "path": "https://karldw.org",
        "role": "contributor",
        "organization": "UC Berkeley",
    },
    "greg-schivley": {
        "title": "Greg Schivley",
        "path": "https://gschivley.github.io",
        "role": "contributor",
        "organization": "Carbon Impact Consulting",
    },
    "austen-sharpe": {
        "title": "Austen Sharpe",
        "email": "austen.sharpe@catalyst.coop",
        "role": "contributor",
        "organization": "Catalyst Cooperative",
    },
    "katherine-lamb": {
        "title": "Katherine Lamb",
        "email": "katherine.lamb@catalyst.coop",
        "role": "contributor",
        "organization": "Catalyst Cooperative",
    },
    "bennett-norman": {
        "title": "Bennett Norman",
        "email": "bennett.norman@catalyst.coop",
        "role": "contributor",
        "organization": "Catalyst Cooperative",
    },
    "trenton-bush": {
        "title": "Trenton Bush",
        "email": "trenton.bush@catalyst.coop",
        "role": "contributor",
        "organization": "Catalyst Cooperative",
    },
    "ethan-welty": {
        "title": "Ethan Welty",
        "email": "ethan.welty@gmail.com",
        "role": "contributor",
        "organization": "Catalyst Cooperative",
    },
}
"""PUDL Contributors for attribution."""

KEYWORDS: dict[str, list[str]] = {
    "electricity": [
        "electricity",
        "electric",
        "generation",
        "energy",
        "utility",
        "transmission",
        "distribution",
        "kWh",
        "MWh",
        "kW",
        "MW",
        "kilowatt hours",
        "kilowatts",
        "megawatts",
        "megawatt hours",
        "power",
    ],
    "fuels": [
        "fuel",
        "coal",
        "bituminous",
        "lignite",
        "natural gas",
        "solar",
        "wind",
        "hydro",
        "nuclear",
        "subbituminous",
        "heat content",
        "mmbtu",
        "fuel cost",
        "fuel price",
    ],
    "plants": [
        "plant",
        "boilers",
        "generators",
        "steam",
        "turbine",
        "combined_cycle",
        "retirement",
        "planned",
        "proposed",
        "combustion",
        "prime mover",
        "capacity",
        "heat rate",
    ],
    "finance": [
        "finance",
        "debt",
        "accounting",
        "capital",
        "cost",
        "contract",
        "price",
        "receipts",
        "ownership",
        "depreciation",
        "plant in service",
        "capex",
        "opex",
        "operating expenses",
        "capital expenses",
    ],
    "environment": [
        "emissions",
        "pollution",
        "ash",
        "sulfur",
        "mercury",
        "chlorine",
        "sox",
        "so2",
        "nox",
        "ghg",
        "co2",
        "carbon dioxide",
        "particulate",
        "pm2.5",
    ],
    "eia": [
        "eia",
        "energy information administration",
    ],
    "ferc": [
        "ferc",
        "federal energy regulatory commission",
    ],
    "epa": [
        "epa",
        "environmental protection agency",
    ],
    "us_govt": [
        "united states",
        "us",
        "usa",
        "government",
        "federal",
    ],
    "msha": [
        "msha",
        "mshamines",
        "mine safety and health administration",
        "mines",
        "mining",
        "coal",
        "metal",
    ],
    "phmsa": [
        "phmsa",
        "phmsagas",
        "pipelines and hazardous materials safety administration",
        "pipelines",
        "natural gas",
        "transmission",
        "distribution",
        "gathering",
        "liquified natural gas",
        "lng",
        "underground natural gas storage",
    ],
    "eia_water": [
        "eia thermoelectric cooling water",
        "eia waterthermoelectric",
        "cooling water",
        "water usage",
    ],
}

XBRL_TABLES = [
    "corporate_officer_certification_001_duration",
    "corporate_officer_certification_001_instant",
    "identification_001_duration",
    "identification_001_instant",
    "list_of_schedules_002_duration",
    "list_of_schedules_002_instant",
    "general_information_101_duration",
    "general_information_101_instant",
    "control_over_respondent_102_duration",
    "control_over_respondent_102_instant",
    "corporations_controlled_by_respondent_103_duration",
    "corporations_controlled_by_respondent_103_instant",
    "officers_104_duration",
    "officers_104_instant",
    "directors_105_duration",
    "directors_105_instant",
    "information_on_formula_rates_106_duration",
    "information_on_formula_rates_106_instant",
    "information_on_formula_rates_106a_duration",
    "information_on_formula_rates_106a_instant",
    "information_on_formula_rates_106b_duration",
    "information_on_formula_rates_106b_instant",
    "important_changes_during_the_quarter_year_108_duration",
    "important_changes_during_the_quarter_year_108_instant",
    "comparative_balance_sheet_assets_and_other_debits_110_duration",
    "comparative_balance_sheet_assets_and_other_debits_110_instant",
    "comparative_balance_sheet_liabilities_and_other_credits_110_duration",
    "comparative_balance_sheet_liabilities_and_other_credits_110_instant",
    "statement_of_income_114_duration",
    "statement_of_income_114_instant",
    "retained_earnings_118_duration",
    "retained_earnings_118_instant",
    "retained_earnings_appropriated_118_duration",
    "retained_earnings_appropriated_118_instant",
    "retained_earnings_appropriations_118_duration",
    "retained_earnings_appropriations_118_instant",
    "retained_earnings_common_stock_118_duration",
    "retained_earnings_common_stock_118_instant",
    "retained_earnings_credit_118_duration",
    "retained_earnings_credit_118_instant",
    "retained_earnings_debit_118_duration",
    "retained_earnings_debit_118_instant",
    "retained_earnings_preferred_stock_118_duration",
    "retained_earnings_preferred_stock_118_instant",
    "retained_earnings_unappropriated_undistributed_subsidiary_earnings_118_duration",
    "retained_earnings_unappropriated_undistributed_subsidiary_earnings_118_instant",
    "statement_of_cash_flows_120_duration",
    "statement_of_cash_flows_120_instant",
    "statement_of_cash_flows_other_payment_for_retirement_to_financing_acitivities_120_duration",
    "statement_of_cash_flows_other_payment_for_retirement_to_financing_acitivities_120_instant",
    "statement_of_cash_flows_sequence_other_adjustments_by_outside_forces_to_financing_cash_flows_120_duration",
    "statement_of_cash_flows_sequence_other_adjustments_by_outside_forces_to_financing_cash_flows_120_instant",
    "statement_of_cash_flows_sequence_other_adjustments_to_financing_cash_flows_120_duration",
    "statement_of_cash_flows_sequence_other_adjustments_to_financing_cash_flows_120_instant",
    "statement_of_cash_flows_sequence_other_adjustments_to_investing_cash_flows_120_duration",
    "statement_of_cash_flows_sequence_other_adjustments_to_investing_cash_flows_120_instant",
    "statement_of_cash_flows_sequence_other_adjustments_to_operating_cash_flows_120_duration",
    "statement_of_cash_flows_sequence_other_adjustments_to_operating_cash_flows_120_instant",
    "statement_of_cash_flows_sequence_other_items_for_investing_cash_flows_120_duration",
    "statement_of_cash_flows_sequence_other_items_for_investing_cash_flows_120_instant",
    "statement_of_cash_flows_sequence_other_operating_cash_flows_120_duration",
    "statement_of_cash_flows_sequence_other_operating_cash_flows_120_instant",
    "notes_to_financial_statements_122_duration",
    "notes_to_financial_statements_122_instant",
    "statement_of_accumulated_other_comprehensive_income_comprehensive_income_and_hedging_activities_122a_duration",
    "statement_of_accumulated_other_comprehensive_income_comprehensive_income_and_hedging_activities_122a_instant",
    "summary_of_utility_plant_and_accumulated_provisions_for_depreciation_amortization_and_depletion_200_duration",
    "summary_of_utility_plant_and_accumulated_provisions_for_depreciation_amortization_and_depletion_200_instant",
    "nuclear_fuel_materials_202_duration",
    "nuclear_fuel_materials_202_instant",
    "electric_plant_in_service_204_duration",
    "electric_plant_in_service_204_instant",
    "electric_plant_leased_to_others_213_duration",
    "electric_plant_leased_to_others_213_instant",
    "electric_plant_leased_to_others_totals_213_duration",
    "electric_plant_leased_to_others_totals_213_instant",
    "electric_plant_held_for_future_use_214_duration",
    "electric_plant_held_for_future_use_214_instant",
    "electric_plant_held_for_future_use_totals_214_duration",
    "electric_plant_held_for_future_use_totals_214_instant",
    "construction_work_in_progress_electric_216_duration",
    "construction_work_in_progress_electric_216_instant",
    "construction_work_in_progress_electric_total_216_duration",
    "construction_work_in_progress_electric_total_216_instant",
    "accumulated_provision_for_depreciation_of_electric_utility_plant_changes_section_a_219_duration",
    "accumulated_provision_for_depreciation_of_electric_utility_plant_changes_section_a_219_instant",
    "accumulated_provision_for_depreciation_of_electric_utility_plant_changes_section_a_sequence_other_accounts_219_duration",
    "accumulated_provision_for_depreciation_of_electric_utility_plant_changes_section_a_sequence_other_accounts_219_instant",
    "accumulated_provision_for_depreciation_of_electric_utility_plant_changes_section_a_sequence_other_items_219_duration",
    "accumulated_provision_for_depreciation_of_electric_utility_plant_changes_section_a_sequence_other_items_219_instant",
    "accumulated_provision_for_depreciation_of_electric_utility_plant_functional_classification_section_b_219_duration",
    "accumulated_provision_for_depreciation_of_electric_utility_plant_functional_classification_section_b_219_instant",
    "investments_in_subsidiary_companies_224_duration",
    "investments_in_subsidiary_companies_224_instant",
    "investments_in_subsidiary_companies_totals_224_duration",
    "investments_in_subsidiary_companies_totals_224_instant",
    "materials_and_supplies_227_duration",
    "materials_and_supplies_227_instant",
    "materials_and_supplies_other_classes_227_duration",
    "materials_and_supplies_other_classes_227_instant",
    "allowances_accounts_1581_and_1582_228a_duration",
    "allowances_accounts_1581_and_1582_228a_instant",
    "allowances_accounts_1581_and_1582_cost_of_sales_and_transfers_228a_duration",
    "allowances_accounts_1581_and_1582_cost_of_sales_and_transfers_228a_instant",
    "allowances_accounts_1581_and_1582_other_relinquished_228a_duration",
    "allowances_accounts_1581_and_1582_other_relinquished_228a_instant",
    "allowances_accounts_1581_and_1582_purchases_and_transfers_228a_duration",
    "allowances_accounts_1581_and_1582_purchases_and_transfers_228a_instant",
    "allowances_accounts_1581_and_1582_cost_of_sales_and_transfers_section_b_228b_duration",
    "allowances_accounts_1581_and_1582_cost_of_sales_and_transfers_section_b_228b_instant",
    "allowances_accounts_1581_and_1582_other_relinquished_section_b_228b_duration",
    "allowances_accounts_1581_and_1582_other_relinquished_section_b_228b_instant",
    "allowances_accounts_1581_and_1582_purchases_and_transfers_section_b_228b_duration",
    "allowances_accounts_1581_and_1582_purchases_and_transfers_section_b_228b_instant",
    "allowances_accounts_1581_and_1582_section_b_228b_duration",
    "allowances_accounts_1581_and_1582_section_b_228b_instant",
    "extraordinary_property_losses_230a_duration",
    "extraordinary_property_losses_230a_instant",
    "extraordinary_property_losses_totals_230a_duration",
    "extraordinary_property_losses_totals_230a_instant",
    "unrecovered_plant_and_regulatory_study_costs_230b_duration",
    "unrecovered_plant_and_regulatory_study_costs_230b_instant",
    "unrecovered_plant_and_regulatory_study_costs_totals_230b_duration",
    "unrecovered_plant_and_regulatory_study_costs_totals_230b_instant",
    "transmission_service_and_generation_interconnection_study_costs_231_duration",
    "transmission_service_and_generation_interconnection_study_costs_231_instant",
    "transmission_service_and_generation_interconnection_study_costs_totals_231_duration",
    "transmission_service_and_generation_interconnection_study_costs_totals_231_instant",
    "other_regulatory_assets_account_1823_232_duration",
    "other_regulatory_assets_account_1823_232_instant",
    "other_regulatory_assets_account_1823_totals_232_duration",
    "other_regulatory_assets_account_1823_totals_232_instant",
    "miscellaneous_deferred_debits_account_186_233_duration",
    "miscellaneous_deferred_debits_account_186_233_instant",
    "miscellaneous_deferred_debits_account_186_totals_233_duration",
    "miscellaneous_deferred_debits_account_186_totals_233_instant",
    "accumulated_deferred_income_taxes_account_190_234_duration",
    "accumulated_deferred_income_taxes_account_190_234_instant",
    "accumulated_deferred_income_taxes_account_190_electric_234_duration",
    "accumulated_deferred_income_taxes_account_190_electric_234_instant",
    "accumulated_deferred_income_taxes_account_190_gas_234_duration",
    "accumulated_deferred_income_taxes_account_190_gas_234_instant",
    "accumulated_deferred_income_taxes_account_190_notes_234_duration",
    "accumulated_deferred_income_taxes_account_190_notes_234_instant",
    "accumulated_deferred_income_taxes_account_190_other_234_duration",
    "accumulated_deferred_income_taxes_account_190_other_234_instant",
    "capital_stock_account_201_and_204_250_duration",
    "capital_stock_account_201_and_204_250_instant",
    "capital_stock_account_201_and_204_totals_250_duration",
    "capital_stock_account_201_and_204_totals_250_instant",
    "capital_stock_common_stock_account_201_250_duration",
    "capital_stock_common_stock_account_201_250_instant",
    "capital_stock_common_stock_account_201_totals_250_duration",
    "capital_stock_common_stock_account_201_totals_250_instant",
    "capital_stock_preferred_stock_account_204_250_duration",
    "capital_stock_preferred_stock_account_204_250_instant",
    "capital_stock_preferred_stock_account_204_totals_250_duration",
    "capital_stock_preferred_stock_account_204_totals_250_instant",
    "other_paid_in_capital_accounts_208211_253_duration",
    "other_paid_in_capital_accounts_208211_253_instant",
    "other_paid_in_capital_accounts_208211_donations_received_from_stockholders_253_duration",
    "other_paid_in_capital_accounts_208211_donations_received_from_stockholders_253_instant",
    "other_paid_in_capital_accounts_208211_miscellaneous_paid_in_capital_253_duration",
    "other_paid_in_capital_accounts_208211_miscellaneous_paid_in_capital_253_instant",
    "other_paid_in_capital_accounts_208211_reduction_in_par_or_stated_value_of_capital_stock_253_duration",
    "other_paid_in_capital_accounts_208211_reduction_in_par_or_stated_value_of_capital_stock_253_instant",
    "other_paid_in_capital_accounts_208211_required_capital_stock_253_duration",
    "other_paid_in_capital_accounts_208211_required_capital_stock_253_instant",
    "other_paid_in_capital_accounts_208211_total_253_duration",
    "other_paid_in_capital_accounts_208211_total_253_instant",
    "capital_stock_expense_account_214_254b_duration",
    "capital_stock_expense_account_214_254b_instant",
    "capital_stock_expense_account_214_totals_254b_duration",
    "capital_stock_expense_account_214_totals_254b_instant",
    "long_term_debt_account_221_222_223_and_224_256_duration",
    "long_term_debt_account_221_222_223_and_224_256_instant",
    "long_term_debt_account_221_222_223_and_224_subtotals_256_duration",
    "long_term_debt_account_221_222_223_and_224_subtotals_256_instant",
    "long_term_debt_account_221_222_223_and_224_totals_256_duration",
    "long_term_debt_account_221_222_223_and_224_totals_256_instant",
    "long_term_debt_advances_from_associated_companies_223_256_duration",
    "long_term_debt_advances_from_associated_companies_223_256_instant",
    "long_term_debt_bonds_221_256_duration",
    "long_term_debt_bonds_221_256_instant",
    "long_term_debt_other_long_term_debt_224_256_duration",
    "long_term_debt_other_long_term_debt_224_256_instant",
    "long_term_debt_reacquired_bonds_222_256_duration",
    "long_term_debt_reacquired_bonds_222_256_instant",
    "reconciliation_of_reported_net_income_with_taxable_income_for_federal_income_taxes_261_duration",
    "reconciliation_of_reported_net_income_with_taxable_income_for_federal_income_taxes_261_instant",
    "reconciliation_of_reported_net_income_with_taxable_income_for_federal_income_taxes_deductions_recorded_on_books_not_deducted_for_return_261_duration",
    "reconciliation_of_reported_net_income_with_taxable_income_for_federal_income_taxes_deductions_recorded_on_books_not_deducted_for_return_261_instant",
    "reconciliation_of_reported_net_income_with_taxable_income_for_federal_income_taxes_deductions_on_return_not_charged_against_book_income_261_duration",
    "reconciliation_of_reported_net_income_with_taxable_income_for_federal_income_taxes_deductions_on_return_not_charged_against_book_income_261_instant",
    "reconciliation_of_reported_net_income_with_taxable_income_for_federal_income_taxes_income_recorded_on_books_not_included_in_return_261_duration",
    "reconciliation_of_reported_net_income_with_taxable_income_for_federal_income_taxes_income_recorded_on_books_not_included_in_return_261_instant",
    "reconciliation_of_reported_net_income_with_taxable_income_for_federal_income_taxes_show_computation_of_tax_261_duration",
    "reconciliation_of_reported_net_income_with_taxable_income_for_federal_income_taxes_show_computation_of_tax_261_instant",
    "reconciliation_of_reported_net_income_with_taxable_income_for_federal_income_taxes_taxable_income_not_reported_on_books_261_duration",
    "reconciliation_of_reported_net_income_with_taxable_income_for_federal_income_taxes_taxable_income_not_reported_on_books_261_instant",
    "taxes_accrued_prepaid_and_charged_during_year_262_duration",
    "taxes_accrued_prepaid_and_charged_during_year_262_instant",
    "taxes_accrued_prepaid_and_charged_during_year_totals_262_duration",
    "taxes_accrued_prepaid_and_charged_during_year_totals_262_instant",
    "accumulated_deferred_investment_tax_credits_account_255_266_duration",
    "accumulated_deferred_investment_tax_credits_account_255_266_instant",
    "accumulated_deferred_investment_tax_credits_account_255_total_266_duration",
    "accumulated_deferred_investment_tax_credits_account_255_total_266_instant",
    "other_deferred_credits_account_253_269_duration",
    "other_deferred_credits_account_253_269_instant",
    "other_deferred_credits_account_253_totals_269_duration",
    "other_deferred_credits_account_253_totals_269_instant",
    "accumulated_deferred_income_taxes_accelerated_amortization_property_account_281_classified_by_tax_types_272_duration",
    "accumulated_deferred_income_taxes_accelerated_amortization_property_account_281_classified_by_tax_types_272_instant",
    "accumulated_deferred_income_taxes_accelerated_amortization_property_account_281_classified_by_utility_types_272_duration",
    "accumulated_deferred_income_taxes_accelerated_amortization_property_account_281_classified_by_utility_types_272_instant",
    "accumulated_deferred_income_taxes_accelerated_amortization_property_account_281_other_272_duration",
    "accumulated_deferred_income_taxes_accelerated_amortization_property_account_281_other_272_instant",
    "accumulated_deferred_income_taxes_accelerated_amortization_property_account_281_other_electric_272_duration",
    "accumulated_deferred_income_taxes_accelerated_amortization_property_account_281_other_electric_272_instant",
    "accumulated_deferred_income_taxes_accelerated_amortization_property_account_281_other_gas_272_duration",
    "accumulated_deferred_income_taxes_accelerated_amortization_property_account_281_other_gas_272_instant",
    "accumulated_deferred_income_taxes_other_property_account_282_classified_by_business_activities_274_duration",
    "accumulated_deferred_income_taxes_other_property_account_282_classified_by_business_activities_274_instant",
    "accumulated_deferred_income_taxes_other_property_account_282_classified_by_tax_types_274_duration",
    "accumulated_deferred_income_taxes_other_property_account_282_classified_by_tax_types_274_instant",
    "accumulated_deferred_income_taxes_other_property_account_282_non_utility_details_274_duration",
    "accumulated_deferred_income_taxes_other_property_account_282_non_utility_details_274_instant",
    "accumulated_deferred_income_taxes_other_account_283_classified_by_business_activities_276_duration",
    "accumulated_deferred_income_taxes_other_account_283_classified_by_business_activities_276_instant",
    "accumulated_deferred_income_taxes_other_account_283_classified_by_business_activities_total_276_duration",
    "accumulated_deferred_income_taxes_other_account_283_classified_by_business_activities_total_276_instant",
    "accumulated_deferred_income_taxes_other_account_283_classified_by_tax_types_276_duration",
    "accumulated_deferred_income_taxes_other_account_283_classified_by_tax_types_276_instant",
    "accumulated_deferred_income_taxes_other_account_283_classified_by_tax_types_notes_276_duration",
    "accumulated_deferred_income_taxes_other_account_283_classified_by_tax_types_notes_276_instant",
    "accumulated_deferred_income_taxes_other_account_283_electric_276_duration",
    "accumulated_deferred_income_taxes_other_account_283_electric_276_instant",
    "accumulated_deferred_income_taxes_other_account_283_gas_276_duration",
    "accumulated_deferred_income_taxes_other_account_283_gas_276_instant",
    "other_regulatory_liabilities_account_254_278_duration",
    "other_regulatory_liabilities_account_254_278_instant",
    "other_regulatory_liabilities_account_254_totals_278_duration",
    "other_regulatory_liabilities_account_254_totals_278_instant",
    "electric_operating_revenues_300_duration",
    "electric_operating_revenues_300_instant",
    "electric_operating_revenues_other_300_duration",
    "electric_operating_revenues_other_300_instant",
    "electric_operating_revenues_unbilled_revenues_300_duration",
    "electric_operating_revenues_unbilled_revenues_300_instant",
    "regional_transmission_service_revenues_account_4571_302_duration",
    "regional_transmission_service_revenues_account_4571_302_instant",
    "regional_transmission_service_revenues_account_4571_totals_302_duration",
    "regional_transmission_service_revenues_account_4571_totals_302_instant",
    "sales_of_electricity_by_rate_schedules_account_440_residential_304_duration",
    "sales_of_electricity_by_rate_schedules_account_440_residential_304_instant",
    "sales_of_electricity_by_rate_schedules_account_442_commercial_304_duration",
    "sales_of_electricity_by_rate_schedules_account_442_commercial_304_instant",
    "sales_of_electricity_by_rate_schedules_account_442_industrial_304_duration",
    "sales_of_electricity_by_rate_schedules_account_442_industrial_304_instant",
    "sales_of_electricity_by_rate_schedules_account_442_total_commercial_and_industrial_304_duration",
    "sales_of_electricity_by_rate_schedules_account_442_total_commercial_and_industrial_304_instant",
    "sales_of_electricity_by_rate_schedules_account_444_public_street_and_highway_lighting_304_duration",
    "sales_of_electricity_by_rate_schedules_account_444_public_street_and_highway_lighting_304_instant",
    "sales_of_electricity_by_rate_schedules_account_445_other_sales_to_public_authorities_304_duration",
    "sales_of_electricity_by_rate_schedules_account_445_other_sales_to_public_authorities_304_instant",
    "sales_of_electricity_by_rate_schedules_account_446_sales_to_railroads_and_railways_304_duration",
    "sales_of_electricity_by_rate_schedules_account_446_sales_to_railroads_and_railways_304_instant",
    "sales_of_electricity_by_rate_schedules_account_448_interdepartmental_sales_304_duration",
    "sales_of_electricity_by_rate_schedules_account_448_interdepartmental_sales_304_instant",
    "sales_of_electricity_by_rate_schedules_account_4491_provision_for_rate_refunds_304_duration",
    "sales_of_electricity_by_rate_schedules_account_4491_provision_for_rate_refunds_304_instant",
    "sales_of_electricity_by_rate_schedules_account_totals_304_duration",
    "sales_of_electricity_by_rate_schedules_account_totals_304_instant",
    "sales_of_electricity_by_rate_schedules_historical_data_304_duration",
    "sales_of_electricity_by_rate_schedules_historical_data_304_instant",
    "sales_of_electricity_by_rate_schedules_historical_data_totals_304_duration",
    "sales_of_electricity_by_rate_schedules_historical_data_totals_304_instant",
    "sales_for_resale_account_447_310_duration",
    "sales_for_resale_account_447_310_instant",
    "sales_for_resale_account_447_total_310_duration",
    "sales_for_resale_account_447_total_310_instant",
    "electric_operations_and_maintenance_expenses_320_duration",
    "electric_operations_and_maintenance_expenses_320_instant",
    "purchased_power_326_duration",
    "purchased_power_326_instant",
    "purchased_power_totals_326_duration",
    "purchased_power_totals_326_instant",
    "transmission_of_electricity_for_others_328_duration",
    "transmission_of_electricity_for_others_328_instant",
    "transmission_of_electricity_for_others_totals_328_duration",
    "transmission_of_electricity_for_others_totals_328_instant",
    "transmission_of_electricity_by_iso_rtos_331_duration",
    "transmission_of_electricity_by_iso_rtos_331_instant",
    "transmission_of_electricity_by_iso_rtos_totals_331_duration",
    "transmission_of_electricity_by_iso_rtos_totals_331_instant",
    "transmission_of_electricity_by_others_332_duration",
    "transmission_of_electricity_by_others_332_instant",
    "transmission_of_electricity_by_others_totals_332_duration",
    "transmission_of_electricity_by_others_totals_332_instant",
    "miscellaneous_general_expenses_335_duration",
    "miscellaneous_general_expenses_335_instant",
    "miscellaneous_general_expenses_totals_335_duration",
    "miscellaneous_general_expenses_totals_335_instant",
    "basis_for_amortization_changes_section_b_336_duration",
    "basis_for_amortization_changes_section_b_336_instant",
    "factors_used_in_estimating_depreciation_charges_section_c_336_duration",
    "factors_used_in_estimating_depreciation_charges_section_c_336_instant",
    "summary_of_depreciation_and_amortization_charges_section_a_336_duration",
    "summary_of_depreciation_and_amortization_charges_section_a_336_instant",
    "regulatory_commission_expenses_350_duration",
    "regulatory_commission_expenses_350_instant",
    "regulatory_commission_expenses_total_350_duration",
    "regulatory_commission_expenses_total_350_instant",
    "research_development_and_demonstration_activities_352_duration",
    "research_development_and_demonstration_activities_352_instant",
    "distribution_of_salaries_and_wages_354_duration",
    "distribution_of_salaries_and_wages_354_instant",
    "distribution_of_salaries_and_wages_other_accounts_354_duration",
    "distribution_of_salaries_and_wages_other_accounts_354_instant",
    "common_utility_plant_and_expenses_356_duration",
    "common_utility_plant_and_expenses_356_instant",
    "amounts_included_in_iso_rto_settlement_statements_397_duration",
    "amounts_included_in_iso_rto_settlement_statements_397_instant",
    "amounts_included_in_iso_rto_settlement_statements_other_397_duration",
    "amounts_included_in_iso_rto_settlement_statements_other_397_instant",
    "purchases_and_sales_of_ancillary_services_398_duration",
    "purchases_and_sales_of_ancillary_services_398_instant",
    "monthly_transmission_system_peak_load_400_duration",
    "monthly_transmission_system_peak_load_400_instant",
    "monthly_iso_rto_transmission_system_peak_load_400a_duration",
    "monthly_iso_rto_transmission_system_peak_load_400a_instant",
    "electric_energy_account_401a_duration",
    "electric_energy_account_401a_instant",
    "monthly_peaks_and_output_401b_duration",
    "monthly_peaks_and_output_401b_instant",
    "steam_electric_generating_plant_statistics_large_plants_402_duration",
    "steam_electric_generating_plant_statistics_large_plants_402_instant",
    "steam_electric_generating_plant_statistics_large_plants_fuel_statistics_402_duration",
    "steam_electric_generating_plant_statistics_large_plants_fuel_statistics_402_instant",
    "hydroelectric_generating_plant_statistics_large_plants_406_duration",
    "hydroelectric_generating_plant_statistics_large_plants_406_instant",
    "pumped_storage_generating_plant_statistics_large_plants_408_duration",
    "pumped_storage_generating_plant_statistics_large_plants_408_instant",
    "generating_plant_statistics_410_duration",
    "generating_plant_statistics_410_instant",
    "energy_storage_operations_large_plants_414_duration",
    "energy_storage_operations_large_plants_414_instant",
    "energy_storage_operations_large_plants_totals_414_duration",
    "energy_storage_operations_large_plants_totals_414_instant",
    "transmission_line_statistics_422_duration",
    "transmission_line_statistics_422_instant",
    "transmission_line_statistics_totals_422_duration",
    "transmission_line_statistics_totals_422_instant",
    "transmission_lines_added_during_year_424_duration",
    "transmission_lines_added_during_year_424_instant",
    "transmission_lines_added_during_year_total_424_duration",
    "transmission_lines_added_during_year_total_424_instant",
    "substations_426_duration",
    "substations_426_instant",
    "substations_total_426_duration",
    "substations_total_426_instant",
    "transactions_with_associated_affiliated_companies_provided_by_429_duration",
    "transactions_with_associated_affiliated_companies_provided_by_429_instant",
    "transactions_with_associated_affiliated_companies_provided_for_429_duration",
    "transactions_with_associated_affiliated_companies_provided_for_429_instant",
]
