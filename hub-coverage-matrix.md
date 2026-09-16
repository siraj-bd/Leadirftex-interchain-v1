# Leadirftex Interchain — 21-Hub & Supporting Module Coverage Matrix

**Document Classification:** Architecture & Coverage Matrix  
**Status:** Canonical Reference  
**Purpose:** Formally proves that the Design Foundation, Component Library, and Template System completely support all 21 platform hubs and the supporting Industry Job Feed & CV Builder module without requiring ad-hoc UI invention.

---

## 1. Master Hub Coverage Matrix

| Hub # | Hub Official Name | Primary Template | Secondary Template(s) | Primary Components | Key Patterns | Domain-Specific Data Displayed |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **01** | Fashion & Design | `TPL-011` (Universal Listing) | `TPL-004` (Detail) | `CARD-001`, `CHIP-001`, `BTN-001` | `PAT-001`, `PAT-003` | Trend boards, tech-sketch galleries, 3D garment renders, color palettes, designer profiles |
| **02** | Textile & Garment Learning | `TPL-003` (Knowledge Hub) | `TPL-011` (Listing) | `CARD-001`, `DOC-001`, `CHIP-001` | `PAT-001`, `PAT-011` | ASTM/AATCC standards, fiber science guides, GSM calculation formulas, machinery manuals |
| **03** | Technology & Automation | `TPL-003` (Knowledge Hub) | `TPL-002` (Directory) | `CARD-001`, `STAT-001`, `BDG-001` | `PAT-001`, `PAT-004` | Auto-cutting algorithms, IoT loom monitoring, ERP integrations, robotics case studies |
| **04** | Raw Materials & Yarn | `TPL-001` (Marketplace) | `TPL-004` (Product Detail) | `CARD-002`, `SRCH-001`, `TABLE-001` | `PAT-001`, `PAT-002`, `PAT-003` | Yarn count (Ne, Nm, Denier), raw cotton staple length, spun vs filament, blend ratios |
| **05** | Fabric Marketplace | `TPL-001` (Marketplace) | `TPL-004` (Product Detail) | `CARD-002`, `SRCH-001`, `BDG-001` | `PAT-001`, `PAT-002`, `PAT-003` | GSM, construction (EPI/PPI), weave (Twill, Poplin, Jersey), dye type, shrinkage %, swatch order |
| **06** | Machinery Marketplace | `TPL-001` (Marketplace) | `TPL-004` (Product Detail) | `CARD-002`, `TABLE-001`, `BTN-001` | `PAT-001`, `PAT-003`, `PAT-004` | Machine RPM, cylinder diameter, gauge, power rating, CE/ISO certification, spare parts |
| **07** | Processing & Washing | `TPL-002` (Directory) | `TPL-004` (Detail) | `CARD-004`, `BDG-001`, `DOC-001` | `PAT-002`, `PAT-004`, `PAT-011` | Enzyme wash, ozone washing, laser distressing, ETP compliance, daily washing capacity |
| **08** | Trims & Accessories | `TPL-001` (Marketplace) | `TPL-004` (Product Detail) | `CARD-002`, `SRCH-001`, `BDG-001` | `PAT-001`, `PAT-002`, `PAT-003` | Zippers (metal/nylon), buttons, interlinings, care labels, OEKO-TEX Class 1 certification |
| **09** | Packaging & Chemical | `TPL-001` (Marketplace) | `TPL-004` (Product Detail) | `CARD-002`, `DOC-001`, `BDG-001` | `PAT-001`, `PAT-003`, `PAT-011` | Polybags (biodegradable/GRS), master cartons, textile dyes, auxiliaries, ZDHC level 3 pass |
| **10** | Product Development & CAD | `TPL-003` (Knowledge/CAD) | `TPL-011` (Listing) | `CARD-001`, `DOC-001`, `UPLD-001` | `PAT-003`, `PAT-008`, `PAT-011` | 3D Clo3D/Optitex files, DXF pattern downloads, grading rule tables, virtual fitting clips |
| **11** | R&D & Sample Development | `TPL-008` (Order Workspace) | `TPL-006` (Submission) | `STEP-001`, `CARD-001`, `UPLD-001` | `PAT-008`, `PAT-009`, `PAT-011` | Proto sample, Fit sample, Lab dip approvals, measurement tolerance variances, courier tracking |
| **12** | Buyer Requirements / Sourcing | `TPL-006` (Requirement Wizard)| `TPL-011` (Feed) | `STEP-001`, `INPUT-001`, `UPLD-001` | `PAT-005`, `PAT-002` | Target FOB, MOQ, target ex-factory date, tech-pack attachments, private/public RFQ scope |
| **13** | AI Matching & RFQ | `TPL-007` (AI Matching / RFQ) | `TPL-002` (Directory) | `CARD-003`, `SCORE-002`, `TABLE-001`| `PAT-006`, `PAT-007` | Algorithmic match score (0-100%), capability fit radar, quotation comparison breakdown |
| **14** | Order & Production Workspace | `TPL-008` (Order Workspace) | `TPL-010` (Dashboard) | `STEP-001`, `STAT-001`, `CHAT-001` | `PAT-008`, `PAT-009`, `PAT-011` | 13-stage order stepper, cutting/sewing output logs, purchase order hash, tri-party chat |
| **15** | Supplier & Service Network | `TPL-002` (Directory) | `TPL-005` (Profile) | `CARD-004`, `SCORE-001`, `BDG-001` | `PAT-002`, `PAT-004`, `PAT-012` | Yarns, fabric mills, finishing units, ISO/BSCI credentials, geographic cluster mapping |
| **16** | Factory Network | `TPL-002` (Directory) | `TPL-005` (Profile) | `CARD-003`, `SCORE-001`, `BDG-001` | `PAT-002`, `PAT-004`, `PAT-012` | Stitching lines, worker count, verified physical audit badges, on-time rate, past lookbook |
| **17** | Quality & Inspection Center | `TPL-009` (Inspection Center)| `TPL-010` (Dashboard) | `CARD-001`, `BDG-001`, `TABLE-001` | `PAT-010`, `PAT-011` | AQL levels (Critical, Major, Minor), defect photo logs, inspector geolocation, certificate hash |
| **18** | Logistics & Trade | `TPL-002` (Directory) | `TPL-011` (Listing) | `CARD-004`, `TABLE-001`, `BDG-001` | `PAT-002`, `PAT-009` | Freight forwarders, container tracking, Bill of Lading (BL) verification, customs clearance |
| **19** | Excess & Stocklot Marketplace| `TPL-001` (Marketplace) | `TPL-004` (Product Detail) | `CARD-002`, `BDG-001`, `BTN-001` | `PAT-001`, `PAT-002`, `PAT-003` | Ready-to-ship stocklot goods, remnant fabric rolls, discount pricing tiers, immediate inspection |
| **20** | Retail Marketplace | `TPL-001` (Marketplace) | `TPL-004` (Product Detail) | `CARD-002`, `SRCH-001`, `BTN-001` | `PAT-001`, `PAT-002`, `PAT-003` | Finished apparel lots, brand overruns, wholesale carton packaging, B2B wholesale pricing |
| **21** | Factory & Buyer Rating / Trust | `TPL-010` (Dashboard) | `TPL-005` (Profile) | `SCORE-001`, `STAT-001`, `TABLE-001`| `PAT-012`, `PAT-013` | Multi-dimensional Trust Score, on-time delivery %, verified dispute rate, PO-verified reviews |

