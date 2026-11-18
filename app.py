from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Zeeshan Arif | Portfolio</title>
  <style>
    :root {
      --bg: #0f172a;
      --surface: #1e293b;
      --surface-hover: #273549;
      --border: #334155;
      --primary: #38bdf8;
      --primary-glow: rgba(56, 189, 248, 0.25);
      --accent: #10b981;
      --text: #f8fafc;
      --muted: #94a3b8;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
      background: radial-gradient(circle at top right, #1e293b, #0f172a 70%);
      color: var(--text);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 2rem 1rem;
    }

    .container {
      width: 100%;
      max-width: 960px;
    }

    header {
      text-align: center;
      margin-bottom: 2.5rem;
    }

    .badge {
      display: inline-block;
      padding: 0.35rem 0.9rem;
      font-size: 0.8rem;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: var(--primary);
      background: rgba(56, 189, 248, 0.1);
      border: 1px solid rgba(56, 189, 248, 0.3);
      border-radius: 999px;
      margin-bottom: 0.9rem;
    }

    h1 {
      font-size: 2.5rem;
      font-weight: 700;
      letter-spacing: -0.02em;
    }

    .subtitle {
      color: var(--muted);
      margin-top: 0.5rem;
      font-size: 1.05rem;
    }

    .options-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 1.25rem;
      margin-bottom: 2rem;
    }

    .option-card {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 1.6rem;
      text-align: left;
      color: inherit;
      cursor: pointer;
      transition: transform 0.2s ease, border-color 0.2s ease, box-shadow 0.2s ease, background 0.2s ease;
      position: relative;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }

    .option-card:hover {
      transform: translateY(-4px);
      background: var(--surface-hover);
      border-color: var(--primary);
    }

    .option-card.active {
      border-color: var(--primary);
      box-shadow: 0 0 0 3px var(--primary-glow);
      background: #1e324a;
    }

    .card-index {
      font-size: 0.75rem;
      font-weight: 700;
      color: var(--primary);
      letter-spacing: 0.1em;
      text-transform: uppercase;
      margin-bottom: 0.6rem;
    }

    .card-title {
      font-size: 1.35rem;
      font-weight: 700;
      margin-bottom: 0.45rem;
    }

    .card-preview {
      color: var(--muted);
      font-size: 0.92rem;
      line-height: 1.45;
    }

    .card-action {
      margin-top: 1.2rem;
      font-size: 0.85rem;
      font-weight: 600;
      color: var(--primary);
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
    }

    .detail-panel {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 18px;
      padding: 2rem;
      box-shadow: 0 20px 40px rgba(0, 0, 0, 0.35);
      animation: fadeIn 0.25s ease;
    }

    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(6px); }
      to { opacity: 1; transform: translateY(0); }
    }

    .panel-header {
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      align-items: center;
      gap: 1rem;
      border-bottom: 1px solid var(--border);
      padding-bottom: 1.2rem;
      margin-bottom: 1.5rem;
    }

    .panel-header h2 {
      font-size: 1.65rem;
    }

    .status-pill {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.4rem 0.9rem;
      border-radius: 999px;
      font-size: 0.85rem;
      font-weight: 600;
      background: rgba(16, 185, 129, 0.15);
      color: #34d399;
      border: 1px solid rgba(16, 185, 129, 0.35);
    }

    .dot {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: #10b981;
      box-shadow: 0 0 8px #10b981;
    }

    .panel-body p {
      color: #cbd5e1;
      line-height: 1.65;
      margin-bottom: 1.25rem;
    }

    .tags {
      display: flex;
      flex-wrap: wrap;
      gap: 0.6rem;
      margin-bottom: 1.5rem;
    }

    .tag {
      background: #0f172a;
      border: 1px solid var(--border);
      padding: 0.45rem 0.85rem;
      border-radius: 8px;
      font-size: 0.85rem;
      color: #e2e8f0;
    }

    .list-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 1rem;
      margin-bottom: 1.25rem;
    }

    .info-box {
      background: #0f172a;
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 1.1rem;
    }

    .info-box h4 {
      color: var(--primary);
      font-size: 0.9rem;
      margin-bottom: 0.4rem;
    }

    .info-box p {
      margin: 0;
      font-size: 0.9rem;
      color: var(--muted);
    }

    .btn-group {
      display: flex;
      flex-wrap: wrap;
      gap: 0.8rem;
      margin-top: 1rem;
    }

    .btn {
      padding: 0.65rem 1.25rem;
      border-radius: 10px;
      font-weight: 600;
      font-size: 0.9rem;
      text-decoration: none;
      cursor: pointer;
      border: 1px solid transparent;
      transition: all 0.2s ease;
    }

    .btn-primary {
      background: var(--primary);
      color: #0f172a;
    }

    .btn-primary:hover {
      background: #7dd3fc;
    }

    .btn-outline {
      background: transparent;
      border-color: var(--border);
      color: var(--text);
    }

    .btn-outline:hover {
      border-color: var(--primary);
      color: var(--primary);
    }

    footer {
      margin-top: 2.5rem;
      text-align: center;
      color: var(--muted);
      font-size: 0.85rem;
    }
  </style>
