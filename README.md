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

The project focuses on using SQL to transform raw relational data into meaningful operational and business insights.

The goal is not simply to store hospital records, but to answer practical questions such as:

* Which patients generate the highest treatment revenue?
* Which patients visit the hospital most frequently?
* Which patients have failed payments?
* Which patients cancel appointments most often?
* Which doctors handle the most appointments?
* Which doctors complete the most appointments?
* Which doctors generate the highest treatment revenue?
* Which doctors have the highest average treatment cost?
* Which doctors have the most no-show appointments?
* Which treatments generate the most revenue?
* How does hospital activity change over time?

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

The relationships between these tables allow the project to perform multi-table analysis using SQL joins and aggregations.

---

## SQL Concepts Used

This project demonstrates practical SQL concepts including:

* `SELECT`
* `WHERE`
* `GROUP BY`
* `ORDER BY`
* `LIMIT`
* `INNER JOIN`
* Aggregate functions

  * `COUNT()`
  * `SUM()`
  * `AVG()`
* `ROUND()`
* `strftime()`
* String concatenation
* Filtering by status
* Multi-table analytical queries
* CSV report generation
* Database exploration
* Relational data analysis

---

## Analytical Reports

The project converts SQL query results into CSV reports organized by database entity.

### Patients

Reports include:

1. Top Spending Patients
2. Most Frequent Patients
3. Patients With Failed Payments
4. Patients With Highest Appointment Cancellations
5. Patients With the Most Treatments
6. Monthly Patient Visits

### Doctors

Reports include:

1. Doctors With the Most Appointments
2. Doctors With the Most Completed Appointments
3. Doctors With the Highest Treatment Revenue
4. Doctors With the Highest Cancelled Appointments
5. Doctors With the Highest Average Treatment Cost
6. Doctors With the Most No-Show Appointments

### Treatments

Treatment analysis includes:

1. Treatment Frequency
2. Treatment Revenue

---

## Example Analysis

A treatment revenue report can answer questions such as:

| Treatment     | Times Performed | Total Revenue |
| ------------- | --------------: | ------------: |
| Chemotherapy  |              49 |    128,855.68 |
| X-Ray         |              41 |    110,653.67 |
| ECG           |              38 |     96,224.24 |
| Physiotherapy |              36 |     99,418.10 |
| MRI           |              36 |    116,098.16 |

This transforms the database from a collection of records into an analytical system that can reveal operational and financial patterns.

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
│   └── treatments/
│
├── README.md
└── ...
```

---

## Database Technology

**Database:** SQLite

**Language:** SQL

**Reporting Format:** CSV

**Version Control:** Git and GitHub

---

## Project Objective

The objective of this project is to demonstrate how SQL can be used to work with a relational healthcare dataset and produce meaningful analytical reports.

Rather than focusing only on basic CRUD operations, the project emphasizes:

* Relational data analysis
* Business-oriented SQL queries
* Data aggregation
* Cross-table analysis
* Operational reporting
* Revenue analysis
* Patient behavior analysis
* Doctor performance analysis
* Exporting analytical results into reusable CSV reports

---

## Skills Demonstrated

This project demonstrates practical experience with:

**SQL**

* Relational database querying
* Joins
* Aggregations
* Filtering
* Sorting
* Grouping
* Date-based analysis
* Analytical reporting

**Data Analysis**

* Patient behavior analysis
* Doctor performance analysis
* Treatment revenue analysis
* Payment failure analysis
* Appointment status analysis

**Data Engineering Workflow**

* SQLite database management
* Query development
* CSV report generation
* Structured project organization
* Git version control

---

## Status

The core patient and doctor analytical reports have been completed, with treatment reporting currently being developed.

The project is being expanded progressively with additional SQL analysis and reporting.
