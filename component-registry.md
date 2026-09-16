# Leadirftex Interchain — Component Registry

**Document Classification:** Component Library Specification  
**Status:** Canonical Reference  
**Naming Standard:** `lowercase-with-hyphens` for filenames, Stable ID convention `[PREFIX]-[NUMBER]` for components.

---

## Component Registry Overview

This registry defines the core reusable UI components utilized across the Leadirftex Interchain platform. Each component includes stable identification, functional purpose, visual aesthetics, supported interactive states, design token dependencies, and strict usage boundaries.

---

## 1. Action & Navigation Components

### `BTN-001` — Master Button System
- **Purpose:** Initiates primary, secondary, tertiary, and destructive user actions.
- **Visual Description:** Solid or outlined rectangle with `4px` or `8px` rounded corners, centered text in `font-body-md` (semi-bold), optional leading/trailing 18px SVG icon.
  - *Primary Variant:* Solid Interchain Blue (`--lt-color-primary-600`) with white text.
  - *Secondary Variant:* Clean white background with slate border (`--lt-color-slate-200`) and slate-700 text.
  - *Verified Action Variant:* Physical Emerald (`--lt-color-verify-600`) for "Approve Sample", "Issue Verification Certificate".
  - *AI Action Variant:* Deep Violet (`--lt-color-ai-600`) for "Run AI Matching", "Analyze Tech-Pack".
  - *Destructive Variant:* Crimson Red (`--lt-color-danger-600`) for "Reject Batch", "Cancel RFQ".
- **States:**
  - `default`: Resting surface with subtle shadow (`--lt-shadow-1`).
  - `hover`: Darkened background (`+10%`), elevated shadow (`--lt-shadow-2`), cursor pointer.
  - `focus`: Active outline with 3px focus ring (`--lt-shadow-glow-blue`).
  - `active`: Compressed scale (`scale(0.98)`), inset shadow.
  - `disabled`: Opacity `0.5`, background `--lt-color-slate-100`, text `--lt-color-slate-400`, cursor `not-allowed`.
  - `loading`: Text hidden or shifted, centered CSS spinner with matching token color.
- **Token Dependencies:** `--lt-color-primary-600`, `--lt-color-slate-200`, `--lt-radius-sm`, `--lt-radius-md`, `--lt-font-sans`, `--lt-shadow-1`.
- **Allowed Usage:** Standard triggers, form submissions, modal confirmations, action toolbars.

### `IBTN-001` — Icon Button
- **Purpose:** Compact actions in table rows, media galleries, card headers, and toolbars.
- **Visual Description:** `36x36px` or `32x32px` square or circular button containing an 18px SVG icon. Borderless or subtle outline.
- **States:** `default`, `hover` (slate-100 fill), `focus` (focus ring), `active`, `disabled`.
- **Token Dependencies:** `--lt-color-slate-600`, `--lt-color-slate-100`, `--lt-radius-sm`, `--lt-radius-full`.
- **Allowed Usage:** Row actions (edit, delete, download, favorite, copy spec hash).

### `LNK-001` — Semantic Hyperlink
- **Purpose:** Text-level navigation to external or internal hub routes.
- **Visual Description:** Underlined on hover, blue `--lt-color-primary-600` or subtle slate `--lt-color-slate-700`.
- **States:** `default`, `hover`, `focus`, `visited`, `disabled`.
- **Token Dependencies:** `--lt-color-primary-600`, `--lt-font-sans`.
- **Allowed Usage:** Inline text links, breadcrumb items, footer navigation links.

### `NAV-001` — Primary Navigation Bar & Hub Tab Item
- **Purpose:** Primary hub switching and global application routing.
- **Visual Description:** Horizontal or vertical tab item with active bottom border (`2px solid --lt-color-primary-600`) or pill background.
- **States:** `default`, `hover` (slate-50 background), `selected` (blue text + bold indicator), `disabled`.
- **Token Dependencies:** `--lt-color-primary-600`, `--lt-color-slate-800`, `--lt-space-4`.
- **Allowed Usage:** Global header hub list, profile tabs, dashboard sub-views.

---

## 2. Form & Data Entry Components

### `INPUT-001` — Text & Numeric Input Field
- **Purpose:** Standard single-line text and numeric inputs for specifications, quantities, and user data.
- **Visual Description:** White field with `1px solid --lt-color-slate-300`, `8px` height padding, placeholder in slate-400.
- **States:**
  - `default`: Border `--lt-color-slate-300`.
  - `hover`: Border `--lt-color-slate-400`.
  - `focus`: Border `--lt-color-primary-600`, glow ring `--lt-shadow-glow-blue`.
  - `disabled`: Background `--lt-color-slate-100`, text `--lt-color-slate-400`.
  - `error`: Border `--lt-color-danger-600`, error text helper below field.
  - `success`: Border `--lt-color-verify-600`, trailing green checkmark icon.
