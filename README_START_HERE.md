# SmartGen Docs — 3 new themes + the live "Switch Style" button

This package has everything for the 3 themes you picked (Agency, Medicine, Utility/API) **and** the live style-switcher button you asked for, so any visitor can click a button and see the whole site redesign itself in the browser — no reload of a different page needed, it's a real button on the live site.

Every file in this folder is a **complete file** — copy it into your GitHub repo at the exact same path shown below, overwriting anything already there at that path. Nothing here needs you to merge or edit code by hand.

---

## Part 1 — Where every file goes

Copy each file from this package into your `smartGenDocs` repo at this exact path (create folders that don't exist yet):

**Brand new theme files (Agency / Service Portal):**
- `smartgen_docs/themes/agency/page.html`
- `smartgen_docs/themes/agency/base.html`
- `smartgen_docs/themes/agency/static/css/agency.css`

**Brand new theme files (Medicine Docs):**
- `smartgen_docs/themes/medicine/page.html`
- `smartgen_docs/themes/medicine/base.html`
- `smartgen_docs/themes/medicine/static/css/medicine.css`

**Brand new theme files (Utility / API Playground):**
- `smartgen_docs/themes/apiplay/page.html`
- `smartgen_docs/themes/apiplay/base.html`
- `smartgen_docs/themes/apiplay/static/css/apiplay.css`

**Brand new files for the live style switcher (used by every theme):**
- `smartgen_docs/themes/_shared/partials/style_switcher.html`
- `smartgen_docs/themes/_shared/partials/style_switcher_script.html`

**Updated files — these already exist in your repo; replace their full contents with the versions in this package** (each one just got the 2 lines added that turn the switcher button on):
- `smartgen_docs/themes/book/base.html`
- `smartgen_docs/themes/education/base.html`
- `smartgen_docs/themes/techblog/base.html`
- `smartgen_docs/themes/default/base_premium.html`
- `.github/workflows/main.yml`

That's it — 16 files total, all in this package, all at the paths above.

---

## Part 2 — How to turn on one of the 3 new themes (like before)

You still pick **one** "main" theme the normal way — this hasn't changed:

1. Open `smartgen.yml` in your repo.
2. Find the `theme:` section near the top and change the `name:` line:
   - `name: agency` → Agency / Service Portal
   - `name: medicine` → Medicine Docs
   - `name: apiplay` → Utility / API Playground
   - (or keep whatever you already have — `book`, `education`, `techblog`, or `premium`)
3. Save, commit, push. GitHub Actions rebuilds and deploys automatically, same as always.

Whatever you put here is what visitors land on first when they open your site.

---

## Part 3 — The live "Switch Style" button (new)

Once all 16 files above are in your repo, every page of your site gets a small round **"Styles"** button that floats in the bottom-left corner, on every theme, on every page, on desktop and mobile.

Click it and a menu pops up listing all 7 looks:
- Premium (Original)
- Book / Writer Docs
- Education / Course
- Tech Blog / Magazine
- Agency / Service Portal
- Medicine Docs
- Utility / API Playground

Click any one and the browser jumps straight to **that same page**, redrawn in that style — instantly, live, no searching for the right link. Click it again to jump to another, or back to where you started. The site remembers nothing — it's just a fast way to preview every look, on the fly, for any visitor.

### Why you don't need to do anything extra for this to work

I updated `.github/workflows/main.yml` (included in this package) so that every time your site deploys, it doesn't just build the *one* theme in `smartgen.yml` — it **also** quietly builds all the other themes into a hidden `styles/` folder alongside your normal site (for example `yoursite.com/styles/medicine/...`). The button on every page simply links between those. You never see or touch that folder — it's just how the button finds the other looks. Your main site at the normal address is completely unaffected and still shows whichever theme you set in `smartgen.yml`.

Nothing about your `smartgen.yml` file itself needs to change for the button to work — the workflow figures out your current theme automatically and builds the other 6 around it.

---

## Part 4 — What I actually tested before sending this

I don't just write the code and hand it over — everything below was built and clicked through for real before I packaged it:

- Built all 7 themes (Premium, Book, Education, Tech Blog, Agency, Medicine, Utility/API) from a real copy of your site, using your real navigation menu and pages — all 7 builds completed with zero errors.
- Ran a real browser (Playwright) against the built site and:
  - Opened an inner page, clicked the Styles button, and confirmed all 7 options show up.
  - Switched from the home style to Agency — confirmed it landed on the *exact same page* in the Agency look, not the Agency homepage.
  - From Agency, switched to Medicine — same page, correct look, confirmed by URL and by the page's own CSS class.
  - Switched back to the original theme — landed back on the exact same page again.
  - Repeated the whole flow on a phone-sized screen (390px wide) starting from a different page — button and menu both worked identically.
  - Checked the browser console for errors on every step — none.
- Along the way I actually caught and fixed two real bugs before they ever reached you:
  1. The button was rendering in the wrong position (top of the page instead of floating bottom-left) on themes whose header uses a frosted-glass blur effect — a known CSS quirk where blur effects on a parent element can hijack "floating" positioning for anything inside it. Fixed by moving the button's markup outside the header in every theme.
  2. On some themes the style menu was tall enough to clip its last couple of options off-screen. Fixed by giving the menu more room to expand before it needs to scroll.
- Took real screenshots of the Agency theme (scrolled to the bottom, where its own "Back to top" button also lives) and the Medicine theme on a phone screen, to make sure the new Styles button never overlaps anything already on the page. It doesn't, in either case.

Everything in this package is what came out the other side of that testing — not a first draft.
