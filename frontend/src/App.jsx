import { useState } from "react";
import "./App.css";

function App() {
  const [page, setPage] = useState("dashboard");

  const [patientText, setPatientText] = useState("");
  const [trialText, setTrialText] = useState("");

  const [patientResults, setPatientResults] = useState([]);
  const [trialResults, setTrialResults] = useState([]);

  // Temporary demo results
  const demoTrials = [
    {
      id: "NCT04123456",
      title: "Clinical Study of Novel Therapy for Brain Tumors",
      score: 92,
      match: "High Match",
      condition: "Anaplastic Astrocytoma",
    },
    {
      id: "NCT03876543",
      title: "Targeted Treatment Study for Recurrent Glioma",
      score: 86,
      match: "High Match",
      condition: "Glioma",
    },
    {
      id: "NCT05234121",
      title: "Study of Combination Therapy in Brain Cancer",
      score: 78,
      match: "Moderate Match",
      condition: "Brain Cancer",
    },
    {
      id: "NCT04781234",
      title: "Advanced Oncology Treatment Trial",
      score: 71,
      match: "Moderate Match",
      condition: "Solid Tumor",
    },
  ];

  const demoPatients = [
    {
      id: "Patient 001",
      age: 45,
      gender: "Male",
      condition: "Anaplastic Astrocytoma",
      score: 94,
    },
    {
      id: "Patient 023",
      age: 51,
      gender: "Male",
      condition: "Glioma",
      score: 88,
    },
    {
      id: "Patient 041",
      age: 39,
      gender: "Female",
      condition: "Brain Tumor",
      score: 82,
    },
    {
      id: "Patient 008",
      age: 47,
      gender: "Male",
      condition: "Brain Cancer",
      score: 76,
    },
  ];

  const runPatientMatching = () => {
    if (!patientText.trim()) {
      alert("Please enter or upload a patient record.");
      return;
    }

    setPatientResults(demoTrials);
  };

  const runTrialMatching = () => {
    if (!trialText.trim()) {
      alert("Please enter a clinical trial description.");
      return;
    }

    setTrialResults(demoPatients);
  };

  const handlePatientFile = (event) => {
    const file = event.target.files[0];

    if (file) {
      setPatientText(
        `Uploaded patient record: ${file.name}\n\nThe clinical record will be processed by the HETRA matching engine.`
      );
    }
  };

  const goTo = (destination) => {
    setPage(destination);
  };

  return (
    <div className="app">

      {/* SIDEBAR */}
      <aside className="sidebar">

        <div className="logo">
          <div className="logo-icon">H</div>

          <div>
            <h2>HETRA</h2>
            <span>Clinical AI</span>
          </div>
        </div>

        <div className="menu-title">MAIN MENU</div>

        <button
          className={page === "dashboard" ? "menu active" : "menu"}
          onClick={() => goTo("dashboard")}
        >
          🏠 <span>Dashboard</span>
        </button>

        <div className="menu-title menu-space">
          MATCHING
        </div>

        <button
          className={page === "patient-trials" ? "menu active" : "menu"}
          onClick={() => goTo("patient-trials")}
        >
          👤 <span>Patient → Trials</span>
        </button>

        <button
          className={page === "trial-patients" ? "menu active" : "menu"}
          onClick={() => goTo("trial-patients")}
        >
          🧪 <span>Trial → Patients</span>
        </button>

        <div className="menu-title menu-space">
          DATA
        </div>

        <button
          className={page === "patients" ? "menu active" : "menu"}
          onClick={() => goTo("patients")}
        >
          👥 <span>Patient Records</span>
        </button>

        <button
          className={page === "trials" ? "menu active" : "menu"}
          onClick={() => goTo("trials")}
        >
          📋 <span>Clinical Trials</span>
        </button>

        <div className="sidebar-bottom">

          <div className="model-status">

            <div className="status-dot"></div>

            <div>
              <strong>HETRA Model</strong>
              <small>System Active</small>
            </div>

          </div>

        </div>

      </aside>


      {/* MAIN CONTENT */}
      <main className="main">

        {/* HEADER */}
        <header className="header">

          <div>
            <h1>
              {page === "dashboard" && "Clinical Trial Matching"}

              {page === "patient-trials" &&
                "Patient → Clinical Trials"}

              {page === "trial-patients" &&
                "Clinical Trial → Patients"}

              {page === "patients" &&
                "Patient Records"}

              {page === "trials" &&
                "Clinical Trials"}
            </h1>

            <p>
              Intelligent patient-to-trial matching using HETRA
            </p>
          </div>

          <div className="header-badge">
            ● Model Active
          </div>

        </header>


        {/* ================= DASHBOARD ================= */}

        {page === "dashboard" && (

          <section>

            <div className="welcome">

              <div>

                <span className="small-label">
                  WELCOME TO HETRA
                </span>

                <h2>
                  Intelligent clinical trial matching.
                </h2>

                <p>
                  Match patients with suitable clinical trials
                  or identify patients who may qualify for a
                  specific clinical trial.
                </p>

              </div>

              <div className="welcome-icon">
                🧠
              </div>

            </div>


            {/* TWO MAIN ACTIONS */}

            <div className="matching-options">

              <div className="matching-card">

                <div className="large-icon">
                  👤
                </div>

                <span className="small-label">
                  PATIENT → TRIAL
                </span>

                <h2>
                  Find Clinical Trials
                </h2>

                <p>
                  Upload or enter a patient's clinical record
                  and discover the most suitable clinical trials.
                </p>

                <button
                  className="primary-button"
                  onClick={() => goTo("patient-trials")}
                >
                  Find Matching Trials →
                </button>

              </div>


              <div className="matching-card">

                <div className="large-icon">
                  🧪
                </div>

                <span className="small-label">
                  TRIAL → PATIENT
                </span>

                <h2>
                  Find Matching Patients
                </h2>

                <p>
                  Enter a clinical trial description and identify
                  patients who best match its requirements.
                </p>

                <button
                  className="primary-button"
                  onClick={() => goTo("trial-patients")}
                >
                  Find Matching Patients →
                </button>

              </div>

            </div>


            {/* STATS */}

            <div className="stats">

              <div className="stat-card">

                <div className="stat-icon">
                  👥
                </div>

                <div>
                  <span>Patient Records</span>
                  <strong>75</strong>
                </div>

              </div>


              <div className="stat-card">

                <div className="stat-icon">
                  🧪
                </div>

                <div>
                  <span>Clinical Trials</span>
                  <strong>26,162</strong>
                </div>

              </div>


              <div className="stat-card">

                <div className="stat-icon">
                  🔗
                </div>

                <div>
                  <span>Matching Engine</span>
                  <strong>HETRA</strong>
                </div>

              </div>

            </div>


            {/* MODEL PIPELINE */}

            <div className="pipeline">

              <span className="small-label">
                HETRA PIPELINE
              </span>

              <div className="pipeline-flow">

                <span>Patient Evidence</span>
                <b>→</b>

                <span>Criterion Matching</span>
                <b>→</b>

                <span>Contrastive Learning</span>
                <b>→</b>

                <span>Temporal Compatibility</span>
                <b>→</b>

                <span>Trial Representation</span>
                <b>→</b>

                <span>Ranking</span>

              </div>

            </div>

          </section>

        )}


        {/* ================= PATIENT → TRIAL ================= */}

        {page === "patient-trials" && (

          <section>

            <div className="page-title">

              <span className="small-label">
                PATIENT → TRIAL MATCHING
              </span>

              <h2>
                Find Clinical Trials for a Patient
              </h2>

              <p>
                Enter the patient's clinical information
                and HETRA will rank the most relevant trials.
              </p>

            </div>


            <div className="input-card">

              <label>
                Upload Patient Record
              </label>

              <input
                type="file"
                accept=".txt,.pdf,.doc,.docx"
                onChange={handlePatientFile}
              />

              <div className="or">
                OR
              </div>

              <label>
                Patient Clinical Description
              </label>

              <textarea
                placeholder="Enter the patient's clinical history, diagnosis, symptoms, previous treatments, age, and other relevant information..."
                value={patientText}
                onChange={(e) => setPatientText(e.target.value)}
              />

              <button
                className="primary-button run"
                onClick={runPatientMatching}
              >
                🔍 Run HETRA Matching
              </button>

            </div>


            {patientResults.length > 0 && (

              <div className="results-section">

                <div className="results-heading">

                  <div>
                    <span className="small-label">
                      MATCHING RESULTS
                    </span>

                    <h2>
                      Ranked Clinical Trials
                    </h2>
                  </div>

                  <span className="result-count">
                    {patientResults.length} matches
                  </span>

                </div>


                {patientResults.map((trial, index) => (

                  <div className="result-card" key={trial.id}>

                    <div className="rank">
                      #{index + 1}
                    </div>

                    <div className="result-info">

                      <span className="trial-id">
                        {trial.id}
                      </span>

                      <h3>
                        {trial.title}
                      </h3>

                      <p>
                        Condition: {trial.condition}
                      </p>

                      <span className="match-label">
                        {trial.match}
                      </span>

                    </div>

                    <div className="score">

                      <strong>
                        {trial.score}%
                      </strong>

                      <span>
                        Match Score
                      </span>

                    </div>

                  </div>

                ))}

              </div>

            )}

          </section>

        )}


        {/* ================= TRIAL → PATIENT ================= */}

        {page === "trial-patients" && (

          <section>

            <div className="page-title">

              <span className="small-label">
                TRIAL → PATIENT MATCHING
              </span>

              <h2>
                Find Patients for a Clinical Trial
              </h2>

              <p>
                Enter the trial description and HETRA will
                identify patients who best match its requirements.
              </p>

            </div>


            <div className="input-card">

              <label>
                Clinical Trial Title
              </label>

              <input
                className="text-input"
                type="text"
                placeholder="Enter clinical trial title..."
              />

              <label>
                Eligibility / Trial Description
              </label>

              <textarea
                placeholder="Enter the clinical trial eligibility criteria, inclusion requirements, exclusion requirements, age limits, treatments, and other requirements..."
                value={trialText}
                onChange={(e) => setTrialText(e.target.value)}
              />

              <button
                className="primary-button run"
                onClick={runTrialMatching}
              >
                🔍 Find Matching Patients
              </button>

            </div>


            {trialResults.length > 0 && (

              <div className="results-section">

                <div className="results-heading">

                  <div>
                    <span className="small-label">
                      MATCHING RESULTS
                    </span>

                    <h2>
                      Ranked Patients
                    </h2>
                  </div>

                  <span className="result-count">
                    {trialResults.length} matches
                  </span>

                </div>


                {trialResults.map((patient, index) => (

                  <div className="result-card" key={patient.id}>

                    <div className="rank">
                      #{index + 1}
                    </div>

                    <div className="result-info">

                      <span className="trial-id">
                        {patient.id}
                      </span>

                      <h3>
                        {patient.condition}
                      </h3>

                      <p>
                        {patient.age} years • {patient.gender}
                      </p>

                      <span className="match-label">
                        Strong Candidate
                      </span>

                    </div>

                    <div className="score">

                      <strong>
                        {patient.score}%
                      </strong>

                      <span>
                        Match Score
                      </span>

                    </div>

                  </div>

                ))}

              </div>

            )}

          </section>

        )}


        {/* ================= PATIENT RECORDS ================= */}

        {page === "patients" && (

          <section>

            <div className="page-title">

              <span className="small-label">
                DATA
              </span>

              <h2>
                Patient Records
              </h2>

              <p>
                Patient information available for clinical
                trial matching.
              </p>

            </div>

            <div className="patient-grid">

              {demoPatients.map((patient) => (

                <div
                  className="patient-card"
                  key={patient.id}
                >

                  <div className="patient-top">

                    <div className="patient-avatar">
                      {patient.id.split(" ")[1]}
                    </div>

                    <span className="patient-id">
                      {patient.id}
                    </span>

                  </div>

                  <h3>
                    {patient.condition}
                  </h3>

                  <p className="patient-details">
                    {patient.age} years • {patient.gender}
                  </p>

                  <button
                    className="match-button"
                    onClick={() => goTo("patient-trials")}
                  >
                    Find Matching Trials →
                  </button>

                </div>

              ))}

            </div>

          </section>

        )}


        {/* ================= TRIALS ================= */}

        {page === "trials" && (

          <section>

            <div className="page-title">

              <span className="small-label">
                DATA
              </span>

              <h2>
                Clinical Trials
              </h2>

              <p>
                Clinical trial information available for
                patient matching.
              </p>

            </div>


            <div className="trial-placeholder">

              <div>
                🧪
              </div>

              <h3>
                Clinical Trial Database
              </h3>

              <p>
                Trial information and eligibility criteria
                will appear here.
              </p>

            </div>

          </section>

        )}

      </main>

    </div>
  );
}

export default App;