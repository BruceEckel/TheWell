# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repository Is

This is not a software project. It is a workspace for planning, structuring, and writing a science fiction novel. There are no build, lint, or test commands.

## Premise

A group of psychologists researches human behavior using an advanced experimental machine that can simulate a reality within itself. The full premise lives in `planning/premise.md`. The author's original statement of intent (INIT.md) was absorbed into the planning files and removed; it remains in git history.

## Repository Structure

- `planning/premise.md`: the premise, thematic questions, and the open decision between structural approaches.
- `planning/world.md`: the two nested settings (research facility and simulation), the rules of the simulation, and open worldbuilding questions.
- `planning/characters.md`: the three levels of character (researcher, incarnations, parts) and what to develop for each.
- `planning/outline.md`: outline work, currently blocked on decisions listed there. Includes the planned development sequence.
- `planning/synopsis.md`: the working synopsis. Drafts are numbered; proposals not yet approved by the author are listed explicitly at the end of the draft.
- `planning/style.md`: voice and style rules for the manuscript, including the narrator's threshold exception, the three-act voice arc, and the motif ledger. Read before drafting any prose.
- `planning/genre.md`: genre positioning, comps, and one-line answers to "what is it?" (literary fiction with a speculative premise; visionary-metaphysical as secondary).
- `manuscript/`: chapter drafts, one file per chapter, named like `act1-ch01-the-funeral.md`. Chapter summaries live in `planning/outline.md`; read `planning/style.md` (voice rules, motif ledger) and the `world.md` glossary before drafting or editing any chapter.
- `docs/`: the GitHub Pages site (hand-built HTML/CSS/JS, no framework), served at https://bruceeckel.github.io/TheWell/. It is generated from `manuscript/` by `tools/gen-site.py`; after any manuscript edit, rerun `python tools/gen-site.py` and commit the regenerated pages. Do not hand-edit the chapter HTML; edit `docs/style.css`, `docs/well.js`, or the generator instead.

## Current State

The title is **The Well** (decided 2026-08-22). The novel is complete in first draft: thirty chapters and a coda in `manuscript/`, about 66,000 words, drafted 2026-08-22. The author has accepted this length as right for the book; do not pad toward the old style-note target. The planning files record every decision and are kept current with the text; `planning/style.md`'s motif ledger is the continuity authority. The title is undecided (candidates on the table: The Well, The Keeping, Oubliette). Next phase: the author's read-through, then revision. When editing any chapter, check the motif ledger and glossary first, and log any new or changed motif. Commit after each meaningful change.

## Working With the Author

- The author is Bruce Eckel.
- All prose and planning documents are in Markdown.
- Writing style: no em dashes; prefer shorter sentences; use commas or parentheses for asides; use a comma or semicolon for a pause.
- This is creative collaboration, not code generation. Prefer discussing ideas, options, and tradeoffs (plot, character, structure) before writing prose. Do not silently rewrite existing prose; propose changes and explain the reasoning.
