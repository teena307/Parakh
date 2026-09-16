// src/services/evidenceService.js

export function createMockEvidence(
  ngo,
  inspector = "INS-042",
  type = "Photo"
) {

  return {
    id: `EVD-${Date.now()}`,

    ngoId: ngo.id,

    ngoName: ngo.name,

    inspector,

    type,

    timestamp:
      new Date().toLocaleTimeString(
        "en-IN",
        {
          hour: "2-digit",
          minute: "2-digit"
        }
      ),

    gps: "28.6139° N, 77.2090° E",

    locationVerified: true,

    fileName:
      type === "Photo"
        ? "inspection-photo-001.jpg"
        : "inspection-video-001.mp4"
  };
}


export function verifyLocation(
  registeredLocation,
  currentLocation
) {

  // Mock GPS calculation for prototype
  const distance =
    Math.floor(
      Math.random() * 80
    ) + 10;

  return {

    verified:
      distance <= 100,

    distanceMeters:
      distance,

    registeredLocation,

    currentLocation,

    accuracy: "± 8 m"
  };
}
