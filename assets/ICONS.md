# Icon system — the icon base for ALL Bitrix24 PDFs

This is the rule and the **catalog** for icons in every PDF this skill builds — the
Industry Guide and all the others (A4 guides, one-pagers, playbooks, brochures).
The icons come from the official **Bitrix24 "Common" icon library** in Figma
(`https://www.figma.com/design/9GHzh0gwFo7vItzWJfplaj/`). The library holds two
matching families; this file catalogs both, with each icon's meaning and its Figma
node id (for export).

---

## The rule (applies to every PDF)

1. **Default to the SOLID set** — *Solid Icons (Web and Mobile)*. Build with Solid
   unless the user explicitly asks for the outline style.
2. **Outline Bold only on request.** If the user says they want the outline / line
   look, use *Outline Bold (Web)* — and then use it **everywhere in that file**.
3. **One icon style per file — never mix.** If a document uses Solid, every icon in
   it is Solid; if it uses Outline Bold, every icon is Outline Bold. Do not put a
   Solid icon and an Outline icon on the same document.
4. **Pick by MEANING, not decoration.** Choose the icon whose meaning matches the
   block or heading. A block about **leads** → the *Lead* icon; about **a sales
   funnel** → *Filter funnel*; about **optimisation / growth / better numbers** →
   an abstract growth arrow (*Trend up*, *Statistics arrow*) or *Graphs diagram*;
   about **automation** → *Business process*; about **security / access** →
   *Shield checked* / *Lock*. Use the semantic index and the catalog below.
5. **Recolour every icon to the design system.** Library icons export in brand
   green — never use them green. Recolour to the surface they sit on:
   - **white** on the navy app tiles / any dark surface (`…-white.svg`);
   - **deep navy `#01447B`** inline on light pages (`….svg`).
   `scripts/prep_icon.py` produces both twins from a raw export (see below).

---

## Pick by meaning — semantic index (Solid)

Common heading / block themes → the icon to reach for first. (Names map to the
catalog; each has a Figma node id there.)

| If the block / heading is about… | Use icon |
|---|---|
| Leads, incoming enquiries | **Lead** |
| CRM, client base, deals | **CRM** |
| Sales funnel, pipeline, stages | **Filter funnel** · **Stages** |
| Growth, optimisation, higher conversion / revenue | **Trend up** · **Statistics arrow** |
| Analytics, dashboards, reporting, visibility | **Graphs diagram** |
| Tasks, to-dos | **Task** · **Task list** |
| Projects, boards | **Kanban** · **Scrum** |
| Automation, workflows, business processes | **Business process** · **Processes** |
| Documents, files, storage | **File** · **Folder** |
| Calendar, scheduling, deadlines | **Calendar** |
| Real-time / field / on the go | **Mobile** · **Tablet** |
| Notifications, alerts, reminders | **Notification** · **Alert** |
| Team chat, coordination, messaging | **Chats** · **Messenger** |
| People, team, roles | **Person** · **Group** · **3 Persons** |
| Subcontractors / external access, permissions | **Shield checked** · **Lock** · **Key** |
| Contact center, support, calls | **Contact center** · **Headset** |
| E-commerce, orders, payments | **Shopping cart** · **Wallet** |
| AI, copilot, smart features | **AI stars** · **AI Robot** |
| Launch, new business, scaling | **Rocket** |
| Do / done, yes | **Check** · **Circle Check** |
| Don't / no, remove | **Cross** · **Circle cross** |

If nothing fits, search the full catalog below by category.

---

## On-demand workflow — fetch only what the document needs (do NOT bulk-download)

Don't try to download the whole library. This catalog IS the reference: for each
document, look up only the handful of icons that document actually needs, pull just
those from Figma, prep them, and use them. A guide needs ~5–10 icons, so this is a
few exports per document — light on Figma's per-seat limit and it keeps the skill lean.

Per document:
1. **List the icons this document needs** and pick each by MEANING from the semantic
   index / catalog — note its Figma **node id**.
2. **Check the cache first:** `bitrix24-images/icons-solid/` holds icons already
   fetched & normalised (reused across documents). Only fetch the ones missing there.
