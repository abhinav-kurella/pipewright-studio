# Pipewright Studio: developer handoff

Everything a developer needs to pick up this project without reading the original chat.

---

## 1. Context

- **What it is:** the website for Pipewright Studio, Abhinav's marketing systems business for B2B teams.
- **Main use:** showing it in person at meetings (laptop, phone or iPad). It must work offline and look sharp on every screen. Being found online comes second, for now.
- **Positioning:** "We build the marketing systems that turn campaigns into pipeline." The studio is founder-led and senior. Avoid the word "agency".
- **Audience:** B2B SaaS; fintech, tax and accounting; professional and outsourcing services; global content and media teams.

## 2. Decisions already made

| Topic | Decision | Why |
|---|---|---|
| Name | **Pipewright Studio** | "Wright" means craftsman, so it reads as "pipeline builder". It describes the work rather than using a personal name. |
| Descriptor | "Studio" | Sounds like small, senior craft rather than a big agency. |
| Founder title | Founder & Principal | Credible for a small firm without sounding inflated. |
| Proof | Real numbers, client names withheld | The results come from Abhinav's previous roles, so they're labelled "founder track record". |
| Visual direction | Technical drawing: mineral grey paper, ink type, one brass accent | Fits "pipeline" and "wright". Credible without looking like a big corporation. |
| Tech | One static HTML file, no build step | Works offline in meetings, is free to host and simple to edit. |

## 3. Files

```
pipewright-studio/        (repo root)
├── index.html    # the whole site: HTML, CSS (in <style>) and JS (in <script>)
├── README.md     # how to view, present and deploy
└── HANDOFF.md    # this file
```

## 4. How the code is organised (`index.html`)

- **Design tokens** are at the top of `<style>` in `:root`: colours, fonts and a type scale. Dark mode overrides the same tokens in two blocks (OS preference and `data-theme`). Change colours only through the tokens.
- **Fonts:** Libre Baskerville (display: logo and headings), IBM Plex Sans (body), IBM Plex Mono (labels and data), loaded from Google Fonts with system fallbacks for offline use. See section 10.
- **Sections** each carry `data-slide`, in this order: Hero → Proof → Problem → Services → Work → Process → Engagements → Founder → Contact.
- **Hero diagram:** an inline SVG pipe drawn as two stacked strokes, with dots animated by `animateMotion`. Animation pauses for users who prefer reduced motion.
- **Pitch mode** (JS at the bottom of the file): adds `html.pitch`, shows one `[data-slide]` at a time, and supports arrow keys, Space, swipe, Esc and the fullscreen API.
- **Logo:** an SVG `<symbol id="mark">` (a pipe elbow with a brass dot), reused through `<use href="#mark">`. Master logo files (SVG/PNG, light/dark/brass, favicons) live in `brand/logo/`. Use those, never a retyped version.

## 5. Open items (priority order)

1. **Domain:** check and buy `pipewright.studio` or `pipewright.co`, then replace `hello@pipewright.studio` in the Contact section.
2. **Founder details:** ✅ name (Abhinav Kumar) and title (Founder & Principal) are set. Still open: an optional photo (it replaces the "AK" monogram) and a LinkedIn link.
3. **Booking:** ✅ the hero and contact buttons link to Calendly (https://calendly.com/abhinavkmr/discovery).
4. **Deploy:** turn on GitHub Pages (the repo must be public on a free plan), then add the custom domain.
5. **Before launch:** remove `<meta name="robots" content="noindex, nofollow">` from `index.html` so search engines can list the site.
6. **Polish:** a favicon from the logo mark, an Open Graph image for link previews, and basic analytics (Plausible or GA4).
7. **Later:** fuller case study pages, a short "Insights" section for posts, and a contact form (Formspree or Netlify Forms).

## 6. Run, edit, deploy

```bash
git clone https://github.com/abhinav-kurella/pipewright-studio.git
cd pipewright-studio
open index.html        # or: npx serve .
```

**Deploy (GitHub Pages):** repo Settings → Pages → Deploy from a branch → `main` / `(root)`. Netlify or Cloudflare Pages also work: drag the folder in.

## 7. Ground rules for changes

- Keep it a single static file until the content settles. Moving to a framework (Astro, Next.js) is the developer's call once there are multiple pages.
- Keep it working offline and with no horizontal scroll at 390px wide.
- Keep claims factual. Every number on the site comes from Abhinav's real track record, so don't add made-up stats or client logos.
- Copy style: short, plain sentences written from the client's point of view.

## 8. Workflow

- Internal sales material (pricing, scripts, playbooks, client work) lives in the private repo, not here.

- `main` is what goes live. Don't push experiments straight to it.
- Work on a branch, open a pull request, and Abhinav reviews it before merging.

## 9. Pre-launch QA (run before the first client or going public)

**Legal and employer**
- [ ] Employment contract reviewed: outside work, non-compete, non-solicit, confidentiality, IP assignment
- [ ] No content that identifies the current employer or uses its confidential results
- [ ] "Who we work with" excludes any market the contract restricts (e.g. tax & accounting)
- [ ] Case study figures cleared, or rewritten as percentages and outcomes
- [ ] Old repo history cleaned if it contains anything not meant to be public

**Content**
- [ ] Founder name, title, photo and LinkedIn are final
- [ ] Real email on the custom domain replaces the placeholder
- [ ] Calendly link opens the right event and availability is set

**Technical**
- [ ] Custom domain connected with HTTPS
- [ ] `<meta name="robots" content="noindex, nofollow">` removed
- [ ] Favicon, Open Graph image and analytics added
- [ ] Checked on phone, tablet and desktop in light and dark mode
- [ ] Pitch mode works (keyboard, swipe, Esc)
- [ ] Repo visibility set to public (needed for free GitHub Pages)

## 10. Brand typography (use everywhere)

| Role | Font | Weights | Use for |
|---|---|---|---|
| Display | **Libre Baskerville** | 700 (400 and italic for accents) | Logo, headlines, signage, posters, slide titles |
| Body | **IBM Plex Sans** | 400, 500 | Paragraphs, UI, proposals, reports |
| Utility | **IBM Plex Mono** | 400, 500 | Small uppercase labels, codes, data |

- Serif only for headings and the logo. Body text stays sans so it reads well on phones.
- Headings: letter-spacing -0.01em, line-height around 1.15.
- Accent colour on key words: brass (`--accent`).
- AI-generated scenes: describe signage as "3D brushed-brass serif letters in a classic Baskerville style".
