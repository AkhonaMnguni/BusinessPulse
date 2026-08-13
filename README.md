# BusinessPulse
BusinessPulse does not determine that a person committed fraud. It detects unusual patterns, calculates a risk/suspicion score, explains the reasons for the score, and sends the case to a human for investigation.

## An Explainable Data Engineering Platform for Business Monitoring, Anomaly Detection and Investigation Support

--- 

## Project Overview

**BusinessPulse** is an end-to-end data engineering and business intelligence platform designed to help businesses identify unusual financial and operational activity before it develops into significant losses.

The system combines data from:

* Sales
* Purchases
* Suppliers
* Invoices
* Payments
* Inventory
* Branches
* Employees
* Purchase orders
* Approvals
* Product prices

BusinessPulse analyses these records using:

* Data validation
* ETL pipelines
* SQL analytics
* Historical comparisons
* Peer comparisons
* Statistical anomaly detection
* Business rules
* Risk scoring
* Optional machine-learning techniques

The platform produces **explainable anomaly alerts** and **investigation cases** for authorised human reviewers.

> **Important:**BusinessPulse does not determine that a person committed fraud. It identifies unusual patterns that require investigation.

---

# Project Name

##     BusinessPulse



### Alternative Project Name

**Business Sentinel**

> **Business Sentinel** represents a system that continuously watches business activity and identifies unusual patterns that may require attention.

If a more professional, portfolio-friendly name is required, the recommended name is:

# **Business Sentinel**

---

# Core Principle

> **Anomaly ≠ Fraud**

The system does not automatically accuse employees, suppliers, managers, customers or other individuals of fraud or misconduct.

Instead, it answers:

> **What changed, why did it change, and should someone investigate?**

An unusual pattern can have many legitimate explanations, including:

* Inflation
* Exchange-rate movements
* Supplier price changes
* Business expansion
* Seasonal demand
* Transportation costs
* Changes in purchasing policies
* Data-entry errors
* Inventory-counting errors
* New suppliers
* Changes in customer demand

Every high-risk alert therefore requires human review.

---

# Problem Statement

Businesses generate large amounts of financial and operational data every day.

Sales, purchases, invoices, supplier payments, inventory movements and employee approvals may each appear normal when examined individually.

However, important patterns can become visible when these records are combined.

For example, an invoice may contain:

```text
Valid supplier
Valid invoice number
Valid amount
Valid purchase order
Valid approval
```

The transaction may appear completely normal.

However, after comparing it with other business information, the system may discover:

```text
Supplier recently introduced
        +
Price significantly above peer branches
        +
Branch spending increased sharply
        +
Same employee approves most invoices
        +
Inventory did not increase proportionally
```

None of these indicators independently proves wrongdoing.

Together, however, they create a pattern that deserves investigation.

Business Sentinel addresses this problem by integrating business data into a centralized data platform and transforming that data into **explainable business intelligence and investigation alerts**.

---

# Project Objectives

The project aims to:

1. Build a repeatable data ingestion pipeline.
2. Integrate multiple business data sources.
3. Validate incoming records.
4. Detect data-quality problems.
5. Transform raw data into analytical datasets.
6. Store structured data in PostgreSQL.
7. Implement a relational database design.
8. Analyse historical business behaviour.
9. Compare suppliers and branches.
10. Detect unusual financial activity.
11. Detect inventory inconsistencies.
12. Detect duplicate invoices.
13. Identify unusual supplier pricing.
14. Identify approval concentration.
15. Identify potential segregation-of-duties weaknesses.
16. Calculate explainable anomaly risk scores.
17. Generate investigation cases.
18. Provide an interactive dashboard.
19. Provide an API for accessing analytical results.
20. Maintain an audit trail.
21. Demonstrate object-oriented programming.
22. Demonstrate automated testing.
23. Demonstrate CI/CD.
24. Demonstrate Docker-based deployment.
25. Maintain a clear separation between anomaly detection and fraud determination.

---

# Key Features

## 1. Automated Data Ingestion

The system can ingest data from sources such as:

```text
CSV
Excel
REST APIs
PostgreSQL
```

The initial implementation can focus on CSV and Excel while maintaining an architecture that allows additional sources to be added later.

---

# 2. Data Quality Monitoring

Every incoming dataset is validated before entering the analytical database.

Example checks include:

```text
Missing supplier IDs
Missing branch IDs
Duplicate invoices
Negative amounts
Invalid quantities
Future transaction dates
Unknown products
Unknown suppliers
Unknown branches
Invalid dates
Invalid currencies
```

Example report:

```text
DATA QUALITY REPORT
────────────────────────────────

Records processed:       125,430

Valid records:           123,811
Invalid records:           1,619

Duplicate invoices:          187
Missing supplier IDs:        231
Negative amounts:             43
Future dates:                 71
Invalid quantities:           92
Unknown branches:             16

Overall quality:           98.7%
```

