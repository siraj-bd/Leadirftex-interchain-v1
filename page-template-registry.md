# Leadirftex Interchain — Page Template Registry

**Document Classification:** Page Template System Blueprint  
**Status:** Canonical Reference  
**Template ID Convention:** `TPL-[NUMBER]`  
**Scope Rule:** Visual and UX blueprints only. Do NOT implement backend or production functionality.

---

## Page Template Registry Overview

This registry establishes the 13 canonical page templates that govern all 21 hubs of Leadirftex Interchain plus the supporting Industry Job Feed & CV Builder modules. Future page implementation will assemble these validated templates rather than inventing custom page layouts.

---

## Master Template Specifications

### `TPL-001` — Industrial Marketplace Template
- **Purpose:** Primary discovery, search, and trade layout for physical materials, yarns, fabrics, trims, machinery, and stocklots.
- **Layout Architecture:**
  - *Top:* Hub banner with high-level stats (e.g., "14,820 Verified Swatches | 420 Certified Mills"), search bar (`SRCH-001`), quick category tags.
  - *Left Sidebar (280px):* Sticky multi-facet filter panel (GSM, yarn count, composition, price range, MOQ, eco-certification, verified supplier only).
  - *Main Canvas:* Grid header with active filter chips, sort dropdown, and 3-to-4 column responsive grid of Product Cards (`CARD-002`).
  - *Bottom:* Pagination bar (`PGN-001`).
- **Primary Components:** `SRCH-001`, `CARD-002`, `CHIP-001`, `SEL-001`, `PGN-001`, `BDG-001`.
- **Primary Patterns:** `PAT-001` (Marketplace Listing Grid), `PAT-002` (Faceted Filter & Sort).
- **Applicable Hubs:** 
  - Hub 4 (Raw Materials & Yarn)
  - Hub 5 (Fabric Marketplace)
  - Hub 6 (Machinery Marketplace)
  - Hub 8 (Trims & Accessories)
  - Hub 9 (Packaging & Chemical)
  - Hub 19 (Excess & Stocklot Marketplace)
  - Hub 20 (Retail Marketplace)

---

### `TPL-002` — Industrial Network Directory Template
- **Purpose:** Discovery and evaluation layout for manufacturing units, dye houses, testing labs, and service providers.
- **Layout Architecture:**
  - *Top:* Directory search with geographic cluster filter (e.g., Dhaka, Tirupur, Shanghai, Istanbul), verified factory filter toggle.
  - *Left Sidebar (280px):* Machinery capabilities filter (Circular knit, Jacquard, Stenter, Continuous dyeing), audit standard checkboxes (BSCI, WRAP, OEKO-TEX).
  - *Main Canvas:* 2-to-3 column responsive grid of Factory Profile Cards (`CARD-003`) and Service Cards (`CARD-004`). Includes "Compare Selected" floating trigger.
  - *Bottom:* Pagination bar (`PGN-001`).
- **Primary Components:** `SRCH-001`, `CARD-003`, `CARD-004`, `SCORE-001`, `BDG-001`, `PGN-001`.
- **Primary Patterns:** `PAT-002` (Faceted Filter), `PAT-004` (Comparison Matrix).
- **Applicable Hubs:**
  - Hub 7 (Processing & Washing)
  - Hub 15 (Supplier & Service Network)
  - Hub 16 (Factory Network)
  - Hub 18 (Logistics & Trade)

---

### `TPL-003` — Knowledge, CAD & Learning Hub Template
- **Purpose:** Structured educational content, garment manufacturing guides, CAD library, and automation case studies.
- **Layout Architecture:**
  - *Top:* Hero search for textile terminology, ASTM/AATCC standards, pattern cutting techniques, and machinery guides.
  - *Left Sidebar (260px):* Category navigation tree (Fiber science, Yarn spinning, Knitting formulas, Dyeing chemistry, Quality standards, CAD files).
  - *Main Content Area:* Curriculum/Resource cards with estimated reading time, difficulty level, downloadable tech-pack templates (`DOC-001`), and embedded video/diagram areas.
- **Primary Components:** `CARD-001`, `DOC-001`, `CHIP-001`, `SRCH-001`, `BTN-001`.
- **Primary Patterns:** `PAT-001` (Categorized Listing), `PAT-011` (Document Library).
- **Applicable Hubs:**
  - Hub 2 (Textile & Garment Learning)
  - Hub 3 (Technology & Automation)
  - Hub 10 (Product Development & CAD)

---

### `TPL-004` — Technical Product & Specification Detail Template
- **Purpose:** Deep-dive view for individual fabrics, machinery units, yarn lots, or trims.
- **Layout Architecture:**
  - *Top:* Breadcrumb trail, Item title, Technical SKU, Verification badge strip.
  - *Two-Column Primary Split (60% / 40%):*
    - *Left:* High-res zoomable gallery, microscopic weave swatch, test certificate previews.
    - *Right:* Sticky commercial block (Unit price tiers, Minimum Order Quantity, Sample swatch cost, Estimated delivery lead time, "Request Swatch" / "Initiate RFQ" CTAs).
  - *Tabbed Bottom Section:*
    - Tab 1: Detailed Specifications (GSM, yarn count, dye stuff, shrinkage test, color fastness).
    - Tab 2: Factory & Mill Credentials (Mill name, location, Trust Score, audited certifications).
    - Tab 3: Packaging & Shipping terms (Roll length, tube diameter, container loading specs).