</head>
<body>
  <div class="container">
    <header>
      <div class="badge">Interactive Portfolio</div>
      <h1>Zeeshan Arif</h1>
      <p class="subtitle">Select an option below to explore profile, designation, and current work status.</p>
    </header>

    <section class="options-grid" role="tablist" aria-label="Profile Sections">
      <button class="option-card active" onclick="selectTab('name', this)" role="tab" aria-selected="true">
        <div>
          <div class="card-index">Option 01</div>
          <div class="card-title">Zeeshan Arif</div>
          <p class="card-preview">Personal profile, location, technical skills, and professional links.</p>
        </div>
        <span class="card-action">View Profile &rarr;</span>
      </button>

      <button class="option-card" onclick="selectTab('designation', this)" role="tab" aria-selected="false">
        <div>
          <div class="card-index">Option 02</div>
          <div class="card-title">Designation</div>
          <p class="card-preview">Application & Systems Support Engineer | IT & Network Engineer.</p>
        </div>
        <span class="card-action">View Role Details &rarr;</span>
      </button>

      <button class="option-card" onclick="selectTab('status', this)" role="tab" aria-selected="false">
        <div>
          <div class="card-index">Option 03</div>
          <div class="card-title">Work Status</div>
          <p class="card-preview">Current employment status, availability, and collaboration options.</p>
        </div>
        <span class="card-action">Check Availability &rarr;</span>
      </button>
    </section>

    <main id="detail-panel" class="detail-panel" aria-live="polite"></main>

    <footer>
      &copy; 2026 Zeeshan Arif. Powered by Python &amp; Flask.
    </footer>
  </div>

  <script>
    const sections = {{ sections | tojson }};

    function selectTab(key, element) {
      document.querySelectorAll('.option-card').forEach(card => {
        card.classList.remove('active');
        card.setAttribute('aria-selected', 'false');
      });
      element.classList.add('active');
      element.setAttribute('aria-selected', 'true');

      const panel = document.getElementById('detail-panel');
      panel.innerHTML = sections[key];
    }

    // Initialize default view
    document.getElementById('detail-panel').innerHTML = sections.name;
  </script>
</body>
</html>
"""

PORTFOLIO_SECTIONS = {
    "name": """
        <div class="panel-header">
          <div>
            <h2>Zeeshan Arif</h2>
            <span style="color: var(--muted); font-size: 0.95rem;">Jeddah, Saudi Arabia</span>
          </div>
          <div class="status-pill"><span class="dot"></span> Verified Profile</div>
        </div>
        <div class="panel-body">
          <p>
            Experienced IT Infrastructure, Systems, and Network Engineer with 5+ years of hands-on expertise managing enterprise servers, Cisco network architecture, Windows Server hybrid environments, and business logistics applications.
          </p>
          <div class="tags">
            <span class="tag">Cisco CCNA</span>
            <span class="tag">Windows Server Hybrid Admin</span>
            <span class="tag">Active Directory &amp; GPO</span>
            <span class="tag">FortiGate &amp; Switching</span>
            <span class="tag">SQL &amp; Power BI</span>
            <span class="tag">Python &amp; Automation</span>
          </div>
          <div class="btn-group">
            <a href="https://www.linkedin.com/in/zeeshan-arif-001058250" target="_blank" rel="noopener" class="btn btn-primary">LinkedIn Profile</a>
            <a href="https://github.com/zeeshanarif1300-creator" target="_blank" rel="noopener" class="btn btn-outline">GitHub Repositories</a>
          </div>
        </div>
    """,
    "designation": """
        <div class="panel-header">
          <div>
            <h2>Designation &amp; Core Responsibilities</h2>
            <span style="color: var(--muted); font-size: 0.95rem;">Application &amp; Systems Support Engineer | IT &amp; Network Engineer</span>
          </div>
        </div>
        <div class="panel-body">
          <p>
            Delivering end-to-end IT operations, infrastructure deployment, and enterprise application support across corporate offices and multi-site logistics facilities.
          </p>
          <div class="list-grid">
            <div class="info-box">
              <h4>Network &amp; Security</h4>
              <p>Cisco Catalyst switches, routers, FortiGate firewalls, Wi-Fi APs, IP telephony, and CCTV/biometric access systems.</p>
            </div>
            <div class="info-box">
              <h4>Systems &amp; Cloud</h4>
              <p>Windows Server, Active Directory, Azure Entra ID, VMware/Hyper-V virtualization, and Endpoint Central management.</p>
            </div>
            <div class="info-box">
              <h4>Enterprise Applications</h4>
              <p>Oracle EBS, document management servers, automated scanning systems, and SQL database administration.</p>
            </div>
            <div class="info-box">
              <h4>Data &amp; Automation</h4>
              <p>Building reporting dashboards and workflow automations using Power BI, SQL, Power Automate, and Python.</p>
            </div>
          </div>
        </div>
    """,
    "status": """
        <div class="panel-header">
          <div>
            <h2>Current Work Status</h2>
            <span style="color: var(--muted); font-size: 0.95rem;">Active Full-Time &amp; Open to Remote Opportunities</span>
          </div>
          <div class="status-pill"><span class="dot"></span> Open to Connect</div>
        </div>
        <div class="panel-body">
          <p>
            Currently serving full-time as an <strong>Application &amp; Systems Support Engineer / IT &amp; Network Engineer</strong> at Mosanada Logistics Services (Jeddah, Saudi Arabia).
          </p>
          <div class="list-grid">
            <div class="info-box">
              <h4>Primary Role</h4>
              <p>Full-Time On-Site IT Infrastructure &amp; Enterprise Systems Support (Jeddah, KSA).</p>
            </div>
            <div class="info-box">
              <h4>Remote Availability</h4>
              <p>Available for part-time remote IT support, systems administration, and data analytics projects.</p>
            </div>
          </div>
          <div class="btn-group">
            <a href="https://www.linkedin.com/in/zeeshan-arif-001058250" target="_blank" rel="noopener" class="btn btn-primary">Message on LinkedIn</a>
          </div>
        </div>
    """
}


@app.route("/")
def home():
    return render_template_string(HTML_TEMPLATE, sections=PORTFOLIO_SECTIONS)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