Invalid records are moved to a quarantine area rather than being silently discarded.

---

# 3. Historical Spending Analysis

The system establishes normal spending patterns for:

* Branches
* Suppliers
* Products
* Departments
* Time periods

Example:

```text
Historical monthly expenditure

R3,000,000
R3,200,000
R3,100,000
R3,400,000
```

Current month:

```text
R9,000,000
```

The system detects a significant deviation from historical behaviour.

---

# 4. Supplier Price Analysis

The system compares current prices against:

* Historical supplier prices
* Branch prices
* Peer suppliers
* Product averages
* Median prices

Example:

```text
Supplier A       R10,000
Supplier B       R10,500
Supplier C       R10,200

Current supplier R17,000
```

The system identifies a significant price variance.

Example explanation:

```text
PRICE_VARIANCE

Current unit price:
R17,000

Peer median:
R10,200

Difference:
+66.67%

Recommendation:
Review supplier pricing and supporting documentation.
```

---

# 5. Expense Anomaly Detection

The system detects unusual increases or decreases in business expenditure.

Example:

```text
Previous expenditure:
R3,000,000

Current expenditure:
R9,000,000

Change:
+200%
```

The system does not automatically interpret this as fraud.

It checks additional business context such as:

```text
Sales growth
Purchase quantity
Branch growth
Supplier pricing
Inventory
Historical trends
```

---

# 6. Duplicate Invoice Detection

The platform identifies potential duplicate invoices using fields such as:

```text
Supplier
Invoice number
Amount
Date
Purchase order
```

Example:

```text
Supplier:
Bright Star Supplies

Invoice:
INV-48392

Amount:
R4,500,000

Date:
2026-07-10
```

If the same invoice appears twice, the system generates:

```text
DUPLICATE_INVOICE
```

The alert is then sent for human review.

---

# 7. Inventory Variance Detection

The system compares:

```text
Purchases
+
Goods received
-
Sales
```

against actual inventory records.

Example:

```text
Units received:       1,000
Units sold:             300

Expected inventory:     700
Actual inventory:       620

Variance:                80
```

The system creates:

```text
INVENTORY_VARIANCE
```

It does not conclude that the missing inventory was stolen.

Possible explanations may include:

* Incorrect stock count
* Damaged goods
* Data-entry errors
* Unrecorded transfers
* Returns
* Incorrect sales records

---

# 8. Approval Concentration Detection

The system analyses employee approval behaviour.

Example:

```text
Total supplier invoices: 100

Employee A approvals:     91

Approval concentration:   91%
```

The system creates:

```text
APPROVAL_CONCENTRATION
```

Explanation:

> 91% of the supplier's invoices were approved by the same employee. Review whether this concentration is consistent with the organisation's approval policy.

The system does not label the employee as corrupt or fraudulent.

---

# 9. Separation-of-Duties Monitoring

The system identifies situations where one employee performs multiple activities in the same procurement process.

For example:

```text
Employee A
    │
    ├── Selected supplier
    │
    ├── Created purchase order
    │
    ├── Approved invoice
    │
    └── Approved payment
```

This creates a:

```text
DUTY_CONCENTRATION
```

indicator.

The system recommends reviewing the activity against the organisation's segregation-of-duties policy.

---

# 10. Supplier Risk Profiles

Each supplier receives a business-monitoring profile.

Example:

```text
SUPPLIER MONITORING PROFILE
────────────────────────────────

Supplier:
Bright Star Supplies

Total spend:
R47,000,000

Year-on-year growth:
+182%

Average price variance:
+38%

Branch concentration:
83%

Approval concentration:
91%

Duplicate invoices:
2

Anomaly indicators:
5

Monitoring level:
HIGH ATTENTION
```

The monitoring level describes the degree of unusual activity detected.

It is not a fraud verdict.

---

# 11. Explainable Risk Scoring

The system calculates an **Anomaly Risk Score** from 0 to 100.

Example scoring model:

| Indicator              | Maximum Score |
| ---------------------- | ------------: |
| Price anomaly          |            20 |
| Expense anomaly        |            20 |
| Supplier concentration |            15 |
| Approval concentration |            15 |
| Inventory variance     |            15 |
| Duplicate transaction  |            15 |
| **Total**              |       **100** |

Risk levels:

|  Score | Level    |
| -----: | -------- |
|   0–24 | NORMAL   |
|  25–49 | LOW      |
|  50–69 | MEDIUM   |
|  70–84 | HIGH     |
| 85–100 | CRITICAL |

The score represents:

> **How unusual the observed business activity is.**

It does not represent:

> **The probability that someone committed fraud.**

---

# 12. Statistical Anomaly Detection

The system can use statistical techniques such as:

* Z-scores
* Moving averages
* Percentage change
* Median comparison
* Standard deviation
* Rolling averages
* Historical baselines