- **Primary Components:** `CARD-001`, `BDG-001`, `SCORE-001`, `TABLE-001`, `DOC-001`, `BTN-001`, `TAB-001`.
- **Primary Patterns:** `PAT-003` (Technical Product Specification), `PAT-011` (Evidence Review).
- **Applicable Hubs:**
  - Hub 4, 5, 6, 8, 9, 19, 20 (All physical marketplace detail views).

---

### `TPL-005` — Factory & Mill Verified Profile Template
- **Purpose:** Complete credential, audit, capacity, and production showcase for a verified garment factory.
- **Layout Architecture:**
  - *Hero Header:* Factory photo banner, official corporate name, verification badge ("PHYSICALLY VERIFIED - SGS 2026"), overall Trust Score (`SCORE-001`).
  - *Analytical KPI Strip:* Monthly capacity, total stitching lines, certified workers, on-time delivery %, historical AQL defect rate.
  - *Multi-Tab Content Section:*
    - Tab 1: Overview & Machine Inventory (Knitting machines, auto-spreaders, sewing lines, washing capacity).
    - Tab 2: Audits & Certifications (`DOC-001` cards with verified download links).
    - Tab 3: Past Production Showcase (Product categories manufactured, non-confidential lookbook).
    - Tab 4: Verified Buyer Reviews & Trust Metrics.
- **Primary Components:** `CARD-003`, `SCORE-001`, `BDG-001`, `STAT-001`, `TABLE-001`, `DOC-001`, `BTN-001`.
- **Primary Patterns:** `PAT-004` (Factory Comparison), `PAT-011` (Document Verification), `PAT-012` (Trust & Rating).
- **Applicable Hubs:**
  - Hub 16 (Factory Network)
  - Hub 15 (Supplier Network)

---

### `TPL-006` — Structured Buyer Requirement Submission Template
- **Purpose:** Guided wizard layout for international buyers to post detailed sourcing requirements.
- **Layout Architecture:**
  - *Top:* Wizard progress stepper (`STEP-001`) with steps 1 through 5.
  - *Form Container (Centered, max-width 840px):*
    - Section 1: Item Category & Style Basics.
    - Section 2: Technical Specifications (Fabric blend, GSM, Colorway specs).
    - Section 3: Commercial Terms (Target quantity, Target FOB, Incoterm, Destination port).
    - Section 4: Tech-Pack Drag-and-Drop Area (`UPLD-001`).
    - Section 5: AI Pre-flight Check (Validates spec completeness before publishing).
  - *Footer Action Bar:* "Save Draft", "Back", "Publish Requirement / Trigger AI Matching".
- **Primary Components:** `STEP-001`, `INPUT-001`, `SEL-001`, `UPLD-001`, `ALRT-001`, `BTN-001`.
- **Primary Patterns:** `PAT-005` (Buyer Requirement Submission Wizard).
- **Applicable Hubs:**
  - Hub 12 (Buyer Requirements / Sourcing Hub).

---

### `TPL-007` — AI Matching & RFQ Dissemination Template
- **Purpose:** Reviewing algorithmic matches, comparing quotations, and managing RFQ responses.
- **Layout Architecture:**
  - *Top Banner:* Requirement overview card with AI Confidence Score and matching status.
  - *Split Canvas:*
    - *Top Half:* Ranked matching factories grid with AI Requirement Match Scores (`SCORE-002`) and capability breakdown.
    - *Bottom Half:* Live Quotation Comparison Table (`TABLE-001`) with multi-supplier cost breakdowns (FOB price, CM, Fabric cost, Lead time, Trust score).
- **Primary Components:** `CARD-003`, `SCORE-002`, `TABLE-001`, `BDG-001`, `BTN-001`, `MODAL-001`.
- **Primary Patterns:** `PAT-006` (AI Matching Engine), `PAT-007` (Quotation Comparison).
- **Applicable Hubs:**
  - Hub 13 (AI Matching & RFQ Hub).

---

### `TPL-008` — Order & Milestone Production Workspace Template
- **Purpose:** Active mission control for bulk garment orders, sample tracking, and milestone sign-offs.
- **Layout Architecture:**
  - *Top:* Order ID header, Purchase Order Hash, Production Status Badge, 13-stage Milestone Stepper (`STEP-001`).
  - *3-Column Enterprise Workspace:*
    - *Column 1 (25%):* Order Specifications & Tech-pack document viewer.
    - *Column 2 (50%):* Live production feed, milestone sign-offs, daily cutting/sewing output logs, inspection reports.
    - *Column 3 (25%):* Tri-party Communication Drawer (`CHAT-001`) & real-time audit log (`TML-001`).
