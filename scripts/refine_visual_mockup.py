#!/usr/bin/env python3
"""
refine_visual_mockup.py
Applies the approved visual refinements to master-ui-mockup.html:
1. 3D Typography (Chrome metallic + fiery orange/crimson extruded lettering)
2. Column-style tall vertical 3D Header buttons (Home, About, Solutions, Network, Resources, Insights, Support, Contact)
3. Header button colors: Silver/white body, orange active, orange 3D icons, dark text on light buttons, no wrap
4. Hero side icon boxes: Strictly upright 0° tilt, straight front-facing, vertically aligned, consistent 84x84 size
5. Hero human/AI head: Front-facing, direct eye contact, internal brain with AI badge, no split body, symmetrical
6. Metallic silver upper 1/3 Hero environment with curved glowing orange/crimson horizon transition
7. Lower section (Black / near-black + deep red/crimson) with Core Areas cards row
"""

import re
from html.parser import HTMLParser

def build_refined_html():
    with open("master-ui-mockup.html", "r", encoding="utf-8") as f:
        content = f.read()

    # 1. ADD / UPDATE CSS IN <style>
    new_css = """
    /* ==========================================================================
       PREMIUM 3D TYPOGRAPHY SYSTEM (CHROME METALLIC + FIERY ORANGE/CRIMSON)
       ========================================================================== */
    .text-3d-chrome {
      display: inline-block;
      font-family: var(--lt-font-sans);
      font-weight: 900;
      text-transform: uppercase;
      letter-spacing: -0.01em;
      color: #f1f5f9;
      background: linear-gradient(180deg, 
        #ffffff 0%, 
        #f8fafc 20%, 
        #cbd5e1 42%, 
        #94a3b8 48%, 
        #e2e8f0 54%, 
        #64748b 85%, 
        #334155 100%
      );
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      filter: drop-shadow(0 1px 0 #ffffff)
              drop-shadow(0 2px 0 #cbd5e1)
              drop-shadow(0 3px 0 #94a3b8)
              drop-shadow(0 4px 0 #64748b)
              drop-shadow(0 5px 2px rgba(0, 0, 0, 0.45))
              drop-shadow(0 10px 20px rgba(0, 0, 0, 0.35));
    }

    .text-3d-orange {
      display: inline-block;
      font-family: var(--lt-font-sans);
      font-weight: 900;
      text-transform: uppercase;
      letter-spacing: -0.01em;
      color: #ff4800;
      background: linear-gradient(180deg, 
        #ffa366 0%, 
        #ff5500 25%, 
        #e62e00 50%, 
        #ff7733 55%, 
        #b31a00 85%, 
        #7a1000 100%
      );
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      filter: drop-shadow(0 1px 0 #ffaa80)
              drop-shadow(0 2px 0 #ff5c1a)
              drop-shadow(0 3px 0 #cc2900)
              drop-shadow(0 4px 0 #991f00)
              drop-shadow(0 5px 2px rgba(122, 16, 0, 0.55))
              drop-shadow(0 8px 24px rgba(255, 78, 0, 0.65));
    }

    .text-3d-chrome-sm {
      display: inline-block;
      font-family: var(--lt-font-sans);
      font-weight: 900;
      text-transform: uppercase;
      letter-spacing: 0.01em;
      color: #f1f5f9;
      background: linear-gradient(180deg, #ffffff 0%, #cbd5e1 50%, #64748b 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      filter: drop-shadow(0 1px 0 #ffffff)
              drop-shadow(0 2px 0 #94a3b8)
              drop-shadow(0 3px 2px rgba(0, 0, 0, 0.4));
    }

    .text-3d-orange-sm {
      display: inline-block;
      font-family: var(--lt-font-sans);
      font-weight: 900;
      text-transform: uppercase;
      letter-spacing: 0.01em;
      color: #ff4800;
      background: linear-gradient(180deg, #ffa366 0%, #ff4e00 50%, #b31a00 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      filter: drop-shadow(0 1px 0 #ffaa80)
              drop-shadow(0 2px 0 #cc2900)
              drop-shadow(0 3px 2px rgba(122, 16, 0, 0.5));
    }

    /* ==========================================================================
       METALLIC SILVER SITE HEADER & TALL VERTICAL 3D BUTTONS
       ========================================================================== */
    .site-header {
      background: linear-gradient(180deg, #c9d2dc 0%, #dfe5ed 60%, #c4ccd7 100%);
      color: #0f172a;
      position: sticky;
      top: 0;
      z-index: 900;
      border-bottom: 1px solid rgba(255, 255, 255, 0.7);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      box-shadow: 0 4px 14px rgba(0, 0, 0, 0.12), 0 1px 3px rgba(0, 0, 0, 0.06), inset 0 1px 0 #ffffff;
      transition: all 0.25s ease;
    }

    .header-command-tier {
      max-width: 1440px;
      margin: 0 auto;
      padding: 8px 20px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: nowrap !important;
      gap: 12px;
      width: 100%;
    }

    .brand-logo-unit {
      display: flex;
      align-items: center;
      gap: 10px;
      text-decoration: none;
      color: #0f172a;
      flex-shrink: 0;
      white-space: nowrap !important;
      transition: transform 0.2s ease;
    }

    .brand-logo-unit:hover {
      transform: translateY(-1px);
    }

    .brand-hex-mark {
      width: 42px;
      height: 42px;
      background: linear-gradient(135deg, #ff5500 0%, #e62e00 50%, #b31a00 100%);
      border-radius: 10px;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 4px 12px rgba(230, 46, 0, 0.4), inset 0 1px 1px rgba(255, 255, 255, 0.6);
      flex-shrink: 0;
      transition: transform 0.2s ease, box-shadow 0.2s ease;
    }

    .brand-logo-unit:hover .brand-hex-mark {
      transform: translateY(-1px) scale(1.03);
      box-shadow: 0 6px 16px rgba(255, 78, 0, 0.5), inset 0 1px 1.5px rgba(255, 255, 255, 0.7);
    }

    .brand-hex-mark svg {
      width: 26px;
      height: 26px;
      fill: white;
      filter: drop-shadow(0 1px 2px rgba(0,0,0,0.3));
    }

    .brand-titles {
      display: flex;
      flex-direction: column;
      line-height: 1.1;
    }

    .brand-name {
      font-size: 20px;
      font-weight: 900;
      letter-spacing: -0.01em;
      line-height: 1.05;
      color: #0f172a;
      white-space: nowrap !important;
    }

    .brand-descriptor {
      font-size: 10.5px;
      font-family: var(--lt-font-mono);
      color: #334155;
      letter-spacing: 1.8px;
      font-weight: 800;
      text-transform: uppercase;
      margin-top: 2px;
      white-space: nowrap !important;
    }

    .brand-tagline {
      font-size: 8px;
      font-family: var(--lt-font-mono);
      color: #64748b;
      letter-spacing: 0.8px;
      text-transform: uppercase;
      margin-top: 2px;
      white-space: nowrap !important;
    }

    /* 3D Vertical Column-Style Navigation Buttons */
    .header-nav-strip {
      display: flex;
      align-items: center;
      gap: 6px;
      flex-shrink: 0;
      flex-wrap: nowrap !important;
    }

    .header-nav-btn-3d {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      gap: 4px;
      width: 58px;
      height: 72px;
      border-radius: 12px;
      text-decoration: none;
      white-space: nowrap !important;
      flex-shrink: 0;
      cursor: pointer;
      background: linear-gradient(180deg, #ffffff 0%, #f1f5f9 60%, #e2e8f0 100%);
      border: 1px solid rgba(255, 255, 255, 0.95);
      box-shadow: 0 4px 10px rgba(0, 0, 0, 0.12), 0 1px 2px rgba(0, 0, 0, 0.06), inset 0 1px 1.5px #ffffff, inset 0 -1px 2px rgba(0, 0, 0, 0.06);
      transition: all 0.18s cubic-bezier(0.16, 1, 0.3, 1);
      position: relative;
    }

    .header-nav-btn-3d:hover {
      transform: translateY(-2px);
      box-shadow: 0 6px 16px rgba(0, 0, 0, 0.16), 0 2px 4px rgba(0, 0, 0, 0.08), 0 0 12px rgba(255, 78, 0, 0.18), inset 0 1px 1.5px #ffffff;
      border-color: rgba(255, 78, 0, 0.3);
    }

    .header-nav-btn-3d.active {
      background: linear-gradient(180deg, #ff4e00 0%, #e62e00 55%, #c81e00 100%);
      border-color: rgba(255, 255, 255, 0.4);
      box-shadow: 0 4px 14px rgba(230, 46, 0, 0.45), 0 1px 3px rgba(0, 0, 0, 0.2), inset 0 1px 1.5px rgba(255, 255, 255, 0.6), inset 0 -1px 2px rgba(0, 0, 0, 0.25);
    }

    .header-nav-btn-3d .nav-3d-icon-wrap {
      width: 28px;
      height: 28px;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }

    .header-nav-btn-3d .nav-3d-svg {
      width: 22px;
      height: 22px;
      filter: drop-shadow(0 2px 3px rgba(0, 0, 0, 0.15));
      transition: transform 0.18s ease;
    }

    .header-nav-btn-3d:hover .nav-3d-svg {
      transform: scale(1.08);
    }

    .header-nav-btn-3d .nav-3d-label {
      font-size: 10.5px;
      font-weight: 700;
      color: #1e293b;
      letter-spacing: 0.2px;
      line-height: 1;
    }

    .header-nav-btn-3d.active .nav-3d-label {
      color: #ffffff;
      text-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);
    }

    /* Pill Search Bar */
    .header-search-pill {
      display: flex;
      align-items: center;
      background: #ffffff;
      border: 1px solid #cbd5e1;
      border-radius: 9999px;
      padding: 3px 3px 3px 14px;
      gap: 8px;
      box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.05), 0 2px 6px rgba(0, 0, 0, 0.04);
      flex-shrink: 0;
      width: 190px;
    }

    .header-search-pill input {
      border: none;
      background: transparent;
      outline: none;
      font-size: 12px;
      color: #1e293b;
      width: 100%;
      font-weight: 500;
    }

    .header-search-pill input::placeholder {
      color: #94a3b8;
    }

    .header-search-btn-3d {
      width: 32px;
      height: 32px;
      border-radius: 50%;
      background: linear-gradient(180deg, #ff4e00 0%, #e62e00 100%);
      border: 1px solid rgba(255, 255, 255, 0.4);
      box-shadow: 0 2px 6px rgba(230, 46, 0, 0.4), inset 0 1px 1px rgba(255, 255, 255, 0.6);
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      flex-shrink: 0;
      color: white;
      transition: transform 0.15s ease;
    }

    .header-search-btn-3d:hover {
      transform: scale(1.05);
    }

    /* ==========================================================================
       METALLIC SILVER HERO ENVIRONMENT (UPPER ~1/3 REGION)
       ========================================================================== */
    .hero-enterprise-section {
      background: linear-gradient(180deg, #c5cdd6 0%, #dbe2ea 20%, #eff2f6 50%, #c9d2dc 85%, #a8b3c0 100%);
      color: #0f172a;
      padding: 56px 24px 0px;
      position: relative;
      overflow: hidden;
      box-shadow: 0 30px 60px -15px rgba(0, 0, 0, 0.5);
    }

    .hero-silver-texture {
      position: absolute;
      inset: 0;
      pointer-events: none;
      z-index: 1;
      opacity: 0.45;
      background: repeating-linear-gradient(90deg, rgba(255,255,255,0.04) 0px, rgba(255,255,255,0.04) 1px, transparent 1px, transparent 3px),
                  radial-gradient(ellipse at 50% 25%, rgba(255, 255, 255, 0.8) 0%, transparent 70%);
    }

    .hero-content-max {
      max-width: 1440px;
      margin: 0 auto;
      position: relative;
      z-index: 3;
    }

    .hero-stage-layout {
      display: grid;
      grid-template-columns: minmax(360px, 1fr) auto minmax(180px, 220px);
      align-items: center;
      gap: 28px;
    }

    .hero-left-column {
      display: flex;
      flex-direction: column;
      justify-content: center;
    }

    .hero-eyebrow-3d {
      font-size: 13px;
      font-weight: 800;
      letter-spacing: 2px;
      color: #475569;
      text-transform: uppercase;
      font-family: var(--lt-font-mono);
      margin-bottom: 12px;
      text-shadow: 0 1px 1px #ffffff;
    }

    .hero-lead-title-3d {
      font-size: 48px;
      line-height: 1.08;
      font-weight: 900;
      margin-bottom: 16px;
      display: flex;
      flex-direction: column;
    }

    .hero-subtag-3d {
      font-size: 12.5px;
      font-weight: 700;
      letter-spacing: 1.8px;
      color: #475569;
      text-transform: uppercase;
      font-family: var(--lt-font-mono);
      margin-bottom: 24px;
      text-shadow: 0 1px 1px #ffffff;
    }

    .hero-cta-group-3d {
      display: flex;
      align-items: center;
      gap: 16px;
      margin-bottom: 28px;
    }

    .hero-cta-explore-3d {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: linear-gradient(180deg, #ff4e00 0%, #e62e00 50%, #cc1f00 100%);
      color: #ffffff;
      font-size: 14.5px;
      font-weight: 800;
      padding: 12px 28px;
      border-radius: 9999px;
      border: 1px solid rgba(255, 255, 255, 0.45);
      box-shadow: 0 8px 24px rgba(230, 46, 0, 0.45), 0 2px 4px rgba(0, 0, 0, 0.15), inset 0 1.5px 1.5px rgba(255, 255, 255, 0.7);
      cursor: pointer;
      text-decoration: none;
      transition: all 0.18s ease;
    }

    .hero-cta-explore-3d:hover {
      transform: translateY(-2px);
      box-shadow: 0 12px 28px rgba(255, 78, 0, 0.55), 0 4px 8px rgba(0, 0, 0, 0.2), inset 0 1.5px 1.5px rgba(255, 255, 255, 0.85);
    }

    .hero-cta-video-3d {
      display: inline-flex;
      align-items: center;
      gap: 10px;
      background: transparent;
      border: none;
      color: #1e293b;
      font-size: 14px;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.18s ease;
    }

    .hero-cta-video-3d .play-3d-btn {
      width: 38px;
      height: 38px;
      border-radius: 50%;
      background: linear-gradient(180deg, #ffffff 0%, #e2e8f0 100%);
      border: 1px solid rgba(255, 255, 255, 0.95);
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15), inset 0 1px 1.5px #ffffff;
      display: flex;
      align-items: center;
      justify-content: center;
      color: #ff4e00;
      font-size: 13px;
      transition: transform 0.18s ease;
    }

    .hero-cta-video-3d:hover .play-3d-btn {
      transform: scale(1.08);
      box-shadow: 0 6px 16px rgba(255, 78, 0, 0.3), inset 0 1px 1.5px #ffffff;
    }

    /* Center Stage: Symmetrical Head + Straight Front-Facing Icon Boxes */
    .hero-center-stage-3d {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 16px;
      position: relative;
    }

    .hero-icon-boxes-column {
      display: flex;
      flex-direction: column;
      gap: 14px;
      z-index: 4;
    }

    /* Strictly Upright Front-Facing 3D Icon Box (0° Tilt, 0° Yaw, 0° Pitch) */
    .hero-icon-box-3d {
      width: 84px;
      height: 84px;
      border-radius: 14px;
      background: linear-gradient(180deg, #ffffff 0%, #f8fafc 55%, #e2e8f0 100%);
      border: 1px solid rgba(255, 255, 255, 0.95);
      border-bottom: 2px solid rgba(255, 78, 0, 0.45);
      box-shadow: 0 6px 16px rgba(0, 0, 0, 0.12), 0 1px 3px rgba(0, 0, 0, 0.08), 0 0 12px rgba(255, 78, 0, 0.14), inset 0 1px 1.5px #ffffff, inset 0 -1px 2px rgba(0, 0, 0, 0.06);
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      gap: 4px;
      padding: 6px;
      transform: none !important; /* Strictly upright, 0° tilt */
      transition: transform 0.18s ease, box-shadow 0.18s ease;
      cursor: pointer;
    }

    .hero-icon-box-3d:hover {
      transform: translateY(-2px) !important;
      box-shadow: 0 10px 22px rgba(0, 0, 0, 0.16), 0 0 18px rgba(255, 78, 0, 0.28), inset 0 1px 1.5px #ffffff;
    }

    .hero-icon-box-3d .icon-box-svg-wrap {
      width: 38px;
      height: 38px;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }

    .hero-icon-box-3d .icon-box-svg-wrap svg {
      width: 32px;
      height: 32px;
      filter: drop-shadow(0 2px 3px rgba(0, 0, 0, 0.15));
    }

    .hero-icon-box-3d .icon-box-label {
      font-size: 9px;
      font-weight: 700;
      color: #1e293b;
      text-align: center;
      line-height: 1.15;
      max-width: 74px;
    }

    /* Head Stage Frame */
    .hero-head-center-frame {
      position: relative;
      width: 190px;
      height: 280px;
      display: flex;
      align-items: flex-end;
      justify-content: center;
      z-index: 3;
    }

    .hero-head-img {
      width: 100%;
      height: 100%;
      object-fit: contain;
      object-position: bottom center;
      pointer-events: none;
      filter: drop-shadow(0 10px 24px rgba(0, 0, 0, 0.2));
    }

    /* Far Right Typography */
    .hero-right-typography {
      display: flex;
      flex-direction: column;
      justify-content: center;
      gap: 18px;
      border-left: 1px solid rgba(0, 0, 0, 0.08);
      padding-left: 20px;
    }

    .hero-intel-title-block {
      display: flex;
      flex-direction: column;
      line-height: 1.35;
    }

    .hero-intel-word {
      font-size: 16px;
      font-weight: 800;
      letter-spacing: 2px;
      text-transform: uppercase;
      color: #334155;
      font-family: var(--lt-font-mono);
    }

    .hero-intel-subblock {
      display: flex;
      flex-direction: column;
      line-height: 1.5;
    }

    .hero-intel-subline {
      font-size: 10px;
      font-weight: 700;
      letter-spacing: 1.4px;
      text-transform: uppercase;
      color: #64748b;
      font-family: var(--lt-font-mono);
    }

    /* Curved Glowing Horizon Transition */
    .hero-silver-boundary {
      position: relative;
      width: 100%;
      height: 38px;
      margin-top: 20px;
      border-top: 2.5px solid #ff4e00;
      box-shadow: 0 -4px 24px rgba(255, 78, 0, 0.8), 0 0 45px rgba(230, 46, 0, 0.4);
      border-radius: 50% 50% 0 0 / 24px 24px 0 0;
      background: #03050a;
      z-index: 10;
    }

    /* ==========================================================================
       CORE AREAS SECTION (LOWER BLACK / NEAR-BLACK + CRIMSON REGION)
       ========================================================================== */
    .core-areas-section {
      background: #03050a;
      padding: 24px 24px 50px;
      position: relative;
      z-index: 10;
    }

    .core-areas-container {
      max-width: 1440px;
      margin: 0 auto;
    }

    .core-areas-header-row {
      display: flex;
      align-items: flex-end;
      justify-content: space-between;
      margin-bottom: 28px;
    }

    .sec-eyebrow-track {
      display: flex;
      align-items: center;
      gap: 10px;
      margin-bottom: 6px;
    }

    .eyebrow-line {
      width: 24px;
      height: 2px;
      background: #ff4e00;
      border-radius: 1px;
    }

    .eyebrow-label {
      font-size: 11px;
      font-weight: 800;
      letter-spacing: 1.5px;
      color: #ff4e00;
      text-transform: uppercase;
      font-family: var(--lt-font-mono);
    }

    .core-areas-headline {
      font-size: 28px;
      font-weight: 900;
      letter-spacing: 0.5px;
      margin: 0;
    }

    .btn-view-all-solutions {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: rgba(15, 23, 42, 0.85);
      color: #e2e8f0;
      border: 1px solid rgba(255, 78, 0, 0.4);
      border-radius: 9999px;
      padding: 8px 18px;
      font-size: 12px;
      font-weight: 700;
      cursor: pointer;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.5), 0 0 12px rgba(255, 78, 0, 0.15);
      transition: all 0.18s ease;
    }

    .btn-view-all-solutions:hover {
      border-color: #ff4e00;
      color: #ffffff;
      box-shadow: 0 6px 18px rgba(0, 0, 0, 0.7), 0 0 20px rgba(255, 78, 0, 0.35);
      transform: translateY(-1.5px);
    }

    .core-areas-cards-row {
      display: grid;
      grid-template-columns: repeat(6, 1fr);
      gap: 14px;
    }

    .core-area-card {
      background: linear-gradient(180deg, rgba(20, 30, 48, 0.75) 0%, rgba(10, 16, 28, 0.92) 100%);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 16px;
      padding: 20px 14px 16px;
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      cursor: pointer;
      box-shadow: 0 10px 24px -6px rgba(0, 0, 0, 0.8), 0 0 16px -4px rgba(255, 78, 0, 0.18), inset 0 1px 0 rgba(255, 255, 255, 0.1);
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .core-area-card:hover {
      transform: translateY(-5px);
      border-color: rgba(255, 78, 0, 0.45);
      box-shadow: 0 16px 36px -6px rgba(0, 0, 0, 0.95), 0 0 24px rgba(255, 78, 0, 0.35), inset 0 1px 0 rgba(255, 255, 255, 0.2);
    }

    .core-card-3d-stage {
      position: relative;
      width: 68px;
      height: 68px;
      display: flex;
      align-items: center;
      justify-content: center;
      margin-bottom: 12px;
    }

    .core-card-icon-wrap {
      width: 52px;
      height: 52px;
      display: flex;
      align-items: center;
      justify-content: center;
      z-index: 2;
      filter: drop-shadow(0 4px 8px rgba(0, 0, 0, 0.4)) drop-shadow(0 0 10px rgba(255, 78, 0, 0.3));
      transition: transform 0.2s ease;
    }

    .core-area-card:hover .core-card-icon-wrap {
      transform: translateY(-3px) scale(1.05);
    }

    .core-card-shadow {
      position: absolute;
      bottom: 6px;
      width: 44px;
      height: 10px;
      border-radius: 50%;
      background: radial-gradient(ellipse at center, rgba(0, 0, 0, 0.7) 0%, transparent 70%);
      z-index: 1;
    }

    .core-card-title {
      font-size: 13px;
      font-weight: 700;
      color: #f8fafc;
      margin: 0 0 6px 0;
      line-height: 1.2;
    }

    .core-card-desc {
      font-size: 11px;
      color: #94a3b8;
      margin: 0 0 14px 0;
      line-height: 1.35;
      flex-grow: 1;
    }

    .core-card-action-btn {
      width: 28px;
      height: 28px;
      border-radius: 50%;
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid rgba(255, 255, 255, 0.12);
      display: flex;
      align-items: center;
      justify-content: center;
      color: #ff4e00;
      font-size: 13px;
      transition: all 0.18s ease;
    }

    .core-area-card:hover .core-card-action-btn {
      background: #ff4e00;
      color: #ffffff;
      border-color: #ff4e00;
      box-shadow: 0 0 10px rgba(255, 78, 0, 0.5);
    }

    @media (max-width: 1200px) {
      .core-areas-cards-row {
        grid-template-columns: repeat(3, 1fr);
      }
      .hero-stage-layout {
        grid-template-columns: 1fr;
      }
      .hero-right-typography {
        display: none;
      }
    }
    """

    # Inject new_css right before </style>
    content = content.replace("</style>", f"\n{new_css}\n  </style>")

    # 2. SHARED SVG DEFS FOR 3D ICONS
    svg_defs = """
    <!-- Global Shared 3D Icon Gradients -->
    <svg style="display:none;" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <linearGradient id="nav-icon-grad-orange" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#ff7733" />
          <stop offset="40%" stop-color="#ff4e00" />
          <stop offset="80%" stop-color="#d92b00" />
          <stop offset="100%" stop-color="#991b00" />
        </linearGradient>
        <linearGradient id="nav-icon-grad-orange-light" x1="0%" y1="0%" x2="0%" y2="100%">
          <stop offset="0%" stop-color="#ffa366" />
          <stop offset="100%" stop-color="#ff5500" />
        </linearGradient>
        <linearGradient id="nav-icon-grad-orange-dark" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#cc2900" />
          <stop offset="100%" stop-color="#661000" />
        </linearGradient>
        <linearGradient id="nav-icon-grad-white" x1="0%" y1="0%" x2="0%" y2="100%">
          <stop offset="0%" stop-color="#ffffff" />
          <stop offset="100%" stop-color="#e2e8f0" />
        </linearGradient>
      </defs>
    </svg>
    """

    # 3. REFINED SITE HEADER HTML
    refined_header_html = """    <header class="site-header" id="main-site-header">
      <div class="header-command-tier">
        <!-- Brand Logo Lockup -->
        <a href="#" class="brand-logo-unit" onclick="showScreen('screen-home'); return false;" title="Leadirftex Interchain Home">
          <div class="brand-hex-mark">
            <svg viewBox="0 0 24 24">
              <path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/>
            </svg>
          </div>
          <div class="brand-titles">
            <span class="brand-name">Leadirftex</span>
            <span class="brand-descriptor">INTERCHAIN</span>
            <span class="brand-tagline">CONNECTING APPAREL, EMPOWERING TOMORROW.</span>
          </div>
        </a>

        <!-- Column-Style Tall Vertical 3D Navigation Buttons (Single Line, No Wrap) -->
        <nav class="header-nav-strip" aria-label="Main Navigation">
          <!-- 1. Home (Active) -->
          <a href="#" class="header-nav-btn-3d active" onclick="showScreen('screen-home'); return false;" title="Home">
            <div class="nav-3d-icon-wrap">
              <svg class="nav-3d-svg" viewBox="0 0 24 24" fill="none">
                <path d="M12 3L2 12h3v8h5v-5h4v5h5v-8h3L12 3z" fill="url(#nav-icon-grad-white)" />
                <path d="M12 3.5L3.5 11.5H5v7.5h4v-5h6v5h4v-7.5h1.5L12 3.5z" stroke="rgba(255,255,255,0.7)" stroke-width="0.8" />
              </svg>
            </div>
            <span class="nav-3d-label">Home</span>
          </a>

          <!-- 2. About -->
          <a href="#" class="header-nav-btn-3d" onclick="showScreen('screen-home'); setTimeout(() => document.getElementById('strategic-architecture')?.scrollIntoView({behavior: 'smooth'}), 120); return false;" title="About">
            <div class="nav-3d-icon-wrap">
              <svg class="nav-3d-svg" viewBox="0 0 24 24" fill="none">
                <path d="M4 21V7l8-4 8 4v14H4z" fill="url(#nav-icon-grad-orange)" />
                <rect x="7" y="9" width="2.5" height="2.5" rx="0.5" fill="#ffffff" fill-opacity="0.85" />
                <rect x="14.5" y="9" width="2.5" height="2.5" rx="0.5" fill="#ffffff" fill-opacity="0.85" />
                <rect x="7" y="14" width="2.5" height="2.5" rx="0.5" fill="#ffffff" fill-opacity="0.85" />
                <rect x="14.5" y="14" width="2.5" height="2.5" rx="0.5" fill="#ffffff" fill-opacity="0.85" />
                <rect x="10.5" y="16" width="3" height="5" rx="0.5" fill="#7a1000" />
              </svg>
            </div>
            <span class="nav-3d-label">About</span>
          </a>

          <!-- 3. Solutions -->
          <a href="#" class="header-nav-btn-3d" onclick="showScreen('screen-marketplace'); return false;" title="Solutions">
            <div class="nav-3d-icon-wrap">
              <svg class="nav-3d-svg" viewBox="0 0 24 24" fill="none">
                <path d="M12 2.5L20.5 7.5V16.5L12 21.5L3.5 16.5V7.5L12 2.5Z" fill="url(#nav-icon-grad-orange)" />
                <path d="M12 2.5L20.5 7.5L12 12.5L3.5 7.5L12 2.5Z" fill="url(#nav-icon-grad-orange-light)" />
                <path d="M12 12.5V21.5L20.5 16.5V7.5L12 12.5Z" fill="url(#nav-icon-grad-orange-dark)" opacity="0.9" />
                <path d="M12 2.5L20.5 7.5L12 12.5L3.5 7.5Z" stroke="#ffffff" stroke-width="0.8" stroke-opacity="0.6" />
              </svg>
            </div>
            <span class="nav-3d-label">Solutions</span>
          </a>

          <!-- 4. Network -->
          <a href="#" class="header-nav-btn-3d" onclick="showScreen('screen-factory'); return false;" title="Network">
            <div class="nav-3d-icon-wrap">
              <svg class="nav-3d-svg" viewBox="0 0 24 24" fill="none">
                <circle cx="12" cy="7" r="3.2" fill="url(#nav-icon-grad-orange)" />
                <path d="M6 19c0-3.3 2.7-6 6-6s6 2.7 6 6" fill="url(#nav-icon-grad-orange)" />
                <circle cx="5" cy="10" r="2.2" fill="url(#nav-icon-grad-orange-light)" />
                <path d="M1 20c0-2.2 1.8-4 4-4 .8 0 1.6.3 2.2.7" stroke="url(#nav-icon-grad-orange)" stroke-width="1.5" stroke-linecap="round" fill="none" />
                <circle cx="19" cy="10" r="2.2" fill="url(#nav-icon-grad-orange-light)" />
                <path d="M23 20c0-2.2-1.8-4-4-4-.8 0-1.6.3-2.2.7" stroke="url(#nav-icon-grad-orange)" stroke-width="1.5" stroke-linecap="round" fill="none" />
              </svg>
            </div>
            <span class="nav-3d-label">Network</span>
          </a>

          <!-- 5. Resources -->
          <a href="#" class="header-nav-btn-3d" onclick="showScreen('screen-hubs'); return false;" title="Resources">
            <div class="nav-3d-icon-wrap">
              <svg class="nav-3d-svg" viewBox="0 0 24 24" fill="none">
                <path d="M12 15a3 3 0 100-6 3 3 0 000 6z" fill="#ffffff" />
                <path fill-rule="evenodd" clip-rule="evenodd" d="M12 2a2 2 0 00-2 2v.2a8.03 8.03 0 00-2.3 1L6.3 4a2 2 0 00-2.8 0L2.1 5.4a2 2 0 000 2.8l1.2 1.4c-.4.7-.7 1.5-1 2.3H2a2 2 0 00-2 2v2a2 2 0 002 2h.3c.3.8.6 1.6 1 2.3l-1.2 1.4a2 2 0 000 2.8l1.4 1.4a2 2 0 002.8 0l1.4-1.2c.7.4 1.5.7 2.3 1V22a2 2 0 002 2h2a2 2 0 002-2v-.3c.8-.3 1.6-.6 2.3-1l1.4 1.2a2 2 0 002.8 0l1.4-1.4a2 2 0 000-2.8l-1.2-1.4c.4-.7.7-1.5 1-2.3H22a2 2 0 002-2v-2a2 2 0 00-2-2h-.3a8.03 8.03 0 00-1-2.3l1.2-1.4a2 2 0 000-2.8l-1.4-1.4a2 2 0 00-2.8 0l-1.4 1.2a8.03 8.03 0 00-2.3-1V4a2 2 0 00-2-2h-2zm-5 10a5 5 0 1110 0 5 5 0 01-10 0z" fill="url(#nav-icon-grad-orange)" />
              </svg>
            </div>
            <span class="nav-3d-label">Resources</span>
          </a>

          <!-- 6. Insights -->
          <a href="#" class="header-nav-btn-3d" onclick="showScreen('screen-ai-matching'); return false;" title="Insights">
            <div class="nav-3d-icon-wrap">
              <svg class="nav-3d-svg" viewBox="0 0 24 24" fill="none">
                <path d="M6 3h8l6 6v12a2 2 0 01-2 2H6a2 2 0 01-2-2V5a2 2 0 012-2z" fill="url(#nav-icon-grad-orange)" />
                <path d="M14 3v6h6" fill="#fca5a5" />
                <line x1="8" y1="13" x2="16" y2="13" stroke="#ffffff" stroke-width="1.5" stroke-linecap="round" />
                <line x1="8" y1="16" x2="16" y2="16" stroke="#ffffff" stroke-width="1.5" stroke-linecap="round" />
                <line x1="8" y1="19" x2="12" y2="19" stroke="#ffffff" stroke-width="1.5" stroke-linecap="round" />
              </svg>
            </div>
            <span class="nav-3d-label">Insights</span>
          </a>

          <!-- 7. Support -->
          <a href="#" class="header-nav-btn-3d" onclick="showScreen('screen-trust'); return false;" title="Support">
            <div class="nav-3d-icon-wrap">
              <svg class="nav-3d-svg" viewBox="0 0 24 24" fill="none">
                <path d="M3 14v-3a9 9 0 0118 0v3" stroke="url(#nav-icon-grad-orange)" stroke-width="2.5" stroke-linecap="round" fill="none" />
                <rect x="2" y="13" width="4" height="7" rx="2" fill="url(#nav-icon-grad-orange)" />
                <rect x="18" y="13" width="4" height="7" rx="2" fill="url(#nav-icon-grad-orange)" />
                <path d="M20 18v2a3 3 0 01-3 3h-4" stroke="url(#nav-icon-grad-orange)" stroke-width="2" stroke-linecap="round" fill="none" />
              </svg>
            </div>
            <span class="nav-3d-label">Support</span>
          </a>

          <!-- 8. Contact -->
          <a href="#" class="header-nav-btn-3d" onclick="showScreen('screen-workspace'); return false;" title="Contact">
            <div class="nav-3d-icon-wrap">
              <svg class="nav-3d-svg" viewBox="0 0 24 24" fill="none">
                <rect x="3" y="5" width="18" height="14" rx="2.5" fill="url(#nav-icon-grad-orange)" />
                <path d="M3 6.5l9 6.5 9-6.5" stroke="#ffffff" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" fill="none" />
              </svg>
            </div>
            <span class="nav-3d-label">Contact</span>
          </a>
        </nav>

        <!-- Compact 3D Pill Search Bar -->
        <div class="header-search-pill">
          <input type="text" placeholder="Search..." aria-label="Search">
          <div class="header-search-btn-3d" title="Search">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
              <circle cx="11" cy="11" r="8"></circle>
              <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
            </svg>
          </div>
        </div>

        <!-- 3D Action CTA Group -->
        <div class="header-cta-group">
          <button class="btn-header-ghost" onclick="showScreen('screen-buyer-req')" title="Create Buyer Requirement">+ Post RFQ</button>
          <button class="btn-header-primary" onclick="showScreen('screen-marketplace')" title="Browse Catalog">Browse Market</button>
          <button class="btn-header-cart" id="header-cart-btn" onclick="toggleCartDrawer()" title="View Swatch &amp; Order Bag" aria-label="Open Swatch Bag">
            <span>🛒 Swatch Bag</span>
            <span class="header-cart-count-badge" id="header-cart-count">1</span>
          </button>
          <div class="header-user-badge" onclick="showScreen('screen-dashboard')" title="View Corporate Profile">
            <div class="user-avatar-initials">✓</div>
            <div class="user-entity-info">
              <span class="user-company-name">Apex Textile Ltd.</span>
              <span class="user-trust-status">● Tier 1 Platinum</span>
            </div>
          </div>
          <!-- Mobile Menu Toggle Button -->
          <button class="header-mobile-toggle" id="header-mobile-toggle-btn" onclick="toggleMobileNav()" aria-label="Toggle Navigation Menu">
            <span class="mobile-toggle-bar"></span>
            <span class="mobile-toggle-bar"></span>
            <span class="mobile-toggle-bar"></span>
          </button>
        </div>
      </div>
    </header>"""

    # Replace the old <header> block
    old_header_pattern = r'<header class="site-header" id="main-site-header">.*?</header>'
    content = re.sub(old_header_pattern, svg_defs + "\n" + refined_header_html, content, flags=re.DOTALL)

    # 4. REFINED HERO SECTION & LOWER CORE AREAS SECTION
    refined_hero_and_core_areas_html = """      <!-- ====================================================================
           HERO SECTION: METALLIC SILVER ENVIRONMENT (UPPER ~1/3 REGION)
           ==================================================================== -->
      <section class="hero-enterprise-section" id="hero-section">
        <!-- Brushed Metallic Grain Sheen -->
        <div class="hero-silver-texture" aria-hidden="true"></div>

        <div class="hero-content-max">
          <div class="hero-stage-layout">
            <!-- Left Column: Premium 3D Typography & Direct CTAs -->
            <div class="hero-left-column">
              <div class="hero-eyebrow-3d">GLOBAL APPAREL ECOSYSTEM</div>
              <h1 class="hero-lead-title-3d">
                <span class="text-3d-chrome">CONNECTING</span>
                <span class="text-3d-orange">APPAREL</span>
                <span class="text-3d-chrome">EMPOWERING TOMORROW</span>
              </h1>
              <div class="hero-subtag-3d">BUYER / SUPPLIER / FACTORY / INNOVATION</div>

              <div class="hero-cta-group-3d">
                <a href="#" class="hero-cta-explore-3d" onclick="showScreen('screen-marketplace'); return false;">
                  <span>Explore Now</span>
                  <span>→</span>
                </a>
                <button type="button" class="hero-cta-video-3d" onclick="showScreen('screen-home'); setTimeout(() => document.getElementById('fashion-design-showcase')?.scrollIntoView({behavior: 'smooth'}), 120); return false;">
                  <span class="play-3d-btn">▶</span>
                  <span>Watch Video</span>
                </button>
              </div>
            </div>

            <!-- Center Stage: Front-Facing AI/Human Head + Straight 0° Upright Side Icon Boxes -->
            <div class="hero-center-stage-3d">
              <!-- Left Stack: 3 Strictly Upright Front-Facing 3D Icon Boxes -->
              <div class="hero-icon-boxes-column">
                <!-- 1. Product Development -->
                <div class="hero-icon-box-3d" onclick="showScreen('screen-workspace')" title="Product Development">
                  <div class="icon-box-svg-wrap">
                    <svg viewBox="0 0 32 32" fill="none">
                      <!-- 3D T-shirt with collar, sleeve cuffs and dimensional shading -->
                      <path d="M10 5L13 8h6l3-3 7 4-3 6-3-2v14H9V13L6 15l-3-6 7-4z" fill="url(#nav-icon-grad-orange)" />
                      <path d="M13 8a3 3 0 006 0" stroke="#ffffff" stroke-width="1.2" fill="none" />
                      <path d="M10 5L13 8h6l3-3" stroke="rgba(255,255,255,0.6)" stroke-width="1" fill="none" />
                      <path d="M12 12v12m8-12v12" stroke="rgba(0,0,0,0.15)" stroke-width="0.8" />
                    </svg>
                  </div>
                  <span class="icon-box-label">Product<br>Development</span>
                </div>

                <!-- 2. Material Sourcing -->
                <div class="hero-icon-box-3d" onclick="showScreen('screen-marketplace')" title="Material Sourcing">
                  <div class="icon-box-svg-wrap">
                    <svg viewBox="0 0 32 32" fill="none">
                      <!-- 3D Rolled Fabric Spools with horizontal winding texture -->
                      <ellipse cx="16" cy="11" rx="9" ry="3.5" fill="url(#nav-icon-grad-orange-light)" />
                      <path d="M7 11v9c0 2 4 3.5 9 3.5s9-1.5 9-3.5v-9" fill="url(#nav-icon-grad-orange)" />
                      <ellipse cx="16" cy="20" rx="9" ry="3.5" fill="url(#nav-icon-grad-orange-dark)" opacity="0.6" />
                      <path d="M7 15c0 2 4 3.5 9 3.5s9-1.5 9-3.5" stroke="rgba(255,255,255,0.5)" stroke-width="0.8" fill="none" />
                    </svg>
                  </div>
                  <span class="icon-box-label">Material<br>Sourcing</span>
                </div>

                <!-- 3. Manufacturing -->
                <div class="hero-icon-box-3d" onclick="showScreen('screen-factory')" title="Manufacturing">
                  <div class="icon-box-svg-wrap">
                    <svg viewBox="0 0 32 32" fill="none">
                      <!-- 3D Industrial Factory with saw-tooth roof and chimneys -->
                      <path d="M4 25V13l7 4v-4l7 4v-4l7 4v12H4z" fill="url(#nav-icon-grad-orange)" />
                      <rect x="20" y="5" width="2.5" height="7" fill="url(#nav-icon-grad-orange-dark)" />
                      <rect x="24" y="3" width="2.5" height="9" fill="url(#nav-icon-grad-orange-dark)" />
                      <rect x="7" y="19" width="3" height="3" fill="#ffffff" fill-opacity="0.85" />
                      <rect x="13" y="19" width="3" height="3" fill="#ffffff" fill-opacity="0.85" />
                      <rect x="19" y="19" width="3" height="3" fill="#ffffff" fill-opacity="0.85" />
                    </svg>
                  </div>
                  <span class="icon-box-label">Manufacturing</span>
                </div>
              </div>

              <!-- Center: Perfectly Front-Facing Human / AI Head with Internal Glowing Brain & AI Badge -->
              <div class="hero-head-center-frame">
                <img src="assets/mockup/hero_head_feathered.png" alt="Leadirftex Front-Facing AI Head with Glowing Internal Brain" class="hero-head-img" />
              </div>

              <!-- Right Stack: 3 Strictly Upright Front-Facing 3D Icon Boxes -->
              <div class="hero-icon-boxes-column">
                <!-- 4. Quality Control -->
                <div class="hero-icon-box-3d" onclick="showScreen('screen-quality')" title="Quality Control">
                  <div class="icon-box-svg-wrap">
                    <svg viewBox="0 0 32 32" fill="none">
                      <!-- 3D Precision Magnifying Glass / QA Shield -->
                      <circle cx="14" cy="14" r="8" stroke="url(#nav-icon-grad-orange)" stroke-width="3" fill="rgba(255,255,255,0.2)" />
                      <line x1="20" y1="20" x2="28" y2="28" stroke="url(#nav-icon-grad-orange)" stroke-width="4" stroke-linecap="round" />
                      <path d="M11 14l2 2 4-4" stroke="#ff4e00" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
                    </svg>
                  </div>
                  <span class="icon-box-label">Quality<br>Control</span>
                </div>

                <!-- 5. Logistics & Shipping -->
                <div class="hero-icon-box-3d" onclick="showScreen('screen-workspace')" title="Logistics & Shipping">
                  <div class="icon-box-svg-wrap">
                    <svg viewBox="0 0 32 32" fill="none">
                      <!-- 3D Delivery Cargo Freight Truck -->
                      <rect x="3" y="9" width="16" height="12" rx="1.5" fill="url(#nav-icon-grad-orange)" />
                      <path d="M19 13h5l4 4v4h-9v-8z" fill="url(#nav-icon-grad-orange-light)" />
                      <circle cx="9" cy="22" r="3" fill="#334155" />
                      <circle cx="9" cy="22" r="1.5" fill="#ffffff" />
                      <circle cx="23" cy="22" r="3" fill="#334155" />
                      <circle cx="23" cy="22" r="1.5" fill="#ffffff" />
                    </svg>
                  </div>
                  <span class="icon-box-label">Logistics<br>&amp; Shipping</span>
                </div>

                <!-- 6. Data & Insights -->
                <div class="hero-icon-box-3d" onclick="showScreen('screen-ai-matching')" title="Data & Insights">
                  <div class="icon-box-svg-wrap">
                    <svg viewBox="0 0 32 32" fill="none">
                      <!-- 3D Ascending Bar Chart with Beveled Facets -->
                      <rect x="5" y="18" width="5" height="9" rx="1" fill="url(#nav-icon-grad-orange-dark)" />
                      <rect x="13" y="11" width="5" height="16" rx="1" fill="url(#nav-icon-grad-orange)" />
                      <rect x="21" y="4" width="5" height="23" rx="1" fill="url(#nav-icon-grad-orange-light)" />
                    </svg>
                  </div>
                  <span class="icon-box-label">Data &amp;<br>Insights</span>
                </div>
              </div>
            </div>

            <!-- Far Right Column: Human Intelligence Typography -->
            <div class="hero-right-typography">
              <div class="hero-intel-title-block">
                <span class="hero-intel-word">HUMAN</span>
                <span class="hero-intel-word">INTELLIGENCE</span>
                <span class="hero-intel-word">GLOBAL</span>
                <span class="hero-intel-word">POSSIBILITIES</span>
              </div>
              <div class="hero-intel-subblock">
                <span class="hero-intel-subline">PEOPLE</span>
                <span class="hero-intel-subline">PRODUCTS</span>
                <span class="hero-intel-subline">TECHNOLOGY</span>
                <span class="hero-intel-subline">A STRONGER TOMORROW</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Curved Glowing Orange/Crimson Horizon Transition Boundary -->
        <div class="hero-silver-boundary" aria-hidden="true"></div>
      </section>

      <!-- ====================================================================
           CORE AREAS SECTION (TRANSITION INTO BLACK / NEAR-BLACK + DEEP RED)
           ==================================================================== -->
      <section class="core-areas-section" id="core-areas-section">
        <div class="core-areas-container">
          <div class="core-areas-header-row">
            <div class="core-areas-title-block">
              <div class="sec-eyebrow-track">
                <span class="eyebrow-line"></span>
                <span class="eyebrow-label">OUR CORE AREAS</span>
              </div>
              <h2 class="core-areas-headline">
                <span class="text-3d-chrome-sm">BUILDING THE FUTURE OF</span>
                <span class="text-3d-orange-sm">APPAREL</span>
              </h2>
            </div>
            <button type="button" class="btn-view-all-solutions" onclick="showScreen('screen-marketplace')">
              <span>View All Solutions</span>
              <span>→</span>
            </button>
          </div>

          <div class="core-areas-cards-row">
            <!-- 1. Product Development -->
            <div class="core-area-card" onclick="showScreen('screen-workspace')" title="Explore Product Development">
              <div class="core-card-3d-stage">
                <div class="core-card-icon-wrap">
                  <svg viewBox="0 0 40 40" fill="none">
                    <path d="M12 7L16 11h8l4-4 8 5-4 7-4-2v16H12V24l-4 2-4-7 8-5z" fill="url(#nav-icon-grad-white)" />
                    <path d="M16 11a4 4 0 008 0" stroke="#ff4e00" stroke-width="1.8" fill="none" />
                  </svg>
                </div>
                <div class="core-card-shadow"></div>
              </div>
              <h3 class="core-card-title">Product Development</h3>
              <p class="core-card-desc">From concept to creation</p>
              <div class="core-card-action-btn">→</div>
            </div>

            <!-- 2. Material Sourcing -->
            <div class="core-area-card" onclick="showScreen('screen-marketplace')" title="Explore Material Sourcing">
              <div class="core-card-3d-stage">
                <div class="core-card-icon-wrap">
                  <svg viewBox="0 0 40 40" fill="none">
                    <ellipse cx="20" cy="14" rx="12" ry="5" fill="url(#nav-icon-grad-orange-light)" />
                    <path d="M8 14v12c0 2.8 5.4 5 12 5s12-2.2 12-5V14" fill="url(#nav-icon-grad-orange)" />
                    <ellipse cx="20" cy="26" rx="12" ry="5" fill="url(#nav-icon-grad-orange-dark)" opacity="0.6" />
                    <path d="M8 20c0 2.8 5.4 5 12 5s12-2.2 12-5" stroke="rgba(255,255,255,0.6)" stroke-width="1" fill="none" />
                  </svg>
                </div>
                <div class="core-card-shadow"></div>
              </div>
              <h3 class="core-card-title">Material Sourcing</h3>
              <p class="core-card-desc">Right materials. Better products</p>
              <div class="core-card-action-btn">→</div>
            </div>

            <!-- 3. Manufacturing -->
            <div class="core-area-card" onclick="showScreen('screen-factory')" title="Explore Manufacturing">
              <div class="core-card-3d-stage">
                <div class="core-card-icon-wrap">
                  <svg viewBox="0 0 40 40" fill="none">
                    <path d="M6 32V16l9 5v-5l9 5v-5l10 5v16H6z" fill="url(#nav-icon-grad-orange)" />
                    <rect x="26" y="6" width="3" height="9" fill="url(#nav-icon-grad-orange-dark)" />
                    <rect x="31" y="3" width="3" height="12" fill="url(#nav-icon-grad-orange-dark)" />
                    <rect x="10" y="24" width="4" height="4" fill="#ffffff" fill-opacity="0.85" />
                    <rect x="18" y="24" width="4" height="4" fill="#ffffff" fill-opacity="0.85" />
                    <rect x="26" y="24" width="4" height="4" fill="#ffffff" fill-opacity="0.85" />
                  </svg>
                </div>
                <div class="core-card-shadow"></div>
              </div>
              <h3 class="core-card-title">Manufacturing</h3>
              <p class="core-card-desc">Reliable production partners</p>
              <div class="core-card-action-btn">→</div>
            </div>

            <!-- 4. Quality Assurance -->
            <div class="core-area-card" onclick="showScreen('screen-quality')" title="Explore Quality Assurance">
              <div class="core-card-3d-stage">
                <div class="core-card-icon-wrap">
                  <svg viewBox="0 0 40 40" fill="none">
                    <path d="M20 4L6 10v10c0 9 6 15 14 17 8-2 14-8 14-17V10L20 4z" fill="url(#nav-icon-grad-orange)" />
                    <path d="M14 20l4 4 8-8" stroke="#ffffff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" />
                  </svg>
                </div>
                <div class="core-card-shadow"></div>
              </div>
              <h3 class="core-card-title">Quality Assurance</h3>
              <p class="core-card-desc">Standards you can trust</p>
              <div class="core-card-action-btn">→</div>
            </div>

            <!-- 5. Logistics & Shipping -->
            <div class="core-area-card" onclick="showScreen('screen-workspace')" title="Explore Logistics & Shipping">
              <div class="core-card-3d-stage">
                <div class="core-card-icon-wrap">
                  <svg viewBox="0 0 40 40" fill="none">
                    <rect x="4" y="10" width="22" height="16" rx="2" fill="url(#nav-icon-grad-orange)" />
                    <path d="M26 15h7l5 5v6h-12v-11z" fill="url(#nav-icon-grad-orange-light)" />
                    <circle cx="12" cy="28" r="4" fill="#334155" />
                    <circle cx="12" cy="28" r="2" fill="#ffffff" />
                    <circle cx="31" cy="28" r="4" fill="#334155" />
                    <circle cx="31" cy="28" r="2" fill="#ffffff" />
                  </svg>
                </div>
                <div class="core-card-shadow"></div>
              </div>
              <h3 class="core-card-title">Logistics &amp; Shipping</h3>
              <p class="core-card-desc">Global delivery support</p>
              <div class="core-card-action-btn">→</div>
            </div>

            <!-- 6. Market Insights -->
            <div class="core-area-card" onclick="showScreen('screen-ai-matching')" title="Explore Market Insights">
              <div class="core-card-3d-stage">
                <div class="core-card-icon-wrap">
                  <svg viewBox="0 0 40 40" fill="none">
                    <rect x="6" y="22" width="7" height="12" rx="1.5" fill="url(#nav-icon-grad-orange-dark)" />
                    <rect x="16" y="14" width="7" height="20" rx="1.5" fill="url(#nav-icon-grad-orange)" />
                    <rect x="26" y="5" width="7" height="29" rx="1.5" fill="url(#nav-icon-grad-orange-light)" />
                  </svg>
                </div>
                <div class="core-card-shadow"></div>
              </div>
              <h3 class="core-card-title">Market Insights</h3>
              <p class="core-card-desc">Data for smarter decisions</p>
              <div class="core-card-action-btn">→</div>
            </div>
          </div>
        </div>
      </section>"""

    # Replace the old <section class="hero-enterprise-section"...> block
    old_hero_pattern = r'<section class="hero-enterprise-section" id="hero-section">.*?</section>'
    content = re.sub(old_hero_pattern, refined_hero_and_core_areas_html, content, flags=re.DOTALL)

    with open("master-ui-mockup.html", "w", encoding="utf-8") as f:
        f.write(content)

    print("Successfully wrote refined markup to master-ui-mockup.html!")

if __name__ == "__main__":
    build_refined_html()