Example:

```text
Historical expenditure:

R3M
R3.2M
R3.1M
R3.4M

Current:

R9M
```

A statistical model can identify the current value as significantly different from historical behaviour.

---

# 13. Machine Learning

An optional machine-learning layer can be added after the rule-based system is working correctly.

A suitable unsupervised technique is:

```text
Isolation Forest
```

Potential features include:

```text
invoice_amount
unit_price
quantity
supplier_age_days
supplier_spend_30d
supplier_spend_90d
price_vs_supplier_mean
price_vs_branch_median
expense_growth_rate
approval_concentration
supplier_concentration
duplicate_invoice_flag
inventory_variance
sales_growth_rate
```

The machine-learning model provides another signal.

The project should still maintain explainability through business rules and statistical indicators.

---

# 14. Explainable Alerts

The system should never produce an unexplained alert such as:

```text
ALERT!!!
```

Instead:

```text
HIGH PRIORITY REVIEW
────────────────────────────────

Anomaly Risk Score:
86 / 100

Why was this case created?

1. Cleaning expenses increased by 200%.

2. Unit prices are 61% above comparable
   branch prices.

3. Supplier spending increased significantly.

4. 91% of supplier invoices were approved
   by the same employee.

5. Purchase volume increased by only 5%.

Interpretation:

The current purchasing pattern differs significantly
from historical and peer behaviour.

Recommended action:

Review supplier pricing, invoices, purchase orders,
goods-received records, inventory records and
approval history.

Important:

This alert does not establish fraud or misconduct.
Human investigation is required.
```

---

# 15. Investigation Case Management

Alerts are converted into investigation cases.

Example:

```text
CASE SB-2026-00127

Status:
OPEN

Anomaly Risk Score:
86 / 100

Priority:
CRITICAL

Subject:
Supplier transaction activity

────────────────────────────────

Indicators:

✓ Expense increase
✓ Price variance
✓ Supplier concentration
✓ Approval concentration
✓ Inventory variance

────────────────────────────────

Recommended investigation:

[ ] Review original invoices
[ ] Verify supplier registration
[ ] Verify goods received
[ ] Compare market prices
[ ] Review purchase orders
[ ] Review approval policy
[ ] Review inventory records
[ ] Document explanation
```

---

# 16. Case Resolution

An authorised investigator can classify a case as:

```text
FALSE POSITIVE
EXPLAINED BUSINESS CHANGE
DATA QUALITY ISSUE
PROCESS ISSUE
POLICY ISSUE
REQUIRES FURTHER REVIEW
REFERRED TO AUDIT
CONFIRMED LOSS
OTHER
```

The system records the human decision in the case history.

---

# 17. System Architecture

```text
                         BUSINESS SENTINEL
                                │
        ┌───────────────────────┼───────────────────────┐
        │                       │                       │
       SALES                 PURCHASES              INVENTORY
        │                       │                       │
        ├──────────────── SUPPLIERS ───────────────────┤
        │                       │                       │
        └────────────────── BRANCHES ──────────────────┘
                                │
                                ▼
                       DATA INGESTION
                                │
                                ▼
                       BRONZE / RAW DATA
                                │
                                ▼
                      DATA QUALITY ENGINE
                                │
                    ┌───────────┴───────────┐
                    │                       │
                  VALID                   INVALID
                    │                       │
                    ▼                       ▼
              TRANSFORMATION           QUARANTINE
                    │
                    ▼
                 SILVER
                    │
                    ▼
                  GOLD
                    │
          ┌─────────┼─────────┐
          ▼         ▼         ▼
         SQL    Statistics    ML
          │         │         │
          └─────────┼─────────┘
                    ▼
               RISK ENGINE
                    │
                    ▼
             EXPLAINABILITY
                    │
                    ▼
          INVESTIGATION CASE
                    │
                    ▼
                 FLASK API
                    │
                    ▼
              WEB DASHBOARD
                    │
                    ▼
             HUMAN INVESTIGATOR
                    │
                    ▼
              CASE OUTCOME
                    │
                    ▼
               AUDIT TRAIL
```

---

# 18. Data Pipeline Architecture

The project follows a modern layered data architecture.

```text
Source Data
    │
    ▼
Bronze
Raw, unchanged source records
    │
    ▼
Silver
Validated and transformed records
    │
    ▼
Gold
Business-ready analytical datasets
    │
    ▼
Risk and Analytics
    │
    ▼
Dashboard / API
```

---

# 19. Bronze Layer

The Bronze layer stores source data in its original form.

Examples:

```text
raw_sales
raw_purchases
raw_invoices
raw_suppliers
raw_inventory
raw_employees
```

The purpose is to maintain traceability back to the original source.

---

# 20. Silver Layer

The Silver layer contains validated and standardized data.

Examples:

