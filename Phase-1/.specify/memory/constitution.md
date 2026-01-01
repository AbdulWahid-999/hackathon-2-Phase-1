<!-- SYNC IMPACT REPORT
Version change: N/A → 1.0.0
List of modified principles:
- PRINCIPLE_1: Simplicity and Clarity in UX
- PRINCIPLE_2: Clean and Maintainable Python Code
- PRINCIPLE_3: No Manual Coding (Claude Code Only)
- PRINCIPLE_4: Spec-Driven Development
- PRINCIPLE_5: In-Memory Storage Only
Added sections: Additional Constraints, Development Workflow
Removed sections: None
Templates requiring updates:
- .specify/templates/plan-template.md ⚠ pending
- .specify/templates/spec-template.md ⚠ pending
- .specify/templates/tasks-template.md ⚠ pending
- .specify/templates/commands/*.md ⚠ pending
Follow-up TODOs: None
-->
# Phase I – In-Memory Python Console Todo Application Constitution

## Core Principles

### Simplicity and Clarity in Console-based UX
Console-based user experience must be simple and clear; All user interactions should be intuitive and require minimal cognitive load; Clear command structure and feedback required - no complex nested menus or ambiguous prompts

### Clean, Readable, and Maintainable Python Code
Python code must follow clean code conventions; Code must be readable, well-structured, and maintainable; All functions should have clear purpose and minimal complexity - no overly long functions or deeply nested logic

### No Manual Coding (Claude Code Only)
All implementation must be done using Claude Code only; No manual coding by humans is allowed; All code changes must originate from AI-assisted development - no direct human code modifications

### All Features Must Originate from Approved Specifications
All features must originate from approved specifications; No feature implementation without explicit spec coverage; All functionality must be documented in specifications before implementation - no ad-hoc feature additions

### In-Memory Storage Only
Storage must be in-memory only; No file-based or database persistence allowed; All data structures must reside in memory - no external storage dependencies

## Additional Constraints

Language: Python 3.13+
Runtime: Console / CLI only
Storage: In-memory data structures only
Tools: UV Package Manager required for dependency management

## Development Workflow

All development must follow Spec-Driven Development approach
Success criteria: All 5 basic features implemented (Add, View, Update, Delete, Mark Complete)
Application must run successfully from the command line
All code must follow clean code conventions

## Governance

Constitution supersedes all other practices; All features must originate from approved specifications; All changes must be documented and reviewed; No feature implementation without explicit spec coverage; All code must follow clean code conventions; In-memory storage only - no external storage dependencies

All PRs/reviews must verify compliance with constitution; Complexity must be justified; Implementation must follow specifications; No manual coding allowed except through Claude Code

**Version**: 1.0.0 | **Ratified**: 2026-01-01 | **Last Amended**: 2026-01-01