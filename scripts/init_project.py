#!/usr/bin/env python3
"""
App Studio Project Initializer
Creates project structure and configures agents for mobile app development

Author: Tuna Pamir
Project: App Studio Sub-Agents
License: MIT
"""

import os
import json
import sys
from datetime import datetime, timedelta
from pathlib import Path


class AppProjectInitializer:
    def __init__(self):
        self.base_path = Path("projects")
        self.project_config = {}

    def create_project_structure(self, project_name, platform="Both"):
        project_path = self.base_path / project_name.lower().replace(" ", "-")
        self.base_path.mkdir(exist_ok=True)

        directories = [
            # Documentation
            "documentation/prd",
            "documentation/design/wireframes",
            "documentation/design/screens",
            "documentation/design/design-system",
            "documentation/technical/architecture",
            "documentation/technical/api-docs",
            "documentation/technical/database-schema",
            "documentation/production/milestones",
            "documentation/production/retrospectives",
            # Source code
            "source/frontend",
            "source/backend",
            "source/shared",
            # Resources
            "resources/market-research",
            "resources/competitor-analysis",
            "resources/user-research",
            "resources/aso",
            # Assets
            "assets/icons",
            "assets/screenshots",
            "assets/marketing",
            # QA
            "qa/test-plans",
            "qa/bug-reports",
            "qa/device-testing",
            # Builds
            "builds/alpha",
            "builds/beta",
            "builds/release",
        ]

        for directory in directories:
            (project_path / directory).mkdir(parents=True, exist_ok=True)

        return project_path

    def configure_agents(self, mode):
        agents = ["master_orchestrator", "producer_agent", "market_analyst", "data_scientist"]

        if mode == "design":
            agents.extend(["sr_product_designer", "mid_product_designer", "monetization_specialist", "aso_specialist"])
        elif mode == "mvp":
            agents.extend(["sr_product_designer", "frontend_developer", "backend_developer", "qa_agent", "monetization_specialist"])
        elif mode == "full":
            agents.extend([
                "sr_product_designer", "mid_product_designer",
                "frontend_developer", "backend_developer",
                "qa_agent", "aso_specialist", "monetization_specialist"
            ])
        return agents

    def calculate_milestones(self, timeline, mode):
        milestones = []
        today = datetime.now()

        if timeline == "Rapid":
            milestones = [
                {
                    "name": "Market Validation",
                    "target_date": (today + timedelta(days=1)).strftime("%Y-%m-%d"),
                    "deliverables": ["Go/No-Go decision", "Competitor analysis", "Keyword list"],
                    "success_criteria": ["Clear market opportunity identified"]
                },
                {
                    "name": "Design Complete",
                    "target_date": (today + timedelta(days=3)).strftime("%Y-%m-%d"),
                    "deliverables": ["PRD", "Core user flows", "Key screens"],
                    "success_criteria": ["PRD approved", "Core loop defined"]
                }
            ]
        elif timeline == "Short":
            milestones = [
                {
                    "name": "Market Validation",
                    "target_date": (today + timedelta(days=3)).strftime("%Y-%m-%d"),
                    "deliverables": ["Market analysis report", "Go/No-Go decision"],
                    "success_criteria": ["Market opportunity confirmed"]
                },
                {
                    "name": "Design Complete",
                    "target_date": (today + timedelta(weeks=1)).strftime("%Y-%m-%d"),
                    "deliverables": ["PRD", "Wireframes", "Design system"],
                    "success_criteria": ["All screens wireframed", "PRD approved"]
                },
                {
                    "name": "MVP Build",
                    "target_date": (today + timedelta(weeks=3)).strftime("%Y-%m-%d"),
                    "deliverables": ["Core features built", "Backend API", "Basic analytics"],
                    "success_criteria": ["Core loop functional", "Internal QA passed"]
                },
                {
                    "name": "Launch",
                    "target_date": (today + timedelta(weeks=4)).strftime("%Y-%m-%d"),
                    "deliverables": ["Store submission", "Store listing ready"],
                    "success_criteria": ["App Store approved", "Live on both stores"]
                }
            ]
        elif timeline == "Medium":
            milestones = [
                {
                    "name": "Market Validation",
                    "target_date": (today + timedelta(weeks=1)).strftime("%Y-%m-%d"),
                    "deliverables": ["Full market analysis", "User persona research", "Monetization model"],
                    "success_criteria": ["Go decision made", "Revenue model chosen"]
                },
                {
                    "name": "Design Complete",
                    "target_date": (today + timedelta(weeks=3)).strftime("%Y-%m-%d"),
                    "deliverables": ["Full PRD", "All wireframes", "High-fidelity designs", "Design system"],
                    "success_criteria": ["Design approved", "Developer handoff ready"]
                },
                {
                    "name": "Alpha",
                    "target_date": (today + timedelta(weeks=6)).strftime("%Y-%m-%d"),
                    "deliverables": ["All features built", "Backend complete", "Analytics instrumented"],
                    "success_criteria": ["Feature complete", "Crash-free for 1 week"]
                },
                {
                    "name": "Beta",
                    "target_date": (today + timedelta(weeks=8)).strftime("%Y-%m-%d"),
                    "deliverables": ["Performance optimized", "Store listing ready", "Beta users onboarded"],
                    "success_criteria": ["Performance targets met", "Beta feedback integrated"]
                },
                {
                    "name": "Launch",
                    "target_date": (today + timedelta(weeks=10)).strftime("%Y-%m-%d"),
                    "deliverables": ["App Store live", "Marketing ready", "Support docs"],
                    "success_criteria": ["Live on stores", "Monitoring active"]
                }
            ]

        return milestones

    def create_initial_files(self, project_path, config):
        # Project config
        config_file = project_path / "project-config.json"
        with open(config_file, 'w') as f:
            json.dump(config, f, indent=2)

        # PRD template
        prd_file = project_path / "documentation/prd/prd.md"
        prd_content = f"""# {config['project']['name']} - Product Requirements Document

## Status: Draft
## Last Updated: {datetime.now().strftime('%Y-%m-%d')}

## Problem Statement
[To be filled by Sr Product Designer]

## App Concept
**{config['project']['concept']}**

## Target Users
**Platform**: {config['project']['platform']}
**Audience**: {config['project']['audience']}
**Category**: {config['project']['category']}

## Monetization Model
{config['project']['monetization']}

## Features (MoSCoW)
### Must Have
- [ ] [Feature 1]
- [ ] [Feature 2]

### Should Have
- [ ] [Feature 3]

### Could Have
- [ ] [Feature 4]

### Won't Have (v1)
- [ ] [Feature 5]

## Success Metrics
- D1 Retention: > [X]%
- D7 Retention: > [X]%
- Trial Conversion: > [X]%
- App Store Rating: > 4.5

## Competitors
{config['project'].get('competitors', 'To be researched')}

## Unique Value Proposition
{config['project'].get('usp', 'To be defined')}
"""
        with open(prd_file, 'w') as f:
            f.write(prd_content)

        # Market research template
        market_file = project_path / "resources/market-research/market_overview.md"
        market_content = f"""# Market Overview: {config['project']['category']} Apps

## App: {config['project']['name']}
## Analysis Date: {datetime.now().strftime('%Y-%m-%d')}

## Market Opportunity
- Market Size: [To be researched]
- Growth Rate: [To be researched]
- Top Apps: [To be researched]

## Competitor Analysis
### Competitor 1
- Name: [App Name]
- Downloads: [Estimate]
- Rating: [X.X stars]
- Strengths: [List]
- Weaknesses: [List] <- Our opportunity

### Competitor 2
- Name: [App Name]
- Downloads: [Estimate]
- Rating: [X.X stars]
- Strengths: [List]
- Weaknesses: [List] <- Our opportunity

## Keyword Opportunities
### High Volume / Low Competition
- [keyword 1]
- [keyword 2]

### Niche / High Intent
- [keyword 3]
- [keyword 4]

## User Pain Points (from competitor reviews)
- "[Pain point from 1-star reviews]"
- "[Pain point from 1-star reviews]"
- "[Pain point from 1-star reviews]"

## Go/No-Go Recommendation
Status: [Pending Market Analyst review]
"""
        with open(market_file, 'w') as f:
            f.write(market_content)

        # Timeline
        timeline_file = project_path / "documentation/production/timeline.md"
        timeline_content = f"""# {config['project']['name']} - Production Timeline

## Timeline: {config['project']['timeline']}
## Mode: {config['project']['mode'].upper()}

## Milestones
"""
        for milestone in config['milestones']:
            timeline_content += f"\n### {milestone['name']} - {milestone['target_date']}\n**Deliverables**:\n"
            for d in milestone['deliverables']:
                timeline_content += f"- {d}\n"
            timeline_content += "\n**Success Criteria**:\n"
            for s in milestone['success_criteria']:
                timeline_content += f"- {s}\n"

        with open(timeline_file, 'w') as f:
            f.write(timeline_content)

        # .gitignore
        gitignore_file = project_path / ".gitignore"
        with open(gitignore_file, 'w') as f:
            f.write("""# Dependencies
node_modules/
.dart_tool/
.pub-cache/

# Build outputs
build/
*.apk
*.ipa
*.aab

# Environment
.env
.env.local
*.env

# IDE
.vscode/
.idea/
*.xcworkspace/xcuserdata/

# OS
.DS_Store
Thumbs.db

# Secrets
*_service_account.json
google-services.json
GoogleService-Info.plist
""")

    def initialize_project(self):
        print("\n" + "="*60)
        print("APP STUDIO PROJECT INITIALIZER")
        print("="*60 + "\n")

        details = {}

        details['name'] = input("1. APP NAME: ").strip()
        details['concept'] = input("2. APP CONCEPT (one sentence): ").strip()

        print("\n3. TARGET PLATFORM:")
        print("   1) iOS only")
        print("   2) Android only")
        print("   3) Both (Cross-platform)")
        p = input("   Select (1-3): ").strip()
        details['platform'] = ["iOS", "Android", "Both"][int(p)-1] if p.isdigit() else "Both"

        print("\n4. TARGET AUDIENCE:")
        details['audience'] = input("   Describe your target user (age, interests, pain point): ").strip()

        print("\n5. APP CATEGORY:")
        cats = ["Productivity","Social","Health & Fitness","Finance","Entertainment",
                "E-commerce","Education","Travel","Food & Drink","Utilities","Other"]
        for i, c in enumerate(cats, 1):
            print(f"   {i}) {c}")
        c = input("   Select (1-11): ").strip()
        details['category'] = cats[int(c)-1] if c.isdigit() and int(c) <= len(cats) else "Other"

        print("\n6. MONETIZATION MODEL:")
        print("   1) Free (ads or data)")
        print("   2) Freemium (free + premium features)")
        print("   3) Subscription")
        print("   4) One-time purchase")
        print("   5) Enterprise / B2B")
        m = input("   Select (1-5): ").strip()
        mons = ["Free","Freemium","Subscription","One-time Purchase","Enterprise"]
        details['monetization'] = mons[int(m)-1] if m.isdigit() else "Freemium"

        print("\n7. DEVELOPMENT MODE:")
        print("   1) Design Only (PRD, UX, strategy)")
        print("   2) MVP (core features only)")
        print("   3) Full Development")
        md = input("   Select (1-3): ").strip()
        modes = ["design", "mvp", "full"]
        details['mode'] = modes[int(md)-1] if md.isdigit() else "mvp"

        print("\n8. TIMELINE:")
        print("   1) Rapid (< 1 week)")
        print("   2) Short (1-4 weeks)")
        print("   3) Medium (1-3 months)")
        print("   4) Long (3+ months)")
        t = input("   Select (1-4): ").strip()
        timelines = ["Rapid", "Short", "Medium", "Long"]
        details['timeline'] = timelines[int(t)-1] if t.isdigit() else "Short"

        print("\n9. TECH STACK:")
        print("   1) Flutter (cross-platform, recommended)")
        print("   2) React Native")
        print("   3) Swift (iOS native)")
        print("   4) Kotlin (Android native)")
        print("   5) No preference")
        ts = input("   Select (1-5): ").strip()
        stacks = ["Flutter", "React Native", "Swift", "Kotlin", "TBD"]
        details['tech_stack'] = stacks[int(ts)-1] if ts.isdigit() else "Flutter"

        print("\n10. COMPETITOR APPS:")
        details['competitors'] = input("    Name 1-3 similar apps: ").strip()

        print("\n11. UNIQUE SELLING POINT:")
        details['usp'] = input("    What makes your app different? (one sentence): ").strip()

        print(f"\nCreating project structure for '{details['name']}'...")
        project_path = self.create_project_structure(details['name'], details['platform'])

        active_agents = self.configure_agents(details['mode'])
        milestones = self.calculate_milestones(details['timeline'], details['mode'])

        config = {
            "project": {
                "name": details['name'],
                "concept": details['concept'],
                "platform": details['platform'],
                "category": details['category'],
                "audience": details['audience'],
                "monetization": details['monetization'],
                "mode": details['mode'],
                "timeline": details['timeline'],
                "tech_stack": details['tech_stack'],
                "competitors": details.get('competitors', ''),
                "usp": details.get('usp', ''),
                "version": "1.0.0",
                "created": datetime.now().isoformat(),
                "phase": "Market Analysis",
                "status": "active"
            },
            "team": {
                "active_agents": active_agents,
                "lead_agent": "producer_agent",
                "orchestrator": "master_orchestrator"
            },
            "milestones": milestones,
            "metrics": {
                "d1_retention_target": "40%",
                "d7_retention_target": "20%",
                "d30_retention_target": "10%",
                "trial_conversion_target": "5%",
                "crash_rate_target": "< 0.1%"
            }
        }

        print("Creating initial documentation...")
        self.create_initial_files(project_path, config)

        print("\n" + "="*60)
        print("PROJECT INITIALIZED SUCCESSFULLY!")
        print("="*60)
        print(f"\nApp: {details['name']}")
        print(f"Location: {project_path.absolute()}")
        print(f"Platform: {details['platform']} | Stack: {details['tech_stack']}")
        print(f"Mode: {details['mode'].upper()} | Timeline: {details['timeline']}")
        print(f"Monetization: {details['monetization']}")
        print(f"Active Agents: {len(active_agents)}")
        print(f"  - {', '.join(active_agents)}")
        print(f"\nMilestones: {len(milestones)}")
        for ms in milestones:
            print(f"  - {ms['name']}: {ms['target_date']}")

        print("\n" + "-"*60)
        print("NEXT STEPS:")
        print("-"*60)
        print("1. Start with Market Analysis:")
        print("   claude 'Read agents/market_analyst.md and analyze the market for this app concept'")
        print("2. Get Go/No-Go decision, then activate Producer:")
        print("   claude 'Read agents/producer_agent.md and project-config.json. Set up the development plan.'")
        print("3. Begin product design:")
        print("   claude 'Read agents/sr_product_designer.md and create the PRD for this app'")

        return project_path, config


if __name__ == "__main__":
    initializer = AppProjectInitializer()
    initializer.initialize_project()