```text
clean_sales
clean_purchases
clean_invoices
clean_suppliers
clean_inventory
```

Typical transformations include:

* Standardizing column names
* Converting dates
* Converting numeric values
* Removing accidental duplicates
* Validating foreign keys
* Standardizing currencies
* Handling missing values

---

# 21. Gold Layer

The Gold layer contains analytical datasets.

Examples:

```text
monthly_supplier_spend
branch_spending_summary
product_price_analysis
supplier_risk_profile
inventory_variance_summary
employee_approval_summary
anomaly_cases
```

These tables/views are designed for dashboards and business analysis.

---

# 22. Database Design

The platform uses PostgreSQL as the primary relational database.

Core entities include:

```text
branches
employees
suppliers
products
purchase_orders
invoices
purchase_items
approvals
payments
sales
inventory_transactions
investigation_cases
risk_indicators
system_audit_log
supplier_history
```

---

# 23. Entity Relationships

```text
BRANCH
   │
   ├──────── PURCHASE_ORDER
   │                │
   │                └──────── SUPPLIER
   │
   ├──────── INVOICE
   │                │
   │                ├──────── SUPPLIER
   │                │
   │                └──────── PURCHASE_ITEM
   │                             │
   │                             └──────── PRODUCT
   │
   ├──────── SALES
   │
   └──────── INVENTORY_TRANSACTION


EMPLOYEE
   │
   └──────── APPROVAL
                    │
                    └──────── INVOICE


INVOICE
   │
   └──────── PAYMENT


INVESTIGATION_CASE
   │
   └──────── RISK_INDICATOR
```

---

# 24. Core Database Tables

## Branches

Stores business branch information.

```text
branch_id
branch_code
branch_name
location
created_at
```

---

## Employees

Stores employee information required for approval and process analysis.

```text
employee_id
employee_code
full_name
department
role
active
created_at
```

---

## Suppliers

Stores supplier information.

```text
supplier_id
supplier_code
supplier_name
registration_date
status
created_at
```

---

## Products

Stores products and categories.

```text
product_id
product_code
product_name
category
unit
```

---

## Purchase Orders

Stores procurement orders.

```text
purchase_order_id
po_number
supplier_id
branch_id
requested_by
order_date
status
```

---

## Invoices

Stores supplier invoices.

```text
invoice_id
invoice_number
supplier_id
purchase_order_id
branch_id
invoice_date
total_amount
currency
```

---

## Purchase Items

Stores individual products purchased on an invoice.

```text
purchase_item_id
invoice_id
product_id
quantity
unit_price
total_amount
```

---

## Approvals

Stores invoice approval activity.

```text
approval_id
invoice_id
employee_id
approval_type
approved_at
```

---

## Payments

Stores supplier payments.

```text
payment_id
invoice_id
payment_date
amount
payment_method
reference
```

---

## Sales

Stores business sales.

```text
sale_id
branch_id
product_id
sale_date
quantity
revenue
```

---

## Inventory Transactions

Stores inventory movements.

```text
inventory_transaction_id
branch_id
product_id
transaction_type
quantity
transaction_date
reference
```

---

# 25. Investigation Cases

The investigation system uses a dedicated case table.

```text
case_id
case_number
created_at
severity
status
risk_score
subject_type
subject_id
summary
explanation
assigned_to
reviewed_at
resolution
```

---

# 26. Risk Indicators

Each case can contain multiple supporting indicators.

```text
indicator_id
case_id
indicator_type
indicator_score
description
evidence_reference
created_at
```

Example:

```text
Case:
SB-2026-00127

Indicators:

PRICE_VARIANCE
20 points

EXPENSE_SPIKE
20 points

APPROVAL_CONCENTRATION
15 points

INVENTORY_VARIANCE
15 points
```

---

# 27. Audit Trail

The system maintains an audit trail of important actions.

Examples:

```text
ETL_STARTED
ETL_COMPLETED
ALERT_CREATED
CASE_OPENED
CASE_ASSIGNED
CASE_REVIEWED
CASE_RESOLVED
DATA_CORRECTED
```

This makes the platform traceable and auditable.

---

# 28. Technology Stack

## Programming

```text
Python 3.12+
SQL
HTML
CSS
JavaScript
```

## Data Engineering

```text
Pandas
NumPy
SQLAlchemy
PostgreSQL
```

## Analytics

```text
SciPy
scikit-learn
Plotly
```

## Backend

```text
Flask
Gunicorn
```

## Testing

```text
pytest
pytest-cov
```

## DevOps

```text
Docker
Docker Compose
Git
GitHub Actions
Make
```

---

# 29. Recommended Project Structure

