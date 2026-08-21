<p align="center">
  <img src="https://raw.githubusercontent.com/ather-ops/Hospital-Management-SQL/main/Assets/Hospital%20management%20.png.png" alt="Hospital Management SQL Banner" width="100%">
</p>

<h1 align="center">Hospital Management SQL</h1>

<p align="center">
  A production-style hospital management database project built with SQL, featuring relational database design, realistic healthcare data, complex queries, joins, aggregation, filtering, and analytical reporting.
</p>

---

## Project Overview

Hospital Management SQL is a relational database project designed to simulate a real-world hospital management system.

The database contains interconnected information about:

* Patients
* Doctors
* Appointments
* Treatments
* Billing

The project focuses on transforming relational healthcare data into meaningful operational, financial, and analytical insights using SQL.

The objective is not simply to store hospital records, but to answer practical questions such as:

* Which patients generate the highest spending?
* Which patients visit the hospital most frequently?
* Which patients have failed payments?
* Which patients cancel appointments most often?
* Which doctors handle the most appointments?
* Which doctors complete the most appointments?
* Which doctors generate the highest treatment revenue?
* Which doctors have the highest average treatment cost?
* Which doctors have the most cancelled appointments?
* Which doctors have the most no-show appointments?
* Which treatments are performed most frequently?
* Which treatments generate the most revenue?
* Which bills have the highest amounts?
* Which payment methods generate the most revenue?
* How does hospital activity change over time?
* What is the distribution of payment statuses?

---

## Database Structure

The database consists of five primary tables:

| Table          | Purpose                                         |
| -------------- | ----------------------------------------------- |
| `patients`     | Stores patient information                      |
| `doctors`      | Stores doctor information                       |
| `appointments` | Stores appointment records and statuses         |
| `treatments`   | Stores treatments performed and their costs     |
| `billing`      | Stores hospital billing and payment information |

### Relationships

```text
Patients
   |
   +---- Appointments ---- Doctors
             |
             +---- Treatments

Patients
   |
   +---- Billing
```

These relationships allow the project to perform multi-table analysis using SQL joins, filtering, aggregation, and grouping.

---

## SQL Concepts Used

This project demonstrates practical SQL concepts including:

* `SELECT`
* `WHERE`
* `GROUP BY`
* `ORDER BY`
* `LIMIT`
* `INNER JOIN`
* `LEFT JOIN`
* Aggregate functions:

  * `COUNT()`
  * `SUM()`
  * `AVG()`
* `ROUND()`
* `CASE WHEN`
* `strftime()`
* String concatenation
* Status-based filtering
* Multi-table analytical queries
* Date-based analysis
* CSV report generation
* Relational data analysis

---

# Phase 1: SQL Reporting

Phase 1 focused on building the analytical reporting layer of the hospital management system.

The SQL database was analyzed table by table, and the resulting analytical queries were exported into organized CSV reports.

The reporting layer currently contains **29 analytical CSV reports** across the five database tables.

```text
Patients      → 6 reports
Doctors       → 6 reports
Treatments    → 5 reports
Billing       → 7 reports
Appointments  → 5 reports
--------------------------------
Total         → 29 reports
```

---

## Analytical Reports

### Patients

Patient analysis includes reports covering:

1. Top spending patients
2. Most frequent patients
3. Patients with failed payments
4. Patients with highest appointment cancellations
5. Patient treatment analysis
6. Monthly patient visits

---

### Doctors

Doctor analysis includes reports covering:

1. Doctors with the most appointments
2. Doctors with the most completed appointments
3. Doctors with the highest treatment revenue
4. Doctors with the highest completed-treatment revenue
5. Doctors with the highest cancelled appointments
6. Doctors with the most no-show appointments

---

### Treatments

Treatment analysis includes:

1. Treatment type summary
2. Top 10 most expensive treatments
3. Top 10 cheapest treatments
4. Most common treatments
5. Treatment revenue analysis

Example treatment summary:

| Treatment     | Times Performed | Total Revenue |
| ------------- | --------------: | ------------: |
| Chemotherapy  |              49 |    128,855.68 |
| X-Ray         |              41 |    110,653.67 |
| ECG           |              38 |     96,224.24 |
| Physiotherapy |              36 |     99,418.10 |
| MRI           |              36 |    116,098.16 |

---

### Billing

Billing analysis includes:

1. Failed payments
2. Pending payments
3. Revenue by payment method
4. Monthly revenue
5. Top 10 highest bills
6. Average bill by payment method
7. Payment status summary

Example payment status summary:

| Payment Status | Number of Bills | Total Amount | Average Amount |
| -------------- | --------------: | -----------: | -------------: |
| Failed         |              67 |   193,212.94 |       2,883.78 |
| Pending        |              69 |   184,612.01 |       2,675.54 |
| Paid           |              64 |   173,424.90 |       2,709.76 |

