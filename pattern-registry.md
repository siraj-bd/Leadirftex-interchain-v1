# Leadirftex Interchain — Pattern Registry

**Document Classification:** Reusable Workflow & UX Pattern Specification  
**Status:** Canonical Reference  
**Pattern ID Convention:** `PAT-[NUMBER]`

---

## 1. Pattern Overview

Workflow patterns assemble individual atomic and molecule components (`BTN-001`, `INPUT-001`, `CARD-001`, etc.) into standardized, consistent user interactions across all 21 hubs of Leadirftex Interchain.

---

## 2. Master Pattern Catalog

### `PAT-001` — Marketplace Listing & Discovery Grid
- **Purpose:** Standard high-efficiency browsing for physical materials, yarns, fabrics, machinery, trims, and stocklots.
- **UX Flow:**
  1. Top bar displays total matched items, active filter chips, view toggles (Grid / High-Density List), and sort dropdown (`SEL-001`).
  2. Main body renders a responsive 3-to-4 column grid of Product Cards (`CARD-002`).
  3. Bottom pagination bar (`PGN-001`) with direct page jumping and items-per-page controls.
- **Required Components:** `CARD-002`, `CHIP-001`, `SEL-001`, `PGN-001`, `IBTN-001`.
- **Allowed Usage:** Hubs 4, 5, 6, 8, 9, 19, 20.
- **Related Page Templates:** `TPL-001` (Marketplace Template), `TPL-011` (Universal Listing).

---

### `PAT-002` — Faceted Industrial Filter & Multi-Criteria Sort
- **Purpose:** Deep domain-specific filtering tailored to industrial textile specifications (GSM, yarn count, dye method, certifications, MOQ, location, audit status).
- **UX Flow:**
  1. Left-hand sticky sidebar (width: `280px`) with collapsible accordion sections.
  2. Includes range sliders (GSM `100 - 450`, Price `$0.50 - $25.00`), multi-select checkboxes (`CHK-001`) for certifications (GOTS, OEKO-TEX, BSCI), and instant toggle switch (`TOG-001`) for "Verified Only".
  3. Active filter chips appear above search results with individual "×" dismiss and "Clear All" button.
- **Required Components:** `INPUT-001`, `CHK-001`, `TOG-001`, `CHIP-001`, `BTN-001`.
- **Allowed Usage:** Universal across all marketplace and directory pages.
- **Related Page Templates:** `TPL-001`, `TPL-002`, `TPL-011`, `TPL-012`.

---

### `PAT-003` — Technical Product & Material Specification View
- **Purpose:** Comprehensive deep-dive presentation of physical textile products, fabric swatches, or garment prototypes.
- **UX Flow:**
  1. Left pane: High-resolution zoomable gallery with macro swatch weave viewer, lab-dip colorways, and certification badge strip.
  2. Right pane: Technical spec sheet (Yarn count, Warp/Weft density, Weave type, Finishing method, Shrinkage test results, MOQ, Tiered volume pricing).
  3. Action bar: Prominent "Request Fabric Swatch / Sample" and "Initiate RFQ" triggers.
- **Required Components:** `CARD-001`, `BDG-001`, `BTN-001`, `TABLE-001`, `DOC-001`.
- **Allowed Usage:** Hubs 4, 5, 6, 8, 9, 19, 20.
- **Related Page Templates:** `TPL-004` (Product Detail Template).

---

### `PAT-004` — Multi-Factory & Supplier Comparison Matrix
- **Purpose:** Side-by-side analytical comparison of up to 4 factories or suppliers on critical procurement metrics.
- **UX Flow:**
  1. Sticky top header displaying factory names, country flags, and overall Trust Scores (`SCORE-001`).
  2. Comparative rows evaluate: Monthly capacity, Certified workers, AQL defect tolerance, On-time delivery %, Minimum MOQ, Audited certifications (WRAP, GOTS, ISO), Sample lead time.
  3. Differences are highlighted with subtle background badges; unverified claims show disclaimer warnings.
- **Required Components:** `CARD-003`, `SCORE-001`, `BDG-001`, `TABLE-001`, `BTN-001`.
- **Allowed Usage:** Hub 15 (Supplier Network), Hub 16 (Factory Network), Hub 13 (AI Matching).
- **Related Page Templates:** `TPL-002` (Directory), `TPL-005` (Factory Profile), `TPL-007` (RFQ Hub).

---