```text
business-sentinel/
│
├── README.md
├── LICENSE
├── .gitignore
├── .env.example
├── requirements.txt
├── Makefile
├── Dockerfile
├── docker-compose.yml
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── config/
│   ├── __init__.py
│   └── settings.py
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── quarantine/
│
├── src/
│   └── business_sentinel/
│       ├── __init__.py
│       │
│       ├── api/
│       │   ├── __init__.py
│       │   └── routes.py
│       │
│       ├── etl/
│       │   ├── __init__.py
│       │   ├── extract.py
│       │   ├── transform.py
│       │   ├── validate.py
│       │   ├── load.py
│       │   └── pipeline.py
│       │
│       ├── analytics/
│       │   ├── __init__.py
│       │   ├── expense_analysis.py
│       │   ├── supplier_analysis.py
│       │   ├── branch_analysis.py
│       │   ├── inventory_analysis.py
│       │   └── anomaly_detection.py
│       │
│       ├── risk/
│       │   ├── __init__.py
│       │   ├── rules.py
│       │   ├── scoring.py
│       │   ├── explanations.py
│       │   └── case_manager.py
│       │
│       ├── database/
│       │   ├── __init__.py
│       │   ├── connection.py
│       │   ├── repositories.py
│       │   └── models.py
│       │
│       └── services/
│           ├── __init__.py
│           ├── supplier_service.py
│           ├── investigation_service.py
│           └── dashboard_service.py
│
├── sql/
│   ├── schema.sql
│   ├── indexes.sql
│   ├── views.sql
│   └── seed.sql
│
├── dashboard/
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── alerts.html
│   │   ├── cases.html
│   │   ├── suppliers.html
│   │   └── branches.html
│   │
│   └── static/
│       ├── css/
│       │   └── style.css
│       └── js/
│           └── dashboard.js
│
├── tests/
│   ├── test_etl.py
│   ├── test_validation.py
│   ├── test_anomaly_detection.py
│   ├── test_scoring.py
│   ├── test_database.py
│   └── test_api.py
│
└── docs/
    ├── architecture.md
    ├── data_dictionary.md
    ├── anomaly_methodology.md
    └── investigation_process.md
```

---

# 30. Object-Oriented Design

The project uses object-oriented programming to separate responsibilities.

Core classes include:

```text
DataExtractor
DataValidator
DataTransformer
DataLoader

AnomalyDetector
ExpenseAnomalyDetector
PriceAnomalyDetector
InventoryAnomalyDetector
DuplicateInvoiceDetector

RiskScorer
CaseManager
ExplanationGenerator

SupplierRepository
InvoiceRepository
CaseRepository

SupplierService
InvestigationService
DashboardService
```

---

# 31. OOP Principles Demonstrated

The implementation demonstrates:

### Encapsulation

Data and behaviour are grouped within classes.

### Abstraction

Common interfaces are defined for extractors and anomaly detectors.

### Inheritance

Specialised detectors inherit from common detector interfaces.

### Polymorphism

Different anomaly detectors can be executed through the same interface.

---

# 32. Anomaly Detection Strategy

The system uses multiple detection approaches.

```text
Business Rules
      +
Statistical Analysis
      +
Peer Comparison
      +
Historical Analysis
      +
Machine Learning
```

These signals are combined by the risk engine.

---

# 33. Example Detection Rules

## Expense Spike

```text
IF current expenditure is significantly
higher than historical expenditure
THEN create EXPENSE_SPIKE indicator.
```

---

## Price Variance

```text
IF current unit price is significantly
above peer median
THEN create PRICE_VARIANCE indicator.
```

---

## Duplicate Invoice

```text
IF supplier + invoice number already exists
THEN create DUPLICATE_INVOICE indicator.
```

---

## Approval Concentration

```text
IF one employee approves an unusually
large percentage of supplier invoices
THEN create APPROVAL_CONCENTRATION indicator.
```

---

## Inventory Variance

```text
IF expected inventory differs significantly
from recorded inventory
THEN create INVENTORY_VARIANCE indicator.
```

---

# 34. Example Risk Calculation

```text
Expense anomaly                 20
Price anomaly                   20
Approval concentration          15
Inventory variance              15
Supplier concentration          15
Duplicate transaction            0
                              ----
Total                           85
```

Result:

```text
CRITICAL
```

Explanation:

```text
Five independent business indicators
contribute to the anomaly score.

Human investigation is required.
```

---

# 35. Dashboard

The dashboard contains the following sections:

## Executive Overview

```text
TOTAL SPEND
R284M

MONTHLY SPEND
R31M

OPEN CASES
17

HIGH PRIORITY
4

DATA QUALITY
98.7%
```

---

## Expense Trend

Shows expenditure over time.

```text
Monthly Spend
│
│                   █
│                   █
│          █        █
│    █     █        █
│    █  █  █        █
└────────────────────────
```

---

## Supplier Analysis

Displays:

* Total supplier spend
* Supplier growth
* Average price variance
* Supplier concentration
* Invoice count
* Duplicate invoices

---

## Branch Analysis

Displays:

