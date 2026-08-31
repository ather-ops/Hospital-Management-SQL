# Hospital Management SQL — Analytical Reports

This folder contains the analytical reports generated from the Hospital Management SQL database.

Each report is generated from SQL queries against the hospital database and exported as a CSV file for further analysis, visualization, dashboard development, and reporting.

The reports are organized by the five core database entities:

* Patients
* Doctors
* Treatments
* Billing
* Appointments

---

## Report Structure

```text
reports/
│
├── patients/
├── doctors/
├── treatments/
├── billing/
└── appointments/
```

The repository currently contains **36 CSV analytical reports** across these five categories.

---

# 1. Patient Reports

Location:

```text
reports/patients/
```

Patient reports focus on patient activity, spending behavior, treatment patterns, appointment cancellations, payment failures, and monthly visits.

| Report                                     | Description                                                          |
| ------------------------------------------ | -------------------------------------------------------------------- |
| `failed_payments.csv`                      | Patients associated with failed payments and their payment amounts.  |
| `high_value_patients_report.csv`           | Analysis of patients with high overall hospital spending.            |
| `monthly_patient_visits.csv`               | Monthly patient visit activity over time.                            |
| `most_frequent_patients.csv`               | Patients with the highest number of hospital visits or appointments. |
| `patients_by_treatment_type.csv`           | Patient activity grouped by treatment type.                          |
| `patients_with_cancelled_appointments.csv` | Patients with cancelled appointments.                                |
| `top_10_high_value_patients.csv`           | Top 10 patients based on hospital value or spending.                 |
| `top_spending_patients.csv`                | Patients ranked by total spending.                                   |

**Total patient reports: 8**

---

# 2. Doctor Reports

Location:

```text
reports/doctors/
```

Doctor reports analyze appointment workload, completed appointments, treatment revenue, cancellations, no-shows, and treatment costs.

| Report                                            | Description                                                           |
| ------------------------------------------------- | --------------------------------------------------------------------- |
| `completed_doctor_appointments.csv`               | Doctors ranked by completed appointments.                             |
| `completed_doctor_treatment_revenue.csv`          | Treatment revenue associated with completed doctor activity.          |
| `doctor_appointment_summary.csv`                  | Summary of appointment activity for each doctor.                      |
| `doctors_total_treatment_revenue_all.csv`         | Total treatment revenue generated across doctors.                     |
| `doctors_with_highest_cancelled_appointments.csv` | Doctors associated with the highest number of cancelled appointments. |
| `doctors_with_highest_no_show_appointments.csv`   | Doctors associated with the highest number of no-show appointments.   |
| `highest_average_treatment_cost_doctors.csv`      | Doctors ranked by average treatment cost.                             |

**Total doctor reports: 7**

---

# 3. Treatment Reports

Location:

```text
reports/treatments/
```

Treatment reports analyze treatment frequency, treatment cost, monthly treatment activity, expensive treatments, and treatment-related appointment activity.

| Report                                     | Description                                         |
| ------------------------------------------ | --------------------------------------------------- |
| `completed_appointments_report.csv`        | Treatment-related appointments that were completed. |
| `most_common_treatments.csv`               | Treatment types ranked by frequency.                |
| `most_performed_treatments.csv`            | Most frequently performed treatments.               |
| `scheduled_treatments_after_june_2023.csv` | Scheduled treatment activity after June 2023.       |
| `top_10_cheapest_treatments.csv`           | 10 treatments with the lowest recorded costs.       |
| `top_10_most_expensive_treatments.csv`     | 10 treatments with the highest recorded costs.      |
| `top_15_expensive_treatments.csv`          | Top 15 treatments based on treatment cost.          |
| `treatments_per_month.csv`                 | Monthly treatment activity.                         |

**Total treatment reports: 8**

---

# 4. Billing Reports

Location:

```text
reports/billing/
```

Billing reports focus on hospital financial activity, payment failures, pending payments, payment methods, payment status, revenue trends, and high-value bills.