- **Token Dependencies:** `--lt-color-slate-300`, `--lt-color-primary-600`, `--lt-radius-sm`, `--lt-font-sans`.
- **Allowed Usage:** RFQ submission forms, search inputs, specification parameters (GSM, weight, MOQ).

### `SRCH-001` — Global & Facet Search Box
- **Purpose:** High-efficiency search with integrated filter triggers and keyboard shortcut indicator (`⌘K`).
- **Visual Description:** Leading magnifying glass icon, trailing shortcut chip, clear button (`×`), clear search suggestion dropdown container.
- **States:** `default`, `focus`, `active-query`, `loading`, `empty-results`.
- **Token Dependencies:** `--lt-color-slate-200`, `--lt-shadow-2`, `--lt-radius-md`.
- **Allowed Usage:** Global header search, marketplace search bars, directory quick-filters.

### `SEL-001` — Select & Dropdown Field
- **Purpose:** Single or multi-select dropdown for standard categories, country selectors, trade terms (FOB, CIF, EXW).
- **Visual Description:** Form container with trailing chevron, opening an elevated popover list (`--lt-shadow-3`).
- **States:** `default`, `hover`, `open`, `focus`, `disabled`, `error`.
- **Token Dependencies:** `--lt-color-white`, `--lt-color-slate-200`, `--lt-shadow-3`, `--lt-radius-sm`.
- **Allowed Usage:** Currency switcher, hub category dropdown, incoterm selection.

### `CHK-001` — Checkbox
- **Purpose:** Multi-selection in filter sidebars, batch table selections, and compliance confirmations.
- **Visual Description:** `18x18px` square with `3px` radius. White fill resting; solid blue fill with white checkmark when checked.
- **States:** `unchecked`, `checked`, `indeterminate`, `hover`, `focus`, `disabled`.
- **Token Dependencies:** `--lt-color-primary-600`, `--lt-color-slate-300`, `--lt-radius-xs`.
- **Allowed Usage:** Facet filters (certifications: GOTS, OEKO-TEX, BSCI), bulk order row selection.

### `RAD-001` — Radio Selector
- **Purpose:** Mutually exclusive option selection (e.g., Shipping type: Air / Sea / Rail).
- **Visual Description:** `18x18px` circle with center solid dot when active.
- **States:** `unselected`, `selected`, `hover`, `focus`, `disabled`.
- **Token Dependencies:** `--lt-color-primary-600`, `--lt-color-slate-300`.
- **Allowed Usage:** Payment term selection, quotation response selection, sample courier type.

### `TOG-001` — Toggle Switch
- **Purpose:** Instant binary setting switches (e.g., "Show Verified Factories Only", "AI Matching Active").
- **Visual Description:** Pill track (`40x22px`) with sliding white circular thumb (`18x18px`).
- **States:** `off` (slate-300 track), `on` (blue-600 track or emerald-600 track), `hover`, `disabled`.
- **Token Dependencies:** `--lt-color-slate-300`, `--lt-color-primary-600`, `--lt-color-verify-600`, `--lt-radius-full`.
- **Allowed Usage:** Filter bars, dashboard configuration toggles, notification settings.

### `UPLD-001` — Evidence & Document Upload Block
- **Purpose:** Uploading tech-packs (PDF/DXF), lab dips, inspection videos, and compliance certificates.
- **Visual Description:** Dashed border container (`2px dashed --lt-color-slate-300`) with cloud upload icon, file format tags (`PDF, DXF, AI, ZIP, JPG`), and drag-and-drop hover highlight.
- **States:** `default`, `drag-over` (blue-50 background, blue border), `uploading` (progress bar), `complete` (document card), `error` (red border, file size warning).
- **Token Dependencies:** `--lt-color-slate-300`, `--lt-color-primary-50`, `--lt-color-primary-600`, `--lt-radius-md`.
- **Allowed Usage:** Buyer RFQ submission, factory certification upload, QA inspection evidence.

---

## 3. Data Display & Card Components

### `CARD-001` — Master Base Container Card
- **Purpose:** Structural container for grouping related content, specs, and metrics.
- **Visual Description:** Crisp white background (`--lt-color-white`), `1px solid --lt-color-slate-200`, subtle resting shadow (`--lt-shadow-1`), `8px` or `12px` border radius.
- **States:** `default`, `hover` (elevated `--lt-shadow-2`), `selected` (blue border).
- **Token Dependencies:** `--lt-color-white`, `--lt-color-slate-200`, `--lt-shadow-1`, `--lt-radius-md`.
- **Allowed Usage:** Universal container across all hubs.