* Branch spending
* Sales
* Expense growth
* Inventory variance
* Supplier concentration

---

## Investigation Dashboard

Displays:

```text
Case
Severity
Risk score
Status
Subject
Created date
Assigned investigator
```

---

# 36. Investigation Case Example

```text
CASE SB-2026-00127
────────────────────────────────────

Severity:
CRITICAL

Risk Score:
86 / 100

Status:
OPEN

Subject:
Supplier purchasing activity

────────────────────────────────────

Indicators

EXPENSE_SPIKE
20 points

PRICE_VARIANCE
20 points

APPROVAL_CONCENTRATION
15 points

SUPPLIER_CONCENTRATION
15 points

INVENTORY_VARIANCE
15 points

────────────────────────────────────

Explanation

The supplier's current activity differs
significantly from historical and peer
business behaviour.

────────────────────────────────────

Recommended Investigation

□ Review invoices
□ Review purchase orders
□ Verify goods received
□ Compare supplier pricing
□ Review inventory records
□ Review approval history
□ Document findings
```

---

# 37. REST API

The application exposes REST endpoints.

```text
GET /api/dashboard
GET /api/expenses
GET /api/suppliers
GET /api/branches
GET /api/alerts
GET /api/cases
GET /api/cases/<case_id>
POST /api/cases/<case_id>/review
POST /api/cases/<case_id>/resolve
```

---

# 38. Example API Response

```json
{
  "case_number": "SB-2026-00127",
  "severity": "CRITICAL",
  "risk_score": 86,
  "status": "OPEN",
  "requires_human_review": true,
  "indicators": [
    {
      "type": "PRICE_VARIANCE",
      "score": 20,
      "description": "Unit price is 63% above peer median."
    },
    {
      "type": "EXPENSE_SPIKE",
      "score": 20,
      "description": "Monthly expense increased by 197%."
    },
    {
      "type": "APPROVAL_CONCENTRATION",
      "score": 15,
      "description": "91% of invoices were approved by one employee."
    }
  ]
}
```

---

# 39. Database Constraints

The database uses appropriate:

```text
PRIMARY KEY
FOREIGN KEY
NOT NULL
UNIQUE
CHECK
INDEX
```

constraints.

Examples:

```text
supplier_code UNIQUE
invoice_number UNIQUE per supplier
employee_code UNIQUE
product_code UNIQUE
```

---

# 40. Database Performance

Indexes should be created for frequently queried fields.

Examples:

```text
supplier_id
branch_id
invoice_date
employee_id
product_id
case status
risk score
```

This improves performance when analysing large transaction datasets.

---

# 41. SQL Analytics

Example supplier spending query:

```sql
SELECT
    s.supplier_name,
    DATE_TRUNC('month', i.invoice_date) AS month,
    SUM(i.total_amount) AS total_spend
FROM invoices i
JOIN suppliers s
    ON i.supplier_id = s.supplier_id
GROUP BY
    s.supplier_name,
    DATE_TRUNC('month', i.invoice_date)
ORDER BY
    month,
    total_spend DESC;
```

---

# 42. Branch Spending Query

```sql
SELECT
    b.branch_name,
    SUM(i.total_amount) AS total_spend
FROM invoices i
JOIN branches b
    ON i.branch_id = b.branch_id
GROUP BY
    b.branch_name
ORDER BY
    total_spend DESC;
```

---

# 43. Approval Concentration Query

```sql
SELECT
    e.full_name,
    COUNT(*) AS approvals,
    ROUND(
        COUNT(*) * 100.0 /
        SUM(COUNT(*)) OVER (),
        2
    ) AS approval_percentage
FROM approvals a
JOIN employees e
    ON a.employee_id = e.employee_id
GROUP BY
    e.full_name
ORDER BY
    approvals DESC;
```

---

# 44. Data Quality Philosophy

The system follows the principle:

> **Never silently discard bad data.**

Invalid records should be:

```text
Detected
      ↓
Logged
      ↓
Quarantined
      ↓
Investigated
      ↓
Corrected or rejected
```

This ensures data lineage and traceability.

---

# 45. Error Handling

The system should handle:

* Missing files
* Invalid CSV structures
* Invalid dates
* Missing fields
* Database connection errors
* Duplicate records
* Invalid foreign keys
* Unexpected API responses

Errors should be logged using Python's logging framework.

---

# 46. Logging

Example:

```text
2026-08-13 09:00:01 INFO  ETL pipeline started
2026-08-13 09:00:03 INFO  Loaded 125430 records
2026-08-13 09:00:04 WARNING 1619 invalid records found
2026-08-13 09:00:05 INFO  Valid records transformed
2026-08-13 09:00:08 INFO  PostgreSQL load completed
2026-08-13 09:00:10 INFO  Anomaly detection started
2026-08-13 09:00:14 INFO  27 investigation cases created
2026-08-13 09:00:14 INFO  ETL pipeline completed
```

