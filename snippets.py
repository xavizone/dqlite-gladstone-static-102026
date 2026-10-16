"""Prompts, SQL, Snowsight routes, use cases and references copied from the live guide
(schema shown as RIVERSIDE_NIELS). Generated from dq-lab-lite/workshop_guide - do not hand-edit."""
import links as L

PAGES = {
  'admin_setup': {
    'prompts': [],
    'fallbacks': [],
    'snowsight': [],
    'checkpoints': [],
    'explanations': [],
    'examples': [
  {
    "title": "Repeatable training environment",
    "body": "The same script stands up a sandbox for new data engineers or for operator-facing demos."
  },
  {
    "title": "Template for operator onboarding",
    "body": "`ADD_ATTENDEE` is a small model of onboarding: clone, own, register - the checks then attach by prompt, by script or by DCM (Bonus B3)."
  }
],
    'refs': {'Docs': [L.DQ_SQL, L.DQ_NOTIFY, L.ALERTS, L.RES_MON, L.DT_OVERVIEW, L.TASKS, L.COCO]},
  },
  'admin_teardown': {
    'prompts': [],
    'fallbacks': [],
    'snowsight': [],
    'checkpoints': [],
    'explanations': [],
    'examples': [
  {
    "title": "Clean sandboxes",
    "body": "One teardown script keeps training accounts free of stray roles, warehouses and cost."
  },
  {
    "title": "Erasure thinking",
    "body": "Dropping data still leaves Time Travel and Fail-safe copies - the same point as Bonus B2's GDPR exercise."
  }
],
    'refs': {'Docs': [L.TIME_TRAVEL, L.FAILSAFE, L.RES_MON]},
  },
  'agenda': {
    'prompts': [],
    'fallbacks': [],
    'snowsight': [],
    'checkpoints': [],
    'explanations': [],
    'examples': [
  {
    "title": "A real triage rota",
    "body": "These are the failure modes of any CDC pipeline: duplicate, late, wrong sign, semantic drift, missing volume. Each one maps to one check."
  },
  {
    "title": "Operator-facing SLAs",
    "body": "Freshness and completeness expectations become the evidence behind \"Nova data is never more than N minutes old\"."
  }
],
    'refs': {'Quickstarts': [L.QS_DQ, L.QS_DT], 'Docs': [L.DQ_EXPECT, L.ALERTS, L.TASKS]},
  },
  'availability': {
    'prompts': [],
    'fallbacks': [],
    'snowsight': [],
    'checkpoints': [],
    'explanations': [],
    'examples': [
  {
    "title": "Pre-flight before the workshop",
    "body": "The admin runs the checks above in `GLADSTONESOFTWARE` the day before and records any gaps on this page."
  },
  {
    "title": "Planning Nova features",
    "body": "Treat preview or upcoming items as roadmap conversations, and design Nova so the core path uses GA features."
  }
],
    'refs': {'Docs': [L.DQ_INTRO, L.DQ_ANOMALY, L.DCM, L.CROSS_REGION, L.AGENTS]},
  },
  'before_you_start': {
    'prompts': [],
    'fallbacks': [],
    'snowsight': [],
    'checkpoints': [],
    'explanations': [],
    'examples': [
  {
    "title": "Onboarding a new operator team",
    "body": "The same checklist (login, CoCo, role, a test prompt) works when a new operator's support engineers get access to their `RIVERSIDE_*` database."
  },
  {
    "title": "Safe changes in a shared account",
    "body": "\"Read the SQL, then approve\" is the habit that matters in production, where one account serves many operators."
  }
],
    'refs': {'Quickstarts': [L.QS_COCO_DESKTOP, L.QS_COCO_CLI], 'Docs': [L.COCO, L.COCO_CLI]},
  },
  'bonus_b1': {
    'prompts': [
  {
    "id": "Prompt B1.1",
    "title": "What does my operator cost?",
    "text": "Show what my operator pipeline in GLADSTONE_DQ_LITE.RIVERSIDE_NIELS costs: data quality (serverless DMF credits from SNOWFLAKE.ACCOUNT_USAGE.DATA_QUALITY_MONITORING_USAGE_HISTORY, filtered to my database and schema), and dynamic table refresh counts and duration from INFORMATION_SCHEMA. Explain which costs land on DQ_LITE_WH and which are serverless, and note any ACCOUNT_USAGE latency."
  },
  {
    "id": "Prompt B1.2",
    "title": "Tag my operator for cost attribution",
    "text": "Tag schema GLADSTONE_DQ_LITE.RIVERSIDE_NIELS with GLADSTONE_DQ_LITE.FINOPS.OPERATOR_ID = 'RIVERSIDE_NIELS' and GLADSTONE_DQ_LITE.FINOPS.COST_CENTRE = 'nova'. Explain how objects inside the schema inherit the tags and how long until tag-based cost views reflect them."
  },
  {
    "id": "Prompt B1.3",
    "title": "A budget for my operator",
    "text": "Create a custom budget GLADSTONE_DQ_LITE.FINOPS.RIVERSIDE_NIELS_BUDGET with a spending limit of 5 credits per month. Add my schema GLADSTONE_DQ_LITE.RIVERSIDE_NIELS to it as a resource. Send email notifications through integration DQ_LITE_EMAIL_INT to my verified email address, at 80% of projected spend. Then list the budget's linked resources and show how to query its spending history."
  },
  {
    "id": "Prompt B1.4",
    "title": "Draft a resource monitor (admin applies it)",
    "text": "Draft, but do not run, a resource monitor for a Nova operator warehouse NOVA_WH_NIELS: 30 credits per month, notify at 75% and 90%, suspend at 100%. Explain why a resource monitor and a budget are both useful, what each one covers (warehouses vs serverless), and why only ACCOUNTADMIN can create the monitor."
  }
],
    'fallbacks': [
  "ALTER SCHEMA GLADSTONE_DQ_LITE.RIVERSIDE_NIELS SET TAG\n  GLADSTONE_DQ_LITE.FINOPS.OPERATOR_ID = 'RIVERSIDE_NIELS',\n  GLADSTONE_DQ_LITE.FINOPS.COST_CENTRE = 'nova';\nUSE SCHEMA GLADSTONE_DQ_LITE.FINOPS;\nCREATE SNOWFLAKE.CORE.BUDGET RIVERSIDE_NIELS_BUDGET();\nCALL RIVERSIDE_NIELS_BUDGET!SET_SPENDING_LIMIT(5);\nCALL RIVERSIDE_NIELS_BUDGET!ADD_RESOURCE(SYSTEM$REFERENCE('SCHEMA', 'GLADSTONE_DQ_LITE.RIVERSIDE_NIELS', 'SESSION', 'applybudget'));\nCALL RIVERSIDE_NIELS_BUDGET!SET_EMAIL_NOTIFICATIONS('DQ_LITE_EMAIL_INT', '<your verified email>');\nCALL RIVERSIDE_NIELS_BUDGET!SET_NOTIFICATION_THRESHOLD(80);\nCALL RIVERSIDE_NIELS_BUDGET!GET_LINKED_RESOURCES();"
],
    'snowsight': [
  {
    "after": "Prompt B1.1",
    "steps": [
      "**Admin \u00bb Cost management \u00bb Consumption**: filter by warehouse `DQ_LITE_WH` and service type.",
      "**Admin \u00bb Cost management \u00bb Consumption** \u00bb service type *Data quality monitoring* for serverless DMF credits."
    ],
    "sql": None
  },
  {
    "after": "Prompt B1.2",
    "steps": [
      "**Catalog \u00bb Database Explorer** \u00bb `RIVERSIDE_NIELS` \u00bb **\u2026** \u00bb **Edit tags** \u00bb add `FINOPS.OPERATOR_ID` and `FINOPS.COST_CENTRE`."
    ],
    "sql": None
  },
  {
    "after": "Prompt B1.3",
    "steps": [
      "**Admin \u00bb Cost management \u00bb Budgets \u00bb + Budget**.",
      "Location `GLADSTONE_DQ_LITE.FINOPS`, name `RIVERSIDE_NIELS_BUDGET`, 5 credits, threshold 80%, your email.",
      "**Budget scope** \u00bb Resources \u00bb Schemas \u00bb `RIVERSIDE_NIELS`. (Or Tags \u00bb `COST_CENTRE = nova` for every operator in a tier.)"
    ],
    "sql": None
  },
  {
    "after": "Prompt B1.4",
    "steps": [
      "**Admin \u00bb Cost management \u00bb Resource monitors \u00bb + Resource monitor** (ACCOUNTADMIN)."
    ],
    "sql": None
  }
],
    'checkpoints': [
  {
    "after": "Prompt B1.3",
    "text": "`GET_LINKED_RESOURCES` lists your schema. Spending history fills after the budget's background refresh (can take hours).",
    "sql": None
  }
],
    'explanations': [
  {
    "title": "Budgets vs resource monitors",
    "body": "\n| | Budget | Resource monitor |\n|---|---|---|\n| Covers | Warehouses **and serverless** (DMFs, serverless tasks, DT background work) | Warehouses only |\n| Action | Notify (projected overspend) | Notify, **suspend** |\n| Scope | Objects, schemas, databases, **tags** | One or more warehouses / account |\n| Who creates | Any role with BUDGET_CREATOR + CREATE BUDGET | ACCOUNTADMIN |\n\nAt Gladstone scale: a **tag-based budget per tier** (e.g. `COST_CENTRE = nova`) plus a **resource monitor per shared warehouse**.\n"
  }
],
    'examples': [
  {
    "title": "Usage and overage warnings per operator",
    "body": "A budget per operator (or per tag) emails before an operator's Nova or DQ usage runs over its contract."
  },
  {
    "title": "Showback to product lines",
    "body": "`COST_CENTRE` tags split Snowflake spend between Nova, reporting and platform without separate accounts."
  },
  {
    "title": "Hard stop on runaway sync",
    "body": "A resource monitor on the Bifrost/merge warehouse suspends it if a replay loop burns credits overnight."
  },
  {
    "title": "Cost of data quality itself",
    "body": "`DATA_QUALITY_MONITORING_USAGE_HISTORY` shows what checks cost per operator - and whether a schedule should move to TRIGGER_ON_CHANGES."
  }
],
    'header': {
  "label": "Bonus B1",
  "title": "Budgets and resource monitors",
  "duration": "20 min, self-paced",
  "building": "Cost attribution, a budget per operator, and a hard cap"
},
    'what': "See what your operator pipeline costs, tag it for cost attribution, put a monthly **budget** on it with an alert, and draft a **resource monitor** the admin would apply.",
    'why': "Data quality and Nova run per operator. Without per-operator cost visibility, overages show up at month-end. Budgets warn early (and cover serverless DMFs); resource monitors hard-stop warehouses.",
    'fallback_after': [
  "Prompt B1.4"
],
    'refs': {'Quickstarts': [L.QS_COST, L.QS_QUERY_COST, L.WAF_COST], 'Docs': [L.BUDGETS, L.BUDGETS_CUSTOM, L.BUDGETS_TUT, L.RES_MON, L.COST_ATTR, L.DQ_USAGE]},
  },
  'bonus_b2': {
    'prompts': [
  {
    "id": "Prompt B2.1",
    "title": "Classify",
    "text": "Classify GLADSTONE_DQ_LITE.RIVERSIDE_NIELS.MEMBERS__MEMBER for personal and sensitive data. List each column with its suggested semantic and privacy category and confidence. Do not apply any tags yet. Which column would be special-category data under UK GDPR?"
  },
  {
    "id": "Prompt B2.2",
    "title": "Tag-based masking",
    "text": "In GLADSTONE_DQ_LITE.RIVERSIDE_NIELS, create a tag PII_TYPE with allowed values email, phone, dob, name, postcode, health. Create a string masking policy that shows the real value only when role DQ_LITE_PII_READER is in the session (keep the email domain visible), and a date masking policy that keeps only the birth year. Attach both policies to the PII_TYPE tag, then tag the email, phone, date_of_birth, first_name, last_name, postcode and health_notes columns of MEMBERS__MEMBER."
  },
  {
    "id": "Prompt B2.3",
    "title": "Row access per site",
    "text": "Create a row access policy RAP_SITE in GLADSTONE_DQ_LITE.RIVERSIDE_NIELS: roles DQ_LITE_ATTENDEE and DQ_LITE_PII_READER see every row, role DQ_LITE_SITE_VIEWER sees only members whose home_site_id = 'S01', everyone else sees nothing. Add it to MEMBERS__MEMBER on home_site_id. Grant SELECT on MEMBERS__MEMBER to roles DQ_LITE_PII_READER and DQ_LITE_SITE_VIEWER.\nThen prove it: query a few member rows with health notes as my role (secondary roles off), as DQ_LITE_PII_READER and as DQ_LITE_SITE_VIEWER (with secondary roles off), and count members per home_site_id. Explain what each role saw."
  },
  {
    "id": "Prompt B2.4",
    "title": "Does Nova expose personal data? Who read it?",
    "text": "Check whether semantic view GLADSTONE_DQ_LITE.RIVERSIDE_NIELS.SV_RIVERSIDE_KPIS exposes any personal-data columns from MEMBERS__MEMBER. Then show who queried MEMBERS__MEMBER in the last day from SNOWFLAKE.ACCOUNT_USAGE.ACCESS_HISTORY (note its latency)."
  },
  {
    "id": "Prompt B2.5",
    "title": "Record GDPR categories, lawful basis and retention",
    "text": "Using tags in GLADSTONE_DQ_LITE.GOVERNANCE (GDPR_CATEGORY, LAWFUL_BASIS, RETENTION_DAYS), tag the columns of GLADSTONE_DQ_LITE.RIVERSIDE_NIELS.MEMBERS__MEMBER and SYSTEM__PAYMENT: identifiers and contact details under contract (730 days), health_notes as special_category under explicit_consent (30 days), marketing_consent under consent, payment amount as financial under legal_obligation (2190 days). Then list every tagged column as a simple record of processing."
  },
  {
    "id": "Prompt B2.6",
    "title": "Subject access request",
    "text": "Create a stored procedure GLADSTONE_DQ_LITE.RIVERSIDE_NIELS.SAR_EXPORT(member_id) with caller's rights that finds every table in RIVERSIDE_NIELS with a MEMBER_ID column, collects that member's rows into one JSON document grouped by table, and logs the request in GLADSTONE_DQ_LITE.GOVERNANCE.GDPR_REQUESTS (request_type 'SAR', completed now). Run it for member M-01043 with role DQ_LITE_PII_READER as a secondary role so masking lets the real data through, then turn secondary roles off again."
  },
  {
    "id": "Prompt B2.7",
    "title": "Erasure you can prove",
    "text": "Log an ERASURE request for member M-01042 in GLADSTONE_DQ_LITE.GOVERNANCE.GDPR_REQUESTS. Create a procedure GLADSTONE_DQ_LITE.RIVERSIDE_NIELS.ERASE_MEMBER(member_id) that: replaces member_id with a salted SHA2 token and nulls contact, date of birth, postcode and health notes in MEMBERS__MEMBER; pseudonymises member_id in MEMBERS__MEMBERSHIP and SYSTEM__PAYMENT (keep payments for tax); deletes the member's SYSTEM__BOOKING and SYSTEM__ATTENDANCE rows; and marks the request completed with row counts as evidence. Run it for M-01042."
  },
  {
    "id": "Prompt B2.8",
    "title": "A data quality check that proves it",
    "text": "Attach GLADSTONE_DQ_LITE.DQ_COMMON.ERASED_MEMBERS_STILL_PRESENT to MEMBERS__MEMBER and SYSTEM__PAYMENT in GLADSTONE_DQ_LITE.RIVERSIDE_NIELS, using GLADSTONE_DQ_LITE.GOVERNANCE.GDPR_REQUESTS(member_id, request_type, completed_at) as the second table, with expectation erasure_complete (value = 0). Evaluate it now."
  },
  {
    "id": "Prompt B2.9",
    "title": "Copies that survive",
    "text": "Is member M-01042 still recoverable anywhere? Check Time Travel on GLADSTONE_DQ_LITE.RIVERSIDE_NIELS.MEMBERS__MEMBER (query the table as it was 2 minutes ago), show the table's retention period, explain Fail-safe, and explain the risk from the template schema this operator was cloned from. Set MEMBERS__MEMBER retention to 1 day. Finally, show the account's CORTEX_ENABLED_CROSS_REGION setting and what it means for UK data residency with Nova."
  }
],
    'fallbacks': [
  "-- See sql/bonus/B2_answer_key.sql for the full Part A + Part B answer key.\nUSE SECONDARY ROLES DQ_LITE_PII_READER;\nCALL GLADSTONE_DQ_LITE.RIVERSIDE_NIELS.SAR_EXPORT('M-01043');\nUSE SECONDARY ROLES NONE;\nCALL GLADSTONE_DQ_LITE.RIVERSIDE_NIELS.ERASE_MEMBER('M-01042');\nSELECT COUNT(*) FROM GLADSTONE_DQ_LITE.RIVERSIDE_NIELS.MEMBERS__MEMBER AT(OFFSET => -120) WHERE member_id = 'M-01042';"
],
    'snowsight': [
  {
    "after": "Prompt B2.1",
    "steps": [
      "**Governance & security \u00bb Trust Center \u00bb Data security \u00bb Sensitive data** (or open the table \u00bb **\u2026** \u00bb **Classify data**).",
      "Review suggestions per column; apply or reject."
    ],
    "sql": "CALL SYSTEM$CLASSIFY('GLADSTONE_DQ_LITE.RIVERSIDE_NIELS.MEMBERS__MEMBER', NULL);"
  },
  {
    "after": "Prompt B2.2",
    "steps": [
      "**Governance & security \u00bb Tags & policies \u00bb Policies \u00bb + Policy** \u00bb Masking policy (string) and (date).",
      "**Tags \u00bb + Tag** `PII_TYPE` \u00bb **Policies** \u00bb attach both masking policies.",
      "Open `MEMBERS__MEMBER` \u00bb **Columns** \u00bb set `PII_TYPE` on each personal column."
    ],
    "sql": None
  },
  {
    "after": "Prompt B2.3",
    "steps": [
      "**Governance & security \u00bb Tags & policies \u00bb Policies \u00bb + Policy** \u00bb Row access policy.",
      "Open `MEMBERS__MEMBER` \u00bb **Policies** \u00bb add row access policy on `home_site_id`.",
      "Switch role in the worksheet's role picker to compare results."
    ],
    "sql": None
  },
  {
    "after": "Prompt B2.4",
    "steps": [
      "Open `SV_RIVERSIDE_KPIS` \u00bb **Definition**.",
      "**Monitoring \u00bb Query history** filtered by object, or query `ACCESS_HISTORY`."
    ],
    "sql": None
  },
  {
    "after": "Prompt B2.5",
    "steps": [
      "Open each table \u00bb **Columns** \u00bb **Edit tags** \u00bb `GOVERNANCE.GDPR_CATEGORY`, `LAWFUL_BASIS`, `RETENTION_DAYS`."
    ],
    "sql": None
  },
  {
    "after": "Prompt B2.6",
    "steps": [
      "Create the procedure in a worksheet, then run `USE SECONDARY ROLES DQ_LITE_PII_READER; CALL SAR_EXPORT('M-01043');`."
    ],
    "sql": None
  }
],
    'checkpoints': [
  {
    "after": "Prompt B2.3",
    "text": "Your role sees `*** MASKED ***`; `DQ_LITE_PII_READER` sees real values; `DQ_LITE_SITE_VIEWER` sees only site **S01**, with personal data masked.",
    "sql": None
  },
  {
    "after": "Prompt B2.8",
    "text": "`erasure_complete` passes (0) on both tables. Try it: comment out the payment update in ERASE_MEMBER, erase another member, and watch the check fail.",
    "sql": None
  }
],
    'explanations': [
  {
    "title": "Why tag-based masking at Gladstone scale",
    "body": "\nA masking policy attached to a **tag** protects every column that carries the tag - in every operator database. Classification\n(or a classification profile with a tag map) applies the tag; the policy follows automatically. One policy, hundreds of operator databases.\n\n**Lab note:** attendees have `APPLY MASKING POLICY` and `APPLY ROW ACCESS POLICY` on the account so each can build their own.\nIn production give these to a central governance role only.\n"
  },
  {
    "title": "Why caller's rights and a secondary role?",
    "body": "\nAn owner's-rights procedure runs as your operator role, so the masking policy masks the export - a useless SAR. With\n**caller's rights** and `DQ_LITE_PII_READER` active as a **secondary role**, `IS_ROLE_IN_SESSION` lets real values through,\nand only people with the privacy role can produce an unmasked SAR.\n"
  },
  {
    "title": "What the lab shows",
    "body": "\n- **Time Travel** still returns the pre-erasure row until retention passes; **Fail-safe** keeps it 7 more days (permanent tables), recoverable only by Snowflake.\n- The **template** (`TEMPLATE`) still holds M-01042 - just like dev/test clones of a production operator. Erasure has to cover clones.\n- Shorter retention on personal-data tables reduces this window; transient tables have no Fail-safe.\n- `CORTEX_ENABLED_CROSS_REGION` controls whether Cortex can process prompts outside the account's region. For UK-only processing, the admin restricts it.\n"
  }
],
    'examples': [
  {
    "title": "Health notes never reach Nova",
    "body": "Tagged as `health`, masked for every role except a privacy role, and absent from the semantic view."
  },
  {
    "title": "SARs for any operator",
    "body": "One SAR procedure pattern, deployed to every operator database, answers within the one-month deadline with an audit trail."
  },
  {
    "title": "Erasure with evidence",
    "body": "The erasure check turns \"we deleted it\" into a scheduled, provable result per operator."
  },
  {
    "title": "Site and region access",
    "body": "The same row access pattern scopes site managers, regional managers or a support team to the rows they need, from one policy."
  }
],
    'header': {
  "label": "Bonus B2",
  "title": "Data governance and GDPR",
  "duration": "40 min, self-paced",
  "building": "Classification, masking, row access, then SAR, erasure and retention"
},
    'what': "Run the three GDPR workflows Gladstone faces as a processor for leisure operators: record **why** you hold each field, answer a **subject access request**, and carry out an **erasure** you can prove.",
    'why': "Members ask operators for their data and for deletion. With one database per operator, Gladstone needs a repeatable, auditable way to do this in Snowflake - including the copies (Time Travel, clones) that survive a DELETE.",
    'fallback_after': [
  "Prompt B2.9"
],
    'refs': {'Quickstarts': [L.QS_HORIZON, L.QS_GOV_ADV, L.WAF_SEC], 'Docs': [L.CLASSIFY, L.CLASSIFY_SP, L.TAG_MASK, L.RAP, L.ACCESS_HIST, L.TIME_TRAVEL, L.FAILSAFE, L.CROSS_REGION, L.AI_REDACT, L.TRUST_CENTER], 'UK GDPR guidance': [L.ICO_SAR, L.ICO_ERASURE, L.ICO_STORAGE, L.ICO_SPECIAL, L.ICO_BREACH]},
  },
  'bonus_b3': {
    'prompts': [
  {
    "id": "Prompt B3.1",
    "title": "Create the project",
    "text": "Create a DCM project for my operator pipeline.\n- Project identifier: GLADSTONE_DQ_LITE.RIVERSIDE_NIELS_DCM.OPERATOR_PIPELINE, owner role DQ_LITE_ATTENDEE, local folder ./operator_pipeline\n- manifest v2 with a target NIELS and templating variables db, schema (RIVERSIDE_NIELS_DCM), operator_id ('RIVERSIDE'), wh (DQ_LITE_WH), dq_schedule ('5 MINUTE'), reporting_lag ('1 minute')\n- Bronze tables MEMBERS__MEMBER and SYSTEM__PAYMENT (same columns as in GLADSTONE_DQ_LITE.RIVERSIDE_NIELS) with change tracking and DATA_METRIC_SCHEDULE\n- dynamic tables REPORTING__DAILY_REVENUE and REPORTING__ACTIVE_MEMBERS, incremental\n- expectations: no duplicate member_id, GLADSTONE_DQ_LITE.DQ_COMMON.ACTIVE_BUT_LEFT, no negative amounts, net_revenue never null\nRegister the project in Snowflake and validate it. Don't deploy yet."
  },
  {
    "id": "Prompt B3.2",
    "title": "Plan, then deploy",
    "text": "Run a plan for target NIELS and summarise what it will create, alter or drop. Explain any entry you weren't expecting. If it looks right, deploy with the alias first-deploy."
  },
  {
    "id": "Prompt B3.3",
    "title": "Test, break, test again",
    "text": "Run snow dcm test for target NIELS. Then insert two rows with the same member_id into GLADSTONE_DQ_LITE.RIVERSIDE_NIELS_DCM.MEMBERS__MEMBER and run the test again. What exit code does the CLI return, and why does that matter for CI?"
  },
  {
    "id": "Prompt B3.4",
    "title": "Change and onboard",
    "text": "1. Change reporting_lag to '5 minutes' and plan again - show me that only the two dynamic tables change.\n2. Show how I'd add a second target ACME (schema RIVERSIDE_ACME_DCM): what to add to manifest.yml and which commands to run.\n3. Write a GitHub Actions workflow that runs plan + test on pull requests and deploy + test on main, using the Snowflake CLI."
  }
],
    'fallbacks': [],
    'snowsight': [
  {
    "after": "Prompt B3.1",
    "steps": [
      "**Projects \u00bb Workspaces** \u00bb **+ Add new \u00bb DCM project** \u00bb choose `GLADSTONE_DQ_LITE.RIVERSIDE_NIELS_DCM`.",
      "Add the definition files (see the answer key below) to the workspace."
    ],
    "sql": None
  },
  {
    "after": "Prompt B3.2",
    "steps": [
      "In the DCM workspace \u00bb **Plan** \u00bb review the change set \u00bb **Deploy**."
    ],
    "sql": None
  }
],
    'checkpoints': [
  {
    "after": "Prompt B3.2",
    "text": "Plan shows 4 creates (2 tables, 2 dynamic tables) and an `ALTER ROLE` that only records ownership of the new objects; deploy succeeds.",
    "sql": None
  },
  {
    "after": "Prompt B3.3",
    "text": "First run: 4/4 pass. After the duplicate: `NO_DUPLICATE_MEMBERS` fails and the CLI exits with **1** - a failed pipeline step in CI.",
    "sql": None
  }
],
    'explanations': [
  {
    "title": "Why DCM for operator databases",
    "body": "\n- **Declarative**: definitions describe the end state; `plan` shows the diff before anything changes.\n- **Templated targets**: one set of definitions, one target per operator (or per tier), different variables.\n- **Data quality ships with the pipeline**: `ATTACH DATA METRIC FUNCTION ... EXPECTATION` lives next to the table it protects.\n- **Test as a gate**: `snow dcm test` exits non-zero on a failed expectation.\n- **Note**: a DCM project can't define its own parent database or schema - they must exist (that's why the admin pre-creates `RIVERSIDE_<NAME>_DCM`).\n"
  }
],
    'examples': [
  {
    "title": "Operator onboarding as a pull request",
    "body": "A new operator is a new target in the manifest; review the plan in the PR, merge to deploy."
  },
  {
    "title": "Same checks everywhere",
    "body": "A new expectation added once reaches every operator on the next deploy - no drift between operator databases."
  },
  {
    "title": "Safer REPORTING changes",
    "body": "`plan` shows whether a change alters or recreates a dynamic table before it touches production."
  },
  {
    "title": "Promotion DEV to PROD",
    "body": "Separate targets and accounts (dev, reporting, production) with the same definitions."
  }
],
    'header': {
  "label": "Bonus B3",
  "title": "DevOps with DCM Projects",
  "duration": "30 min, self-paced",
  "building": "One operator's pipeline and its data quality checks as code"
},
    'what': "Turn what you built by hand into a **DCM project**: Bronze tables, REPORTING Dynamic Tables and their expectations, declared once, deployed per operator with `plan`, `deploy` and `test`.",
    'why': "Hundreds of operator databases can't be configured by hand. With DCM, onboarding operator N is a new target and a `deploy`; every operator gets the same data quality from day one, and `snow dcm test` is a CI gate.",
    'refs': {'Quickstarts': [L.QS_DCM, L.QS_DCM_PIPE, L.QS_DCM_DT, L.QS_DCM_TASKS, L.QS_DEVOPS], 'Docs': [L.DCM, L.SNOW_CLI, L.DQ_EXPECT]},
  },
  'getting_started': {
    'prompts': [],
    'fallbacks': [],
    'snowsight': [],
    'checkpoints': [],
    'explanations': [],
    'examples': [
  {
    "title": "Same pattern in production",
    "body": "A support engineer connects CoCo with a read role for one operator database and investigates one operator's database at a time."
  },
  {
    "title": "CLI for repeatable runs",
    "body": "The CoCo CLI can be scripted, so the same prompts can run across operators from a terminal or a scheduled job."
  }
],
    'refs': {'Quickstarts': [L.QS_COCO_DESKTOP, L.QS_COCO_CLI, L.QS_COCO_BP], 'Docs': [L.COCO, L.COCO_CLI]},
  },
  'home': {
    'prompts': [],
    'fallbacks': [],
    'snowsight': [],
    'checkpoints': [],
    'explanations': [],
    'examples': [
  {
    "title": "Before a Nova answer reaches an operator",
    "body": "Guards on the Bronze tables Bifrost writes to, so a bad sync stops at Silver instead of reaching the Nova Portal."
  },
  {
    "title": "Customer Success escalations",
    "body": "\"Nova gave me the wrong number\" is answered from the incident log and a five-minute CoCo root cause, often before the call."
  },
  {
    "title": "Onboarding a new operator",
    "body": "The same checks attach to the new operator database on day one, so the first Bifrost sync is already guarded."
  },
  {
    "title": "GCP-to-Azure migration",
    "body": "The same checks prove the migrated operator data matches before cut-over."
  }
],
    'refs': {'Quickstarts': [L.QS_DQ, L.QS_COCO_DESKTOP, L.QS_COCO_CLI], 'Docs': [L.DQ_INTRO, L.DT_OVERVIEW, L.SV_OVERVIEW, L.COCO]},
  },
  'install_coco': {
    'prompts': [],
    'fallbacks': [],
    'snowsight': [],
    'checkpoints': [],
    'explanations': [],
    'examples': [
  {
    "title": "Rolling CoCo out to the data team",
    "body": "The same checklist - access role, account identifier, SSO connection, a test prompt - works for every Gladstone engineer, not just the lab."
  },
  {
    "title": "IT-managed laptops",
    "body": "The Windows System installer and CoCo Desktop managed settings let IT deploy and configure CoCo centrally."
  }
],
    'refs': {'Downloads': [L.COCO_DOWNLOADS, L.SNOW_CLI_RELEASES], 'Quickstarts': [L.QS_COCO_DESKTOP, L.QS_COCO_CLI], 'Docs': [L.COCO_DESKTOP, L.COCO_DESKTOP_SETUP, L.COCO_DESKTOP_FAQ, L.COCO_CLI, L.COCO_CLI_REF, L.SNOW_CLI_INSTALL, L.CROSS_REGION, L.ACCOUNT_ID]},
  },
  'reference_coco': {
    'prompts': [],
    'fallbacks': [],
    'snowsight': [],
    'checkpoints': [],
    'explanations': [],
    'examples': [
  {
    "title": "Support playbook",
    "body": "Save these prompts as a CoCo skill so every CS and data engineer investigates an operator the same way."
  },
  {
    "title": "Scripted fleet checks",
    "body": "Run the same prompts with the CoCo CLI against several operator databases from a terminal or a scheduled job."
  }
],
    'refs': {'Quickstarts': [L.QS_COCO_BP, L.QS_COCO_DE, L.QS_COCO_CLI], 'Docs': [L.COCO, L.COCO_CLI, L.DQ_DASH]},
  },
  'scaling': {
    'prompts': [],
    'fallbacks': [],
    'snowsight': [],
    'checkpoints': [],
    'explanations': [],
    'examples': [
  {
    "title": "500 operator databases, one change",
    "body": "A new expectation added to the DCM project reaches every operator on the next deploy."
  },
  {
    "title": "Reporting account",
    "body": "Results and the fleet view can also be shared to `GLADSTONEREPORTING` for CS and leadership dashboards."
  },
  {
    "title": "Migration waves",
    "body": "Each GCP-to-Azure migration wave runs the same reconciliation checks per operator before cut-over."
  }
],
    'refs': {'Quickstarts': [L.QS_DQ, L.QS_DCM_PIPE, L.WAF_SEC], 'Docs': [L.DQ_SCHEMA, L.DQ_GROUP, L.DQ_DASH, L.DQ_USAGE, L.DCM]},
  },
  'session_01': {
    'prompts': [
  {
    "id": "Prompt 1.1",
    "title": "Map the pipeline",
    "text": "In GLADSTONE_DQ_LITE.RIVERSIDE_NIELS, explain the data pipeline end to end:\n- which tables are Bronze (MEMBERS__, SHARED__, SYSTEM__ prefixes) and what _SYNC_META__MERGE_BATCH records\n- what task TSK_BIFROST_MERGE does and how often it runs\n- what each REPORTING__ dynamic table computes, its target lag, refresh mode, and which Bronze tables feed it\n- what semantic view SV_RIVERSIDE_KPIS exposes (metrics and verified queries)\nDraw the lineage as a simple left-to-right diagram. Do not change anything."
  },
  {
    "id": "Prompt 1.2",
    "title": "Reproduce the operator's numbers",
    "text": "Using semantic view GLADSTONE_DQ_LITE.RIVERSIDE_NIELS.SV_RIVERSIDE_KPIS, answer the operator's two questions:\n1. How many active members do we have?\n2. What was net revenue for each of the last 3 days?\nShow which metric or verified query you used. If \"active members\" can be calculated two ways in this semantic view, show both numbers side by side and explain the difference. Save these as my \"clean\" baseline."
  }
],
    'fallbacks': [
  "USE SCHEMA GLADSTONE_DQ_LITE.RIVERSIDE_NIELS;\nSHOW DYNAMIC TABLES;\nSHOW TASKS;\nSELECT * FROM SEMANTIC_VIEW(SV_RIVERSIDE_KPIS METRICS am.active_members, ms.paid_members_35d);\nSELECT * FROM SEMANTIC_VIEW(SV_RIVERSIDE_KPIS DIMENSIONS rev.payment_date METRICS rev.net_revenue)\nWHERE payment_date >= CURRENT_DATE() - 2 ORDER BY payment_date;"
],
    'snowsight': [
  {
    "after": "Prompt 1.1",
    "steps": [
      "**Catalog \u00bb Database Explorer** \u00bb `GLADSTONE_DQ_LITE` \u00bb `RIVERSIDE_NIELS`.",
      "Open `REPORTING__DAILY_REVENUE` \u00bb **Lineage** tab to see its upstream Bronze table.",
      "**Transformation \u00bb Dynamic tables**: target lag, refresh mode and refresh history.",
      "**Transformation \u00bb Tasks** \u00bb `TSK_BIFROST_MERGE` \u00bb **Run history**.",
      "**AI & ML \u00bb Cortex Analyst** \u00bb `SV_RIVERSIDE_KPIS` to browse metrics and verified queries."
    ],
    "sql": "USE SCHEMA GLADSTONE_DQ_LITE.RIVERSIDE_NIELS;\nSHOW DYNAMIC TABLES;   -- target_lag, refresh_mode, scheduling_state\nSHOW TASKS;\nDESCRIBE SEMANTIC VIEW SV_RIVERSIDE_KPIS;"
  },
  {
    "after": "Prompt 1.2",
    "steps": [
      "**AI & ML \u00bb Cortex Analyst** \u00bb open `SV_RIVERSIDE_KPIS` \u00bb **Playground** and ask the same questions.",
      "Note which answer uses the verified query `vq_active_members`."
    ],
    "sql": "SELECT * FROM SEMANTIC_VIEW(GLADSTONE_DQ_LITE.RIVERSIDE_NIELS.SV_RIVERSIDE_KPIS\n  METRICS am.active_members, ms.paid_members_35d);\nSELECT * FROM SEMANTIC_VIEW(GLADSTONE_DQ_LITE.RIVERSIDE_NIELS.SV_RIVERSIDE_KPIS\n  DIMENSIONS rev.payment_date METRICS rev.net_revenue)\nWHERE payment_date >= CURRENT_DATE() - 2 ORDER BY payment_date;"
  }
],
    'checkpoints': [
  {
    "after": "Prompt 1.2",
    "text": "On clean data you see **1,598 active members** by status and **1,520** paid in the last 35 days, plus a net revenue figure per day. Note them: in Session 3 they move.",
    "sql": None
  }
],
    'explanations': [
  {
    "title": "Why two answers for active members?",
    "body": "\n`am.active_members` counts members whose **source status** is `ACTIVE`. The verified query (`vq_active_members`) uses the\n**finance definition**: members who **paid in the last 35 days**. About 6% of ACTIVE members haven't paid for longer,\nso the two differ even on clean data. When an operator says \"Nova is wrong\", first check **which definition** answered.\n"
  }
],
    'examples': [
  {
    "title": "Customer Success first response",
    "body": "Before escalating to engineering, CS asks CoCo to map the operator's pipeline and which definition Nova used."
  },
  {
    "title": "Onboarding a data engineer",
    "body": "A new joiner gets a plain-English map of any operator database in minutes, from live metadata."
  }
],
    'header': {
  "label": "Session 1",
  "title": "The complaint",
  "duration": "5 min",
  "building": "Your mental model of Riverside's Nova pipeline"
},
    'what': "Ask CoCo to map Riverside's pipeline end to end, then reproduce the two numbers the operator is asking about.",
    'why': "Before you can guard a pipeline you need to know where a number comes from: which Bronze tables, which REPORTING Dynamic Table, which semantic-view metric. Every investigation starts here.",
    'fallback_after': [
  "Prompt 1.2"
],
    'tech': [
  {
    "name": "Dynamic Tables",
    "icon": "sync",
    "description": "REPORTING layer, incremental refresh, 1-minute target lag"
  },
  {
    "name": "Tasks",
    "icon": "schedule",
    "description": "TSK_BIFROST_MERGE simulates the Bifrost merge every minute"
  },
  {
    "name": "Semantic view",
    "icon": "schema",
    "description": "Gold layer Nova answers from, with a verified query"
  }
],
    'refs': {'Quickstarts': [L.QS_SV, L.QS_DT], 'Docs': [L.LINEAGE, L.DT_MONITOR, L.SV_CREATE]},
  },
  'session_02': {
    'prompts': [
  {
    "id": "Prompt 2.1",
    "title": "Guard the pipeline",
    "text": "Set up data quality monitoring in GLADSTONE_DQ_LITE.RIVERSIDE_NIELS. Run every check every 5 minutes.\nOn MEMBERS__MEMBER:\n- no duplicate member_id (expect 0)\n- no ACTIVE members with a leave date: use GLADSTONE_DQ_LITE.DQ_COMMON.ACTIVE_BUT_LEFT on (status, left_on) (expect 0)\nOn SYSTEM__PAYMENT:\n- no negative amounts (expect 0)\n- table updated in the last 3 minutes (FRESHNESS on the table itself, expect under 180 seconds)\nOn SYSTEM__ATTENDANCE:\n- every booking_id exists in SYSTEM__BOOKING (referential integrity, expect 0 orphans)\nOn dynamic table REPORTING__DAILY_REVENUE:\n- trails SYSTEM__PAYMENT by under 5 minutes: GLADSTONE_DQ_LITE.DQ_COMMON.REPORTING_LAG_SECONDS on (last_loaded_at) with SYSTEM__PAYMENT(_loaded_at) (expect under 300)\nOn SYSTEM__BOOKING:\n- row count with anomaly detection turned on\nGive each expectation a clear name. Show me the SQL before running it, then evaluate the single-table expectations now and show check, value and pass/fail."
  },
  {
    "id": "Prompt 2.2",
    "title": "Tell someone: email + incident log",
    "text": "In GLADSTONE_DQ_LITE.RIVERSIDE_NIELS:\n1. Turn on data quality email notifications for the duplicate-member and negative-amount checks only (the database already has an email integration configured).\n2. Create an alert DQ_INCIDENT_ALERT on warehouse DQ_LITE_WH that runs every minute. When any expectation in my schema is failing in SNOWFLAKE.LOCAL.DATA_QUALITY_MONITORING_EXPECTATION_STATUS (measured in the last 30 minutes, and not before my schema was created - results of an earlier copy with the same name stay in that view) and has no row yet in DQ_INCIDENTS for that table, expectation and measurement, insert one row into DQ_INCIDENTS (table_name, metric_name, expectation_name, value, measured_at) - only the latest failing measurement per check.\n3. Resume the alert and show me it is started."
  }
],
    'fallbacks': [
  "USE SCHEMA GLADSTONE_DQ_LITE.RIVERSIDE_NIELS;\nALTER TABLE MEMBERS__MEMBER    SET DATA_METRIC_SCHEDULE = '5 MINUTE';\nALTER TABLE SYSTEM__PAYMENT    SET DATA_METRIC_SCHEDULE = '5 MINUTE';\nALTER TABLE SYSTEM__ATTENDANCE SET DATA_METRIC_SCHEDULE = '5 MINUTE';\nALTER TABLE SYSTEM__BOOKING    SET DATA_METRIC_SCHEDULE = '5 MINUTE';\nALTER DYNAMIC TABLE REPORTING__DAILY_REVENUE SET DATA_METRIC_SCHEDULE = '5 MINUTE';\nALTER TABLE MEMBERS__MEMBER ADD DATA METRIC FUNCTION SNOWFLAKE.CORE.DUPLICATE_COUNT ON (member_id)\n  EXPECTATION no_duplicate_members (VALUE = 0);\nALTER TABLE MEMBERS__MEMBER ADD DATA METRIC FUNCTION GLADSTONE_DQ_LITE.DQ_COMMON.ACTIVE_BUT_LEFT ON (status, left_on)\n  EXPECTATION no_active_leavers (VALUE = 0);\nALTER TABLE SYSTEM__PAYMENT ADD DATA METRIC FUNCTION SNOWFLAKE.CORE.NEGATIVE_COUNT ON (amount)\n  EXPECTATION no_negative_amounts (VALUE = 0);\nALTER TABLE SYSTEM__PAYMENT ADD DATA METRIC FUNCTION SNOWFLAKE.CORE.FRESHNESS ON ()\n  EXPECTATION payments_fresh_3min (VALUE < 180);\nALTER TABLE SYSTEM__ATTENDANCE ADD DATA METRIC FUNCTION SNOWFLAKE.CORE.REFERENTIAL_INTEGRITY_COUNT\n  ON (booking_id, TABLE(GLADSTONE_DQ_LITE.RIVERSIDE_NIELS.SYSTEM__BOOKING(booking_id)))\n  EXPECTATION no_orphan_checkins (VALUE = 0);\nALTER DYNAMIC TABLE REPORTING__DAILY_REVENUE ADD DATA METRIC FUNCTION GLADSTONE_DQ_LITE.DQ_COMMON.REPORTING_LAG_SECONDS\n  ON (last_loaded_at, TABLE(GLADSTONE_DQ_LITE.RIVERSIDE_NIELS.SYSTEM__PAYMENT(_loaded_at)))\n  EXPECTATION reporting_within_5min (VALUE < 300);\nALTER TABLE SYSTEM__BOOKING ADD DATA METRIC FUNCTION SNOWFLAKE.CORE.ROW_COUNT ON () ANOMALY_DETECTION = TRUE;\n\nALTER TABLE MEMBERS__MEMBER MODIFY DATA METRIC FUNCTION SNOWFLAKE.CORE.DUPLICATE_COUNT ON (member_id)\n  SET DATA_QUALITY_NOTIFICATION = TRUE;\nALTER TABLE SYSTEM__PAYMENT MODIFY DATA METRIC FUNCTION SNOWFLAKE.CORE.NEGATIVE_COUNT ON (amount)\n  SET DATA_QUALITY_NOTIFICATION = TRUE;\n\nCREATE OR REPLACE ALERT DQ_INCIDENT_ALERT\n  WAREHOUSE = DQ_LITE_WH SCHEDULE = '1 MINUTE'\n  IF (EXISTS (\n    SELECT 1 FROM SNOWFLAKE.LOCAL.DATA_QUALITY_MONITORING_EXPECTATION_STATUS s\n    WHERE s.table_database = 'GLADSTONE_DQ_LITE' AND s.table_schema = 'RIVERSIDE_NIELS'\n      AND s.measurement_time >= (SELECT created FROM GLADSTONE_DQ_LITE.INFORMATION_SCHEMA.SCHEMATA WHERE schema_name = 'RIVERSIDE_NIELS') AND s.expectation_violated\n      AND s.measurement_time > DATEADD(minute, -30, CURRENT_TIMESTAMP())\n      AND NOT EXISTS (SELECT 1 FROM GLADSTONE_DQ_LITE.RIVERSIDE_NIELS.DQ_INCIDENTS i\n                      WHERE i.table_name = s.table_name AND i.expectation_name = s.expectation_name\n                        AND i.measured_at >= s.measurement_time)))\n  THEN\n    INSERT INTO GLADSTONE_DQ_LITE.RIVERSIDE_NIELS.DQ_INCIDENTS (table_name, metric_name, expectation_name, value, measured_at)\n    SELECT s.table_name, s.metric_name, s.expectation_name, s.value::VARCHAR, s.measurement_time\n    FROM SNOWFLAKE.LOCAL.DATA_QUALITY_MONITORING_EXPECTATION_STATUS s\n    WHERE s.table_database = 'GLADSTONE_DQ_LITE' AND s.table_schema = 'RIVERSIDE_NIELS'\n      AND s.measurement_time >= (SELECT created FROM GLADSTONE_DQ_LITE.INFORMATION_SCHEMA.SCHEMATA WHERE schema_name = 'RIVERSIDE_NIELS') AND s.expectation_violated\n      AND s.measurement_time > DATEADD(minute, -30, CURRENT_TIMESTAMP())\n      AND NOT EXISTS (SELECT 1 FROM GLADSTONE_DQ_LITE.RIVERSIDE_NIELS.DQ_INCIDENTS i\n                      WHERE i.table_name = s.table_name AND i.expectation_name = s.expectation_name\n                        AND i.measured_at >= s.measurement_time)\n    QUALIFY ROW_NUMBER() OVER (PARTITION BY s.table_name, s.expectation_name ORDER BY s.measurement_time DESC) = 1;\nALTER ALERT DQ_INCIDENT_ALERT RESUME;"
],
    'snowsight': [
  {
    "after": "Prompt 2.1",
    "steps": [
      "Open **Catalog \u00bb Database Explorer** \u00bb `RIVERSIDE_NIELS` \u00bb `MEMBERS__MEMBER` \u00bb **Data Quality** tab.",
      "Select **Monitor** \u00bb set the schedule to every 5 minutes.",
      "Add **Duplicate count** on `member_id` with the expectation *Value = 0*; add **Custom DMF** `DQ_COMMON.ACTIVE_BUT_LEFT` on `status, left_on`.",
      "Repeat on `SYSTEM__PAYMENT` (Negative count, Freshness), `SYSTEM__ATTENDANCE` (Referential integrity), `REPORTING__DAILY_REVENUE` (custom `REPORTING_LAG_SECONDS`) and `SYSTEM__BOOKING` (Row count with anomaly detection)."
    ],
    "sql": "SELECT * FROM TABLE(SYSTEM$EVALUATE_DATA_QUALITY_EXPECTATIONS(REF_ENTITY_NAME => 'GLADSTONE_DQ_LITE.RIVERSIDE_NIELS.MEMBERS__MEMBER'));\nSELECT * FROM TABLE(SYSTEM$EVALUATE_DATA_QUALITY_EXPECTATIONS(REF_ENTITY_NAME => 'GLADSTONE_DQ_LITE.RIVERSIDE_NIELS.SYSTEM__PAYMENT'));"
  },
  {
    "after": "Prompt 2.2",
    "steps": [
      "Open `MEMBERS__MEMBER` \u00bb **Data Quality** \u00bb the duplicate check \u00bb **Notifications** \u00bb on. Repeat for negative amounts on `SYSTEM__PAYMENT`.",
      "Create the alert in a worksheet (below), then **Monitoring \u00bb Alerts** shows its state and history."
    ],
    "sql": "CREATE OR REPLACE ALERT GLADSTONE_DQ_LITE.RIVERSIDE_NIELS.DQ_INCIDENT_ALERT\n  WAREHOUSE = DQ_LITE_WH SCHEDULE = '1 MINUTE'\n  IF (EXISTS (SELECT 1 FROM SNOWFLAKE.LOCAL.DATA_QUALITY_MONITORING_EXPECTATION_STATUS s\n              WHERE s.table_database = 'GLADSTONE_DQ_LITE' AND s.table_schema = 'RIVERSIDE_NIELS'\n      AND s.measurement_time >= (SELECT created FROM GLADSTONE_DQ_LITE.INFORMATION_SCHEMA.SCHEMATA WHERE schema_name = 'RIVERSIDE_NIELS') AND s.expectation_violated\n                AND s.measurement_time > DATEADD(minute, -30, CURRENT_TIMESTAMP())\n                AND NOT EXISTS (SELECT 1 FROM GLADSTONE_DQ_LITE.RIVERSIDE_NIELS.DQ_INCIDENTS i\n                                WHERE i.table_name = s.table_name AND i.expectation_name = s.expectation_name\n                                  AND i.measured_at >= s.measurement_time)))\n  THEN INSERT INTO GLADSTONE_DQ_LITE.RIVERSIDE_NIELS.DQ_INCIDENTS (table_name, metric_name, expectation_name, value, measured_at)\n       SELECT ... ;   -- same filter, latest row per check (see \"Behind? Run this\")\nALTER ALERT GLADSTONE_DQ_LITE.RIVERSIDE_NIELS.DQ_INCIDENT_ALERT RESUME;"
  }
],
    'checkpoints': [
  {
    "after": "Prompt 2.2",
    "text": "All expectations **pass** on clean data, two checks notify by email, and `DQ_INCIDENT_ALERT` is **started** with `DQ_INCIDENTS` still empty. Tell the facilitator you're ready - faults go in next.",
    "sql": None
  }
],
    'explanations': [
  {
    "title": "Email, alert, or both?",
    "body": "\n**Data quality notifications** are built in: one setting per database, switched on per check. Good for the few checks\nthat should wake someone up. They have a cooldown, so you aren't flooded.\n\n**An alert writing to `DQ_INCIDENTS`** gives you a record of every failure: when it opened, which check, what value.\nThat table is what Customer Success, a dashboard or a ticketing integration reads. Use both.\n\n**Expectations vs anomaly detection:** expectations encode rules that must **always** hold and fail on the first bad run.\nAnomaly detection (on `ROW_COUNT` / `FRESHNESS`) learns normal behaviour and needs about **two weeks** of history -\nduring the lab it shows `TRAINING_IN_PROGRESS`. Turn it on now so it's working in two weeks.\n"
  }
],
    'examples': [
  {
    "title": "Replacing homegrown DATA_MONITORING_WH checks",
    "body": "Warehouse-scheduled checks become serverless DMFs with history, pass/fail and notifications built in."
  },
  {
    "title": "Bifrost sync SLAs",
    "body": "FRESHNESS and Bronze-to-REPORTING lag give CS and engineering one shared definition of \"late\"."
  },
  {
    "title": "Incidents into ServiceNow / Jira",
    "body": "`DQ_INCIDENTS` is the hand-off point: a webhook notification or a connector turns each row into a ticket."
  },
  {
    "title": "Payments integrity",
    "body": "NEGATIVE_COUNT catches sign bugs before revenue dashboards move."
  }
],
    'header': {
  "label": "Session 2",
  "title": "Put guards on it",
  "duration": "8 min",
  "building": "Checks with pass/fail rules, an email, and an incident log"
},
    'what': "Turn each thing that must always be true about Riverside's data into an **expectation** on a data metric function (DMF). Then make failures **tell someone**: an email for the critical checks, and an alert that writes every failure to `DQ_INCIDENTS`.",
    'why': "This is the shift from reactive to proactive. The checks run serverless, next to the data, every few minutes. A bad Bifrost batch becomes an incident row and an email **before** the operator opens Nova.",
    'fallback_after': [
  "Prompt 2.2"
],
    'tech': [
  {
    "name": "System and custom DMFs",
    "icon": "fact_check",
    "description": "DUPLICATE_COUNT, NEGATIVE_COUNT, FRESHNESS, REFERENTIAL_INTEGRITY_COUNT, ROW_COUNT + DQ_COMMON checks"
  },
  {
    "name": "Expectations + notifications",
    "icon": "notifications_active",
    "description": "Pass/fail rules; email on the critical ones"
  },
  {
    "name": "Alerts",
    "icon": "campaign",
    "description": "CREATE ALERT writes every new failure to DQ_INCIDENTS"
  }
],
    'concepts': [
  {
    "term": "Data metric function (DMF)",
    "definition": "A function attached to a table or dynamic table that returns one number on a schedule. Runs on serverless compute."
  },
  {
    "term": "Expectation",
    "definition": "A rule on a DMF's value, e.g. `VALUE = 0`. Violations are recorded in `SNOWFLAKE.LOCAL.DATA_QUALITY_MONITORING_EXPECTATION_STATUS`."
  },
  {
    "term": "Alert",
    "definition": "A scheduled condition (a query) and an action (SQL). Here: 'is any check newly failing?' then 'insert an incident row'."
  }
],
    'refs': {'Quickstarts': [L.QS_DQ, L.QS_DQM], 'Docs': [L.DQ_SQL, L.DQ_EXPECT, L.DQ_CUSTOM, L.DQ_NOTIFY, L.ALERTS, L.DQ_ANOMALY]},
  },
  'session_03': {
    'prompts': [
  {
    "id": "Prompt 3.1",
    "title": "What broke, and why?",
    "text": "My operator Riverside says Nova shows too many active members and revenue looks too low. Investigate GLADSTONE_DQ_LITE.RIVERSIDE_NIELS:\n1. What's in DQ_INCIDENTS, and which expectations are failing right now? Evaluate now if results are older than 5 minutes.\n2. For each failing check, show sample failing rows and the merge batch (_batch_id / _SYNC_META__MERGE_BATCH) that introduced them.\n3. Is the pipeline running? Check TSK_BIFROST_MERGE state and run history.\n4. Which Nova numbers in SV_RIVERSIDE_KPIS are affected, and by roughly how much compared to my clean baseline?\nGive me a one-paragraph root cause I could send to the operator."
  },
  {
    "id": "Prompt 3.2",
    "title": "Contain it: circuit breaker",
    "text": "In GLADSTONE_DQ_LITE.RIVERSIDE_NIELS, create a task TSK_DQ_CIRCUIT_BREAKER on warehouse DQ_LITE_WH that runs every minute:\n- count the expectations on MEMBERS__MEMBER, SYSTEM__PAYMENT and SYSTEM__ATTENDANCE whose LATEST result in SNOWFLAKE.LOCAL.DATA_QUALITY_MONITORING_EXPECTATION_STATUS (measured since my schema was created) is violated\n- if any: suspend dynamic tables REPORTING__ACTIVE_MEMBERS and REPORTING__DAILY_REVENUE, and set the task return value to 'OPEN: <n> failing Bronze check(s)'\n- otherwise resume them and return 'CLOSED: Bronze clean'\nBuild the return message in a variable first, then pass that variable to SYSTEM$SET_RETURN_VALUE. Resume the task, then show its last runs and the dynamic tables' scheduling state."
  }
],
    'fallbacks': [
  "USE SCHEMA GLADSTONE_DQ_LITE.RIVERSIDE_NIELS;\nSELECT * FROM DQ_INCIDENTS ORDER BY opened_at;\nSELECT * FROM TABLE(SYSTEM$DATA_METRIC_SCAN(\n  REF_ENTITY_NAME => 'GLADSTONE_DQ_LITE.RIVERSIDE_NIELS.MEMBERS__MEMBER',\n  METRIC_NAME => 'SNOWFLAKE.CORE.DUPLICATE_COUNT', ARGUMENT_NAME => 'member_id')) LIMIT 20;\nSELECT batch_id, table_name, COUNT(*) AS times_applied FROM _SYNC_META__MERGE_BATCH GROUP BY 1, 2 HAVING COUNT(*) > 1;\nSELECT _batch_id, COUNT(*), SUM(amount) FROM SYSTEM__PAYMENT WHERE amount < 0 GROUP BY 1;\nSHOW TASKS LIKE 'TSK_BIFROST_MERGE';\n\nCREATE OR REPLACE TASK TSK_DQ_CIRCUIT_BREAKER\n  WAREHOUSE = DQ_LITE_WH SCHEDULE = '1 MINUTE'\nAS\nEXECUTE IMMEDIATE $$\nDECLARE\n  bad NUMBER;\n  msg VARCHAR;\nBEGIN\n  SELECT COUNT(*) INTO :bad FROM (\n    SELECT expectation_violated FROM SNOWFLAKE.LOCAL.DATA_QUALITY_MONITORING_EXPECTATION_STATUS\n    WHERE table_database = 'GLADSTONE_DQ_LITE' AND table_schema = 'RIVERSIDE_NIELS'\n      AND measurement_time >= (SELECT created FROM GLADSTONE_DQ_LITE.INFORMATION_SCHEMA.SCHEMATA WHERE schema_name = 'RIVERSIDE_NIELS')\n      AND table_name IN ('MEMBERS__MEMBER', 'SYSTEM__PAYMENT', 'SYSTEM__ATTENDANCE')\n    QUALIFY ROW_NUMBER() OVER (PARTITION BY table_name, expectation_name ORDER BY measurement_time DESC) = 1)\n  WHERE expectation_violated;\n  IF (bad > 0) THEN\n    ALTER DYNAMIC TABLE GLADSTONE_DQ_LITE.RIVERSIDE_NIELS.REPORTING__ACTIVE_MEMBERS SUSPEND;\n    ALTER DYNAMIC TABLE GLADSTONE_DQ_LITE.RIVERSIDE_NIELS.REPORTING__DAILY_REVENUE SUSPEND;\n    msg := 'OPEN: ' || :bad || ' failing Bronze check(s) - REPORTING frozen at last good state';\n    CALL SYSTEM$SET_RETURN_VALUE(:msg);\n  ELSE\n    ALTER DYNAMIC TABLE GLADSTONE_DQ_LITE.RIVERSIDE_NIELS.REPORTING__ACTIVE_MEMBERS RESUME;\n    ALTER DYNAMIC TABLE GLADSTONE_DQ_LITE.RIVERSIDE_NIELS.REPORTING__DAILY_REVENUE RESUME;\n    CALL SYSTEM$SET_RETURN_VALUE('CLOSED: Bronze clean');\n  END IF;\nEND;\n$$;\nALTER TASK TSK_DQ_CIRCUIT_BREAKER RESUME;"
],
    'snowsight': [
  {
    "after": "Prompt 3.1",
    "steps": [
      "**Governance & security \u00bb Data quality**: open incidents across the account. Select a failing check \u00bb **Investigate** opens CoCo with the incident loaded.",
      "Open the failing table \u00bb **Data Quality** tab \u00bb select the check to see its value history.",
      "**Transformation \u00bb Tasks** \u00bb `TSK_BIFROST_MERGE` \u00bb **Run history** (suspended? no runs?)."
    ],
    "sql": "SELECT * FROM GLADSTONE_DQ_LITE.RIVERSIDE_NIELS.DQ_INCIDENTS ORDER BY opened_at;\nSELECT table_name, metric_name, expectation_name, value, measurement_time\nFROM SNOWFLAKE.LOCAL.DATA_QUALITY_MONITORING_EXPECTATION_STATUS\nWHERE table_database = 'GLADSTONE_DQ_LITE' AND table_schema = 'RIVERSIDE_NIELS'\n      AND measurement_time >= (SELECT created FROM GLADSTONE_DQ_LITE.INFORMATION_SCHEMA.SCHEMATA WHERE schema_name = 'RIVERSIDE_NIELS') AND expectation_violated\nQUALIFY ROW_NUMBER() OVER (PARTITION BY table_name, expectation_name ORDER BY measurement_time DESC) = 1;"
  },
  {
    "after": "Prompt 3.2",
    "steps": [
      "Create the task in a worksheet (see *Behind? Run this*), then **Transformation \u00bb Tasks** \u00bb `TSK_DQ_CIRCUIT_BREAKER` \u00bb **Run history** shows each return value.",
      "**Transformation \u00bb Dynamic tables**: the two REPORTING tables show **Suspended** while the breaker is OPEN."
    ],
    "sql": "SELECT state, scheduled_time, return_value\nFROM TABLE(GLADSTONE_DQ_LITE.INFORMATION_SCHEMA.TASK_HISTORY(TASK_NAME => 'TSK_DQ_CIRCUIT_BREAKER', RESULT_LIMIT => 5))\nORDER BY scheduled_time DESC;\nSHOW DYNAMIC TABLES IN SCHEMA GLADSTONE_DQ_LITE.RIVERSIDE_NIELS;"
  }
],
    'checkpoints': [
  {
    "after": "Prompt 3.2",
    "text": "`DQ_INCIDENTS` has rows for **duplicates (150)**, **negative amounts (40)** and **freshness (over 180 s)**. The breaker returns **OPEN** and both REPORTING tables are **SUSPENDED**: Nova keeps showing the last good numbers.",
    "sql": None
  }
],
    'explanations': [
  {
    "title": "What each fault looks like",
    "body": "\n| If CoCo finds... | It's the... | Notice |\n|---|---|---|\n| `DUPLICATE_COUNT(member_id)` = 150, batch `B-REPLAY-01` applied twice | Bifrost replay | Active members inflated by 150 |\n| `NEGATIVE_COUNT(amount)` = 40, batch `B-SIGNBUG-01` | Refund sign flip | Today's net revenue drops by \u00a310,000 |\n| `FRESHNESS` over 180 s, task SUSPENDED | Merge task stalled | REPORTING lag stays **0**: REPORTING isn't behind its source - the **source** stopped. That's why you need both checks. |\n"
  },
  {
    "title": "Why freeze REPORTING instead of deleting the bad rows?",
    "body": "\nContainment and repair are different jobs. The breaker is automatic and safe: it stops bad numbers reaching Nova **now**,\nwithout guessing which rows to delete. The repair (Session 4) is a deliberate fix by the source team, and the breaker\ncloses by itself on its next run once every Bronze check passes.\n"
  }
],
    'examples': [
  {
    "title": "CS escalation in five minutes",
    "body": "The one-paragraph root cause from Prompt 3.1 is what goes back to the operator - with the batch id and the fix."
  },
  {
    "title": "Stop bad data at Silver",
    "body": "The breaker pattern keeps the Nova Portal on yesterday's correct numbers rather than today's wrong ones."
  },
  {
    "title": "Bifrost incident review",
    "body": "Batch-level evidence (`_SYNC_META`) shows whether a replay hit one operator or many."
  }
],
    'header': {
  "label": "Session 3",
  "title": "Catch, explain, contain",
  "duration": "9 min",
  "building": "A root cause from one prompt, and a circuit breaker"
},
    'what': "Watch your guards fire, then ask CoCo what broke and why - the way Customer Success would. Then add a **circuit breaker** that freezes REPORTING while any Bronze check is failing, so Nova keeps serving the last good numbers.",
    'why': "Catching is half the job. Explaining it (which batch, which rows) and **containing** it (bad data never reaches Nova) is what lets Customer Success tell the operator *\"we know, it's fixed\"* before they ring.",
    'fallback_after': [
  "Prompt 3.2"
],
    'tech': [
  {
    "name": "DQ results + incident log",
    "icon": "table_view",
    "description": "SNOWFLAKE.LOCAL expectation status and your DQ_INCIDENTS table"
  },
  {
    "name": "SYSTEM$DATA_METRIC_SCAN",
    "icon": "search",
    "description": "Returns the rows that made a system DMF fail"
  },
  {
    "name": "Tasks + Dynamic Tables",
    "icon": "power_settings_new",
    "description": "A task suspends and resumes REPORTING; SYSTEM$SET_RETURN_VALUE records why"
  }
],
    'refs': {'Quickstarts': [L.QS_DQ, L.QS_COCO_DE], 'Docs': [L.DQ_DASH, L.DQ_SCAN, L.TASK_HISTORY, L.TASK_RETURN, L.DT_MONITOR]},
  },
  'session_04': {
    'prompts': [
  {
    "id": "Prompt 4.1",
    "title": "One health view",
    "text": "In GLADSTONE_DQ_LITE.RIVERSIDE_NIELS, create a view V_DQ_HEALTH with one row per expectation in my schema (use only results measured since the schema was created): table, expectation, metric, latest value, status ('OK' or 'FAILING'), last checked time, first incident time and number of incidents from DQ_INCIDENTS. Failing checks first.\nThen show it, and tell me in two sentences whether Riverside's Nova numbers can be trusted right now."
  },
  {
    "id": "Prompt 4.2",
    "title": "Fix it and watch it recover",
    "text": "Riverside's source team has fixed the feed. Clean up GLADSTONE_DQ_LITE.RIVERSIDE_NIELS the way they would:\n1. delete the replayed member rows (batch B-REPLAY-01) and the negative payments (batch B-SIGNBUG-01)\n2. set members from batch B-STATUS-01 back to CANCELLED\n3. resume TSK_BIFROST_MERGE\nThen evaluate every expectation now, and show me V_DQ_HEALTH and the circuit breaker's last return values until it reports CLOSED. Compare the active members and net revenue with my clean baseline from Session 1."
  }
],
    'fallbacks': [
  "USE SCHEMA GLADSTONE_DQ_LITE.RIVERSIDE_NIELS;\nCREATE OR REPLACE VIEW V_DQ_HEALTH AS\nWITH latest AS (\n  SELECT table_name, metric_name, expectation_name, value, expectation_violated, measurement_time\n  FROM SNOWFLAKE.LOCAL.DATA_QUALITY_MONITORING_EXPECTATION_STATUS\n  WHERE table_database = 'GLADSTONE_DQ_LITE' AND table_schema = 'RIVERSIDE_NIELS'\n      AND measurement_time >= (SELECT created FROM GLADSTONE_DQ_LITE.INFORMATION_SCHEMA.SCHEMATA WHERE schema_name = 'RIVERSIDE_NIELS')\n  QUALIFY ROW_NUMBER() OVER (PARTITION BY table_name, expectation_name ORDER BY measurement_time DESC) = 1)\nSELECT l.table_name, l.expectation_name, l.metric_name, l.value,\n       IFF(l.expectation_violated, 'FAILING', 'OK') AS status, l.measurement_time AS last_checked,\n       (SELECT MIN(i.opened_at) FROM GLADSTONE_DQ_LITE.RIVERSIDE_NIELS.DQ_INCIDENTS i\n         WHERE i.table_name = l.table_name AND i.expectation_name = l.expectation_name) AS first_incident_at,\n       (SELECT COUNT(*) FROM GLADSTONE_DQ_LITE.RIVERSIDE_NIELS.DQ_INCIDENTS i\n         WHERE i.table_name = l.table_name AND i.expectation_name = l.expectation_name) AS incidents\nFROM latest l ORDER BY l.expectation_violated DESC, l.table_name;\nSELECT * FROM V_DQ_HEALTH;\n\n-- the fix\nDELETE FROM MEMBERS__MEMBER WHERE _batch_id = 'B-REPLAY-01';\nDELETE FROM SYSTEM__PAYMENT WHERE _batch_id = 'B-SIGNBUG-01';\nUPDATE MEMBERS__MEMBER SET status = 'CANCELLED' WHERE _batch_id = 'B-STATUS-01';\nALTER TASK TSK_BIFROST_MERGE RESUME;\nSELECT * FROM TABLE(SYSTEM$EVALUATE_DATA_QUALITY_EXPECTATIONS(REF_ENTITY_NAME => 'GLADSTONE_DQ_LITE.RIVERSIDE_NIELS.MEMBERS__MEMBER'));\nSELECT state, scheduled_time, return_value\nFROM TABLE(GLADSTONE_DQ_LITE.INFORMATION_SCHEMA.TASK_HISTORY(TASK_NAME => 'TSK_DQ_CIRCUIT_BREAKER', RESULT_LIMIT => 5))\nORDER BY scheduled_time DESC;"
],
    'snowsight': [
  {
    "after": "Prompt 4.1",
    "steps": [
      "Create the view in a worksheet (see *Behind? Run this*).",
      "**Governance & security \u00bb Data quality** gives the same picture account-wide; your view is the operator-specific one CS can share."
    ],
    "sql": "SELECT * FROM GLADSTONE_DQ_LITE.RIVERSIDE_NIELS.V_DQ_HEALTH;"
  },
  {
    "after": "Prompt 4.2",
    "steps": [
      "Run the fix in a worksheet; **Transformation \u00bb Tasks** \u00bb resume `TSK_BIFROST_MERGE`.",
      "Watch `TSK_DQ_CIRCUIT_BREAKER` run history flip to **CLOSED** (after the next scheduled check, up to 5 minutes)."
    ],
    "sql": None
  }
],
    'checkpoints': [
  {
    "after": "Prompt 4.2",
    "text": "`V_DQ_HEALTH` showed **4 FAILING** checks including `NO_ACTIVE_LEAVERS` (292). After the fix every check is **OK**, the breaker returns **CLOSED: Bronze clean**, REPORTING is running again, and `DQ_INCIDENTS` keeps the history.",
    "sql": None
  }
],
    'explanations': [
  {
    "title": "Why does reporting_within_5min fail after the fix?",
    "body": "\nWhile the breaker was OPEN, REPORTING was frozen on purpose, so it fell behind Bronze (about 500 seconds in the dry run).\nThe first check after the breaker closes measures that gap and fails once; the next run passes. The breaker only watches\n**Bronze** checks, so this REPORTING check can never hold it open - otherwise it would freeze itself forever.\n"
  },
  {
    "title": "Why fault 4 is the hardest one",
    "body": "\nEvery row in the status-drift batch is well-formed: no duplicates, no nulls, no negative amounts. Only a **business rule**\ncatches it - *a member with a leave date can't be ACTIVE* - which is why `ACTIVE_BUT_LEFT` is a **custom** DMF defined\nonce in `DQ_COMMON`. The symptom in Nova is the two \"active members\" numbers drifting apart.\n"
  }
],
    'examples': [
  {
    "title": "Before the operator calls",
    "body": "CS checks `V_DQ_HEALTH` each morning (or gets it as a digest - see Stretch) and calls the operator first."
  },
  {
    "title": "Post-incident review",
    "body": "`DQ_INCIDENTS` plus the breaker's return values give a timeline: when it broke, when it was contained, when it recovered."
  },
  {
    "title": "Every operator",
    "body": "The same view over every operator database is the *Rolling out* page: one template, many databases."
  }
],
    'header': {
  "label": "Session 4",
  "title": "Operate it",
  "duration": "8 min",
  "building": "One health view, a semantic fault, and a recovery"
},
    'what': "Build `V_DQ_HEALTH`, the one view Customer Success opens first: every check, OK or FAILING, and its incident history. Then catch fault 4, fix the data the way the source team would, and watch the breaker close by itself.",
    'why': "Monitoring only pays off if someone looks at it. One view per operator, in plain terms, is how Gladstone moves from *the operator told us* to *we told the operator*.",
    'fallback_after': [
  "Prompt 4.2"
],
    'tech': [
  {
    "name": "Custom DMF",
    "icon": "function",
    "description": "ACTIVE_BUT_LEFT: a business rule defined once, attached anywhere"
  },
  {
    "name": "Health view",
    "icon": "monitor_heart",
    "description": "Latest expectation status joined to the incident log"
  },
  {
    "name": "Self-healing breaker",
    "icon": "autorenew",
    "description": "Closes and resumes REPORTING once every Bronze check passes"
  }
],
    'built': [
  "Seven expectations and an anomaly monitor on Riverside's Bronze and REPORTING tables",
  "Email notifications on the two critical checks",
  "`DQ_INCIDENT_ALERT` writing every new failure to `DQ_INCIDENTS`",
  "`TSK_DQ_CIRCUIT_BREAKER` holding back bad numbers from Nova",
  "`V_DQ_HEALTH`, the first thing Customer Success opens"
],
    'refs': {'Quickstarts': [L.QS_DQ, L.QS_DQM], 'Docs': [L.DQ_CUSTOM, L.DQ_EXPECT, L.DQ_DASH, L.TASK_RETURN]},
  },
  'snowsight_map': {
    'prompts': [],
    'fallbacks': [],
    'snowsight': [],
    'checkpoints': [],
    'explanations': [],
    'examples': [
  {
    "title": "Analysts without CoCo",
    "body": "Business users and CS can follow the same checks from Snowsight menus, with no prompts needed."
  },
  {
    "title": "Incident handover",
    "body": "On-call shares a Snowsight link to the failing check's Data Quality tab instead of screenshots."
  }
],
    'refs': {'Docs': [L.DQ_DASH, L.DT_MONITOR, L.LINEAGE, L.BUDGETS, L.TRUST_CENTER, L.DCM]},
  },
  'stretch': {
    'prompts': [
  {
    "id": "Prompt S.1",
    "title": "Create and question the agent",
    "text": "Create a Cortex Agent GLADSTONE_DQ_LITE.RIVERSIDE_NIELS.NOVA_RIVERSIDE_AGENT that uses semantic view GLADSTONE_DQ_LITE.RIVERSIDE_NIELS.SV_RIVERSIDE_KPIS as a Cortex Analyst tool on warehouse DQ_LITE_WH. Instruct it to always say which metric or verified query it used.\nThen ask it: \"How many active members do we have?\" and \"What was net revenue yesterday?\"\nCompare its answers with the active_members metric and the verified query, and with my current data quality results. Would you trust each answer? Why?"
  },
  {
    "id": "Prompt S.2",
    "title": "Daily digest for Customer Success",
    "text": "In GLADSTONE_DQ_LITE.RIVERSIDE_NIELS, create a view V_DQ_DIGEST that lists, for the last 24 hours, every expectation in my schema with: latest value, pass/fail, number of failed runs and first failure time. Then create a task that runs it daily at 07:00 Europe/London and writes the result into a table DQ_DIGEST_HISTORY. Keep the task suspended - show me how I would resume it."
  },
  {
    "id": "Prompt S.3",
    "title": "Would anything catch a missing day?",
    "text": "A day of bookings may have gone missing in GLADSTONE_DQ_LITE.RIVERSIDE_NIELS.SYSTEM__BOOKING. Which of my expectations would catch that, and why don't they? Show bookings per day for the last 7 days, the ROW_COUNT anomaly detection status on SYSTEM__BOOKING, and propose an expectation that would catch a missing day today without waiting for anomaly training."
  },
  {
    "id": "Prompt S.4",
    "title": "Before/after migration check",
    "text": "Pretend GLADSTONE_DQ_LITE.RIVERSIDE_NIELS is an operator that has just been migrated from GCP to Azure, and GLADSTONE_DQ_LITE.TEMPLATE is not visible to me. Using only my schema, design the reconciliation checks I'd run before cut-over: row counts per Bronze table, sum of payment amounts per day, distinct members per status, and max _loaded_at. Write them as data metric functions or SQL I can run against both copies, and explain which differences are acceptable."
  }
],
    'fallbacks': [
  "CREATE OR REPLACE AGENT GLADSTONE_DQ_LITE.RIVERSIDE_NIELS.NOVA_RIVERSIDE_AGENT FROM SPECIFICATION $$\n{\"instructions\": {\"response\": \"Answer for this leisure operator only. Always say which metric or verified query you used.\",\n                  \"orchestration\": \"Use the operator_kpis tool for members, revenue and utilisation questions.\"},\n \"tools\": [{\"tool_spec\": {\"type\": \"cortex_analyst_text_to_sql\", \"name\": \"operator_kpis\",\n                          \"description\": \"Active members, revenue, class utilisation for this operator\"}}],\n \"tool_resources\": {\"operator_kpis\": {\"semantic_view\": \"GLADSTONE_DQ_LITE.RIVERSIDE_NIELS.SV_RIVERSIDE_KPIS\",\n                    \"execution_environment\": {\"type\": \"warehouse\", \"warehouse\": \"DQ_LITE_WH\"}}}}\n$$;"
],
    'snowsight': [
  {
    "after": "Prompt S.1",
    "steps": [
      "**AI & ML \u00bb Agents** \u00bb **Create agent** in `RIVERSIDE_NIELS`; add a **Cortex Analyst** tool on `SV_RIVERSIDE_KPIS`, warehouse `DQ_LITE_WH`.",
      "Use the agent's **Playground** to ask the questions; open the thinking trace to see the verified query being used."
    ],
    "sql": None
  },
  {
    "after": "Prompt S.2",
    "steps": [
      "Create the view and table in a worksheet, then **Transformation \u00bb Tasks \u00bb + Task** with a CRON schedule `0 7 * * * Europe/London`."
    ],
    "sql": None
  }
],
    'checkpoints': [],
    'explanations': [
  {
    "title": "What to look for",
    "body": "\nThe agent answers *\"How many active members?\"* from the **verified query** (paid in the last 35 days) - so it disagrees with the\nstatus-based dashboard number. Neither is a bug: they're two definitions. Fix it in the semantic view (rename the metric, document the definition,\nor align the verified query), then re-test. For ongoing quality, use **Cortex Agent evaluations** and **AI Observability**.\n"
  },
  {
    "title": "Why anomaly detection, and what to do until it's trained",
    "body": "\nEvery remaining row is valid, so no row-level rule fails. `ROW_COUNT` with **anomaly detection** learns the normal daily\nvolume and flags the drop - after about two weeks of history. Until then, a simple custom DMF (rows loaded in the last\n24 hours, expect over a floor) covers the gap.\n"
  }
],
    'examples': [
  {
    "title": "Nova agent regression tests",
    "body": "A fixed set of operator questions with known answers runs after every semantic-view change, using agent evaluations."
  },
  {
    "title": "CS morning digest",
    "body": "The daily digest goes to Customer Success, so they know about a broken operator before the operator rings."
  },
  {
    "title": "GCP to Azure cut-over",
    "body": "Reconciliation DMFs give a signed-off, repeatable before/after comparison per operator database."
  }
],
    'what': "Create a Cortex Agent over `SV_RIVERSIDE_KPIS` (a mini Nova), ask it the operator's questions, and check the answer against the data quality results.",
    'why': "Nova's trust problem is at the agent layer: the agent picks a metric or a verified query. Testing agent answers against known-good numbers is the AI-side half of data quality.",
    'fallback_after': [
  "Prompt S.1"
],
    'refs': {'Quickstarts': [L.QS_AGENTS, L.QS_AGENT_EVAL, L.QS_AI_OBS, L.QS_SV_BP], 'Docs': [L.AGENTS, L.AI_OBS, L.SV_CREATE, L.TASKS]},
  },
  'troubleshooting': {
    'prompts': [],
    'fallbacks': [],
    'snowsight': [],
    'checkpoints': [],
    'explanations': [],
    'examples': [
  {
    "title": "Rollout runbook",
    "body": "These fixes become the runbook when the checks are rolled out to every operator database."
  },
  {
    "title": "Least privilege in production",
    "body": "The lab shares one role for simplicity. In production each operator database gets its own read and admin roles."
  }
],
    'refs': {'Docs': [L.DQ_EXPECT, L.DQ_ANOMALY, L.TAG_MASK, L.DT_MONITOR, L.TASK_HISTORY]},
  },
}