3. **Fetch the missing ones** from Figma by node id — Figma MCP `download_assets`,
   `defaultFormat: svg`. Each 24×24 export comes in brand green (#15C674) on a grey
   canvas rect. (A few calls per document; if you ever hit the per-seat tool-call
   limit, fetch across turns or from an editor seat — never bulk-pull the set.)
4. **Normalise** each into the two brand twins (drops the canvas rects, recolours):
   `python3 scripts/prep_icon.py raw-export.svg <name> --dir assets/bitrix24-images/icons-solid`
   → `<name>.svg` (navy `#01447B`) + `<name>-white.svg` (white).
5. **Use** it: white twin inside a navy `.b24-tile`
   (`<img src="…/icons-solid/<name>-white.svg">`), navy twin inline on light pages
   (`.b24-ic`). Never the green original.

> **Cache.** `bitrix24-images/icons-solid/` holds a ready set of the most-used Solid
> icons (each with a `-white` twin) — **reuse these before re-fetching**:
> `ai, ai-robot, alert, arrow-down, arrow-right, business-process, calendar, cart, chart,
> chats, check, chevron-down, chevron-right, circle-check, circle-cross, circle-minus,
> circle-plus, clock, cloud, contact-center, crm, cross, download, earth, edit,
> enterprise, exclamation-circle, favorite, file, filter, flag, folder, funnel, group,
> headset, home, info-circle, kanban, key, lead, link, lock, mail, message, messenger,
> mic, minus, mobile, money, notification, pause, person, persons, phone-in, phone-out,
> pin, play, plus, process, processes, rocket, sale-tag, scrum, search, settings, share,
> shield, shield-checked, sound-off, sound-on, stages, stats-arrow, tablet, tag, task,
> task-list, timer, trend-up, upload, wallet`. It grows as new icons are pulled on demand.
>
> **One style per document still applies.** Every icon in a document is the same
> family — all Solid (default) or all Outline Bold (on request). The older curated set
> in `bitrix24-images/icons/` is its own consistent style (the current Industry Guide
> uses it); when you build with `icons-solid/`, use it for every icon in that file.

---

## Full catalog

Every icon in both families, grouped by theme, with its Figma node id. The **Solid**
set is the default; the **Outline Bold** set is the alternative used only when the
outline style is requested. Node ids are for `download_assets` export.

### SOLID set — the DEFAULT (534 icons)


**CRM & Sales**

| Icon (meaning) | Figma node |
|---|---|
| Add funnel | `46637:62782` |
| CRM | `27341:16287` |
| CRM Field except | `40658:6402` |
| CRM Field linked | `40658:6405` |
| CRM Field simple | `40658:6404` |
| CRM Letters | `27534:16434` |
| CRM Online store | `46637:62781` |
| CRM Optional Accepted | `40658:6411` |
| CRM Optional Not Accepted | `40658:6394` |
| CRM Payment and delivery | `46637:62780` |
| CRM Required Consent | `40658:6399` |
| Change funnel | `46637:62783` |
| Crm form | `46637:62786` |
| Cup winner | `48200:12765` |
| Filter funnel | `42531:6600` |
| Lead | `36373:8871` |
| MCP Letters | `46655:12300` |
| Money | `49349:12466` |
| Money prize | `37856:8431` |
| Quick CRM fill | `46655:12327` |
| Repeat sales | `46655:12273` |
| Sale Tag | `46638:62809` |
| Segment sales | `49055:12752` |
| Segment sales ai | `49055:12723` |
| Stage | `27034:37542` |
| Stage minus | `46637:62778` |
| Stage plus | `46637:62779` |
| Stages | `46637:62773` |
| Tag | `46637:62738` |
| VK Lead Form | `48200:12767` |
| Wallet | `33389:21148` |

**Tasks & Projects**

| Icon (meaning) | Figma node |
|---|---|
| AI Projects | `47795:12519` |
| Board | `27827:18318` |
| Check list | `46637:62737` |
| Complete task list | `33389:21193` |
| Interval | `46638:62794` |
| Kanban | `33389:21158` |
| Keyboard | `46655:12287` |
| List tasks add | `48067:12444` |
| Move to checklist | `46637:62721` |
| Related tasks | `46637:62775` |
| Scrum | `46637:62787` |
| Share Task | `46637:62777` |
| Subtask | `46637:62774` |
| Task | `27341:16283` |
| Task fire | `47642:13100` |
| Task list | `33389:21145` |
| Timeline | `46638:62797` |

**Analytics, Growth & Reports**

| Icon (meaning) | Figma node |
|---|---|
| A Letter Sort Down | `46637:62730` |
| A Letter Sort Up | `46637:62745` |
| Business process progress | `46638:62800` |
| Graphs diagram | `28672:36632` |
| Graphs settings | `48200:12785` |
| Pulse | `46638:62808` |
| Rocket | `33389:21192` |
| Statistics arrow | `46655:12296` |
| Superscript | `46655:12321` |
| Trend down | `46634:62705` |
| Trend up | `37856:8432` |

**Communication**

| Icon (meaning) | Figma node |
|---|---|
| A Letter | `46637:62749` |
| Add Chat | `46637:62759` |
| Chat list | `46637:62762` |
| Chats | `27341:16288` |
| Close chat | `49265:12532` |
| Empty message | `46637:62761` |
| Headset | `46638:62801` |
| Mail | `30005:24971` |
| Message | `33389:21162` |
| Messenger | `46637:62757` |
| Messenger (meta) | `46637:62753` |
| Microphone Ai | `46655:12326` |
| Microphone Off | `48144:12469` |
| Microphone On | `45505:12460`  (variant frame XS/S/M/L stacked — export & crop the L / 24px variant to viewBox `20 27 24 24`, then prep) |
| Microphone sounds Ai | `46655:12325` |
| Notification | `33389:21169` |
| Notification off | `46638:62806` |
| Notification settings | `48200:12740` |
| Notification with cross | `48200:12739` |
| Open chat | `49265:12533` |
| Phone Add | `33389:21161` |
| Phone Broken | `33389:21173` |
| Phone In | `33389:21149` |
| Phone Out | `33389:21164` |
| Phone Up | `33389:21166` |
| Phone down | `46637:62758` |
| Sound Off | `33389:21151` |
| Sound On | `33389:21188` |

**Files & Documents**

| Icon (meaning) | Figma node |
|---|---|
| Cloud | `33389:21187` |
| Cloud Sync | `33389:21201` |
| Cloud Sync cross | `46655:12308` |
| Cloud download | `46655:12264` |
| Cloud time | `46655:12272` |
| Cloud with check | `46655:12266` |
| Create file | `37856:8428` |
| Document sign | `29830:19489` |
| Download | `46634:62714` |
| File | `27341:16280` |
| File with calendar | `46637:62764` |
| File with check | `46637:62771` |
| File with check 2 | `46637:62769` |
| File with crown | `46637:62766` |
| File with person | `46637:62765` |
| Folder | `33389:21165` |
| Folder 24 | `46637:62767` |
| Folder plus | `46637:62768` |
| Folders | `46655:12322` |
| Sign | `29990:19966` |
| Sign default | `48200:12779` |
| Signal | `46655:12305` |
| Signal 1 | `43068:7352` |
| Signal 2 | `43068:7353` |
| Upload | `46655:12267` |
| Upload document | `46637:62772` |
| Upload file | `46637:62770` |

**People & Team**

| Icon (meaning) | Figma node |
|---|---|
| 3 Persons | `29990:20675` |
| Contact center | `34776:8485` |
| Contact details | `48200:12772` |
| Enterprise | `33389:21194` |
| Group | `27341:16284` |
| Neutral | `33389:21150` |
| Person | `33389:21160` |
| Person detect | `46655:12284` |
| Personal Data Consent | `49265:12605` |
| Sad | `33389:21167` |
| Smile | `33389:21159` |
| Sticker Smile | `47642:12873` |
| Stress | `33389:21163` |
| Stress no | `48141:12494` |

**Security & Access**

| Icon (meaning) | Figma node |
|---|---|
| Ban | `45765:12175` |
| Bank card | `41570:7002` |
| Block insertion | `46655:12319` |
| Clock | `45490:12176` |
| Clock back | `46638:62799` |
| Crossed eye | `40658:6410` |
| Crown | `33389:21199` |
| Crown 1 | `39968:11721` |
| Crown forward | `46685:12317` |
| Earth with clock | `46644:12217` |
| IP address | `46655:12336` |
| IP address crossed | `46655:12334` |
| Key | `33389:21180` |
| Lock | `45490:12423` |
| Lock 2 | `48200:12731` |
| Online Bank | `45004:7018` |
| Shield | `33389:21177` |
| Shield attention | `46655:12255` |
| Shield checked | `33389:21140` |
| Unlock | `45490:12539` |

**Devices**

| Icon (meaning) | Figma node |
|---|---|
| Mobile | `38070:8467` |
| Mobile fill | `46655:12324` |
| Tablet | `46644:12223` |

**Time & Calendar**

| Icon (meaning) | Figma node |
|---|---|
| Calendar | `46638:62791` |
| Calendar Empty | `46170:12322` |
| Calendar share | `48200:12737` |
| Calendar with checks | `46638:62793` |
| Calendar with slots | `27341:16285` |
| Location time | `46644:12213` |
| Login history | `48200:12729` |
| Sort calendar | `48200:12738` |
| Timer | `48200:12733` |
| Timer dot | `48200:12732` |

**AI & Automation**

| Icon (meaning) | Figma node |
|---|---|
| AI Process | `46655:12332` |
| AI Robot | `37572:8415` |
| AI stars | `33389:21141` |
| AI stars question | `46655:12260` |
| AI stars question 4 | `46658:23643` |
| Ai Internet search | `48200:12786` |
| Ai Reflection | `46655:12285` |
| Ai two stars | `43167:37265` |
| Business process | `36690:9138` |
| Fill out again | `40658:6400` |
| Legal process | `48200:12784` |
| Magic wand | `33389:21195` |
| Main tool | `33389:21157` |
| Process | `46655:12328` |
| Process stop | `46655:12330` |
| Processes | `33389:21170` |
| Robot | `29990:19766` |
| Smart process | `27341:16282` |
| Start education | `44595:6659` |

**Navigation & UI controls**

| Icon (meaning) | Figma node |
|---|---|
| Add database | `49265:12535` |
| Add event | `48200:12736` |
| Alert | `45495:12712` (variant frame XS/S/M/L stacked — export & crop the L / 24px variant to viewBox `20 27 24 24`, then prep) |
| Alert accent | `29924:41498` |
| Arrow down | `45746:12797`  (variant frame XS/S/M/L stacked — export & crop the L / 24px variant to viewBox `20 27 24 24`, then prep) |
| Arrow to the Right | `45746:12747`  (variant frame XS/S/M/L stacked — export & crop the L / 24px variant to viewBox `20 27 24 24`, then prep) |
| Arrow to the left | `45746:13787` |
| Arrow top | `45716:12236` |
| Auto Check in | `46644:12200` |
| Bottom Top Collapse | `45765:12549` |
| Check | `45505:12172` |
| Check deferred | `46655:12290` |
| Check in cancel | `46644:12203` |
| Check in negative | `46644:12205` |
| Chevron Down | `45666:12277`  (variant frame XS/S/M/L stacked — export & crop the L / 24px variant to viewBox `20 27 24 24`, then prep) |
| Chevron Up | `45666:12260` |
| Chevron to the Left | `45666:12239` |
| Chevron to the Right | `45594:13055`  (variant frame XS/S/M/L stacked — export & crop the L / 24px variant to viewBox `20 27 24 24`, then prep) |
| Circle Check | `36655:9194` |
| Circle Check forward | `46655:12247` |
| Circle cross | `37651:11635` |
| Circle minus | `46655:12246` |
| Circle more | `46655:12242` |
| Circle plus | `46655:12251` |
| Collab add | `46655:12331` |
| Collapse | `45712:12409` |
| Copy link | `46655:12306` |
| Cross | `45692:12291` |
| Double check | `46638:62807` |
| Drag | `45842:12481` |
| Earth | `33389:21189` |
| Earth with check | `46644:12209` |
| Earth with cross | `46644:12216` |
| Earth with stop | `46644:12208` |
| Earth with tree | `46644:12214` |
| Edit | `45845:12714`  (variant frame XS/S/M/L stacked — export & crop the L / 24px variant to viewBox `20 27 24 24`, then prep) |
| Exclamation | `45757:12154` |
| Exclamation circle | `46655:12238` |
| Expand | `45712:12183` |
| Favorite | `26839:18247` |
| Filter | `46638:62790` |
| Filter 2 | `45746:13838` |
| Filter 2 lines | `46655:12275` |
| Find filters | `46655:12230` |
| Flag | `46638:62804` |
| Flag with cross | `46638:62810` |
| Go to | `45694:12542` |
| Heart | `28483:18333` |
| Home | `30886:19621` |
| Home star | `46644:12207` |
| Image Plus | `48200:12778` |
| Info Circle | `46655:12245` |
| Lightning plus | `46644:12201` |
| Link | `46655:12240` |
| Link settings | `46655:12234` |
| Link update | `48200:12777` |
| Location Plus | `48200:12745` |
| Lower Left Arrow | `46634:62710` |
| Lower Right Arrow | `46634:62716` |
| Minus | `45694:12430`  (variant frame XS/S/M/L stacked — export & crop the L / 24px variant to viewBox `20 27 24 24`, then prep) |
| More | `45842:12356` |
| More vertical | `45842:12227` |
| Non favorite | `48200:12742` |
| Parts Record Play | `46655:12303` |
| Parts Record Stop | `46655:12311` |
| Pause | `45490:12309`  (variant frame XS/S/M/L stacked — export & crop the L / 24px variant to viewBox `20 27 24 24`, then prep) |
| Pin | `33389:21147` |
| Ping | `48200:12744` |
| Play | `45482:12207`  (variant frame XS/S/M/L stacked — export & crop the L / 24px variant to viewBox `20 27 24 24`, then prep) |
| Plus | `45590:12492`  (variant frame XS/S/M/L stacked — export & crop the L / 24px variant to viewBox `20 27 24 24`, then prep) |
| Power | `45758:12222` |
| Refresh | `45590:12338` |
| Save template plus | `46655:12315` |
| Search | `46655:12248` |
| Settings | `45434:12265` |
| Share | `46634:62709` |
| Shopping cart | `30005:25052` |
| Speaker add | `46655:12333` |
| Stop | `45698:12158` |
| Stop hand | `36492:8886` |
| Top Bottom Expand | `45765:12410` |
| Unlink | `46658:23626` |
| Vibe Plus | `47555:13872` |
| Vibe Plus 2 | `47576:12331` |
| Window flag | `33389:21152` |

**Other**

| Icon (meaning) | Figma node |
|---|---|
| 2GIS | `46644:12211` |
| Achievement | `48200:12743` |
| Action Required | `48200:12787` |
| Activity | `33389:21183` |
| Alarm | `48200:12734` |
| Align center | `46637:62744` |
| Align image center | `46841:12506` |
| Align image left | `46841:12509` |
| Align image right | `46841:12507` |
| Align justify | `46637:62751` |
| Align left | `46637:62748` |
| Align right | `46637:62724` |
| Apps | `36690:9137` |
| Attach | `27341:16281` |
| Attach 2 | `46655:12237` |
| Auto selection | `48200:12759` |
| Back | `46634:62699` |
| Back 10 | `46655:12231` |
| Back 15 | `46634:62701` |
| Ball one | `48200:12773` |
| Barcode | `49349:12468` |
| Battery (1 stick) | `46644:12225` |
| Battery (2 sticks) | `46644:12226` |
| Battery no charge | `46644:12221` |
| Beer | `48200:12766` |
| Black list | `48200:12780` |
| Bluetooth | `46655:12277` |
| Bold | `46637:62729` |
| Book open | `40778:6872` |
| Bookmark | `27870:18307` |
| Bookmark 4 | `46655:12279` |
| Bottleneck | `33389:21176` |
| Bottom menu | `46655:12270` |
| Box | `33389:21200` |
| Box with lid | `46655:12278` |
| Branch network | `47795:12521` |
| Broom | `48200:12789` |
| Browser | `30033:19103` |
| Bug | `33389:21142` |
| Bulleted List | `46637:62742` |
| Cake celebrating | `48200:12764` |
| Camera | `33389:21184` |
| Card | `46655:12268` |
| Change order 3 | `46634:62708` |
| Change places | `46634:62704` |
| Claw | `46655:12323` |
| Collab | `29990:20550` |
| Collaboration | `30037:19490` |
| Collection | `45076:6709` |
| Columns sidebar pending | `48200:12753` |
| Columns sidebar pending left | `48200:12752` |
| Commands | `48200:12758` |
| Company | `33389:21144` |
| Compass | `46644:12206` |
| Condition | `46655:12298` |
| Connection | `46644:12204` |
| Contrast | `46655:12329` |
| Cookies | `42630:6593` |
| Copilot | `33389:21186` |
| Core | `48200:12762` |
| Cursor click | `33389:21198` |
| Cursors strike | `46655:12256` |
| Data reading | `48200:12783` |
| Database | `33389:21181` |
| Day off | `48200:12741` |
| Delete event | `46638:62798` |
| Demonstration On | `44463:6590` |
| Department | `33389:21146` |
| Developer Resources | `27473:16477` |
| Dial 10 | `48200:12788` |
| Dial 20 | `48200:12782` |
| Digits 123 | `46655:12291` |
| Digits 24 | `48200:12775` |
| Discount | `46655:12307` |
| Disike | `39507:8733` |
| Distribution | `46638:62812` |
| Do not use captcha | `40658:6401` |
| Dots | `48200:12761` |
| Employee | `29830:19637` |
| Empty battery | `46644:12222` |
| Excel | `45004:7021` |
| Expert mode | `48200:12735` |
| Export | `45076:6710` |
| Face ident | `46655:12293` |
| Feedback | `46637:62754` |
| Feedback form | `48200:12771` |
| Fingerprint | `48200:12781` |
| Fire | `28620:18454` |
| Flower | `48200:12769` |
| Form | `46655:12263` |
| Forward | `46634:62718` |
| Forward 10 | `46655:12235` |
| Forward 16 | `46634:62698` |
| Frame create | `46655:12289` |
| Freelance | `46644:12219` |
| Full Battery | `33389:21185` |
| Function | `48175:12716` |
| Galaxy | `46765:12362` |
| Galaxy server | `46835:12329` |
| Glasses | `46655:12265` |
| Globe extranet | `46655:12271` |
| Google maps | `46644:12218` |
| Graduation cap | `33389:21143` |
| Hamburger menu | `46655:12269` |
| Handshake | `36373:8870` |
| Headlines | `46655:12320` |
| Headlines H1 | `46655:12312` |
| Headlines H2 | `46655:12316` |
| Headlines H3 | `46655:12318` |
| Headlines H4 | `46655:12313` |
| Headlines H5 | `46655:12310` |
| Hide 3 | `46637:62747` |
| Hide 4 | `46637:62740` |
| High temperature | `49244:12493` |
| Hourglass | `46638:62796` |
| Idea Lamp | `40658:6403` |
| Image | `42653:6645` |
| Import | `45076:6713` |
| Inventory Management | `38642:6161` |
| Italic | `46637:62734` |
| Knowledge base | `33389:21196` |
| Layers | `46655:12261` |
| Left right | `46634:62703` |
| Library base | `45798:19615` |
| Like | `27398:17004` |
| List Viewer | `46655:12299` |
| Location | `33389:21182` |
| Log in | `37856:8429` |
| Log out | `46634:62707` |
| Logo Android | `46655:12283` |
| Logo Apple | `46655:12286` |
| MCP | `46655:12302` |
| Maneki Neko | `49130:12473` |
| Map | `48200:12747` |
| Market | `29990:20266` |
| Marketing | `29990:20585` |
| Martini glass | `48200:12774` |
| Maximize | `46634:62706` |
| Maximize 2 | `46634:62702` |
| Mention | `46638:62803` |
| Merge | `46655:12295` |
| Minimize | `46634:62715` |
| Minimize 2 | `46634:62700` |
| Moon | `33389:21154` |
| Multi page form | `48200:12760` |
| Multichoice Off | `48200:12751` |
| Multichoice On | `48200:12749` |
| Music | `46638:62805` |
| Newsfeed | `27341:16286` |
| Next | `46655:12249` |
| No Compass | `46644:12202` |
| No wifi | `48200:12746` |
| Note | `27557:16614` |
| Numbered List | `46637:62722` |
| Observer | `33389:21191` |
| Online booking | `27398:16766` |
| Online events | `48200:12755` |
| Open channels | `33389:21174` |
| Open sequence | `42131:7088` |
| Palette | `46655:12258` |
| Partner nfc | `46655:12262` |
| Parts Record | `46655:12304` |
| Path | `46644:12220` |
| Payment | `41570:7001` |
| Payment terminal | `36690:9139` |
| Planning | `46638:62789` |
| Planning 2 | `46638:62795` |
| Point left | `46637:62726` |
| Point right | `46637:62728` |
| Poll | `47409:12796` |
| Previous | `46655:12232` |
| Product | `30005:25087` |
| Products payment | `41570:7003` |
| Products shirt | `48200:12757` |
| Prompt var | `46655:12254` |
| QR code | `49349:12467` |
| Quantity | `46655:12274` |
| Question | `37856:8427` |
| Question L | `46655:12233` |
| Quote | `46655:12250` |
| Radiant | `49052:12690` |
| Receipt note | `48200:12756` |
| Recent items | `46638:62792` |
| Record on | `46398:12249` |
| Record video | `33389:21153` |
| Redirect | `40658:6393` |
| Redo | `46634:62717` |
| Registration on site | `48200:12754` |
| Repeat | `27341:16289` |
| Reply | `46634:62711` |
| Reply to all | `46634:62696` |
| Resume | `46634:62712` |
| Reveal 3 | `46637:62746` |
| Reveal 4 | `46637:62750` |
| Roles library | `33389:21190` |
| SMS | `46637:62752` |
| SSO | `46655:12294` |
| Save template | `46655:12314` |
| Screen | `33389:21175` |
| Sended | `46638:62811` |
| Service | `29990:20413` |
| Services | `46655:12276` |
| Shop order | `48200:12776` |
| Shuffle | `46634:62697` |
| Sick | `46638:62802` |
| Sigma summ | `46637:62785` |
| Size W L | `46655:12297` |
| Slash | `46637:62733` |
| Sort activity | `48200:12730` |
| Speaker | `48235:19556` |
| Speed 0_5 | `46655:12228` |
| Speed 0_7 | `46655:12252` |
| Speed 1 | `46655:12239` |
| Speed 1_2 | `46655:12241` |
| Speed 1_5 | `46655:12253` |
| Speed 1_7 | `46655:12229` |
| Speed 2 | `46655:12227` |
| Speed meter | `46655:12243` |
| Spoiler | `46637:62732` |
| Sticker | `48200:12763` |
| Stock | `30033:19252` |
| Storage | `29990:24915` |
| Strikethrough | `46637:62743` |
| Structure horizontal | `46637:62784` |
| Structure vertical | `46637:62788` |
| Subscript | `46655:12317` |
| Subscription | `29990:19594` |
| Suitcase | `43942:6578` |
| Sun | `46644:12212` |
| Switch camera | `46644:12224` |
| Telephony | `46637:62763` |
| Text | `46637:62720` |
| Text format Bottom | `46637:62727` |
| Text format Cancel | `46637:62741` |
| Text format Top | `46637:62731` |
| Text format Top left | `46637:62725` |
| Text format Top right | `46637:62723` |
| Text format reset | `46637:62735` |
| Theme | `48200:12750` |
| Thread | `46637:62756` |
| Thread single | `47201:12507` |
| Threads | `47211:12249` |
| Three squares | `48200:12770` |
| Topic | `46655:12257` |
| Transcription | `46655:12301` |
| Translation | `46637:62736` |
| Trashcan | `45505:12319` |
| UNC 1 | `49229:12508` |
| Underline | `46637:62739` |
| Undo | `46634:62713` |
| Universal access | `47211:12279` |
| Vacation | `46644:12210` |
| Verification | `30982:23246` |
| Vibecode | `47795:12520` |
| Video Record | `46655:12282` |
| Video Record 2 | `46655:12281` |
| Video Record 3 | `46655:12292` |
| Video Record 4 | `46655:12280` |
| Video Record 5 | `46655:12288` |
| Virtual server | `48200:12768` |
| Virtual storage | `46655:12335` |
| Webhook | `46655:12309` |
| WhatsApp | `46637:62760` |
| Wifi | `48200:12748` |
| Wiki | `47445:12400` |
| Window ring | `46637:62776` |
| Yandex maps | `46644:12215` |
| Zoom in | `46655:12244` |
| Zoom out | `46655:12236` |


### OUTLINE BOLD set — alternative, only on explicit request (621 icons)


**CRM & Sales**

| Icon (meaning) | Figma node |
|---|---|
| Add funnel | `45206:14309` |
| Busines process stages | `45206:14374` |
| Business process money | `45206:14489` |
| CRM | `45206:14054` |
| CRM Analytics | `45206:14104` |
| CRM Field except | `45206:14470` |
| CRM Field linked | `45206:14469` |
| CRM Field simple | `45206:14468` |
| CRM Letters | `45206:14342` |
| CRM Online store | `45206:14102` |
| CRM Optional Accepted | `45206:14587` |
| CRM Optional Not Accepted | `45206:14588` |
| CRM Payment and delivery | `45206:14103` |
| CRM Required Consent | `45206:14589` |
| Change funnel | `45206:14139` |
| Client chat | `45206:14550` |
| Client letter | `45206:14561` |
| Crm form | `45206:14631` |
| Cup winner | `45206:14428` |
| Filter funnel | `45206:14396` |
| Invoice | `45206:14155` |
| Issue Invoice | `45206:14156` |
| Lead | `45206:14159` |
| Lead send | `45206:14622` |
| MCP Letters | `45206:14562` |
| Money | `45206:14119` |
| Money prize | `45206:14429` |
| My Deals | `45206:14341` |
| My Deals send | `45206:14623` |
| Quick CRM fill | `45206:14486` |
| Repeat sales | `45206:14418` |
| Sale Tag | `45206:14182` |
| Stage | `45206:14125` |
| Stage minus | `45206:14383` |
| Stage plus | `45206:14382` |
| Stages | `45206:14124` |
| Tag | `45206:14257` |
| VK Lead Form | `45206:14480` |
| Wallet | `45206:14087` |

**Tasks & Projects**

| Icon (meaning) | Figma node |
|---|---|
| AI Projects 2 | `47862:12404` |
| Add timeline | `45206:14187` |
| Board | `45206:14399` |
| Check list | `45206:14254` |
| Complete task list | `45206:14048` |
| Interval | `45206:14051` |
| Kanban | `45206:14138` |
| Keyboard | `45206:14544` |
| List tasks add | `47334:12400` |
| Move to checklist | `45206:14261` |
| Related tasks | `45206:14130` |
| Scrum | `45206:14081` |
| Share Task | `45206:14109` |
| Subtask | `45206:14049` |
| Task | `45206:14108` |
| Task fire | `45206:14565` |
| Task list | `45206:14047` |
| Template task | `45206:14650` |
| Timeline | `45206:14050` |

**Analytics, Growth & Reports**

| Icon (meaning) | Figma node |
|---|---|
| A Letter Sort Down | `45206:14455` |
| A Letter Sort Up | `45206:14456` |
| Graphs diagram | `45206:14092` |
| Graphs link | `46094:12416` |
| Graphs settings | `45206:14539` |
| Mail in progress | `45206:14243` |
| Pulse | `45206:14078` |
| Rocket | `45206:14214` |
| Statistics arrow | `45206:14535` |
| Superscript | `45206:14647` |
| Trend down | `45206:14289` |
| Trend up | `45206:14290` |

**Communication**

| Icon (meaning) | Figma node |
|---|---|
| A Letter | `45206:14256` |
| Add Chat | `45206:14230` |
| Add to chat | `45206:14639` |
| Call back | `45206:14472` |
| Chat list | `45206:14322` |
| Chats | `45206:14226` |
| Chats with check | `45206:14227` |
| Close chat | `45206:14391` |
| Create chat | `45206:14329` |
| Empty message | `45206:14231` |
| Go to message | `45206:14315` |
| Headset | `45206:14065` |
| Mail | `45206:14241` |
| Mail counter | `45206:14244` |
| Mail forward | `45206:14246` |
| Mail open | `45206:14245` |
| Mail plus | `45206:14605` |
| Mail return | `45206:14247` |
| Mail send | `45206:14248` |
| Media message | `45206:14533` |
| Message | `45206:14224` |
| Message To | `45206:14435` |
| Messages | `45206:14225` |
| Messages multi | `45206:14629` |
| Messenger | `45206:14240` |
| Messenger (meta) | `45206:14239` |
| Messenger send | `45206:14626` |
| Microphone Ai | `45206:14609` |
| Microphone Off | `45206:14334` |
| Microphone sounds Ai | `45206:14610` |
| New message | `45206:14321` |
| Notification | `45206:14071` |
| Notification off | `45206:14287` |
| Notification settings | `45206:14168` |
| Notification with cross | `45206:14288` |
| Open chat | `45206:14390` |
| Phone Add | `45206:14410` |
| Phone Broken | `45206:14409` |
| Phone In | `45206:14408` |
| Phone Out | `45206:14407` |
| Phone Up | `45206:14233` |
| Phone down | `45206:14234` |
| Private message | `45206:14488` |
| Recent chats | `45206:14604` |
| Screen phone | `45206:14467` |
| Sound Off | `45206:14067` |
| Sound On | `45206:14066` |

**Files & Documents**

| Icon (meaning) | Figma node |
|---|---|
| Cloud | `45206:14381` |
| Cloud Sync | `45206:14199` |
| Cloud Sync cross | `45206:14634` |
| Cloud download | `45206:14411` |
| Cloud time | `45206:14337` |
| Cloud with check | `45206:14412` |
| Create file | `45206:14164` |
| Design | `45206:14218` |
| Disk shared | `45206:14105` |
| Document link | `45206:14573` |
| Document print | `45206:14574` |
| Document sign | `45206:14445` |
| Document update | `45206:14150` |
| Download | `45206:14274` |
| File | `45206:14059` |
| File settings | `45206:14645` |
| File with calendar | `45206:14369` |
| File with check | `45206:14062` |
| File with check 2 | `45206:14063` |
| File with clock | `45206:14395` |
| File with crown | `45206:14367` |
| File with person | `45206:14368` |
| Folder | `45206:14057` |
| Folder 24 | `45206:14056` |
| Folder plus | `45206:14058` |
| Folder success | `45206:14310` |
| Folder with card | `45206:14052` |
| Folders | `45206:14644` |
| No cloud Sync | `45206:14632` |
| Sign | `45206:14262` |
| Sign default | `45206:14538` |
| Signal | `45206:14619` |
| Upload | `45206:14307` |
| Upload document | `45206:14060` |
| Upload file | `45206:14061` |
| User Profile | `45206:14242` |

**People & Team**

| Icon (meaning) | Figma node |
|---|---|
| 3 Persons | `45206:14196` |
| 3 Persons check | `45206:14549` |
| Add person | `45206:14191` |
| Contact | `45206:14147` |
| Contact center | `45206:14513` |
| Contact details | `45206:14473` |
| Contact send | `45206:14627` |
| Delete person | `45206:14510` |
| Enterprise | `45206:14216` |
| Group | `45206:14189` |
| Neutral | `45206:14177` |
| Person | `45206:14188` |
| Person Mention | `45206:14436` |
| Person checks | `45206:14190` |
| Person descending | `45206:14192` |
| Person detect | `45206:14541` |
| Person office | `45206:14599` |
| Person search | `45206:14405` |
| Person settings | `45206:14198` |
| Person speak | `45206:14355` |
| Personal form | `45206:14481` |
| Remove person | `45206:14316` |
| Sad | `45206:14176` |
| Smile | `45206:14175` |
| Sticker Smile | `45206:14547` |
| Stress | `45206:14080` |
| Teams | `45206:14426` |
| User mask | `45206:14379` |

**Security & Access**

| Icon (meaning) | Figma node |
|---|---|
| Bank card | `45206:14578` |
| Block insertion | `45206:14662` |
| Clock back | `45206:14083` |
| Crossed eye | `45206:14140` |
| Crown | `45206:14077` |
| Crown 1 | `45206:14572` |
| Earth with clock | `45206:14184` |
| IP address | `45206:14490` |
| IP address crossed | `45206:14491` |
| Key | `45206:14076` |
| Lock 2 | `45206:14524` |
| Online Bank | `45206:14652` |
| Set canban | `45206:14618` |
| Shield | `45206:14068` |
| Shield attention | `45206:14404` |
| Shield checked | `45206:14403` |

**Devices**

| Icon (meaning) | Figma node |
|---|---|
| Desktop MacOS | `45206:14611` |
| Desktop Windows | `45206:14612` |
| Mobile | `45206:14074` |
| Mobile Constructor | `45206:14422` |
| Mobile Selected | `45206:14529` |
| Mobile Service | `45206:14414` |
| Mobile Stars | `45206:14416` |
| Mobile fill | `45206:14621` |
| Tablet | `45206:14075` |

**Time & Calendar**

| Icon (meaning) | Figma node |
|---|---|
| Calendar | `45206:14387` |
| Calendar Empty | `45206:14314` |
| Calendar share | `45206:14389` |
| Calendar with checks | `45206:14281` |
| Calendar with slots | `45206:14112` |
| Location time | `45206:14185` |
| Login history | `45206:14608` |
| Sort calendar | `45206:14392` |
| Timer | `45206:14179` |
| Timer dot | `45206:14180` |
| Trashcan timer | `45206:14442` |

**AI & Automation**

| Icon (meaning) | Figma node |
|---|---|
| AI Process | `45206:14492` |
| AI Robot | `45206:14551` |
| AI stars | `45206:14213` |
| AI stars question | `45206:14402` |
| AI stars question 2 | `45206:14425` |
| Ai Internet search | `45206:14512` |
| Ai Reflection | `45206:14511` |
| Ai two stars | `45206:14628` |
| Business process | `45206:14134` |
| Deep search ai | `45206:14616` |
| Fill out again | `45206:14586` |
| Legal process | `45206:14552` |
| List AI | `45206:14459` |
| List AI 2 | `45206:14570` |
| Magic wand | `45206:14420` |
| Main tool | `45206:14306` |
| Process | `45206:14548` |
| Process stop | `45206:14497` |
| Processes | `45206:14223` |
| Record video Ai | `45206:14641` |
| Robot | `45206:14201` |
| Smart process | `45206:14323` |
| Start education | `45206:14651` |
| Trainee | `45206:14496` |

**Navigation & UI controls**

| Icon (meaning) | Figma node |
|---|---|
| Add database | `45206:14563` |
| Add event | `45206:14331` |
| Add product | `45206:14162` |
| Alert accent | `45206:14293` |
| Auto Check in | `45206:14519` |
| Check deferred | `45206:14536` |
| Check in cancel | `45206:14517` |
| Check in negative | `45206:14518` |
| Circle Check | `45206:14053` |
| Circle Check forward | `45206:14571` |
| Circle cross | `45206:14106` |
| Circle minus | `45206:14318` |
| Circle more | `45206:14145` |
| Circle plus | `45206:14107` |
| Collab add | `45206:14494` |
| Company plus | `45206:14594` |
| Copy link | `45206:14640` |
| Double check | `45206:14148` |
| Earth | `45206:14069` |
| Earth with check | `45206:14173` |
| Earth with cross | `45206:14174` |
| Earth with stop | `45206:14172` |
| Earth with tree | `45206:14171` |
| Exclamation circle | `45206:14596` |
| Favorite | `45206:14070` |
| Filter | `45206:14082` |
| Filter 2 lines | `45206:14375` |
| Find filters | `45206:14282` |
| Flag | `45206:14073` |
| Flag with cross | `45206:14371` |
| Heart | `45206:14072` |
| Home | `45206:14079` |
| Home star | `45206:14144` |
| Image Plus | `45206:14643` |
| Info Circle | `45206:14064` |
| Lightning plus | `45206:14553` |
| Link | `45206:14084` |
| Link settings | `45206:14291` |
| Link update | `45206:14595` |
| Links list | `45206:14292` |
| Location Plus | `45206:14514` |
| Lower Left Arrow | `45206:14264` |
| Lower Right Arrow | `45206:14265` |
| Move to | `45206:14366` |
| Non favorite | `45206:14373` |
| Open channels cross | `45206:14606` |
| Parts Record Play | `45206:14580` |
| Parts Record Stop | `45206:14581` |
| Pin | `45206:14086` |
| Pin list | `45206:14417` |
| Ping | `45206:14115` |
| Play waves | `46159:13683` |
| Save template plus | `45206:14636` |
| Screen no share | `45206:14444` |
| Screen share | `45206:14443` |
| Screen share pause | `45206:14546` |
| Search | `45206:14055` |
| Search and RAG | `45206:14438` |
| Server settings | `45206:14453` |
| Share | `45206:14275` |
| Shopping cart | `45206:14091` |
| Speaker add | `45206:14493` |
| Stop hand | `45206:14336` |
| Stop hand crossed | `45206:14343` |
| Unlink | `45206:14127` |
| Unpin | `45206:14085` |
| Window flag | `45206:14111` |

**Other**

| Icon (meaning) | Figma node |
|---|---|
| 2GIS | `45206:14167` |
| Achievement | `45206:14129` |
| Action Required | `45206:14508` |
| Activity | `45206:14101` |
| Alarm | `45206:14100` |
| Align center | `45206:14295` |
| Align justify | `45206:14296` |
| Align left | `45206:14297` |
| Align right | `45206:14298` |
| Apps | `45206:14209` |
| Attach | `45206:14531` |
| Attach 2 | `45206:14294` |
| Auto selection | `45206:14471` |
| Autofill | `45206:14406` |
| Back | `45206:14279` |
| Back 10 | `45206:14354` |
| Back 15 | `45206:14313` |
| Ball one | `45206:14427` |
| Barcode | `45206:14157` |
| Battery (1 stick) | `45206:14097` |
| Battery (2 sticks) | `45206:14096` |
| Battery no charge | `45206:14099` |
| Beer | `45206:14433` |
| Bitrix GPT | `45206:14597` |
| Bitrix GPT round | `45206:14598` |
| Black list | `45206:14520` |
| Bluetooth | `45206:14202` |
| Bold | `45206:14249` |
| Book open | `45206:14592` |
| Bookmark | `45206:14377` |
| Bookmark 2 | `45206:14376` |
| Bottleneck | `45206:14181` |
| Bottom menu | `45206:14215` |
| Box | `45206:14123` |
| Box with lid | `45206:14203` |
| Broom | `45206:14534` |
| Browser | `45206:14449` |
| Bug | `45206:14413` |
| Bulleted List | `45206:14253` |
| Cake celebrating | `45206:14431` |
| Camera | `45206:14339` |
| Camera Off | `45206:14335` |
| Card | `45206:14393` |
| Cash Terminal | `45206:14088` |
| Change order | `45206:14186` |
| Change order 2 | `45206:14271` |
| Change places | `45206:14441` |
| Claw | `45206:14642` |
| Collab | `45206:14210` |
| Collaboration | `45206:14090` |
| Collection | `45206:14656` |
| Columns | `45206:14361` |
| Columns sidebar pending | `45206:14362` |
| Columns sidebar pending left | `45206:14363` |
| Commands | `45206:14630` |
| Company | `45206:14135` |
| Company send | `45206:14624` |
| Compass | `45206:14516` |
| Condition | `45206:14559` |
| Connection | `45206:14555` |
| Contrast | `45206:14498` |
| Cookies | `45206:14615` |
| Copied | `45206:14554` |
| Copilot | `45206:14212` |
| Copy | `45206:14116` |
| Core | `45206:14450` |
| Cursor click | `45206:14137` |
| Cursors strike | `45206:14378` |
| Customization | `45206:14487` |
| Data reading | `45206:14558` |
| Database | `45206:14415` |
| Day off | `45206:14302` |
| Ddos attack | `45206:14454` |
| Delay | `45206:14299` |
| Delegate | `45206:14300` |
| Delete event | `45206:14462` |
| Delivery | `45206:14421` |
| Delivery with item | `45206:14482` |
| Demonstration On | `45206:14358` |
| Department | `45206:14305` |
| Developer Resources | `45206:14200` |
| Device Rotate | `45206:14118` |
| Dial 10 | `45206:14569` |
| Dial 20 | `45206:14568` |
| Digits 123 | `45206:14507` |
| Digits 24 | `45206:14460` |
| Discount | `45206:14635` |
| Dislike | `45206:14311` |
| Distribution | `45206:14093` |
| Do not use captcha | `45206:14584` |
| Dots | `45206:14458` |
| Duplicate | `45206:14117` |
| Employee | `45206:14446` |
| Empty battery | `45206:14098` |
| Excel | `45206:14653` |
| Expert mode | `45206:14332` |
| Export | `45206:14655` |
| Face ident | `45206:14542` |
| Feedback | `45206:14228` |
| Feedback form | `45206:14474` |
| Fingerprint | `45206:14543` |
| Fire | `45206:14114` |
| Flower | `45206:14432` |
| Form | `45206:14401` |
| Forward | `45206:14278` |
| Forward 10 | `45206:14345` |
| Forward 15 | `45206:14312` |
| Frame create | `45206:14557` |
| Freelance | `45206:14158` |
| Full Battery | `45206:14095` |
| Gift | `45206:14222` |
| Glasses | `45206:14370` |
| Globe extranet | `45206:14338` |
| Google maps | `45206:14166` |
| Graduation cap | `45206:14204` |
| Hamburger menu | `45206:14344` |
| Handshake | `45206:14160` |
| Handshake send | `45206:14625` |
| Headlines | `45206:14646` |
| Headlines H1 | `45206:14661` |
| Headlines H2 | `45206:14657` |
| Headlines H3 | `45206:14658` |
| Headlines H4 | `45206:14659` |
| Headlines H5 | `45206:14660` |
| Hide 1 | `45206:14601` |
| Hide 2 | `45206:14603` |
| High temperature | `45206:14170` |
| Hourglass | `45206:14217` |
| Idea Lamp | `45206:14207` |
| Image | `45206:14221` |
| Image small | `45206:14617` |
| Import | `45206:14654` |
| Intranet | `45206:14340` |
| Inventory Management | `45206:14120` |
| Italic | `45206:14250` |
| Knowledge base | `45206:14205` |
| Layers | `45206:14219` |
| Left right | `45206:14280` |
| Like | `45206:14133` |
| List Viewer | `45206:14526` |
| Location | `45206:14183` |
| Log in | `45206:14276` |
| Log out | `45206:14277` |
| Logo Android | `45206:14501` |
| Logo Apple | `45206:14500` |
| MCP | `45206:14556` |
| Map | `45206:14142` |
| Market | `45206:14372` |
| Marketing | `45206:14440` |
| Martini glass | `45206:14430` |
| Maximize | `45206:14356` |
| Maximize 2 | `45206:14357` |
| Meeting point | `45206:14365` |
| Mention | `45206:14113` |
| Merge | `45206:14560` |
| Minimize | `45206:14272` |
| Minimize 2 | `45206:14273` |
| Moderator | `45206:14197` |
| Moon | `45206:14154` |
| Multi page form | `45206:14475` |
| Multichoice Off | `45206:14424` |
| Multichoice On | `45206:14423` |
| Music | `45206:14178` |
| My plan | `45206:14195` |
| Newsfeed | `45206:14211` |
| Next | `45206:14151` |
| No Compass | `45206:14532` |
| No screenshot | `45206:14463` |
| No wifi | `45206:14320` |
| Note | `45206:14394` |
| Numbered List | `45206:14255` |
| Observer | `45206:14131` |
| Online Booking | `45206:14385` |
| Online events | `45206:14484` |
| Open channels | `45206:14304` |
| Open new | `45206:14509` |
| Open sequence | `45206:14607` |
| Package | `45206:14128` |
| Package cancel | `45206:14614` |
| Package receive | `45206:14613` |
| Palette | `45206:14286` |
| Partner nfc | `45206:14359` |
| Parts Record | `45206:14579` |
| Path | `45206:14143` |
| Payment | `45206:14126` |
| Payment and delivery | `45206:14483` |
| Payment terminal | `45206:14122` |
| Pitch zoom | `45206:14400` |
| Planning | `45206:14388` |
| Planning 2 | `45206:14582` |
| Point left | `45206:14259` |
| Point right | `45206:14260` |
| Poll | `45206:14437` |
| Previous | `45206:14152` |
| Printer | `45206:14141` |
| Product | `45206:14163` |
| Products cube | `45206:14476` |
| Products payment | `45206:14477` |
| Products photo | `45206:14478` |
| Products shirt | `45206:14479` |
| Prompt Library | `45206:14380` |
| Prompt var | `45206:14419` |
| QR code | `45206:14136` |
| Quantity | `45206:14327` |
| Question | `45206:14161` |
| Question L | `45206:14384` |
| Quote | `45206:14146` |
| Receipt | `45206:14465` |
| Receipt note | `45206:14466` |
| Recent cards | `45379:12238` |
| Recent items | `45206:14638` |
| Record on | `45206:14495` |
| Record on 2 | `45206:14499` |
| Record video | `45206:14235` |
| Redirect | `45206:14585` |
| Redo | `45206:14267` |
| Registration on site | `45206:14485` |
| Repeat | `45206:14269` |
| Repeat cycle | `45206:14270` |
| Reply | `45206:14303` |
| Reply to all | `45206:14525` |
| Resume | `45206:14285` |
| Reveal 1 | `45206:14600` |
| Reveal 2 | `45206:14602` |
| Roles library | `45206:14439` |
| Running man | `45206:14194` |
| SMS | `45206:14229` |
| SSO | `45206:14564` |
| Save template | `45206:14637` |
| Screen | `45206:14094` |
| Screen selected | `45206:14530` |
| Seen items | `45206:14576` |
| Send | `45206:14236` |
| Send via Bitrix | `45206:14593` |
| Sended | `45206:14308` |
| Service | `45206:14448` |
| Services | `45206:14206` |
| Set columns | `45206:14364` |
| Shop order | `45206:14577` |
| Shuffle | `45206:14268` |
| Sick | `45206:14301` |
| Sigma summ | `45206:14149` |
| Size W L | `45206:14545` |
| Slash | `45206:14633` |
| Smart activity | `45206:14317` |
| Sort activity | `45206:14132` |
| Speaker | `45206:14208` |
| Speed 0_5 | `45206:14349` |
| Speed 0_7 | `45206:14347` |
| Speed 1 | `45206:14351` |
| Speed 1_2 | `45206:14348` |
| Speed 1_5 | `45206:14350` |
| Speed 1_7 | `45206:14352` |
| Speed 2 | `45206:14353` |
| Speed meter | `45206:14346` |
| Spoiler | `45206:14590` |
| Sticker | `45206:14537` |
| Stock | `45206:14121` |
| Storage | `45206:14089` |
| Strikethrough | `45206:14252` |
| Structure horizontal | `45206:14325` |
| Structure vertical | `45206:14324` |
| Subscript | `45206:14648` |
| Subscription | `45206:14447` |
| Suitcase | `45206:14360` |
| Sun | `45206:14153` |
| Switch camera | `45206:14333` |
| Switch device | `45206:14649` |
| Switcher | `45206:14328` |
| Table | `45206:14567` |
| Tariff | `45206:14620` |
| Tariff scaner | `45206:14398` |
| Telegram | `45206:14237` |
| Telephony | `45206:14232` |
| Text | `45206:14263` |
| Text format Bottom | `45206:14502` |
| Text format Cancel | `45206:14504` |
| Text format Top | `45206:14503` |
| Text format Top left | `45206:14505` |
| Text format Top right | `45206:14506` |
| Text format reset | `45206:14591` |
| Theme | `45206:14220` |
| Thread | `45206:14326` |
| Thread single | `45206:14330` |
| Three squares | `45206:14434` |
| Topic | `45206:14397` |
| Transcription | `45206:14515` |
| Translation | `45206:14258` |
| UNC 1 | `45206:14540` |
| Underline | `45206:14251` |
| Undo | `45206:14266` |
| Universal access | `45206:14566` |
| Vacation | `45206:14169` |
| Verification | `45206:14457` |
| Vibecode catalog | `45397:12230` |
| Video Record | `45206:14521` |
| Video Record 2 | `45206:14522` |
| Video Record 3 | `45206:14523` |
| Video Record 4 | `45206:14527` |
| Video Record 5 | `45206:14528` |
| Virtual server | `45206:14452` |
| Virtual storage | `45206:14451` |
| Visited items | `45206:14575` |
| Walking man | `45206:14193` |
| Watermark | `45206:14464` |
| Webhook | `45206:14583` |
| WhatsApp | `45206:14238` |
| Wifi | `45206:14319` |
| Wiki | `45206:14461` |
| Window ring | `45206:14110` |
| Yandex maps | `45206:14165` |
| Zoom in | `45206:14283` |
| Zoom out | `45206:14284` |
