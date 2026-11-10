<!-- Выдержки первоисточников для карточки normapi-einvoices. Фрагменты дословные. Файл создаёт tools/wiki.py evidence; не править вручную. -->

## [1] инвентарь сессии: запись позиции (ListConnectors, ListSkills, системные уведомления)
- Снимок: 2026-11-10
- Фрагмент:

````text
    {"id": "normapi-einvoices", "kind": "connector", "cluster": "14-accounting-einvoice", "group": "электронные счета", "name": "NormAPI – German e-invoices (XRechnung, ZUGFeRD)", "vendor": "NormAPI", "state": "connected", "platform_description": "", "source": "ListConnectors"},
````

## [2] список инструментов, загруженных в сессию
- Снимок: 2026-11-10
- Фрагмент:

````text
[normapi-einvoices] инструменты (префикс mcp__NormAPI_German_e-invoices_XRechnung_ZUGFeRD__): explain_rule, generate_invoice, parse_invoice, validate_invoice
````

## [3] системные инструкции MCP-сервера (сессия 2026-11-10)
- Снимок: 2026-11-10
- Фрагмент:

````text
### NormAPI
NormAPI checks, produces and reads German e-invoices (XRechnung in UBL or CII, ZUGFeRD/Factur-X PDF) against the official KoSIT rule set, and states the rule set version with every result.
validate_invoice needs no account. Its verdict is `acceptable`; every business-rule finding carries a plain-language explanation (meaning, cause, fix) — quote the fix rather than paraphrasing the rule text.
parse_invoice needs no account either. It reads a received invoice into data: `invoice` in the shape generate_invoice takes, `stated` with the totals as the document wrote them, and `notMapped` naming every value it did not carry. Answer questions about an invoice from this data rather than from the raw XML, and say so when notMapped lists something relevant.
generate_invoice turns invoice data into a document that passed validation before it was returned. It needs the user's NormAPI account and counts against their monthly allowance, so build the invoice from data the user gave you and do not retry blindly: a refusal names the rules the data breaks.
Pick its profile by the recipient: xrechnung (the default) for a public-sector buyer, en16931 for a business, which then needs no Leitweg-ID, contact person or electronic addresses.
When the user's account has a letterhead (uploaded at normapi.com/konto/briefkopf), zugferd PDFs are printed on it automatically; pass letterhead "none" only when the user asks for NormAPI's standard layout.
explain_rule explains a rule code (e.g. BR-DE-15) the user already has.
Invoices are processed in memory and never stored. This is technical validation, not tax or legal advice.
````