---

### Appointments

Appointment analysis includes:

1. Patients with cancelled appointments
2. Doctors with completed appointments
3. Doctor no-show analysis
4. Monthly appointments
5. Doctors schedule summary

Example monthly appointment analysis:

| Month   | Total Appointments |
| ------- | -----------------: |
| 2023-01 |                 20 |
| 2023-02 |                 14 |
| 2023-03 |                 19 |
| 2023-04 |                 25 |
| 2023-05 |                 19 |
| 2023-06 |                 18 |
| 2023-07 |                 16 |
| 2023-08 |                 15 |
| 2023-09 |                 11 |
| 2023-10 |                 14 |
| 2023-11 |                 17 |
| 2023-12 |                 12 |

---

## Report Organization

All analytical reports are organized by database table:

```text
reports/
│
├── patients/
│   └── *.csv
│
├── doctors/
│   └── *.csv
│
├── treatments/
│   └── *.csv
│
├── billing/
│   └── *.csv
│
└── appointments/
    └── *.csv
```

This structure keeps the analytical outputs organized and makes them easier to reuse during the dashboard phase.

---

## Example Analysis

The reporting layer transforms raw hospital records into useful business questions.

For example, treatment analysis can identify which treatments are performed most frequently and how much revenue each treatment generates.

Billing analysis can identify:

* Failed payment amounts
* Pending payment amounts
* Revenue by payment method
* Highest-value bills
* Average bill amounts
* Payment-status distribution

Appointment analysis can identify:

* Cancellation patterns
* Completed appointments by doctor
* No-show patterns
* Monthly appointment volume
* Doctor scheduling workload

Doctor analysis can identify differences in appointment volume, completed appointments, treatment revenue, cancellations, and no-shows.

This transforms the database from a collection of records into an analytical reporting system.

---

## Project Structure

```text
Hospital-Management-SQL/
│
├── Assets/
│   └── Hospital management.png.png
│
├── database/
│   └── hospital.db
│
├── reports/
│   ├── patients/
│   ├── doctors/
│   ├── treatments/
│   ├── billing/
│   └── appointments/
│
├── README.md
└── ...
```

---

## Technology

**Database:** SQLite

**Language:** SQL

**Reporting Format:** CSV

**Version Control:** Git and GitHub

---

## Skills Demonstrated

### SQL

* Relational database querying
* Multi-table joins
* Aggregations
* Filtering
* Sorting
* Grouping
* Conditional aggregation
* Date-based analysis
* Business-oriented analytical queries

### Data Analysis

* Patient behavior analysis
* Doctor performance analysis
* Treatment frequency analysis
* Treatment revenue analysis
* Billing analysis
* Payment failure analysis
* Payment-status analysis
* Appointment analysis
* Monthly trend analysis

### Data Engineering Workflow

* SQLite database management
* Database exploration
* Query development
* SQL debugging
* Analytical report generation
* CSV export
* Structured project organization
* Git version control
* GitHub project management

---

# Phase 1 Status

**Completed**

The complete SQL reporting layer has been built across all five tables:

```text
Patients
   ↓
Doctors
   ↓
Treatments
   ↓
Billing
   ↓
Appointments
   ↓
29 Analytical CSV Reports
```

Phase 1 established the data analysis and reporting foundation for the project.

---

# Phase 2: Dashboard

The next phase of the project is the **Hospital Management Dashboard**.

The dashboard will use the analytical reports created during Phase 1 to provide an interactive visual view of hospital operations.

Planned dashboard areas include:

* Hospital overview KPIs
* Revenue analysis
* Patient analysis
* Doctor performance
* Treatment analysis
* Appointment trends
* Billing and payment analysis
* Monthly trends
* Interactive filters
* Executive-level hospital insights

The dashboard will be developed step by step, starting with the data layer and basic visualizations before moving into advanced interactions and final UI polishing.

---

## Project Roadmap

```text
Phase 1
SQL Database
     ↓
SQL Analysis
     ↓
Analytical Queries
     ↓
29 CSV Reports
     ↓
Phase 1 Complete

Phase 2
Dashboard Data Preparation
     ↓
KPIs
     ↓
Charts & Visualizations
     ↓
Filters & Interactions
     ↓
Dashboard Design
     ↓
Final Polish
     ↓
Dashboard Complete
```

---

## Project Objective

The overall objective of this project is to demonstrate how a relational healthcare dataset can be transformed into a practical analytics system.

The project follows a complete workflow:

```text
Raw Healthcare Data
        ↓
Relational SQLite Database
        ↓
SQL Analysis
        ↓
Analytical Reports
        ↓
Interactive Dashboard
        ↓
Hospital Business Insights
```

The project is being developed progressively with an emphasis on practical SQL, analytical thinking, data organization, visualization, and portfolio-quality presentation.
