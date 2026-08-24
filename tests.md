# Test Plan - Employee Attendance & Overtime Analyser

Manual test cases for `main.py`, run against the built-in `EMPLOYEE_RECORDS`
dataset (20 supplied records: 14 valid, 6 invalid).

| Test | Input or condition | Expected result | Actual result | Status |
|------|--------------------|-----------------|---------------|--------|
| Normal | Valid record (E001 Jane Wanjiku) | Processed successfully: attendance 100.00% (Excellent), OT 16.00 hrs, total pay 156,400.00 | Processed successfully: attendance 100.00% (Excellent), OT 16.00 hrs, total pay 156,400.00 | Pass |
| Missing/invalid | Required value missing or invalid (E015 Esther Jepkoech, hours worked = -5) | Rejected with reason: "Hours worked cannot be negative." | Rejected with reason: "Hours worked cannot be negative." | Pass |
| Boundary | Value exactly on a classification limit (E003 Amina Hassan, attendance = 95.00%) | Correct category: "Excellent" (>= 95%) | Categorised as "Excellent" | Pass |
| Search | Existing item `Joseph Maina` and non-existing item `Maina` | Existing returns Joseph Maina (E020); non-existing returns "Employee not found." | Existing returned Joseph Maina (E020); partial `Maina` returned "Employee not found." | Pass |
| Menu | Invalid option (`12`) then Exit (`9`) | Invalid option: "Invalid selection. Please choose 1 to 9." then menu repeats; Exit prints "Program closed." and terminates | Invalid option showed "Invalid selection. Please choose 1 to 9." and menu repeated; Exit printed "Program closed." and terminated | Pass |

---

- Total test cases: 5
- Passed: 5
- Failed: 0
- Tested by: All 5 Members
- Date: 24 August 2026
