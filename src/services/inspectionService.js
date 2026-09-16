// src/services/inspectionService.js

export function generateRandomAssignment(
  ngos,
  inspectors = [
    "Inspector 04",
    "Inspector 17",
    "Inspector 23",
    "Inspector 42"
  ]
) {

  // Prioritize higher-risk NGOs
  const highRisk = ngos.filter(
    ngo => ngo.riskScore >= 60
  );

  const pool =
    highRisk.length > 0
      ? highRisk
      : ngos;

  const ngo =
    pool[
      Math.floor(
        Math.random() * pool.length
      )
    ];

  const inspector =
    inspectors[
      Math.floor(
        Math.random() *
        inspectors.length
      )
    ];

  let priority = "Low";

  if (ngo.riskScore >= 60) {
    priority = "High";
  } else if (ngo.riskScore >= 35) {
    priority = "Medium";
  }

  const reasons = [];

  if (
    ngo.attendance -
    ngo.verifiedAttendance >= 10
  ) {
    reasons.push(
      "Attendance anomaly detected"
    );
  }

  if (ngo.complaints >= 5) {
    reasons.push(
      "Multiple complaints"
    );
  }

  if (ngo.cctv === "Offline") {
    reasons.push(
      "CCTV downtime"
    );
  }

  if (ngo.status === "Inspection Due") {
    reasons.push(
      "Inspection due"
    );
  }

  return {
    ngo,
    inspector,
    priority,

    reason:
      reasons[0] ||
      "Randomised monitoring selection",

    scheduledDate:
      new Date().toLocaleDateString(
        "en-IN",
        {
          day: "2-digit",
          month: "short",
          year: "numeric"
        }
      ),

    status: "Assigned"
  };
}


export function createInspectionDraft(
  ngo,
  inspector,
  type = "Scheduled"
) {

  return {
    id: `INS-${Date.now()}`,

    ngoId: ngo.id,

    ngoName: ngo.name,

    inspector,

    type,

    startedAt:
      new Date().toISOString(),

    gpsVerified: false,

    evidence: [],

    checklist: {},

    status: "In Progress"
  };
}


export function submitInspection(
  inspection
) {

  return {
    ...inspection,

    submittedAt:
      new Date().toISOString(),

    status: "Submitted"
  };
}
