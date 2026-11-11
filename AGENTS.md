# Rules for every AI assistant (Claude, ChatGPT, Codex): Pipewright Studio

`CLAUDE.md` imports this file, so Claude and ChatGPT follow the same rules. Edit rules here only.

This repo is **public**. It holds only what clients may see: the website, the sample audit and the brand kit.
Pricing, sales scripts, prospects and client work live in the **private** repo `abhinav-kurella/pipewright-internal`. Never add confidential material here.

## When Abhinav says he hit his limit on the other assistant

A short message such as "hit my limit on the other one, continue from here", "limit hit, pick up" or "continue from Claude" (or ChatGPT) means: take over now. Do not ask him for context or a longer prompt.

1. Read the status file on `main` in all four repos: `NOW.md` in abhinav-ai-ops-lab, pipewright-internal and pipewright-studio, and `Working-plan.md` (newest section) in nestarrival-uk. Also check open pull requests and the Google Drive folder "Assistant Handoff". Claude: attach any repo the session does not have yet.
2. The newest dated entry across them is the work in flight. Reply in 5 lines or fewer: what was done, what is in flight, what you must not repeat (for example scheduled sends), and the next step.
3. Start the next step straight away, unless it needs his approval.

## Switching between Claude and ChatGPT

Abhinav moves between Claude, ChatGPT and Codex when one hits a usage limit. None of them sees the others' chats. This repo is the only shared memory.

1. **Start:** read this file, then `NOW.md`. Check the Google Drive folder "Assistant Handoff" for unanswered messages to you. Continue from "Next step" without asking Abhinav to repeat context.
2. **While working:** commit and push after every meaningful step, not only at the end. A limit can end a session mid-task, and unpushed work is lost.
3. **Keep `NOW.md` current:** before a long step, write what you are about to do. When you stop, write what is done, the next step, files touched and open questions. Date each entry and name the assistant.
4. **Where work lands:** `main` is the live website (GitHub Pages). Work on a branch and open a pull request for Abhinav to merge. Write the branch name and pull request link in `NOW.md` so the other assistant can continue on the same branch.
5. **Decisions stay decided:** do not redo or re-ask anything recorded as decided. Read a file again just before editing it and keep the other assistant's changes.
6. **Approvals do not change when switching:** nothing is sent, published, booked or paid for without Abhinav's approval.


## What's here
- `index.html`: the whole website (single static file, offline-friendly, Pitch mode). Hosted with GitHub Pages from `main` / root.
- `samples/pipeline-leak-audit.html`: sample audit for a fictional company, with sourced benchmarks.
- `brand/logo/`: master logo files (outlined SVG + PNG, light/dark/brass, favicons) and build scripts.
- `brand/social/`: finished social posts, with prompts and editable sources.
- `NOW.md`: what is in progress right now and the next step. Public, so no confidential detail.
- `HANDOFF.md`: developer guide for Sireesha (structure, open items, brand typography, QA checklist).

## Brand rules
- Fonts: **Libre Baskerville** (logo, headings), **IBM Plex Sans** (body), **IBM Plex Mono** (labels).
- Colours: ink #111A1C, paper #EDF0EE, brass #A9761B (light bg) / #D9A748 (dark bg).
- Proof numbers are real (past roles, client names withheld). Never invent numbers.
- English only on brand assets. Founder name: Abhinav Kumar.

## Storage rules
- Keep images web-sized (under ~5 MB each). Large source files and videos go to Google Drive, not Git. GitHub blocks files over 100 MB.

## Working style
- Structured, practical answers with one clear recommendation; back claims with sourced data.
- Site keeps `noindex` until launch (see HANDOFF.md section 9 for the pre-launch QA).