### `CARD-002` — Product / Material Card
- **Purpose:** Displays fabric, yarn, machinery, trims, or stocklot items in marketplace feeds.
- **Visual Description:** 
  - Top: Aspect ratio `4:3` image preview with badges (Stocklot, MOQ, Fabric Type).
  - Middle: Title in `font-h4`, supplier name with verification badge, technical specs row (GSM, Composition, Yarn Count).
  - Bottom: Price range (`$2.40 - $3.10 / meter`), MOQ (`500 M`), and "Request Sample / RFQ" button.
- **States:** `default`, `hover` (subtle zoom on thumbnail, elevated shadow), `selected`, `out-of-stock`.
- **Token Dependencies:** `--lt-color-white`, `--lt-color-slate-200`, `--lt-radius-md`, `--lt-shadow-1`.
- **Allowed Usage:** Hubs 4, 5, 6, 8, 9, 19, 20.

### `CARD-003` — Factory Profile Card
- **Purpose:** Displays manufacturing facilities in the Factory Network and matching results.
- **Visual Description:**
  - Header: Factory name, country flag, geographic cluster (e.g., Gazipur, Chittagong, Tirupur, Shaoxing).
  - Trust Strip: Verified physical badge, audit date, overall Trust Score (`SCORE-001`).
  - Capabilities Grid: Monthly capacity, machine count, employee count, audited certifications (GOTS, BSCI).
  - Footer: Primary product focus (Knitwear, Woven, Denim, Outerwear) + "View Audit Profile" & "Invite to RFQ".
- **States:** `default`, `hover`, `active-contract`, `audited`.
- **Token Dependencies:** `--lt-color-brand-950`, `--lt-color-verify-500`, `--lt-radius-md`, `--lt-shadow-1`.
- **Allowed Usage:** Hub 16 (Factory Network), Hub 13 (AI Matching), Hub 15 (Supplier Network).

### `CARD-004` — Service & Specialist Card
- **Purpose:** Product development studios, CAD specialists, testing laboratories, washing units.
- **Visual Description:** Service offering overview, turnaround SLA, lab accreditation tags (ISO 17025), sample rating.
- **States:** `default`, `hover`, `selected`.
- **Token Dependencies:** `--lt-color-white`, `--lt-color-slate-200`, `--lt-radius-md`.
- **Allowed Usage:** Hubs 1, 7, 10, 11, 15, 17, 18.

### `STAT-001` — KPI Metric & Statistic Card
- **Purpose:** High-level dashboard metrics (Active RFQs, Production Units, On-Time Rate, Defect AQL).
- **Visual Description:** Clean card with metric title (`font-body-sm`), giant numerical value (`font-display-lg`), trend indicator (`+4.2%` green arrow or `-1.8%` red arrow), and micro sparkline or progress bar.
- **States:** `default`, `positive-trend`, `negative-trend`, `neutral`.
- **Token Dependencies:** `--lt-color-white`, `--lt-color-slate-900`, `--lt-color-verify-600`, `--lt-radius-md`.
- **Allowed Usage:** Hub 14 (Order Workspace), Hub 17 (Quality Center), Hub 21 (Rating Dashboard).

---

## 4. Trust, Verification & Score Components

### `BDG-001` — Trust & Verification Status Badge
- **Purpose:** Unmistakable visual tag indicating whether a piece of data is physically audited, AI-generated, or self-reported.
- **Variants:**
  - `VERIFIED_PHYSICAL`: Green badge (`--lt-color-verify-50`), border `--lt-color-verify-500`, text `--lt-color-verify-900`. Shield check icon.
  - `AI_ASSESSED`: Purple badge (`--lt-color-ai-50`), border `--lt-color-ai-500`, text `--lt-color-ai-900`. Sparkle/circuit icon.
  - `FACTORY_REPORTED`: Slate badge (`--lt-color-slate-100`), border `--lt-color-slate-400`, text `--lt-color-slate-700`. Info icon.
  - `AUDIT_EXPIRED`: Amber badge (`--lt-color-amber-50`), border `--lt-color-amber-500`, text `--lt-color-amber-900`. Clock warning icon.
- **States:** `default`, `hover` (reveals audit provenance tooltip `TLP-001`).
- **Token Dependencies:** `--lt-color-verify-500`, `--lt-color-ai-500`, `--lt-color-slate-400`, `--lt-radius-xs`.
- **Allowed Usage:** Appears on factories, audit certificates, lab test results, pricing quotes, lead-time promises.

