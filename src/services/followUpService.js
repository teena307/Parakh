// src/services/followUpService.js

export function createFollowUp(
  ngo,
  issue,
  assignedTo = "PMU Team - Field 07"
) {

  return {

    id:
      `FU-${Date.now()}`,

    ngoId:
      ngo.id,

    ngoName:
      ngo.name,

    issue,

    assignedTo,

    deadline:
      new Date(
        Date.now() +
        7 * 86400000
      ).toLocaleDateString(
        "en-IN"
      ),

    status: "Pending",

    progress: 0
  };
}


export function updateFollowUp(
  followUp,
  status
) {

  const progress = {

    Pending: 0,

    "In Progress": 50,

    Resolved: 100,

    Overdue: 25

  };

  return {

    ...followUp,

    status,

    progress:
      progress[status] ??
      followUp.progress
  };
}
