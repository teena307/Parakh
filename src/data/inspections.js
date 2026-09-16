// src/data/inspections.js

export const inspections = [
  {
    id: "INS-26091",
    ngoId: "NGO-001",
    type: "Scheduled",
    date: "16 Sep 2026",
    inspector: "INS-042",
    priority: "Low",
    status: "Scheduled"
  },

  {
    id: "INS-26092",
    ngoId: "NGO-003",
    type: "Surprise",
    date: "16 Sep 2026",
    inspector: "INS-017",
    priority: "High",
    status: "Pending"
  },

  {
    id: "INS-26093",
    ngoId: "NGO-002",
    type: "Scheduled",
    date: "17 Sep 2026",
    inspector: "INS-031",
    priority: "Medium",
    status: "Pending"
  },

  {
    id: "INS-26094",
    ngoId: "NGO-010",
    type: "Surprise",
    date: "15 Sep 2026",
    inspector: "INS-042",
    priority: "High",
    status: "In Progress"
  },

  {
    id: "INS-26095",
    ngoId: "NGO-004",
    type: "Scheduled",
    date: "14 Sep 2026",
    inspector: "INS-009",
    priority: "Low",
    status: "Completed"
  }
];

export const checklistSections = [
  {
    title: "Infrastructure",
    items: [
      "Building condition",
      "Safety measures",
      "Facilities available",
      "Accessibility"
    ]
  },

  {
    title: "Beneficiary Services",
    items: [
      "Beneficiary attendance",
      "Services actually provided",
      "Staff availability",
      "Beneficiary verification"
    ]
  },

  {
    title: "Documentation",
    items: [
      "Registers maintained",
      "Financial records",
      "Beneficiary records",
      "Government scheme compliance"
    ]
  },

  {
    title: "CCTV",
    items: [
      "CCTV installed?",
      "CCTV operational?",
      "Coverage adequate?",
      "Feed available?"
    ]
  }
];
