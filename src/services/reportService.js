// src/services/reportService.js

export function generateInspectionReport({
  ngo,
  inspection,
  riskResult,
  attendanceResult,
  evidence = []
}) {

  return {

    reportId:
      `RPT-${Date.now()}`,

    generatedAt:
      new Date().toISOString(),

    ngo: {
      id: ngo.id,
      name: ngo.name,
      location: ngo.location,
      scheme: ngo.scheme
    },

    inspector:
      inspection?.inspector ||
      "INS-042",

    gpsVerification:
      inspection?.gpsVerified
        ? "Verified"
        : "Pending",

    checklist:
      inspection?.checklist ||
      {},

    evidence,

    attendance:
      attendanceResult,

    aiRisk:
      riskResult,

    recommendations: [
      riskResult.recommendation,

      ...(riskResult.factors || [])
        .map(
          factor =>
            `Review: ${factor}`
        )
    ],

    followUpRequired:
      riskResult.level === "HIGH"
  };
}


// Prototype report download
export function downloadReport(
  report
) {

  const text = `
PARAKH
SMART, TRANSPARENT & REAL-TIME NGO MONITORING

INSPECTION REPORT
--------------------------------

Report ID:
${report.reportId}

NGO:
${report.ngo.name}

Location:
${report.ngo.location}

Scheme:
${report.ngo.scheme}

Inspector:
${report.inspector}

GPS:
${report.gpsVerification}

Risk:
${report.aiRisk.level}

Risk Score:
${report.aiRisk.score}/100

Follow-up Required:
${report.followUpRequired ? "YES" : "NO"}

Recommendations:
${report.recommendations.join("\n")}
`;

  const blob =
    new Blob(
      [text],
      {
        type:
          "text/plain;charset=utf-8"
      }
    );

  const url =
    URL.createObjectURL(blob);

  const link =
    document.createElement("a");

  link.href = url;

  link.download =
    `${report.reportId}.txt`;

  link.click();

  URL.revokeObjectURL(url);
}
