# Post Variant 2 — Problem / Pain Point (EN)

**Tone:** Direct, problem-first
**Channel:** Business groups (Pattaya Business Network, Digital Nomads)
**Rule:** No link in the first line — link at the end
**Status:** Ready to post (rewritten 01.08.2026, see notes below)

---

**A question for the group:**

How many hours a week do you spend on work a computer could do for you?

For a lot of businesses here it's the same picture:
→ Copying enquiries from Facebook, LINE and WhatsApp into a spreadsheet
→ Typing the same replies over and over
→ Using ChatGPT, but starting from zero every single time

I'm Franz — I work as an **AI guide here in Pattaya**. I help small businesses
automate exactly that, from "show me how to actually use ChatGPT" all the way to
"just build the thing for me."

**A real example:** for a pool company in Austria I built a complete business
system — enquiry, quote, PDF, invoice, maintenance contracts, all in one browser
tab. Quotes that used to take hours are now a two-minute click, and there are no
monthly software fees.

Next week I have **3 free 30-minute calls** open. No agency, no sales pressure —
we find the biggest time sink in your business, and I'll tell you honestly
whether AI is worth it for you or not.

Comment below, send me a DM, or find LINE, WhatsApp and my calendar here:
https://ki-lotse.tech/?lang=en

Cheers from Pattaya ☀️

---

## What changed on 01.08.2026 — and why

**1. Link now goes to ki-lotse.tech, not to the Linktree.** Facebook pulls the
preview card from the linked target; the Linktree only ever shows its own generic
card. Same reasoning as Variante 1 (changed 29.07.). Nothing is lost — LINE (with
QR), WhatsApp, e-mail, the contact form and Calendly are all on the front page.

**2. The property example was replaced by the Strodos case.** The old version
claimed "property inquiries — from ~8h down to ~2h per week". That number comes
from `werbung/demo-case-study-immobilien.md`, which says in its own first line:
demo data, no real customer. In a business group, where the goal is paying
clients, that is precisely the figure someone will ask about. The pool company in
Austria is real, live, and running — and `werbung/case-study-strodos.md` itself
sanctions the anonymised form ("Pool-Unternehmer in Österreich reicht"). The
customer name stays out; the customer's data never gets shown, only the demo
(demo.ki-lotse.tech) or the printed prospectus.

**3. "This week" → "Next week".** The post goes out on a Saturday; an offer for
"this week" expires the same evening.

---

## Before posting — group rules quick check (kanaele.md)

- [ ] Self-promo allowed in this group? On which day? (Many groups: Saturdays only)
- [ ] Links allowed in the post, or DM/comments only?
- [ ] Account old enough / member long enough?
- [ ] Posted as **Franz · KI-Lotse** (private person, not a company)
- [ ] Value in the post, not just a link

**After posting:** add the row to the tracker in `kanaele.md` (date, group,
variant) — otherwise the two-week evaluation has nothing to measure.

---

## The landing page — fixed, and what is still open

**Fixed and live (01.08.2026, commit `fdc1033`):** `https://ki-lotse.tech/?lang=en`
now opens the page in English. Before this, the toggle read `localStorage` only
with a German default, so an English reader landed on German text and had to find
the EN pill first. Verified live: English headline and English CTAs. The same
parameter works on the package pages —
`https://ki-lotse.tech/paket/poolservice-garten?lang=en` — which matters for the
direct outreach (#453). Without the parameter nothing changed: German stays the
default.

**Also fixed and live (01.08.2026, commit `221da61`, Todo #456): the preview card
is English.** `app.py` rewrites the meta tags when `?lang=en` is requested —
Facebook's scraper runs no JavaScript, so the language toggle alone was never
enough for the card. `shots/og-bild-en.png` carries the English wording ("I will
show you the way." / "explained in plain English"). Confirmed in the Sharing
Debugger: English card, own canonical URL, image loads. The German card is
untouched.

**Why the first attempt was pulled (01.08.):** the post was already submitted to
Pattaya Expats when the German card appeared under it — including the line
"verständlich erklärt, auf Deutsch". A later fix could not have saved that post:
Facebook builds the card while the post is being written and stores it with the
post. It was withdrawn before an admin approved it, so nothing was ever visible
in the group. Nothing about the text needs changing — it can go out as is.

**Note on this group: posts are reviewed by an admin before they appear.** Having
clicked "Post" is not the same as being published.

---

**Tip:** Reply to every comment — it builds trust and reach.

**Rotation:** same variant in the same group no more often than every 2–3 weeks.