---

# 47. Testing

The project uses `pytest`.

Tests cover:

```text
ETL
Data validation
Transformations
Anomaly detection
Risk scoring
Database schema
API endpoints
Case management
```

Example:

```python
def test_percentage_change():

    previous = 3_000_000
    current = 9_000_000

    result = percentage_change(
        previous,
        current
    )

    assert result == 200
```

---

# 48. CI/CD

GitHub Actions automatically:

```text
Checkout code
       ↓
Install dependencies
       ↓
Run tests
       ↓
Run coverage
       ↓
Compile application
       ↓
Build Docker image
```

The purpose is to ensure that every change can be tested consistently.

---

# 49. Docker

The application can be run using Docker Compose.

```text
┌─────────────────────┐
│ Flask Application   │
│ Port 5000           │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ PostgreSQL          │
│ Port 5432           │
└─────────────────────┘
```

---

# 50. Environment Variables

Sensitive configuration must not be committed to Git.

Use:

```text
.env
```

for local development and:

```text
.env.example
```

as a template.

Example:

```text
DATABASE_URL=postgresql://user:password@localhost:5432/business_sentinel
FLASK_ENV=development
SECRET_KEY=change-me
```

The real `.env` file must be included in `.gitignore`.

---

# 51. Makefile

The project should provide simple commands:

```bash
make install
make test
make coverage
make etl
make run
make lint
make docker-up
make docker-down
```

This provides a consistent development workflow.

---

# 52. CI Pipeline Stages

The CI pipeline should follow:

```text
test
    ↓
build
    ↓
docker
```

The pipeline should fail if:

* Tests fail
* Python code cannot compile
* Required dependencies cannot install
* Docker build fails

---

# 53. Security

The project considers:

```text
Authentication
Authorization
Role-based access
Input validation
Secret management
Database permissions
Audit logging
```

Suggested roles:

```text
ADMIN
BUSINESS_OWNER
AUDITOR
INVESTIGATOR
ANALYST
VIEWER
```

---

# 54. Ethical Design

Business monitoring systems can cause significant harm if their outputs are presented as facts when they are only predictions or anomalies.

Therefore, Business Sentinel follows these principles:

### No automatic accusations

The system never automatically labels an individual as fraudulent.

### Explainability

Every case must contain the indicators that caused the alert.

### Human review

High-risk cases require authorised human investigation.

### Evidence traceability

Indicators should reference the underlying transaction or analytical evidence.

### Data quality awareness

Poor-quality data should reduce confidence in conclusions.

### Auditability

Changes to cases and investigation outcomes are recorded.

---

# 55. Example End-to-End Scenario

A branch normally spends:

```text
R3,000,000 per month
```

on cleaning supplies.

Historical sales:

```text
R50,000,000 per month
```

A new month arrives.

The system detects:

```text
Cleaning expenditure:
R9,000,000

Sales:
R52,000,000

Expense growth:
+200%

Sales growth:
+4%

Purchase quantity:
+5%

Supplier unit price:
R18,000

Peer median:
R10,500

Approval concentration:
91%
```

The system generates:

```text
EXPENSE_SPIKE
PRICE_VARIANCE
APPROVAL_CONCENTRATION
SUPPLIER_CONCENTRATION
```

Risk engine:

```text
20
+
20
+
15
+
15
+
15
=
85
```

Result:

```text
CRITICAL REVIEW
```

The investigator receives:

> Multiple independent indicators suggest that the current purchasing pattern differs significantly from historical and peer behaviour.

The investigator can then review the supporting evidence.

---

# 56. What the System Does Not Do

Business Sentinel does **not**:

* Automatically accuse people of fraud
* Automatically terminate employees
* Automatically block payments
* Automatically report individuals to authorities
* Treat anomaly scores as proof
* Replace auditors
* Replace investigators
* Replace management decisions

The platform is an **investigation-support and business-monitoring system**.

---

# 57. Expected Outputs

The completed project should produce:

```text
1. Working ETL pipeline
2. PostgreSQL database
3. Data-quality reports
4. Analytical SQL views
5. Statistical anomaly detection
6. Risk scoring engine
7. Investigation cases
8. Explainable alerts
9. Flask REST API
10. Interactive dashboard
11. Automated tests
12. CI/CD pipeline
13. Docker environment
14. Database documentation
15. Data dictionary
16. Architecture documentation
17. Investigation methodology
18. Audit trail
```

---

# 58. Project Success Criteria

The project will be considered successful when it can:

* Ingest raw business data.
* Validate incoming records.
* Quarantine invalid data.
* Transform valid records.
* Load data into PostgreSQL.
* Run analytical SQL queries.
* Detect unusual business activity.
* Calculate anomaly risk scores.
* Explain why a case was generated.
* Create investigation cases.
* Display cases on a dashboard.
* Allow authorised users to record case outcomes.
* Maintain an audit history.
* Pass automated tests.
* Run inside Docker.
* Execute through a repeatable Makefile workflow.
* Pass the CI pipeline.

