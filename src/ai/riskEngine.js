// src/ai/riskEngine.js

export function calculateRisk(ngo, extra = {}) {

  let score = 10;

  // Attendance mismatch
  const attendanceGap = Math.max(
    0,
    (ngo.attendance || 0) -
    (ngo.verifiedAttendance || 0)
  );

  score += Math.min(attendanceGap * 1.2, 25);

  // Complaints
  score += Math.min(
    (ngo.complaints || 0) * 4,
    20
  );

  // Previous violations
  score += Math.min(
    (ngo.previousViolations || 0) * 8,
    24
  );

  // CCTV
  if (ngo.cctv === "Offline") {
    score += 10;
  }

  // Inspection due
  if (ngo.status === "Inspection Due") {
    score += 10;
  }

  // Additional inspection findings
  if (extra.financialIssue) {
    score += 15;
  }

  if (extra.beneficiaryMismatch) {
    score += 12;
  }

  if (extra.reportingInconsistency) {
    score += 8;
  }

  score = Math.min(
    Math.round(score),
    100
  );

  let level = "LOW";

  if (score >= 60) {
    level = "HIGH";
  } else if (score >= 35) {
    level = "MEDIUM";
  }

  const factors = [];

  if (attendanceGap >= 10) {
    factors.push("Attendance mismatch");
  }

  if (ngo.complaints >= 5) {
    factors.push("Previous complaints");
  }

  if (ngo.previousViolations > 0) {
    factors.push("Previous violations");
  }

  if (ngo.cctv === "Offline") {
    factors.push("CCTV downtime");
  }

  if (ngo.status === "Inspection Due") {
    factors.push("Inspection irregularity");
  }

  if (extra.financialIssue) {
    factors.push("Financial record concern");
  }

  if (extra.beneficiaryMismatch) {
    factors.push("Beneficiary data mismatch");
  }

  let recommendation;

  if (level === "HIGH") {
    recommendation =
      "Prioritise for immediate or surprise inspection.";
  } else if (level === "MEDIUM") {
    recommendation =
      "Schedule inspection and request additional evidence.";
  } else {
    recommendation =
      "Continue routine monitoring.";
  }

  return {
    score,
    level,
    factors,
    recommendation
  };
}


export function detectAttendanceAnomaly(
  reported,
  verified
) {

  const mismatch = Math.max(
    0,
    reported - verified
  );

  return {
    mismatch,

    detected: mismatch >= 10,

    message:
      mismatch >= 10
        ? "Reported attendance is significantly higher than verified beneficiary presence."
        : "Attendance is within the expected verification range."
  };
}