---

## 2. Supporting Module Coverage Matrix

| Supporting Module Area | Primary Template | Secondary Template | Primary Components | Key Patterns | Domain-Specific Data Displayed |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Industry Job Feed** | `TPL-012` (Job Feed) | `TPL-011` (Listing) | `JOB-001`, `CHIP-001`, `DRW-001`, `BTN-001` | `PAT-014` | Merchandisers, CAD Pattern Masters, QA Managers, Knitting Technicians, salary range, factory link, External Apply |
| **Free Professional CV Builder** | `TPL-013` (CV Builder) | `TPL-010` (Dashboard) | `CV-001`, `INPUT-001`, `SCORE-001`, `BTN-001` | `PAT-015` | Textile technical competencies, machine proficiencies, factory work history, live ATS score meter, PDF generation |

---

## 3. Trust & Verification Matrix Across Hubs

```
┌─────────────────────────────────┬───────────────────┬───────────────────┬───────────────────┐
│ Hub Category                    │ Factory-Reported  │ AI-Assessed       │ Physically Verified│
├─────────────────────────────────┼───────────────────┼───────────────────┼───────────────────┤
│ Marketplaces (Hubs 4,5,6,8,9)   │ Stock quantity,   │ Price trend,      │ Swatch GSM audit, │
│                                 │ color shade photo │ similar fabrics   │ OEKO-TEX/GOTS cert│
├─────────────────────────────────┼───────────────────┼───────────────────┼───────────────────┤
│ Factory Network (Hubs 15, 16)   │ Self-claimed MOQ, │ Production lead-  │ On-site audit,    │
│                                 │ machine count     │ time prediction   │ WRAP/BSCI cert    │
├─────────────────────────────────┼───────────────────┼───────────────────┼───────────────────┤
│ AI Matching & RFQ (Hub 12, 13)  │ Initial RFQ specs │ Match score (0-100),Quotation signed  │
│                                 │ target FOB        │ capacity fit      │ with escrow terms │
├─────────────────────────────────┼───────────────────┼───────────────────┼───────────────────┤
│ Order & Quality (Hubs 14, 17)   │ Daily sewing count│ Risk delay alert, │ AQL defect tally, │
│                                 │ packing progress  │ defect classifier │ signed QA report  │
├─────────────────────────────────┼───────────────────┼───────────────────┼───────────────────┤
│ Trust Hub (Hub 21)              │ Company bio       │ Predicted default │ Audit trail,      │
│                                 │ claimed clients   │ risk score        │ PO verified review│
└─────────────────────────────────┴───────────────────┴───────────────────┴───────────────────┘
```
