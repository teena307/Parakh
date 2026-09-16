// src/services/alertService.js

export function createAlert(
  type,
  ngo,
  message,
  severity = "Medium"
) {

  return {
    id: `ALT-${Date.now()}`,

    type,

    ngoId: ngo.id,

    ngoName: ngo.name,

    message,

    severity,

    createdAt:
      new Date().toISOString(),

    status: "Unread"
  };
}


export function generateNGOAlerts(ngo) {

  const alerts = [];

  if (ngo.riskScore >= 60) {

    alerts.push(
      createAlert(
        "HIGH RISK NGO",
        ngo,
        `Risk score is ${ngo.riskScore}/100.`,
        "High"
      )
    );
  }

  if (
    ngo.attendance -
    ngo.verifiedAttendance >= 10
  ) {

    alerts.push(
      createAlert(
        "ATTENDANCE MISMATCH",
        ngo,
        `Reported ${ngo.attendance}% vs verified ${ngo.verifiedAttendance}%.`,
        "High"
      )
    );
  }

  if (ngo.cctv === "Offline") {

    alerts.push(
      createAlert(
        "CCTV OFFLINE",
        ngo,
        "One or more camera feeds require attention.",
        "Medium"
      )
    );
  }

  return alerts;
}
