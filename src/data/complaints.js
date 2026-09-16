// src/data/complaints.js

export const complaints = [
  {
    id: "CMP-1001",
    ngoId: "NGO-003",
    beneficiary: "Beneficiary 104",
    category: "Attendance",
    date: "15 Sep 2026",
    priority: "High",
    status: "New",
    description:
      "Reported attendance does not match actual service availability."
  },

  {
    id: "CMP-1002",
    ngoId: "NGO-010",
    beneficiary: "Beneficiary 217",
    category: "Service Quality",
    date: "14 Sep 2026",
    priority: "High",
    status: "Under Investigation",
    description:
      "Beneficiary reported inconsistent service delivery."
  },

  {
    id: "CMP-1003",
    ngoId: "NGO-002",
    beneficiary: "Beneficiary 088",
    category: "Documentation",
    date: "12 Sep 2026",
    priority: "Medium",
    status: "New",
    description:
      "Requested clarification on beneficiary record entry."
  },

  {
    id: "CMP-1004",
    ngoId: "NGO-005",
    beneficiary: "Beneficiary 151",
    category: "Facilities",
    date: "10 Sep 2026",
    priority: "Medium",
    status: "Resolved",
    description:
      "Facility maintenance concern was addressed."
  }
];