---

# 59. Assessment Alignment

The project directly supports the three formative assessment learning outcomes.

| Learning Outcome            | Business Sentinel Implementation                             |
| --------------------------- | ------------------------------------------------------------ |
| Build Pipelines / Scripting | ETL pipeline, Makefile, CI/CD, Docker                        |
| OOP                         | Extractors, validators, detectors, services and repositories |
| Relational Database Design  | PostgreSQL schema, relationships, constraints and indexes    |

---

# 60. Build and Release Management

The development process follows:

```text
Developer
    │
    ▼
Git commit
    │
    ▼
GitHub
    │
    ▼
CI Pipeline
    │
    ├── Tests
    │
    ├── Validation
    │
    ├── Build
    │
    └── Docker
            │
            ▼
       Deployable Image
```

---

# 61. Useful Commands

Install dependencies:

```bash
make install
```

Run tests:

```bash
make test
```

Run coverage:

```bash
make coverage
```

Run the ETL pipeline:

```bash
make etl
```

Start the Flask application:

```bash
make run
```

Start Docker:

```bash
make docker-up
```

Stop Docker:

```bash
make docker-down
```

Run the application directly:

```bash
python -m business_sentinel
```

---

# 62. Example Development Workflow

```text
1. Add or modify source code
            ↓
2. Run unit tests
            ↓
3. Run ETL pipeline
            ↓
4. Validate database results
            ↓
5. Check anomaly results
            ↓
6. Review dashboard
            ↓
7. Commit changes
            ↓
8. Push to GitHub
            ↓
9. CI pipeline runs
            ↓
10. Build succeeds
```

---

# 63. Future Improvements

Potential future improvements include:

* Apache Airflow orchestration
* Cloud deployment
* AWS S3 integration
* Cloud data warehouse
* Apache Spark
* Real-time transaction streaming
* Kafka
* Advanced ML models
* Model monitoring
* Automated data lineage
* Role-based authentication
* Email notifications
* Slack notifications
* Scheduled reports
* Mobile dashboard
* Advanced supplier network analysis
* Graph-based relationship analysis

These are optional extensions and are not required for the first version.

---

# 64. Future Real-Time Architecture

A future version could support:

```text
Transaction
     │
     ▼
Kafka
     │
     ▼
Streaming Processor
     │
     ▼
Real-Time Risk Engine
     │
     ▼
Investigation Case
     │
     ▼
Dashboard
```

This would allow the system to detect unusual behaviour almost immediately.

---

# 65. Data Lineage

Every analytical result should be traceable back to its source.

Example:

```text
Dashboard Alert
      │
      ▼
Risk Indicator
      │
      ▼
Analytics View
      │
      ▼
Silver Table
      │
      ▼
Bronze Table
      │
      ▼
Original Source File
```

This provides transparency and improves auditability.

---

# 66. Data Dictionary

The project should maintain documentation describing:

```text
Table
Column
Data type
Description
Nullable
Primary key
Foreign key
Business meaning
Source
Transformation
```

Example:

| Table    | Column       | Type    | Description                      |
| -------- | ------------ | ------- | -------------------------------- |
| invoices | invoice_id   | BIGINT  | Unique invoice identifier        |
| invoices | supplier_id  | INTEGER | Supplier associated with invoice |
| invoices | total_amount | NUMERIC | Total invoice value              |
| invoices | invoice_date | DATE    | Invoice date                     |
| invoices | currency     | VARCHAR | Transaction currency             |

---

# 67. Currency

All financial examples and monetary values in the project use **South African Rand (ZAR / R)**.

Examples:

```text
R3,000,000
R9,000,000
R47,000,000
R10,500
```

Database records should use:

```text
currency = 'ZAR'
```

For example:

```text
total_amount = 4500000.00
currency = 'ZAR'
```

The project should use **Rands rather than Naira** throughout the documentation, examples, test data and dashboard.

---

# 68. Recommended Project Tagline

> **Business Sentinel — Turning Business Data Into Explainable Risk Intelligence.**

---

# 69. Final Project Statement

Business Sentinel is an end-to-end data engineering platform that transforms raw business transactions into reliable, explainable and actionable intelligence.

It combines:

```text
Data Engineering
       +
SQL
       +
Python
       +
Statistics
       +
Machine Learning
       +
Business Intelligence
       +
OOP
       +
Software Engineering
```

The system does not attempt to replace human investigators.

Instead, it helps them focus their attention on the business activities that differ most significantly from expected behaviour.

> **Business Sentinel does not ask who is guilty. It identifies what is unusual, explains why it is unusual, and helps the right person investigate.**

---

# End of README



