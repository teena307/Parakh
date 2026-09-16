// src/data/dashboardData.js

export const dashboardData = {

  stats: {
    totalNGOs: 10,
    inspectedNGOs: 7,
    pendingInspections: 3,
    highRiskNGOs: 3,
    activeAlerts: 6,
    complaints: 12
  },

  trends: {
    totalNGOs: "+8.3%",
    inspectedNGOs: "+12.5%",
    pendingInspections: "-6.2%",
    highRiskNGOs: "+4.1%",
    activeAlerts: "+2",
    complaints: "-9.4%"
  },

  riskDistribution: [
    {
      label: "Low Risk",
      value: 5
    },
    {
      label: "Medium Risk",
      value: 2
    },
    {
      label: "High Risk",
      value: 3
    }
  ],

  monthlyInspections: [
    { month: "Apr", completed: 18, pending: 5 },
    { month: "May", completed: 21, pending: 6 },
    { month: "Jun", completed: 24, pending: 4 },
    { month: "Jul", completed: 27, pending: 5 },
    { month: "Aug", completed: 31, pending: 4 },
    { month: "Sep", completed: 23, pending: 3 }
  ],

  attendanceTrend: [
    { month: "Apr", reported: 91, verified: 86 },
    { month: "May", reported: 92, verified: 85 },
    { month: "Jun", reported: 90, verified: 82 },
    { month: "Jul", reported: 93, verified: 84 },
    { month: "Aug", reported: 94, verified: 79 },
    { month: "Sep", reported: 92, verified: 76 }
  ]
};
