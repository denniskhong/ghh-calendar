# The Greek-Hanke-Henry (GHH) Permanent Calendar

The **Greek-Hanke-Henry (GHH) Permanent Calendar** is a proposed calendar reform designed to resolve the economic and administrative inefficiencies of the Gregorian system. It couples the structural stability of the Hanke-Henry Permanent Calendar (HHPC) with a politically neutral nomenclature based on the Greek alphabet.

This repository contains the **computational implementation** (Python) of the system.

## 📅 The Concept

The GHH calendar divides the year into four identical quarters, ensuring that every date falls on the same day of the week, every year, forever.

* **Structure:** 364-day standard year.
* **Quarters:** Each quarter has a **30-30-31** day pattern.
* **Leap System:** Instead of a leap day, a **Leap Week (Omega)** is added every 5-6 years to synchronize with the solar year.
* **Nomenclature:** Months are named **Alpha** through **Mu** to avoid confusion with Gregorian names (e.g., "January 30" vs "Alpha 30").
* **Synchronization:** "Alpha 1" is anchored to the Monday of **ISO Week 1**, making it fully compatible with the ISO-8601 standard.

| Order | GHH Name | Days | Fixed Start Day |
| :--- | :--- | :--- | :--- |
| 1 | **Alpha** | 30 | Monday |
| 2 | **Beta** | 30 | Wednesday |
| 3 | **Gamma** | 31 | Friday |
| ... | ... | ... | ... |
| 13 | **Omega** | 7 | *Leap Week* |

## 🛠️ Python Implementation

The included script `ghh_calendar.py` provides a robust CLI tool for interacting with the GHH system.

### Features
* **Bidirectional Conversion:**
    * Convert Gregorian dates to GHH.
    * Convert GHH dates to Gregorian.
* **Visual Calendar Generation:** Renders a full annual calendar using Unicode box-drawing characters for perfect alignment in text editors.
* **Proleptic Support:** Supports historical dates prior to the Gregorian adoption (Oct 15, 1582) by using the Proleptic Gregorian system.
* **Validation:** Automatically detects and handles the "Omega" leap week logic based on ISO-8601 week 53.

### Usage

1.  **Prerequisites:** Python 3.x (Standard library only).
2.  **Run the script:**
    ```bash
    python ghh_calendar.py
    ```

3.  **Menu Options:**

    * **Option 1: Convert Gregorian Date -> GHH Date**
        * Input format: `YYYY-MM-DD`
        * *Example:* `2026-01-01` → `2026 Alpha 04 (Thu)`
        * *Note:* If the date is before Oct 15, 1582, a warning will indicate that the calculation uses the Proleptic Gregorian system.

    * **Option 2: Convert GHH Date -> Gregorian Date**
        * Input format: `YYYY-MM-DD`
        * *Note:* Use **Month 13** to represent the **Omega** leap week.
        * *Example:* `2026-13-05` → `Gregorian: Sunday, 2026-12-29` (If 2026 were a leap year).

    * **Option 3: Generate GHH Annual Calendar**
        * Generates a visual grid of the entire year.
        * Displays the fixed 30-30-31 quarters.
        * Automatically appends the Omega week if the year contains 53 ISO weeks.

    * **Option 0: Exit**

## 📄 Academic Paper

The formal proposal for the GHH system, detailing the economic arguments, nomenclature shifts, and historical context, will be made available on **arXiv** in the near future.

## 📂 File Structure

* `ghh_calendar.py`: The main Python application.
* `README.md`: This documentation file.

## 👥 Authors

* **Dennis WK Khong** (Multimedia University, Malaysia) - *Corresponding Author*
* **Gemini 3 Pro** (Google DeepMind) - *Co-author & Code Implementation*

## 📜 Citations & References

This project references the following works:

* **Bushell, W. F. (1961).** Calendar reform. *The Mathematical Gazette*, 45(352), 117–124.
* **David, P. A. (1985).** Clio and the economics of QWERTY. *The American Economic Review*, 75(2), 332–337.
* **Davies, C., Trivizas, E., & Wolfe, R. (1999).** The failure of calendar reform (1922–1931): Religious minorities, businessmen, scientists, and bureaucrats. *Journal of Historical Sociology*, 12, 251–270.
* **Hanke, S. H., & Henry, R. C. (n.d.).** *The Hanke-Henry Permanent Calendar*. Retrieved from http://hankehenryontime.com/html/calendar.html
* **International Organization for Standardization. (2019).** *ISO 8601-1:2019. Date and time — Representations for information interchange*. Geneva, Switzerland: ISO.