### `PAT-005` — Structured Buyer Requirement Submission Wizard
- **Purpose:** Step-by-step guided submission of procurement requirements, ensuring complete technical specs to eliminate vague RFQs.
- **UX Flow:**
  1. Step 1 (Classification): Garment category, target gender/season, product sketch/reference upload.
  2. Step 2 (Technical Parameters): Fabric composition, desired GSM, yarn count, wash requirement, target size ratio.
  3. Step 3 (Commercials & Compliance): Target quantity (MOQ), Target FOB price, Required certifications (BSCI, OEKO-TEX), Target delivery date.
  4. Step 4 (Tech-Pack & Evidence): Drag-and-drop tech-pack upload (`UPLD-001`) with automatic format validation.
  5. Step 5 (Review & Disseminate): AI Requirement Analysis preview + Dissemination scope selection (Private invite vs. Public matching).
- **Required Components:** `STEP-001`, `INPUT-001`, `SEL-001`, `UPLD-001`, `ALRT-001`, `BTN-001`.
- **Allowed Usage:** Hub 12 (Buyer Requirements / Sourcing Hub).
- **Related Page Templates:** `TPL-006` (Buyer Requirement Submission Template).

---

### `PAT-006` — AI Matching & RFQ Dissemination Engine
- **Purpose:** Automated algorithmic matching between buyer requirements and vetted factory capacity.
- **UX Flow:**
  1. Requirement summary card at the top displaying key parameters and AI analysis confidence.
  2. Ranked list of candidate factories sorted by AI Requirement Match Score (`SCORE-002`).
  3. Match explanation accordion detailing exactly why the factory matched (e.g., "98% match on circular knitting capacity; ISO9001 certified; within target price range").
  4. One-click batch RFQ dissemination button ("Send RFQ to Top 3 Verified Matches").
- **Required Components:** `CARD-003`, `SCORE-002`, `BDG-001`, `BTN-001`, `ALRT-001`.
- **Allowed Usage:** Hub 13 (AI Matching & RFQ Hub).
- **Related Page Templates:** `TPL-007` (AI Matching & RFQ Template).

---

### `PAT-007` — Quotation Comparison & Cost Breakdown Analysis
- **Purpose:** High-density side-by-side analysis of incoming bids from multiple manufacturers.
- **UX Flow:**
  1. Data table (`TABLE-001`) with expandable rows breaking down: Fabric cost, Cut & Make (CM), Trims cost, Packaging, Washing/Finishing, Freight estimate, Total FOB unit price.
  2. Trust score and verification status displayed directly alongside each quoted price.
  3. Action buttons: "Accept Quote", "Counter-Offer", "Request Sample".
- **Required Components:** `TABLE-001`, `BDG-001`, `SCORE-001`, `BTN-001`, `MODAL-001`.
- **Allowed Usage:** Hub 13 (RFQ Hub), Hub 14 (Order Workspace).
- **Related Page Templates:** `TPL-007`, `TPL-008`.

---

### `PAT-008` — Sample Development & Approval Loop
- **Purpose:** Managing tech-pack review, proto-sample, fit sample, lab-dip, and pre-production (PP) approvals.
- **UX Flow:**
  1. Milestone Stepper (`STEP-001`) showing Proto 1 -> Proto 2 -> Fit Sample -> Lab Dip -> PP Sample.
  2. High-resolution photo upload showing measurement tape verification against spec sheet.
  3. Approval decision panel: "Approve Sample", "Approve with Comments", "Reject & Request Counter-Sample".
  4. Automatic timestamped audit logging into production timeline (`TML-001`).
- **Required Components:** `STEP-001`, `CARD-001`, `UPLD-001`, `TML-001`, `BTN-001`, `ALRT-001`.
- **Allowed Usage:** Hub 11 (R&D & Sample Development), Hub 14 (Order Workspace).
- **Related Page Templates:** `TPL-008` (Order Workspace Template).

---

### `PAT-009` — Unified Order & Production Workspace
- **Purpose:** Central mission control for an active purchase order from contract signing through shipment.
- **UX Flow:**
  1. Top banner: Order ID, PO Hash, Production Status Badge, Target Ex-Factory Date, Milestone Stepper.
  2. Left Pane (30%): Production milestones & progress breakdown (Yarn spinning, Knitting/Weaving, Dyeing, Cutting, Sewing, Finishing).
  3. Center Pane (45%): Live production feed, daily output logs, inspection reports, document locker.
  4. Right Pane (25%): Tri-party communication panel (`CHAT-001`) with buyer, factory lead, and inspection officer.
- **Required Components:** `STEP-001`, `STAT-001`, `TABLE-001`, `TML-001`, `CHAT-001`, `DOC-001`.
- **Allowed Usage:** Hub 14 (Order & Product Development Workspace).
- **Related Page Templates:** `TPL-008`.

---