- **Primary Components:** `STEP-001`, `STAT-001`, `TABLE-001`, `TML-001`, `CHAT-001`, `DOC-001`, `BTN-001`.
- **Primary Patterns:** `PAT-008` (Sample Approval Loop), `PAT-009` (Unified Order Workspace).
- **Applicable Hubs:**
  - Hub 14 (Order & Product Development Workspace)
  - Hub 11 (R&D & Sample Development Hub).

---

### `TPL-009` — Inspection & Quality Assurance Center Template
- **Purpose:** Detailed quality audit reporting, defect tracking, AQL standard evaluations, and lab dip reviews.
- **Layout Architecture:**
  - *Top:* Inspection overview card with AQL level (e.g., Critical 0 / Major 2.5 / Minor 4.0), Inspector Geolocation verification tag, and Final Verdict Banner ("PASS").
  - *Center Section:* Defect classification grid with photographic evidence, defect frequency counts, and measurement variance tables.
  - *Right/Bottom:* Leadirftex cryptographically verifiable inspection certificate card (`DOC-001`) and corrective action plan (CAP).
- **Primary Components:** `CARD-001`, `BDG-001`, `TABLE-001`, `STAT-001`, `DOC-001`, `ALRT-001`, `BTN-001`.
- **Primary Patterns:** `PAT-010` (Quality Inspection & AQL Defect Review), `PAT-011` (Document Verification Chain).
- **Applicable Hubs:**
  - Hub 17 (Quality & Inspection Center).

---

### `TPL-010` — Operations & Analytics Dashboard Template
- **Purpose:** Executive and operational overview of active orders, sourcing spend, trust metrics, and supplier performance.
- **Layout Architecture:**
  - *Top Row:* 4 KPI Metric Cards (`STAT-001`) for Active Orders, Total Value, On-Time Delivery Rate, and Quality AQL Pass Rate.
  - *Middle Grid:* Production pipeline timeline visualization + AI risk prediction alerts (e.g., "Potential fabric delay in Weaving Line 4").
  - *Bottom Section:* High-density interactive data table of pending actions and supplier trust ratings (`SCORE-001`).
- **Primary Components:** `STAT-001`, `TABLE-001`, `SCORE-001`, `ALRT-001`, `STEP-001`, `BTN-001`.
- **Primary Patterns:** `PAT-012` (Trust & Rating Review), `PAT-013` (Executive KPI Dashboard).
- **Applicable Hubs:**
  - Hub 21 (Factory & Buyer Rating / Trust Hub)
  - Global Executive Management.

---

### `TPL-011` — Universal Listing & Feed Template
- **Purpose:** General-purpose listing layout for service directories, CAD design lookbooks, or processing units.
- **Layout Architecture:**
  - Search and filter bar at top, followed by 3-column card grid or structured list with inline tags, badges, and quick CTA buttons.
- **Primary Components:** `SRCH-001`, `CARD-001`, `CHIP-001`, `PGN-001`.
- **Primary Patterns:** `PAT-001`, `PAT-002`.
- **Applicable Hubs:**
  - Hub 1 (Fashion & Design)
  - Hub 10 (Product Development & CAD)
  - Hub 18 (Logistics & Trade).

---

### `TPL-012` — Textile & Garment Industry Job Feed Template
- **Purpose:** Industry-specific job board connecting professionals with certified factories and global buying houses.
- **Layout Architecture:**
  - *Top Bar:* Job search input (Role, Skill, Factory), location filter, and "Free CV Builder" callout banner.
  - *Split View (Desktop):*
    - *Left Pane (45%):* Chronological feed of Job Cards (`JOB-001`) with salary, location, and verified factory badge.
    - *Right Pane (55%):* Sticky job detail view with full JD, factory audit summary, requirements checklist, and "External Apply" button.
- **Primary Components:** `JOB-001`, `CHIP-001`, `CARD-001`, `BTN-001`, `PGN-001`, `ALRT-001`.
- **Primary Patterns:** `PAT-014` (Industry Job Feed with External Apply).
- **Applicable Hubs:**
  - Supporting Module: Industry Job Feed.

---

### `TPL-013` — Free Professional Textile CV Builder Template
- **Purpose:** Interactive browser-based CV builder with textile industry domain fields and live ATS score meter.
- **Layout Architecture:**
  - *Top Bar:* Progress tracker (Profile Completeness: 85%), ATS Optimization Score badge (`92 / 100`), Export PDF action button.
  - *Two-Pane Split (50% / 50%):*
    - *Left Pane:* Form accordion sections (`CV-001`) covering Personal Info, Factory & Mill Experience, Machine & Technical Expertise, Certifications, and CAD/ERP Software.
    - *Right Pane:* Sticky, real-time live preview of the formatted curriculum vitae ready for download.
- **Primary Components:** `CV-001`, `INPUT-001`, `SEL-001`, `SCORE-001`, `BTN-001`, `ALRT-001`.
- **Primary Patterns:** `PAT-015` (Interactive Textile CV Builder).
- **Applicable Hubs:**
  - Supporting Module: Free Professional CV Builder.