### `SCORE-001` — Trust & Multi-Metric Score Indicator
- **Purpose:** Renders comprehensive 0-100 scores across Trust, Capability, Delivery, and Quality.
- **Visual Description:** Radial gauge or structured score block with score value (e.g., `94.8 / 100`), classification tag ("Tier 1 - Platinum Verified"), and breakdown bar.
- **States:** `high` (85-100, Emerald), `medium` (65-84, Amber), `low` (<65, Red).
- **Token Dependencies:** `--lt-color-verify-600`, `--lt-color-amber-600`, `--lt-color-danger-600`, `--lt-font-mono`.
- **Allowed Usage:** Hub 21 (Trust Hub), Hub 16 (Factory Profile), Hub 13 (Matching).

### `SCORE-002` — AI Requirement Match Score
- **Purpose:** Quantifies alignment between buyer RFQ requirements and supplier factory capabilities.
- **Visual Description:** Violet pill badge with matching percentage (e.g., `96% Match`), expandable to show sub-scores (GSM Match: 100%, MOQ Fit: 95%, Lead Time: 90%, Compliance: Pass).
- **States:** `default`, `hover` (opens AI Match Factor Inspector).
- **Token Dependencies:** `--lt-color-ai-600`, `--lt-color-ai-50`, `--lt-radius-full`.
- **Allowed Usage:** Hub 13 (AI Matching & RFQ Hub).

---

## 5. Workflow, Stepper & Timeline Components

### `STEP-001` — Workflow Milestone Stepper
- **Purpose:** Guides users visually through the 13-stage Leadirftex industrial order pipeline.
- **Visual Description:** Horizontal (desktop) or vertical (mobile) connected nodes.
  - Completed: Green circular icon with checkmark + solid green connecting line.
  - Active: Blue circular node with pulsing halo ring + bold step label.
  - Pending: Slate-300 circular ring + muted step label.
  - Alert/Revision: Amber/Red circular node with alert icon (e.g., "Lab Dip Rejected").
- **States:** `completed`, `active`, `pending`, `alert`, `disabled`.
- **Token Dependencies:** `--lt-color-verify-600`, `--lt-color-primary-600`, `--lt-color-slate-300`, `--lt-space-4`.
- **Allowed Usage:** Hub 14 (Order Workspace), Hub 12 (Buyer Requirements), Hub 11 (Sample Development).

### `TML-001` — Audit & Production Timeline
- **Purpose:** Real-time chronological audit trail of all actions, file uploads, inspections, and status changes.
- **Visual Description:** Vertical line with chronological event nodes, timestamps in `font-mono-sm`, actor badge (Buyer, Factory Manager, Leadirftex QA Inspector, AI System), and attached document cards.
- **States:** `default`, `expanded-detail`.
- **Token Dependencies:** `--lt-color-slate-200`, `--lt-color-slate-600`, `--lt-font-mono`.
- **Allowed Usage:** Hub 14 (Order Workspace), Hub 17 (Quality Center).

### `DOC-001` — Document & Evidence Block
- **Purpose:** Verifiable digital document card representing tech-packs, lab reports, invoices, or certificates.
- **Visual Description:** File extension badge (`PDF`, `XLS`, `DXF`), file name, byte size, cryptographic hash snippet (`SHA-256: 8f9b...`), verification checkmark, and direct download/preview button.
- **States:** `verified`, `pending-audit`, `rejected`.
- **Token Dependencies:** `--lt-color-slate-100`, `--lt-color-verify-500`, `--lt-radius-sm`.
- **Allowed Usage:** Order documents, factory certificates, inspection defect logs.

---

## 6. Data Tables & Data Density Components

### `TABLE-001` — Enterprise Data Table
- **Purpose:** High-density display of RFQ quotes, machine inventories, fabric specs, inspection defect logs.
- **Visual Description:**
  - Header: Slate-50 background (`--lt-color-slate-50`), bold column titles (`font-body-sm`), sort direction arrows.
  - Rows: Alternating zebra or clean white rows with `1px solid --lt-color-slate-200` border, vertical alignment center, row height `48px` (standard) or `36px` (compact).
  - Sticky Headers: Fixed during vertical scrolling.
  - Selection: Leftmost column contains `CHK-001` for batch operations.
- **States:** `default`, `row-hover` (slate-50), `row-selected` (primary-50 with blue border), `loading-skeleton`, `empty`.
- **Token Dependencies:** `--lt-color-slate-50`, `--lt-color-slate-200`, `--lt-color-primary-50`, `--lt-font-sans`.
- **Allowed Usage:** Quotation comparisons, order tracking, machinery lists, defect logs.