### `PAT-010` — Quality Inspection, AQL Defect & Audit Review
- **Purpose:** In-depth quality assurance reporting based on internationally standard AQL (Acceptable Quality Limit) levels (e.g., Critical: 0, Major: 2.5, Minor: 4.0).
- **UX Flow:**
  1. Header shows Inspection Type (Inline / Mid-production / Final Pre-Shipment / FRI), Leadirftex Inspector ID, Audit Geolocation stamp.
  2. Defect classification cards with photo evidence, defect code (e.g., Stitch slip, Color shading, Broken needle), and frequency count.
  3. Final verdict banner: "PASS", "PENDING RE-WORK", "FAIL".
  4. Cryptographically signed inspection certificate download (`DOC-001`).
- **Required Components:** `CARD-001`, `BDG-001`, `TABLE-001`, `DOC-001`, `ALRT-001`, `BTN-001`.
- **Allowed Usage:** Hub 17 (Quality & Inspection Center).
- **Related Page Templates:** `TPL-009` (Inspection Center Template).

---

### `PAT-011` — Document & Evidence Verification Chain
- **Purpose:** Displays physical audit reports, lab certificates (OEKO-TEX, GOTS, ISO), test reports with full cryptographic provenance.
- **UX Flow:**
  1. Grid of verifiable document cards (`DOC-001`).
  2. Each card shows Issuing Authority, Verification Date, Expiry Date, QR/Hash code, and Leadirftex Physical Verification Shield.
  3. Clicking opens Side Inspector Drawer (`DRW-001`) with high-res document scan viewer and verified audit checklist.
- **Required Components:** `DOC-001`, `BDG-001`, `DRW-001`, `IBTN-001`.
- **Allowed Usage:** Hub 16 (Factory Profile), Hub 17 (Inspection Center), Hub 21 (Trust Hub).
- **Related Page Templates:** `TPL-005`, `TPL-009`.

---

### `PAT-012` — Multi-Dimensional Trust, Rating & Reputation Review
- **Purpose:** Public and authenticated trust scoring for factories and buyers based on verified transaction history.
- **UX Flow:**
  1. Overall Trust Score gauge (`SCORE-001`) with tier badge (e.g., "Tier 1 - Platinum Verified").
  2. Sub-metric radar breakdown: On-Time Shipment (98%), Quality Pass Rate (97.4%), Response Time (2.1 hrs), Dispute Resolution Rate (100%).
  3. Verified buyer review cards with attached PO reference hashes (ensuring only real transactions can leave reviews).
- **Required Components:** `SCORE-001`, `BDG-001`, `CARD-001`, `STAT-001`, `PGN-001`.
- **Allowed Usage:** Hub 21 (Factory & Buyer Rating / Trust Hub).
- **Related Page Templates:** `TPL-010` (Dashboard / Analytics), `TPL-005` (Factory Profile).

---

### `PAT-013` — Executive & Operational KPI Dashboard
- **Purpose:** Consolidated overview of orders, spend, supplier performance, and pending actions.
- **UX Flow:**
  1. Top row of 4 KPI Metric Cards (`STAT-001`).
  2. Center section: Active Production Pipeline split-view with milestone progress bars.
  3. Bottom section: Pending Approvals table (Quotes awaiting decision, Samples pending review, Inspection reports).
- **Required Components:** `STAT-001`, `TABLE-001`, `STEP-001`, `ALRT-001`, `BTN-001`.
- **Allowed Usage:** Hub 14, Hub 21, Platform Global Dashboard.
- **Related Page Templates:** `TPL-010` (Operations Dashboard).

---

### `PAT-014` — Textile & Garment Industry Job Feed with External Apply
- **Purpose:** Connecting textile engineers, apparel merchandisers, production managers, and fashion designers with global employers.
- **UX Flow:**
  1. Filter bar by role (Knitting, Dyeing, CAD, QA, Merchandising), location, experience level, salary range.
  2. Clean list of Industry Job Cards (`JOB-001`).
  3. Right-hand preview drawer (`DRW-001`) showing job description, factory profile link, required skills chips, and one-click "External Apply" redirect button.
- **Required Components:** `JOB-001`, `CHIP-001`, `DRW-001`, `BTN-001`, `PGN-001`.
- **Allowed Usage:** Industry Job Feed module.
- **Related Page Templates:** `TPL-012` (Job Feed Template).

---

### `PAT-015` — Free Interactive Textile CV & Resume Builder
- **Purpose:** Empowering garment professionals to build ATS-optimized industrial resumes with textile-specific competencies.
- **UX Flow:**
  1. Left pane: Guided section editor (Personal info, Factory experience, Machinery mastered, Quality certifications, Tech-pack CAD software).
  2. Right pane: Real-time live PDF preview mirror with ATS score meter and instant free download trigger.
- **Required Components:** `CV-001`, `INPUT-001`, `SEL-001`, `SCORE-001`, `BTN-001`.
- **Allowed Usage:** Free Professional CV Builder module.
- **Related Page Templates:** `TPL-013` (CV Builder Template).
