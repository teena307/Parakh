// src/data/ngos.js
// Fictional demo data only.

export const ngos = [
  {
    id: "NGO-001",
    name: "Asha Foundation",
    registrationId: "REG-DEL-2401",
    location: "New Delhi",
    state: "Delhi",
    district: "New Delhi",
    scheme: "PM-AJAY",
    beneficiaries: 420,
    riskScore: 28,
    attendance: 94,
    verifiedAttendance: 91,
    complaints: 2,
    previousViolations: 0,
    cctv: "Online",
    lastInspection: "08 Sep 2026",
    nextInspection: "22 Sep 2026",
    status: "Compliant"
  },

  {
    id: "NGO-002",
    name: "Udaan Welfare Society",
    registrationId: "REG-HR-2402",
    location: "Gurugram",
    state: "Haryana",
    district: "Gurugram",
    scheme: "Scholarship Support",
    beneficiaries: 310,
    riskScore: 54,
    attendance: 86,
    verifiedAttendance: 78,
    complaints: 5,
    previousViolations: 1,
    cctv: "Online",
    lastInspection: "05 Sep 2026",
    nextInspection: "17 Sep 2026",
    status: "Pending"
  },

  {
    id: "NGO-003",
    name: "Samarth NGO",
    registrationId: "REG-UP-2403",
    location: "Noida",
    state: "Uttar Pradesh",
    district: "Gautam Buddha Nagar",
    scheme: "PM-AJAY",
    beneficiaries: 275,
    riskScore: 72,
    attendance: 92,
    verifiedAttendance: 67,
    complaints: 7,
    previousViolations: 2,
    cctv: "Offline",
    lastInspection: "02 Sep 2026",
    nextInspection: "16 Sep 2026",
    status: "Action Required"
  },

  {
    id: "NGO-004",
    name: "Navjeevan Foundation",
    registrationId: "REG-UP-2404",
    location: "Ghaziabad",
    state: "Uttar Pradesh",
    district: "Ghaziabad",
    scheme: "Senior Citizen Welfare",
    beneficiaries: 190,
    riskScore: 39,
    attendance: 90,
    verifiedAttendance: 87,
    complaints: 2,
    previousViolations: 0,
    cctv: "Online",
    lastInspection: "07 Sep 2026",
    nextInspection: "24 Sep 2026",
    status: "Compliant"
  },

  {
    id: "NGO-005",
    name: "Sahayata Trust",
    registrationId: "REG-RAJ-2405",
    location: "Jaipur",
    state: "Rajasthan",
    district: "Jaipur",
    scheme: "PM-AJAY",
    beneficiaries: 360,
    riskScore: 61,
    attendance: 84,
    verifiedAttendance: 76,
    complaints: 4,
    previousViolations: 1,
    cctv: "Online",
    lastInspection: "01 Sep 2026",
    nextInspection: "18 Sep 2026",
    status: "Inspection Due"
  },

  {
    id: "NGO-006",
    name: "Seva Jyoti Foundation",
    registrationId: "REG-DEL-2406",
    location: "Dwarka",
    state: "Delhi",
    district: "South West Delhi",
    scheme: "Disability Support",
    beneficiaries: 225,
    riskScore: 22,
    attendance: 97,
    verifiedAttendance: 95,
    complaints: 1,
    previousViolations: 0,
    cctv: "Online",
    lastInspection: "09 Sep 2026",
    nextInspection: "28 Sep 2026",
    status: "Compliant"
  },

  {
    id: "NGO-007",
    name: "Saksham Care Initiative",
    registrationId: "REG-UP-2407",
    location: "Lucknow",
    state: "Uttar Pradesh",
    district: "Lucknow",
    scheme: "Women Welfare",
    beneficiaries: 480,
    riskScore: 67,
    attendance: 81,
    verifiedAttendance: 70,
    complaints: 6,
    previousViolations: 1,
    cctv: "Offline",
    lastInspection: "30 Aug 2026",
    nextInspection: "15 Sep 2026",
    status: "Action Required"
  },

  {
    id: "NGO-008",
    name: "Jan Kalyan Initiative",
    registrationId: "REG-MP-2408",
    location: "Bhopal",
    state: "Madhya Pradesh",
    district: "Bhopal",
    scheme: "Educational Support",
    beneficiaries: 340,
    riskScore: 45,
    attendance: 89,
    verifiedAttendance: 84,
    complaints: 3,
    previousViolations: 0,
    cctv: "Online",
    lastInspection: "06 Sep 2026",
    nextInspection: "21 Sep 2026",
    status: "Pending"
  },

  {
    id: "NGO-009",
    name: "Pragati Social Trust",
    registrationId: "REG-MH-2409",
    location: "Nagpur",
    state: "Maharashtra",
    district: "Nagpur",
    scheme: "Senior Citizen Welfare",
    beneficiaries: 210,
    riskScore: 31,
    attendance: 93,
    verifiedAttendance: 90,
    complaints: 2,
    previousViolations: 0,
    cctv: "Online",
    lastInspection: "10 Sep 2026",
    nextInspection: "25 Sep 2026",
    status: "Compliant"
  },

  {
    id: "NGO-010",
    name: "Sahyog Child Care",
    registrationId: "REG-UP-2410",
    location: "Meerut",
    state: "Uttar Pradesh",
    district: "Meerut",
    scheme: "Child Welfare",
    beneficiaries: 295,
    riskScore: 81,
    attendance: 88,
    verifiedAttendance: 61,
    complaints: 8,
    previousViolations: 3,
    cctv: "Offline",
    lastInspection: "29 Aug 2026",
    nextInspection: "15 Sep 2026",
    status: "High Risk"
  }
];

export const states = [
  ...new Set(ngos.map((ngo) => ngo.state))
];

export const districts = [
  ...new Set(ngos.map((ngo) => ngo.district))
];

export const schemes = [
  ...new Set(ngos.map((ngo) => ngo.scheme))
];