### `PGN-001` — Pagination & Record Count
- **Purpose:** Navigation controls for large data tables and marketplace search grids.
- **Visual Description:** Current page numbers, previous/next buttons, jump-to-page input, and items-per-page selector (`25 / 50 / 100 per page`).
- **States:** `default`, `page-active`, `disabled-prev/next`.
- **Token Dependencies:** `--lt-color-primary-600`, `--lt-color-slate-200`, `--lt-radius-sm`.
- **Allowed Usage:** All listings, tables, feeds, directories.

---

## 7. Overlays, Feedback & Messaging Components

### `MODAL-001` — Enterprise Dialog Modal
- **Purpose:** Focused user tasks (e.g., Submit Counter-Offer, Book Physical Inspection, Confirm Milestone).
- **Visual Description:** Semi-transparent backdrop (`rgba(15, 23, 42, 0.6)` with backdrop blur), centered dialog (`max-width: 560px` or `780px`), header with title and close button, body area, sticky footer with action buttons.
- **States:** `opening`, `open`, `closing`.
- **Token Dependencies:** `--lt-shadow-4`, `--lt-radius-lg`, `--lt-color-white`.
- **Allowed Usage:** Critical workflows, confirmations, interactive wizards.

### `DRW-001` — Side Inspector Drawer
- **Purpose:** In-depth inspection of tech-packs, factory audits, or RFQ details without leaving the current list.
- **Visual Description:** Slide-out panel anchored to the right edge (width: `480px` or `640px`), full viewport height, independent scroll area.
- **States:** `open`, `closed`.
- **Token Dependencies:** `--lt-shadow-4`, `--lt-color-white`, `--lt-transition-normal`.
- **Allowed Usage:** Tech-pack viewer, quick factory audit inspector, filter sheet on tablet.

### `ALRT-001` — Inline Notification & Alert Callout
- **Purpose:** System notifications, compliance alerts, inspection failure notices, AI recommendation tips.
- **Visual Description:** Rectangular callout with left accent border (`4px solid`), status icon, title, description, and action link.
  - *Success:* Emerald background `--lt-color-verify-50`, border `--lt-color-verify-600`.
  - *Warning:* Amber background `--lt-color-amber-50`, border `--lt-color-amber-600`.
  - *Critical:* Crimson background `--lt-color-danger-50`, border `--lt-color-danger-600`.
  - *AI Recommendation:* Violet background `--lt-color-ai-50`, border `--lt-color-ai-600`.
- **States:** `default`, `dismissed`.
- **Token Dependencies:** `--lt-radius-md`, `--lt-font-sans`.
- **Allowed Usage:** Everywhere contextual guidance or warning is required.

### `CHAT-001` — Order Communication & Negotiation Panel
- **Purpose:** Direct communication between buyer, manufacturer, and Leadirftex inspection officers.
- **Visual Description:** Pinned to order workspace. Chronological chat bubbles, sender role badge (Buyer / Factory Lead / QA Officer), file attachment chips, milestone tag pins.
- **States:** `active`, `minimized`, `sending`.
- **Token Dependencies:** `--lt-color-white`, `--lt-color-slate-100`, `--lt-radius-md`.
- **Allowed Usage:** Hub 14 (Order Workspace), Hub 13 (RFQ Negotiation).

---

## 8. Careers & Supporting Module Components

### `JOB-001` — Industry Job Card
- **Purpose:** Showcases textile, apparel, merchandiser, and QA job listings.
- **Visual Description:** Company logo, job role title (`font-h4`), factory/brand name, location (e.g., Dhaka, Surat, Ho Chi Minh City), salary range, employment type chip (Full-time / Contract), posted date, and "External Apply" action.
- **States:** `default`, `hover`, `bookmarked`, `applied`.
- **Token Dependencies:** `--lt-color-white`, `--lt-color-slate-200`, `--lt-radius-md`, `--lt-shadow-1`.
- **Allowed Usage:** Industry Job Feed module.

### `CV-001` — Interactive CV Builder Section Card
- **Purpose:** Section container for textile professional resume building (Personal Info, Factory Experience, Machinery Competence, Certifications).
- **Visual Description:** Clean form card with progress bar, ATS readability score badge, drag-and-drop reorder handle, and live PDF preview mirror.
- **States:** `editing`, `saved`, `ats-verified`.
- **Token Dependencies:** `--lt-color-white`, `--lt-color-slate-200`, `--lt-radius-md`.
- **Allowed Usage:** Free Professional CV Builder module.