| Report                               | Description                                               |
| ------------------------------------ | --------------------------------------------------------- |
| `average_bill_by_payment_method.csv` | Average bill amount grouped by payment method.            |
| `billing_summary_report.csv`         | Detailed billing summary across hospital billing records. |
| `failed_billing_report.csv`          | Billing records associated with failed payments.          |
| `failed_payments_report.csv`         | Patients and amounts associated with failed payments.     |
| `monthly_revenue_by_billing.csv`     | Monthly billing revenue trends.                           |
| `payment_status_summary.csv`         | Billing totals grouped by payment status.                 |
| `pending_payments_report.csv`        | Billing records associated with pending payments.         |
| `revenue_by_payment_method.csv`      | Revenue grouped by payment method.                        |
| `top_10_highest_bills.csv`           | Top 10 bills by billing amount.                           |

**Total billing reports: 9**

---

# 5. Appointment Reports

Location:

```text
reports/appointments/
```

Appointment reports analyze cancellations, completed appointments, no-show behavior, monthly appointment activity, and doctor schedules.

| Report                                | Description                                             |
| ------------------------------------- | ------------------------------------------------------- |
| `doctor_no_show_analysis.csv`         | No-show appointments analyzed by doctor.                |
| `doctors_completed_appointments.csv`  | Doctors ranked by completed appointments.               |
| `doctors_schedule_summary.csv`        | Doctor appointment workload and scheduled appointments. |
| `monthly_appointments.csv`            | Monthly appointment activity over time.                 |
| `patients_cancelled_appointments.csv` | Patients with cancelled appointments.                   |

**Total appointment reports: 5**

---

# Report Summary

| Category     | Number of Reports |
| ------------ | ----------------: |
| Patients     |                 8 |
| Doctors      |                 7 |
| Treatments   |                 8 |
| Billing      |                 9 |
| Appointments |                 5 |
| **Total**    |            **37** |

---

## SQL Analysis Behind the Reports

The reports were generated using practical SQL analysis techniques including:

* `SELECT`
* `WHERE`
* `GROUP BY`
* `ORDER BY`
* `LIMIT`
* `INNER JOIN`
* `LEFT JOIN`
* `COUNT()`
* `SUM()`
* `AVG()`
* `ROUND()`
* `CASE`
* `strftime()`
* String concatenation
* Conditional aggregation
* Date-based aggregation
* Filtering by appointment status
* Filtering by payment status
* Multi-table analysis

---

## Report Generation Workflow

The reports were created through the following workflow:

```text
Hospital Database
       |
       v
SQL Query
       |
       v
Data Aggregation
       |
       v
Analysis
       |
       v
CSV Export
       |
       v
reports/
       |
       +---- patients/
       +---- doctors/
       +---- treatments/
       +---- billing/
       +---- appointments/
```

Each CSV represents a specific analytical question answered using the hospital database.

---

## Purpose of the Reports

These reports form the analytical foundation of the Hospital Management System.

They can be used for:

* Hospital performance analysis
* Patient behavior analysis
* Doctor performance analysis
* Treatment analysis
* Revenue analysis
* Payment monitoring
* Appointment monitoring
* Operational reporting
* Dashboard development
* Business intelligence analysis

The CSV reports are also used as a foundation for the project's Streamlit dashboard.

---

## Dashboard Integration

The reports produced during the SQL analysis phase provide the foundation for the next stage of the project:

```text
SQLite Database
       |
       v
SQL Analysis
       |
       v
CSV Reports
       |
       v
Streamlit Application
       |
       v
Interactive Dashboard
       |
       v
Hospital Management Insights
```

The dashboard will bring these analytical results together into an interactive interface for exploring hospital operations and financial performance.

---

## Data Source

All reports are generated from the project's SQLite hospital database.

Core tables:

```text
patients
doctors
appointments
treatments
billing
```

The database contains interconnected records that allow cross-table analysis between patients, doctors, appointments, treatments, and billing.

---

## Project Status

The SQL reporting phase has been completed.

The project has progressed from:

```text
Database Design
       ↓
Data Population
       ↓
SQL Query Development
       ↓
Query Debugging
       ↓
Analytical Reporting
       ↓
CSV Report Generation
       ↓
Streamlit Dashboard
```

The next phase focuses on transforming these SQL-generated insights into an interactive hospital management dashboard using Streamlit.

---

## Notes

The CSV files in this directory are analytical outputs generated from SQL queries. They are intended for reporting, analysis, visualization, and dashboard development rather than as replacements for the primary SQLite database.

The SQLite database remains the source of truth for the hospital records.
