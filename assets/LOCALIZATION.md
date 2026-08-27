# Industry Guide — Localization

Industry Guides ship per market. The layout never changes; three things do:

1. **Body copy** — title, intro, pains, outcomes, value bullets, quote.
2. **Tool link text** — the product names in every "Bitrix24 Tools" list.
3. **Tool link URL** — the `href` on each of those names.
4. **UI labels** — "Business pain" / "Bitrix24 Tools" / "Practical Outcome" / "Quick Guide".

Everything else (colors, logo, components, page geometry) stays identical.

---

## 1. The URL rule — swap the domain, keep the path

Bitrix24 mirrors the same URL path across its localized domains. So a link only
needs its **domain suffix** changed; the path after the domain stays the same.

| Market | Language | Domain root |
|---|---|---|
| International (default) | English | `https://www.bitrix24.com` |
| Spain / LatAm | Spanish | `https://www.bitrix24.es` |
| Poland | Polish | `https://www.bitrix24.pl` |
| Europe | English (EU) | `https://www.bitrix24.eu` |
| Germany | German | `https://www.bitrix24.de` |
| Brazil | Portuguese | `https://www.bitrix24.com.br` |

Example — the CRM tool page:

```
EN  https://www.bitrix24.com/tools/crm/
ES  https://www.bitrix24.es/tools/crm/
PL  https://www.bitrix24.pl/tools/crm/
```

> **Rule:** to localize a link, replace only the part before the first `/tools/…`
> (or `/solutions/…`) with the market's domain root. The path is unchanged.
>
> **Before publishing,** open a couple of the localized links: most paths are
> shared across domains, but a few deep pages differ per locale (or 302-redirect).
> If a localized path 404s, fall back to that tool's **hub** page (`/tools/crm/`,
> `/tools/tasks_and_projects/`, `/tools/communications/`) on the same domain —
> hubs exist on every market domain. Keep the `href` real either way so the PDF
> stays clickable.

---

## 2. Tool glossary (EN → ES → PL → URL path)

The names below are the ones used across the construction/marketing/etc. guides.
`URL path` is appended to the market domain from §1. ES names are the official
wording from the reference file; **PL names are a working translation — confirm
against bitrix24.pl before publishing.**

| EN (link text) | ES | PL | URL path (after domain) |
|---|---|---|---|
| CRM | CRM | CRM | `/tools/crm/` |
| Contact Center | Contact Center | Contact Center | `/tools/crm/` |
| CRM Forms | Formularios CRM | Formularze CRM | `/tools/crm/` |
| Tasks in CRM | Tareas en CRM | Zadania w CRM | `/tools/crm/` |
| CRM Analytics | CRM Analytics | Analityka CRM | `/tools/crm/analytics-and-reports.php` |
| Dashboards in BI Builder | Paneles de control | Pulpity w BI Builder | `/tools/crm/analytics-and-reports.php` |
| Tasks in Projects | Tareas en Proyectos | Zadania w Projektach | `/tools/tasks_and_projects/` |
| Kanban | Kanban | Kanban | `/tools/tasks_and_projects/` |
| Workgroups and Projects | Grupos de Trabajo | Grupy robocze i Projekty | `/tools/tasks_and_projects/` |
| Automation in Scrum | Automatización en Scrum | Automatyzacja w Scrum | `/tools/tasks_and_projects/` |
| Work Reports | Reportes de trabajo | Raporty pracy | `/tools/tasks_and_projects/` |
| Flows | Flujos de trabajo | Przepływy (Flows) | `/tools/tasks_and_projects/` |
| Workflow Autorun | Procesos de negocio | Procesy biznesowe | `/tools/hr_automation/` |
| Drive | Drive | Dysk | `/tools/communications/` |
| Online Documents | Documentos online | Dokumenty online | `/tools/communications/` |
| File version storage | Historial de cambios | Historia wersji plików | `/tools/communications/` |
| Group Chats | Chats grupales | Czaty grupowe | `/tools/communications/` |
| Shared Calendars | Calendarios Compartidos | Współdzielone kalendarze | `/tools/communications/` |
| Notifications | Notificaciones | Powiadomienia | `/tools/communications/` |
| Extranet Users | Usuarios de Extranet | Użytkownicy ekstranetu | `/tools/communications/` |
| Access Permissions | Permisos de acceso | Uprawnienia dostępu | `/tools/communications/` |
| Mobile App | App móvil | Aplikacja mobilna | `/tools/` |

Add a row whenever a new guide introduces a tool. Keep EN as the key.

---

## 3. UI label glossary

| EN | ES | PL |
|---|---|---|
| Quick Guide | Guía rápida | Szybki przewodnik |
| Business pain | Dolor del cliente | Problem biznesowy |
| Bitrix24 Tools | Herramientas Bitrix24 | Narzędzia Bitrix24 |
| Practical Outcome | Valor práctico de Bitrix24 | Praktyczny rezultat |

(ES wording matches the reference file; confirm PL wording with a native reviewer.)

---

## 4. How to localize a finished guide

1. **Copy** the built HTML to a per-market filename, e.g.
   `industry-guide-construction.es.html`.
2. **Translate the visible copy** in place — leave every tag, class, and
   structure untouched. Set the document `lang` (`<html lang="es">`).
3. **For each `<a>` in a "Bitrix24 Tools" list:** translate the link *text* per
   §2, and change the `href` **domain** per §1 (keep the path).
4. **Translate the labels** ("Business pain" → …) per §3, the "Quick Guide" pill,
   and the CTA if present.
5. **Watch the layout** — Spanish/Polish/German run ~20–30% longer than English.
   The cards tolerate a couple of extra lines; if a page overflows its fixed
   1080×1350 sheet, move a card to the next page rather than shrinking type.
6. **Re-render:** `python3 scripts/render.py industry-guide-construction.es.html --format guide`.
7. **Verify:** eyeball each page for clipping, and click-test 2–3 localized links
   in the exported PDF (they must open the right market domain).

> Claude can do all of the above on request — e.g. *"localize this guide into
> Spanish and Polish"* — producing one rendered PDF per market.
