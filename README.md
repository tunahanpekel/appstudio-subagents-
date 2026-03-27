<<<<<<< HEAD
# App Studio Sub-Agents

## AI-Powered Mobile App Development Team in Your Terminal

An intelligent team of specialized AI agents that work together to take your app from idea to App Store — with market research, design, development, ASO, and monetization all covered.

---

## The Team (11 Agents)

| Layer | Agent | Role |
|-------|-------|------|
| **Management** | Master Orchestrator | System coordinator, project initialization |
| **Management** | Producer Agent | Roadmap, team coordination, scope control |
| **Intelligence** | Market Analyst | App Store research, competitor analysis, Go/No-Go |
| **Intelligence** | Data Scientist | Analytics, A/B testing, retention, LTV |
| **Design** | Sr Product Designer | UX strategy, PRD, user research |
| **Design** | Mid Product Designer | Screen specs, interactions, developer handoff |
| **Engineering** | Frontend Developer | Mobile UI (Flutter/React Native/Swift/Kotlin) |
| **Engineering** | Backend Developer | API, database, auth, infrastructure |
| **Growth** | ASO Specialist | App Store Optimization, keywords, store listing |
| **Growth** | Monetization Specialist | Paywall design, pricing, LTV optimization |
| **Quality** | QA Agent | Testing, bug reports, pre-release checklist |

---

## Quick Start (5 minutes)

### Prerequisites
- Python 3.8+
- Claude Code CLI

### Setup
```bash
# 1. Clone or navigate to the repo
cd appstudio-subagents

# 2. Create your first app project
python scripts/init_project.py

# 3. Start with Market Analysis
claude "Read agents/master_orchestrator.md and agents/market_analyst.md.
Analyze the market for my app: [your app concept]"

# 4. Get Go/No-Go, then activate full team
claude "Read agents/producer_agent.md and project-config.json.
Begin coordinating the development team."
```

---

## Development Modes

### 1. Design Only
Validate your idea before writing a single line of code.
- Market analysis + Go/No-Go decision
- Product Requirements Document (PRD)
- User flows and wireframes
- Monetization strategy
- ASO keyword research

```bash
# Select "Design Only" mode in init_project.py
python scripts/init_project.py
```

### 2. MVP Mode
Ship a focused v1 fast.
- Core features only (strict scope)
- Frontend + Backend built
- Analytics instrumented
- Store submission ready

### 3. Full Development
Complete product with all agents active.
- Full design system
- Complete feature set
- Performance optimized
- Post-launch monitoring

---

## Workflow

```
Your Idea
    ↓
Market Analyst → Competitor Research → Go/No-Go
    ↓ (if GO)
Producer Agent → Project Plan → Team Coordination
    ↓
Sr Product Designer → PRD → User Flows
    ↓
Mid Product Designer → Screen Specs → Developer Handoff
    ↓
Frontend Dev + Backend Dev → Building (parallel)
    ↓
QA Agent → Testing → Bug Reports
    ↓
ASO Specialist → Store Listing → Keyword Optimization
Monetization Specialist → Paywall Design → Pricing
    ↓
Data Scientist → Analytics Setup → Post-Launch Monitoring
    ↓
LAUNCH
```

---

## Platform Support

| Platform | Stack | Config |
|----------|-------|--------|
| iOS + Android | Flutter | `platform_configs/flutter_config.json` |
| iOS + Android | React Native | `platform_configs/react_native_config.json` |
| iOS | Swift | Native |
| Android | Kotlin | Native |

---

## Project Structure (after init)

```
projects/your-app-name/
├── project-config.json          ← Project settings & active agents
├── documentation/
│   ├── prd/prd.md               ← Product Requirements Document
│   ├── design/                  ← Wireframes, screens, design system
│   ├── technical/               ← Architecture, API docs, DB schema
│   └── production/              ← Timeline, milestones
├── source/
│   ├── frontend/                ← Mobile app code
│   └── backend/                 ← Server code
├── resources/
│   ├── market-research/         ← Market Analyst reports
│   ├── competitor-analysis/     ← Competitor breakdowns
│   └── aso/                     ← ASO briefs and keyword lists
├── assets/
│   ├── screenshots/             ← Store screenshots
│   └── marketing/               ← Marketing assets
└── qa/                          ← Test plans, bug reports
```

---

## Example Agent Commands

```bash
# Market Research
claude "Read agents/market_analyst.md. Analyze the productivity app market
and identify the top 3 keyword opportunities for a focus timer app."

# Product Design
claude "Read agents/sr_product_designer.md and projects/my-app/documentation/prd/prd.md.
Create the core user flows for the onboarding experience."

# ASO
claude "Read agents/aso_specialist.md. Write the App Store listing for my app
based on the market research in resources/market-research/"

# Monetization
claude "Read agents/monetization_specialist.md. Design the paywall for a
meditation app targeting busy professionals. Budget: $9.99/month."

# Full Team Kickoff
claude "Read agents/master_orchestrator.md and projects/my-app/project-config.json.
Initialize the team and begin the market analysis phase."
```

---

## Key Differences from Game Studio Sub-Agents

| Aspect | Game Studio | App Studio |
|--------|-------------|------------|
| Focus | Games (Godot/Unity/Unreal) | Mobile apps (Flutter/RN/Native) |
| Market Research | Gaming market | App Store / Google Play |
| Unique Agents | Game Designer, Artist, QA | ASO Specialist, Monetization |
| Metrics | MAU, session length, FTUE | D1/D7/D30 retention, LTV, MRR |
| Launch | PC/Console stores | App Store + Google Play |

---

## License
MIT — by Tuna Pamir
=======
# appstudio-subagents-
An intelligent team of specialized AI agents that work together to take your app from idea to App Store — with market research, design, development, ASO, and monetization all covered.
>>>>>>> 9ceeba4c265d41ddd319cf57134c8384fee8bba1
