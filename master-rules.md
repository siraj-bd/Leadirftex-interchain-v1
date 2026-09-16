## MANDATORY WORKFLOW

1. Read `../master-rules.md` before touching code.

2. Follow strict execution flow: **AUDIT → FIX ROOT CAUSE ONLY → RE-AUDIT → FINAL VERIFY**.

3. After completing the task, update `..project-execution-status.md` with actual verified results only.

4. "Understand them before starting the task." project-status-for-chatgpt.html — completed work, findings, fixes, verification ও current readiness status update chatgpt ke jananor jonno)


Project Name : Leadirftex Interchain

Brand: Leadirftex
Full Platform Name: Leadirftex Interchain
Plan Domain will be : Leadirftex.com

-----------------------------------------------------------------

## CORE MASTER RULES

1. **Task Scope & Module Isolation:** Stay strictly within the assigned task boundary. Never modify, refactor, or delete unrelated files, routes, or modules without explicit instruction.

2. **Existing-First, Anti-Duplication & Canonical Naming:** Always search existing components, functions, routes, schemas, and other resources before creating new ones. The single canonical project naming standard is lowercase kebab-case (`lowercase-with-hyphens`) for all new files, folders, assets, components, routes, URLs, CSS classes, DOM IDs, data attributes, schema/API keys, and other project resources. Never use spaces, uppercase, `_`, camelCase, or PascalCase for these resource names.

**Programming Identifier Exception:** Where kebab-case is technically invalid in the programming language, use the deterministic language-standard form derived directly from the canonical kebab-case name: JavaScript functions/variables → camelCase; JavaScript classes → PascalCase; JavaScript constants → UPPER_SNAKE_CASE; Python modules/functions/variables → snake_case; Python classes → PascalCase. No arbitrary naming convention is permitted.

**Legacy Preservation:** Never rename existing non-compliant resources merely for cosmetic consistency. Preserve existing names and references unless an explicit migration/refactoring task is assigned. All NEW resources MUST follow this rule.

--------------------------------------------------------------------

## ENVIRONMENT, GIT & DEPLOYMENT RULES

1. DEVELOPMENT MUST BE LOCAL-FIRST
   - Development and initial testing MUST run primarily in the local environment.
   - External managed services MUST NOT be mandatory unless technically required.

2. ENVIRONMENT VARIABLES
   - All environment-specific configuration MUST use environment variables.
   - Maintain `.env` for local configuration and `.env.example` with variable names/placeholders only.

3. SECRET PROTECTION
   - `.env` and all secret-containing files MUST be excluded from Git.
   - Never commit passwords, tokens, API keys, private keys, or credentials.
   - Secrets MUST never be hardcoded in source code, frontend code, templates, or committed configuration.
   - Production secrets MUST use the hosting platform's secure Environment Variables/Secrets system.

4. GIT SOURCE REPOSITORY
   - Git MUST contain the complete reproducible application source code and required non-secret configuration.
   - Git MUST NOT contain databases, user data, private uploads, caches, build artifacts, or secrets.
   - Required database schemas and migrations MUST be version-controlled.

5. DATA & ENVIRONMENT SEPARATION
   - Local, testing/staging, and production environments MUST use separate configuration, credentials, and data.
   - Production data MUST NOT be used for ordinary development/testing unless explicitly sanitized and authorized.

6. REPOSITORY STRUCTURE
   - Use one primary application repository unless a documented technical requirement justifies separation.
   - Do NOT create separate repositories solely for deployment files or secrets.

7. TEST DEPLOYMENT
   - The project SHOULD support deployment from the Git repository to a suitable free or low-cost testing environment when technically possible.
   - Testing MUST use separate test credentials and test data.

8. PRODUCTION DEPLOYMENT
   - Production MUST be deployed from the controlled project source through the hosting platform's standard deployment process.
   - Production configuration, secrets, and production data MUST remain outside Git.

9. REPRODUCIBILITY
   - A clean Git checkout MUST be capable of being configured and deployed without undocumented files or hidden local settings.
   - Required dependencies, setup steps, and environment variables MUST be documented.

10. AUTHORITATIVE BRAND GREEN SPECIFICATION (USER MANDATE)
   - Whenever green text, green badges, green status dots, glow halos, verification checks, or green elements of ANY kind are used, they MUST strictly match the approved Cyber/Neon Electric Green:
     - **Primary Hex:** `#00FF22` (RGB: `0, 255, 34`)
     - **Text / Highlight:** `#00FF22` or `#00FF44`
     - **Glow & Shadow:** `rgba(0, 255, 34, 0.5)` / `0 0 8px #00FF22`
     - **Soft Badge Background:** `rgba(0, 255, 34, 0.12)` with border `rgba(0, 255, 34, 0.45)`
   - NEVER use dull emerald, muted teal, olive, or dark forest green. All green elements must pop with pure electric neon intensity.