"""Results captured from a real run of the Gladstone DQ lab (Lite) on a Snowflake demo account (16 Oct 2026).
Account and user identifiers are replaced with placeholders. Data is synthetic. Generated - do not hand-edit."""

A_ROOM_AFTER = [
 {
  "SHORT_NAME": "AMY",
  "USER_NAME": None,
  "SCHEMA_NAME": "RIVERSIDE_AMY",
  "CHECKS": 0,
  "FAILING": 0,
  "FAILING_CHECKS": "[]",
  "LAST_MEASURED": None
 },
 {
  "SHORT_NAME": "NIELS",
  "USER_NAME": "NJOHANSEN",
  "SCHEMA_NAME": "RIVERSIDE_NIELS",
  "CHECKS": 6,
  "FAILING": 0,
  "FAILING_CHECKS": "[]",
  "LAST_MEASURED": "2026-10-16 09:50:27"
 }
]

A_ROOM_FAULTED = [
 {
  "SHORT_NAME": "AMY",
  "USER_NAME": None,
  "SCHEMA_NAME": "RIVERSIDE_AMY",
  "CHECKS": 0,
  "FAILING": 0,
  "FAILING_CHECKS": "[]",
  "LAST_MEASURED": None
 },
 {
  "SHORT_NAME": "NIELS",
  "USER_NAME": "NJOHANSEN",
  "SCHEMA_NAME": "RIVERSIDE_NIELS",
  "CHECKS": 6,
  "FAILING": 3,
  "FAILING_CHECKS": "[\n  \"NO_DUPLICATE_MEMBERS\",\n  \"PAYMENTS_FRESH_3MIN\",\n  \"NO_NEGATIVE_AMOUNTS\"\n]",
  "LAST_MEASURED": "2026-10-16 09:35:54"
 }
]

A_ROOM_READY = [
 {
  "SHORT_NAME": "AMY",
  "USER_NAME": None,
  "SCHEMA_NAME": "RIVERSIDE_AMY",
  "CHECKS": 0,
  "FAILING": 0,
  "FAILING_CHECKS": "[]",
  "LAST_MEASURED": None
 },
 {
  "SHORT_NAME": "NIELS",
  "USER_NAME": "NJOHANSEN",
  "SCHEMA_NAME": "RIVERSIDE_NIELS",
  "CHECKS": 0,
  "FAILING": 0,
  "FAILING_CHECKS": "[]",
  "LAST_MEASURED": None
 }
]

B1_DT_COST = [
 {
  "NAME": "REPORTING__CLASS_UTILISATION",
  "REFRESHES": 50,
  "REFRESH_SECONDS": 93
 },
 {
  "NAME": "REPORTING__DAILY_REVENUE",
  "REFRESHES": 50,
  "REFRESH_SECONDS": 45
 }
]

B1_LIMIT = [
 {
  "GET_SPENDING_LIMIT": 5
 }
]

B1_LINKED = [
 {
  "RESOURCE_ID": 2927,
  "NAME": "RIVERSIDE_NIELS",
  "DOMAIN": "SCHEMA",
  "SCHEMA_NAME": None,
  "DATABASE_NAME": "GLADSTONE_DQ_LITE"
 }
]

B1_MONITORS = [
 {
  "name": "DQ_LITE_RM",
  "credit_quota": "20.00",
  "used_credits": "1.47",
  "remaining_credits": "18.53",
  "frequency": "MONTHLY",
  "notify_at": "75%",
  "suspend_at": "100%"
 },
 {
  "name": "DQ_LITE_RM_DEMO",
  "credit_quota": "2.00",
  "used_credits": "0.00",
  "remaining_credits": "2.00",
  "frequency": "DAILY",
  "notify_at": "50%,90%",
  "suspend_at": "100%"
 }
]

B1_TAGS = [
 {
  "TAG_NAME": "COST_CENTRE",
  "TAG_VALUE": "nova",
  "LEVEL": "SCHEMA",
  "OBJECT_NAME": "RIVERSIDE_NIELS"
 },
 {
  "TAG_NAME": "OPERATOR_ID",
  "TAG_VALUE": "RIVERSIDE_NIELS",
  "LEVEL": "SCHEMA",
  "OBJECT_NAME": "RIVERSIDE_NIELS"
 }
]

B1_THRESHOLD = [
 {
  "GET_NOTIFICATION_THRESHOLD": 80
 }
]

B1_WH = [
 {
  "name": "DQ_LITE_WH",
  "size": "X-Small",
  "min_cluster_count": 1,
  "max_cluster_count": 3,
  "auto_suspend": 60,
  "resource_monitor": "DQ_LITE_RM"
 }
]

B2_CLASSIFY = [
 {
  "SYSTEM$CLASSIFY": "{\n  \"classification_result\": {\n    \"DATE_OF_BIRTH\": {\n      \"alternates\": [],\n      \"recommendation\": {\n        \"confidence\": \"HIGH\",\n        \"coverage\": 1,\n        \"details\": [],\n        \"privacy_category\": \"QUASI_IDENTIFIER\",\n        \"semantic_category\": \"DATE_OF_BIRTH\",\n        \"tags\": [\n          {\n            \"tag_applied\": False,\n            \"tag_name\": \"snowflake.core.semantic_category\",\n            \"tag_value\": \"DATE_OF_BIRTH\"\n          },\n          {\n            \"tag_applied\": False,\n            \"tag_name\": \"snowflake.core.privacy_category\",\n            \"tag_value\": \"QUASI_IDENTIFIER\"\n          }\n        ]\n      },\n      \"valid_value_ratio\": 1\n    },\n    \"EMAIL\": {\n      \"alternates\": [],\n      \"recommendation\": {\n        \"confidence\": \"HIGH\",\n        \"coverage\": 1,\n        \"details\": [],\n        \"privacy_category\": \"IDENTIFIER\",\n        \"semantic_category\": \"EMAIL\",\n        \"tags\": [\n          {\n            \"tag_applied\": False,\n            \"tag_name\": \"snowflake.core.semantic_category\",\n            \"tag_value\": \"EMAIL\"\n          },\n          {\n            \"tag_applied\": False,\n            \"tag_name\": \"snowflake.core.privacy_category\",\n            \"tag_value\": \"IDENTIFIER\"\n          }\n        ]\n      },\n      \"valid_value_ratio\": 1\n    },\n    \"FIRST_NAME\": {\n      \"alternates\": [],\n      \"recommendation\": {\n        \"confidence\": \"HIGH\",\n        \"coverage\": 1,\n        \"details\": [],\n        \"privacy_category\": \"IDENTIFIER\",\n        \"semantic_category\": \"NAME\",\n        \"tags\": [\n          {\n            \"tag_applied\": False,\n            \"tag_name\": \"snowflake.core.semantic_category\",\n            \"tag_value\": \"NAME\"\n          },\n          {\n            \"tag_applied\": False,\n            \"tag_name\": \"snowflake.core.privacy_category\",\n            \"tag_value\": \"IDENTIFIER\"\n          }\n        ]\n      },\n      \"valid_value_ratio\": 1\n    },\n    \"HEALTH_NOTES\": {\n      \"alternates\": []\n    },\n    \"HOME_SITE_ID\": {\n      \"alternates\": []\n    },\n    \"JOINED_ON\": {\n      \"alternates\": []\n    },\n    \"LAST_ACTIVITY_AT\": {\n      \"alternates\": []\n    },\n    \"LAST_NAME\": {\n      \"alternates\": [],\n      \"recommendation\": {\n        \"confidence\": \"HIGH\",\n        \"coverage\": 1,\n        \"details\": [],\n        \"privacy_category\": \"IDENTIFIER\",\n        \"semantic_category\": \"NAME\",\n        \"tags\": [\n          {\n            \"tag_applied\": False,\n            \"tag_name\": \"snowflake.core.semantic_category\",\n            \"tag_value\": \"NAME\"\n          },\n          {\n            \"tag_applied\": False,\n            \"tag_name\": \"snowflake.core.privacy_category\",\n            \"tag_value\": \"IDENTIFIER\"\n          }\n        ]\n      },\n      \"valid_value_ratio\": 1\n    },\n    \"LEFT_ON\": {\n      \"alternates\": []\n    },\n    \"MARKETING_CONSENT\": {\n      \"alternates\": []\n    },\n    \"MEMBER_ID\": {\n      \"alternates\": []\n    },\n    \"OPERATOR_ID\": {\n      \"alternates\": []\n    },\n    \"PHONE\": {\n      \"alternates\": []\n    },\n    \"POSTCODE\": {\n      \"alternates\": [],\n      \"recommendation\": {\n        \"confidence\": \"LOW\",\n        \"coverage\": 0.4645,\n        \"details\": [\n          {\n            \"coverage\": 0.4645,\n            \"semantic_category\": \"UK_POSTAL_CODE\"\n          }\n        ],\n        \"privacy_category\": \"QUASI_IDENTIFIER\",\n        \"semantic_category\": \"POSTAL_CODE\",\n        \"tags\": [\n          {\n            \"tag_applied\": False,\n            \"tag_name\": \"snowflake.core.semantic_category\",\n            \"tag_value\": \"POSTAL_CODE\"\n          },\n          {\n            \"tag_applied\": False,\n            \"tag_name\": \"snowflake.core.privacy_category\",\n            \"tag_value\": \"QUASI_IDENTIFIER\"\n          }\n        ]\n      },\n      \"valid_value_ratio\": 1\n    },\n    \"STATUS\": {\n      \"alternates\": []\n    },\n    \"_BATCH_ID\": {\n      \"alternates\": []\n    },\n    \"_LOADED_AT\": {\n      \"alternates\": []\n    }\n  }\n}"
 }
]

B2_CLEAR_READER = [
 {
  "MEMBER_ID": "M-01030",
  "FIRST_NAME": "Amelia",
  "EMAIL": "member1030@example.co.uk",
  "DATE_OF_BIRTH": "1972-08-30",
  "HEALTH_NOTES": "Asthma - inhaler on poolside"
 },
 {
  "MEMBER_ID": "M-01043",
  "FIRST_NAME": "Amelia",
  "EMAIL": "member1043@example.co.uk",
  "DATE_OF_BIRTH": "1967-03-10",
  "HEALTH_NOTES": "Asthma - inhaler on poolside"
 },
 {
  "MEMBER_ID": "M-01048",
  "FIRST_NAME": "Isla",
  "EMAIL": "member1048@example.co.uk",
  "DATE_OF_BIRTH": "1986-12-13",
  "HEALTH_NOTES": "Recent knee surgery - low impact only"
 }
]

B2_CROSS_REGION = [
 {
  "key": "CORTEX_ENABLED_CROSS_REGION",
  "value": "ANY_REGION",
  "default": "DISABLED",
  "level": "ACCOUNT"
 }
]

B2_ERASE = [
 {
  "ERASE_MEMBER": "{\n  \"attendance_deleted\": 6,\n  \"bookings_deleted\": 8,\n  \"member_rows\": 1,\n  \"payments_pseudonymised\": 3\n}"
 }
]

B2_ERASURE_EVAL = [
 {
  "METRIC_NAME": "DUPLICATE_COUNT",
  "EXPECTATION_NAME": "NO_DUPLICATE_MEMBERS",
  "EXPECTATION_EXPRESSION": "VALUE = 0",
  "VALUE": 0,
  "EXPECTATION_VIOLATED": False
 },
 {
  "METRIC_NAME": "ERASED_MEMBERS_STILL_PRESENT",
  "EXPECTATION_NAME": "ERASURE_COMPLETE",
  "EXPECTATION_EXPRESSION": "VALUE = 0",
  "VALUE": 0,
  "EXPECTATION_VIOLATED": False
 },
 {
  "METRIC_NAME": "ACTIVE_BUT_LEFT",
  "EXPECTATION_NAME": "NO_ACTIVE_LEAVERS",
  "EXPECTATION_EXPRESSION": "VALUE = 0",
  "VALUE": 0,
  "EXPECTATION_VIOLATED": False
 }
]

B2_GDPR_TAGS = [
 {
  "COLUMN_NAME": "EMAIL",
  "TAG_NAME": "GDPR_CATEGORY",
  "TAG_VALUE": "contact"
 },
 {
  "COLUMN_NAME": "EMAIL",
  "TAG_NAME": "LAWFUL_BASIS",
  "TAG_VALUE": "contract"
 },
 {
  "COLUMN_NAME": "EMAIL",
  "TAG_NAME": "RETENTION_DAYS",
  "TAG_VALUE": "730"
 },
 {
  "COLUMN_NAME": "HEALTH_NOTES",
  "TAG_NAME": "GDPR_CATEGORY",
  "TAG_VALUE": "special_category"
 },
 {
  "COLUMN_NAME": "HEALTH_NOTES",
  "TAG_NAME": "LAWFUL_BASIS",
  "TAG_VALUE": "explicit_consent"
 },
 {
  "COLUMN_NAME": "HEALTH_NOTES",
  "TAG_NAME": "RETENTION_DAYS",
  "TAG_VALUE": "30"
 },
 {
  "COLUMN_NAME": "MARKETING_CONSENT",
  "TAG_NAME": "GDPR_CATEGORY",
  "TAG_VALUE": "behavioural"
 },
 {
  "COLUMN_NAME": "MARKETING_CONSENT",
  "TAG_NAME": "LAWFUL_BASIS",
  "TAG_VALUE": "consent"
 },
 {
  "COLUMN_NAME": "MEMBER_ID",
  "TAG_NAME": "GDPR_CATEGORY",
  "TAG_VALUE": "identifier"
 },
 {
  "COLUMN_NAME": "MEMBER_ID",
  "TAG_NAME": "LAWFUL_BASIS",
  "TAG_VALUE": "contract"
 },
 {
  "COLUMN_NAME": "MEMBER_ID",
  "TAG_NAME": "RETENTION_DAYS",
  "TAG_VALUE": "730"
 },
 {
  "COLUMN_NAME": "PHONE",
  "TAG_NAME": "GDPR_CATEGORY",
  "TAG_VALUE": "contact"
 },
 {
  "COLUMN_NAME": "PHONE",
  "TAG_NAME": "LAWFUL_BASIS",
  "TAG_VALUE": "contract"
 },
 {
  "COLUMN_NAME": "PHONE",
  "TAG_NAME": "RETENTION_DAYS",
  "TAG_VALUE": "730"
 }
]

B2_MASKED_OWNER = [
 {
  "MEMBER_ID": "M-01000",
  "FIRST_NAME": "*** MASKED ***",
  "EMAIL": "*****@example.co.uk",
  "DATE_OF_BIRTH": "1970-01-01",
  "HEALTH_NOTES": "*** MASKED ***"
 },
 {
  "MEMBER_ID": "M-01001",
  "FIRST_NAME": "*** MASKED ***",
  "EMAIL": "*****@example.co.uk",
  "DATE_OF_BIRTH": "1982-01-01",
  "HEALTH_NOTES": "*** MASKED ***"
 },
 {
  "MEMBER_ID": "M-01002",
  "FIRST_NAME": "*** MASKED ***",
  "EMAIL": "*****@example.co.uk",
  "DATE_OF_BIRTH": "1997-01-01",
  "HEALTH_NOTES": "*** MASKED ***"
 }
]

B2_REQUESTS = [
 {
  "OPERATOR_ID": "RIVERSIDE_NIELS",
  "MEMBER_ID": "M-01042",
  "REQUEST_TYPE": "ERASURE",
  "COMPLETED": True,
  "EVIDENCE": "{\n  \"attendance_deleted\": 6,\n  \"bookings_deleted\": 8,\n  \"member_rows\": 1,\n  \"payments_pseudonymised\": 3,\n  \"token\": \"ERASED-96235932dc8ea9c1\"\n}"
 },
 {
  "OPERATOR_ID": "RIVERSIDE_NIELS",
  "MEMBER_ID": "M-01043",
  "REQUEST_TYPE": "SAR",
  "COMPLETED": True,
  "EVIDENCE": "[\n  \"MEMBERS__MEMBER\",\n  \"MEMBERS__MEMBERSHIP\",\n  \"SYSTEM__ATTENDANCE\",\n  \"SYSTEM__BOOKING\",\n  \"SYSTEM__PAYMENT\"\n]"
 }
]

B2_RETENTION = [
 {
  "name": "MEMBERS__MEMBER",
  "retention_time": "1",
  "change_tracking": "ON"
 }
]

B2_SAR = [
 {
  "SAR_EXPORT": "{\n  \"data\": {\n    \"MEMBERS__MEMBER\": [\n      {\n        \"DATE_OF_BIRTH\": \"1967-03-10\",\n        \"EMAIL\": \"member1043@example.co.uk\",\n        \"FIRST_NAME\": \"Amelia\",\n        \"HEALTH_NOTES\": \"Asthma - inhaler on poolside\",\n        \"HOME_SITE_ID\": \"S01\",\n        \"JOINED_ON\": \"2023-06-04\",\n        \"LAST_ACTIVITY_AT\": \"2026-10-11 09:26:54.093 -0700\",\n        \"LAST_NAME\": \"Smith\",\n        \"MARKETING_CONSENT\": False,\n        \"MEMBER_ID\": \"M-01043\",\n        \"OPERATOR_ID\": \"RIVERSIDE\",\n        \"PHONE\": \"07700 938200\",\n        \"POSTCODE\": \"OX1 4AB\",\n        \"STATUS\": \"ACTIVE\",\n        \"_BATCH_ID\": \"B-SEED\",\n        \"_LOADED_AT\": \"2026-10-16 09:26:54.093 -0700\"\n      }\n    ],\n    \"MEMBERS__MEMBERSHIP\": [\n      {\n        \"LAST_PAID_ON\": \"2026-10-05\",\n        \"MEMBERSHIP_ID\": \"MS-01043\",\n        \"MEMBER_ID\": \"M-01043\",\n        \"MONTHLY_FEE\": 49.99,\n        \"OPERATOR_ID\": \"RIVERSIDE\",\n        \"PLAN_NAME\": \"Premium Plus\",\n        \"START_DATE\": \"2023-06-04\",\n        \"_LOADED_AT\": \"2026-10-16 09:26:54.832 -0700\"\n      }\n    ],\n    \"SYSTEM__ATTENDANCE\": [\n      {\n        \"ATTENDANCE_ID\": \"AT-000206\",\n        \"BOOKING_ID\": \"BK-000206\",\n        \"CHECKED_IN_AT\": \"2026-10-12 19:46:55.513 -0700\",\n        \"MEMBER_ID\": \"M-01043\",\n        \"OPERATOR_ID\": \"RIVERSIDE\",\n        \"_LOADED_AT\": \"2026-10-16 09:26:56.213 -0700\"\n      },\n      {\n        \"ATTENDANCE_ID\": \"AT-003371\",\n        \"BOOKING_ID\": \"BK-003371\",\n        \"CHECKED_IN_AT\": \"2026-09-21 15:25:55.513 -0700\",\n        \"MEMBER_ID\": \"M-01043\",\n        \"OPERATOR_ID\": \"RIVERSIDE\",\n        \"_LOADED_AT\": \"2026-10-16 09:26:56.213 -0700\"\n      },\n      {\n        \"ATTENDANCE_ID\": \"AT-006995\",\n        \"BOOKING_ID\": \"BK-006995\",\n        \"CHECKED_IN_AT\": \"2026-10-06 03:52:55.513 -0700\",\n        \"MEMBER_ID\": \"M-01043\",\n        \"OPERATOR_ID\": \"RIVERSIDE\",\n        \"_LOADED_AT\": \"2026-10-16 09:26:56.213 -0700\"\n      },\n      {\n        \"ATTENDANCE_ID\": \"AT-008122\",\n        \"BOOKING_ID\": \"BK-008122\",\n        \"CHECKED_IN_AT\": \"2026-10-11 10:05:55.513 -0700\",\n        \"MEMBER_ID\": \"M-01043\",\n        \"OPERATOR_ID\": \"RIVERSIDE\",\n        \"_LOADED_AT\": \"2026-10-16 09:26:56.213 -0700\"\n      }\n    ],\n    \"SYSTEM__BOOKING\": [\n      {\n        \"ACTIVITY_ID\": \"A00465\",\n        \"BOOKED_AT\": \"2026-10-12 19:41:55.513 -0700\",\n        \"BOOKING_ID\": \"BK-000206\",\n        \"MEMBER_ID\": \"M-01043\",\n        \"OPERATOR_ID\": \"RIVERSIDE\",\n        \"_LOADED_AT\": \"2026-10-16 09:26:55.513 -0700\"\n      },\n      {\n        \"ACTIVITY_ID\": \"A00246\",\n        \"BOOKED_AT\": \"2026-09-21 15:20:55.513 -0700\",\n        \"BOOKING_ID\": \"BK-003371\",\n        \"MEMBER_ID\": \"M-01043\",\n        \"OPERATOR_ID\": \"RIVERSIDE\",\n        \"_LOADED_AT\": \"2026-10-16 09:26:55.513 -0700\"\n      },\n      {\n        \"ACTIVITY_ID\": \"A00459\",\n        \"BOOKED_AT\": \"2026-10-06 03:47:55.513 -0700\",\n        \"BOOKING_ID\": \"BK-006995\",\n        \"MEMBER_ID\": \"M-01043\",\n        \"OPERATOR_ID\": \"RIVERSIDE\",\n        \"_LOADED_AT\": \"2026-10-16 09:26:55.513 -0700\"\n      },\n      {\n        \"ACTIVITY_ID\": \"A00566\",\n        \"BOOKED_AT\": \"2026-10-11 10:00:55.513 -0700\",\n        \"BOOKING_ID\": \"BK-008122\",\n        \"MEMBER_ID\": \"M-01043\",\n        \"OPERATOR_ID\": \"RIVERSIDE\",\n        \"_LOADED_AT\": \"2026-10-16 09:26:55.513 -0700\"\n      }\n    ],\n    \"SYSTEM__PAYMENT\": [\n      {\n        \"AMOUNT\": 49.99,\n        \"MEMBER_ID\": \"M-01043\",\n        \"OPERATOR_ID\": \"RIVERSIDE\",\n        \"PAYMENT_DATE\": \"2026-10-05\",\n        \"PAYMENT_ID\": \"PY-0001691\",\n        \"PAYMENT_TYPE\": \"PAYMENT\",\n        \"_BATCH_ID\": \"B-SEED\",\n        \"_LOADED_AT\": \"2026-10-16 09:26:56.981 -0700\"\n      },\n      {\n        \"AMOUNT\": 24.99,\n        \"MEMBER_ID\": \"M-01043\",\n        \"OPERATOR_ID\": \"RIVERSIDE\",\n        \"PAYMENT_DATE\": \"2026-10-07\",\n        \"PAYMENT_ID\": \"PY-0001885\",\n        \"PAYMENT_TYPE\": \"PAYMENT\",\n        \"_BATCH_ID\": \"B-SEED\",\n        \"_LOADED_AT\": \"2026-10-16 09:26:56.981 -0700\"\n      },\n      {\n        \"AMOUNT\": 24.99,\n        \"MEMBER_ID\": \"M-01043\",\n        \"OPERATOR_ID\": \"RIVERSIDE\",\n        \"PAYMENT_DATE\": \"2026-09-23\",\n        \"PAYMENT_ID\": \"PY-0003635\",\n        \"PAYMENT_TYPE\": \"PAYMENT\",\n        \"_BATCH_ID\": \"B-SEED\",\n        \"_LOADED_AT\": \"2026-10-16 09:26:56.981 -0700\"\n      }\n    ]\n  },\n  \"generated_at\": \"2026-10-16 09:55:03.551 -0700\",\n  \"member_id\": \"M-01043\",\n  \"note\": \"REPORTING dynamic tables hold aggregates only (no member_id)\",\n  \"operator\": \"RIVERSIDE_NIELS\"\n}"
 }
]

B2_SITE_OWNER = [
 {
  "HOME_SITE_ID": "S01",
  "MEMBERS": 670
 },
 {
  "HOME_SITE_ID": "S02",
  "MEMBERS": 664
 },
 {
  "HOME_SITE_ID": "S03",
  "MEMBERS": 666
 }
]

B2_SITE_VIEWER = [
 {
  "HOME_SITE_ID": "S01",
  "MEMBERS": 670
 }
]

B2_SV_DESCRIBE = [
 {
  "object_kind": None,
  "object_name": None,
  "property": "COMMENT",
  "property_value": "Nova Gold layer for Riverside Leisure"
 },
 {
  "object_kind": "CUSTOM_INSTRUCTION",
  "object_name": None,
  "property": "AI_SQL_GENERATION",
  "property_value": "Unless the user says otherwise, \"active members\" means the active_members metric (source status)."
 },
 {
  "object_kind": "AI_VERIFIED_QUERY",
  "object_name": "VQ_ACTIVE_MEMBERS",
  "property": "QUESTION",
  "property_value": "How many active members do we have?"
 },
 {
  "object_kind": "AI_VERIFIED_QUERY",
  "object_name": "VQ_ACTIVE_MEMBERS",
  "property": "SQL",
  "property_value": "SELECT COUNT_IF(last_paid_on >= DATEADD(day, -35, CURRENT_DATE())) AS active_members FROM GLADSTONE_DQ_LITE.RIVERSIDE_NIELS.MEMBERS__MEMBERSHIP"
 },
 {
  "object_kind": "TABLE",
  "object_name": "AM",
  "property": "BASE_TABLE_DATABASE_NAME",
  "property_value": "GLADSTONE_DQ_LITE"
 },
 {
  "object_kind": "TABLE",
  "object_name": "AM",
  "property": "BASE_TABLE_SCHEMA_NAME",
  "property_value": "RIVERSIDE_NIELS"
 },
 {
  "object_kind": "TABLE",
  "object_name": "AM",
  "property": "BASE_TABLE_NAME",
  "property_value": "REPORTING__ACTIVE_MEMBERS"
 },
 {
  "object_kind": "TABLE",
  "object_name": "AM",
  "property": "PRIMARY_KEY",
  "property_value": "[\"SITE_ID\"]"
 },
 {
  "object_kind": "METRIC",
  "object_name": "ACTIVE_MEMBERS",
  "property": "TABLE",
  "property_value": "AM"
 },
 {
  "object_kind": "METRIC",
  "object_name": "ACTIVE_MEMBERS",
  "property": "EXPRESSION",
  "property_value": "SUM(am.active_members)"
 },
 {
  "object_kind": "METRIC",
  "object_name": "ACTIVE_MEMBERS",
  "property": "DATA_TYPE",
  "property_value": "NUMBER(25,0)"
 },
 {
  "object_kind": "METRIC",
  "object_name": "ACTIVE_MEMBERS",
  "property": "SYNONYMS",
  "property_value": "[\"members\",\"active members\"]"
 },
 {
  "object_kind": "METRIC",
  "object_name": "ACTIVE_MEMBERS",
  "property": "COMMENT",
  "property_value": "Members whose source status is ACTIVE"
 },
 {
  "object_kind": "METRIC",
  "object_name": "ACTIVE_MEMBERS",
  "property": "ACCESS_MODIFIER",
  "property_value": "PUBLIC"
 },
 {
  "object_kind": "DIMENSION",
  "object_name": "SITE_ID",
  "property": "TABLE",
  "property_value": "AM"
 },
 {
  "object_kind": "DIMENSION",
  "object_name": "SITE_ID",
  "property": "EXPRESSION",
  "property_value": "am.site_id"
 },
 {
  "object_kind": "DIMENSION",
  "object_name": "SITE_ID",
  "property": "DATA_TYPE",
  "property_value": "VARCHAR(16777216)"
 },
 {
  "object_kind": "DIMENSION",
  "object_name": "SITE_ID",
  "property": "COMMENT",
  "property_value": "Site"
 },
 {
  "object_kind": "DIMENSION",
  "object_name": "SITE_ID",
  "property": "ACCESS_MODIFIER",
  "property_value": "PUBLIC"
 },
 {
  "object_kind": "TABLE",
  "object_name": "MS",
  "property": "BASE_TABLE_DATABASE_NAME",
  "property_value": "GLADSTONE_DQ_LITE"
 },
 {
  "object_kind": "TABLE",
  "object_name": "MS",
  "property": "BASE_TABLE_SCHEMA_NAME",
  "property_value": "RIVERSIDE_NIELS"
 },
 {
  "object_kind": "TABLE",
  "object_name": "MS",
  "property": "BASE_TABLE_NAME",
  "property_value": "MEMBERS__MEMBERSHIP"
 },
 {
  "object_kind": "TABLE",
  "object_name": "MS",
  "property": "PRIMARY_KEY",
  "property_value": "[\"MEMBERSHIP_ID\"]"
 },
 {
  "object_kind": "METRIC",
  "object_name": "PAID_MEMBERS_35D",
  "property": "TABLE",
  "property_value": "MS"
 },
 {
  "object_kind": "METRIC",
  "object_name": "PAID_MEMBERS_35D",
  "property": "EXPRESSION",
  "property_value": "COUNT_IF(ms.last_paid_on >= DATEADD(day, -35, CURRENT_DATE()))"
 },
 {
  "object_kind": "METRIC",
  "object_name": "PAID_MEMBERS_35D",
  "property": "DATA_TYPE",
  "property_value": "NUMBER(13,0)"
 },
 {
  "object_kind": "METRIC",
  "object_name": "PAID_MEMBERS_35D",
  "property": "COMMENT",
  "property_value": "Members who paid in the last 35 days (finance definition)"
 },
 {
  "object_kind": "METRIC",
  "object_name": "PAID_MEMBERS_35D",
  "property": "ACCESS_MODIFIER",
  "property_value": "PUBLIC"
 },
 {
  "object_kind": "DIMENSION",
  "object_name": "PLAN_NAME",
  "property": "TABLE",
  "property_value": "MS"
 },
 {
  "object_kind": "DIMENSION",
  "object_name": "PLAN_NAME",
  "property": "EXPRESSION",
  "property_value": "ms.plan_name"
 },
 {
  "object_kind": "DIMENSION",
  "object_name": "PLAN_NAME",
  "property": "DATA_TYPE",
  "property_value": "VARCHAR(16777216)"
 },
 {
  "object_kind": "DIMENSION",
  "object_name": "PLAN_NAME",
  "property": "COMMENT",
  "property_value": "Membership plan"
 },
 {
  "object_kind": "DIMENSION",
  "object_name": "PLAN_NAME",
  "property": "ACCESS_MODIFIER",
  "property_value": "PUBLIC"
 },
 {
  "object_kind": "TABLE",
  "object_name": "REV",
  "property": "BASE_TABLE_DATABASE_NAME",
  "property_value": "GLADSTONE_DQ_LITE"
 },
 {
  "object_kind": "TABLE",
  "object_name": "REV",
  "property": "BASE_TABLE_SCHEMA_NAME",
  "property_value": "RIVERSIDE_NIELS"
 },
 {
  "object_kind": "TABLE",
  "object_name": "REV",
  "property": "BASE_TABLE_NAME",
  "property_value": "REPORTING__DAILY_REVENUE"
 },
 {
  "object_kind": "TABLE",
  "object_name": "REV",
  "property": "PRIMARY_KEY",
  "property_value": "[\"PAYMENT_DATE\"]"
 },
 {
  "object_kind": "METRIC",
  "object_name": "NET_REVENUE",
  "property": "TABLE",
  "property_value": "REV"
 },
 {
  "object_kind": "METRIC",
  "object_name": "NET_REVENUE",
  "property": "EXPRESSION",
  "property_value": "SUM(rev.net_revenue)"
 },
 {
  "object_kind": "METRIC",
  "object_name": "NET_REVENUE",
  "property": "DATA_TYPE",
  "property_value": "NUMBER(34,2)"
 },
 {
  "object_kind": "METRIC",
  "object_name": "NET_REVENUE",
  "property": "COMMENT",
  "property_value": "Payments minus refunds, GBP"
 },
 {
  "object_kind": "METRIC",
  "object_name": "NET_REVENUE",
  "property": "ACCESS_MODIFIER",
  "property_value": "PUBLIC"
 },
 {
  "object_kind": "DIMENSION",
  "object_name": "PAYMENT_DATE",
  "property": "TABLE",
  "property_value": "REV"
 },
 {
  "object_kind": "DIMENSION",
  "object_name": "PAYMENT_DATE",
  "property": "EXPRESSION",
  "property_value": "rev.payment_date"
 },
 {
  "object_kind": "DIMENSION",
  "object_name": "PAYMENT_DATE",
  "property": "DATA_TYPE",
  "property_value": "DATE"
 },
 {
  "object_kind": "DIMENSION",
  "object_name": "PAYMENT_DATE",
  "property": "COMMENT",
  "property_value": "Payment date"
 },
 {
  "object_kind": "DIMENSION",
  "object_name": "PAYMENT_DATE",
  "property": "ACCESS_MODIFIER",
  "property_value": "PUBLIC"
 },
 {
  "object_kind": "TABLE",
  "object_name": "UTIL",
  "property": "BASE_TABLE_DATABASE_NAME",
  "property_value": "GLADSTONE_DQ_LITE"
 },
 {
  "object_kind": "TABLE",
  "object_name": "UTIL",
  "property": "BASE_TABLE_SCHEMA_NAME",
  "property_value": "RIVERSIDE_NIELS"
 },
 {
  "object_kind": "TABLE",
  "object_name": "UTIL",
  "property": "BASE_TABLE_NAME",
  "property_value": "REPORTING__CLASS_UTILISATION"
 },
 {
  "object_kind": "TABLE",
  "object_name": "UTIL",
  "property": "PRIMARY_KEY",
  "property_value": "[\"ACTIVITY_ID\"]"
 },
 {
  "object_kind": "DIMENSION",
  "object_name": "CLASS_DATE",
  "property": "TABLE",
  "property_value": "UTIL"
 },
 {
  "object_kind": "DIMENSION",
  "object_name": "CLASS_DATE",
  "property": "EXPRESSION",
  "property_value": "util.class_date"
 },
 {
  "object_kind": "DIMENSION",
  "object_name": "CLASS_DATE",
  "property": "DATA_TYPE",
  "property_value": "DATE"
 },
 {
  "object_kind": "DIMENSION",
  "object_name": "CLASS_DATE",
  "property": "COMMENT",
  "property_value": "Class date"
 },
 {
  "object_kind": "DIMENSION",
  "object_name": "CLASS_DATE",
  "property": "ACCESS_MODIFIER",
  "property_value": "PUBLIC"
 },
 {
  "object_kind": "DIMENSION",
  "object_name": "CLASS_NAME",
  "property": "TABLE",
  "property_value": "UTIL"
 },
 {
  "object_kind": "DIMENSION",
  "object_name": "CLASS_NAME",
  "property": "EXPRESSION",
  "property_value": "util.class_name"
 },
 {
  "object_kind": "DIMENSION",
  "object_name": "CLASS_NAME",
  "property": "DATA_TYPE",
  "property_value": "VARCHAR(16777216)"
 },
 {
  "object_kind": "DIMENSION",
  "object_name": "CLASS_NAME",
  "property": "COMMENT",
  "property_value": "Class type"
 },
 {
  "object_kind": "DIMENSION",
  "object_name": "CLASS_NAME",
  "property": "ACCESS_MODIFIER",
  "property_value": "PUBLIC"
 },
 {
  "object_kind": "DIMENSION",
  "object_name": "CLASS_SITE",
  "property": "TABLE",
  "property_value": "UTIL"
 },
 {
  "object_kind": "DIMENSION",
  "object_name": "CLASS_SITE",
  "property": "EXPRESSION",
  "property_value": "util.site_id"
 },
 {
  "object_kind": "DIMENSION",
  "object_name": "CLASS_SITE",
  "property": "DATA_TYPE",
  "property_value": "VARCHAR(16777216)"
 },
 {
  "object_kind": "DIMENSION",
  "object_name": "CLASS_SITE",
  "property": "COMMENT",
  "property_value": "Site of the class"
 },
 {
  "object_kind": "DIMENSION",
  "object_name": "CLASS_SITE",
  "property": "ACCESS_MODIFIER",
  "property_value": "PUBLIC"
 },
 {
  "object_kind": "METRIC",
  "object_name": "NO_SHOW_RATE",
  "property": "TABLE",
  "property_value": "UTIL"
 },
 {
  "object_kind": "METRIC",
  "object_name": "NO_SHOW_RATE",
  "property": "EXPRESSION",
  "property_value": "DIV0(SUM(util.bookings) - SUM(util.attended), SUM(util.bookings)) * 100"
 },
 {
  "object_kind": "METRIC",
  "object_name": "NO_SHOW_RATE",
  "property": "DATA_TYPE",
  "property_value": "NUMBER(38,6)"
 },
 {
  "object_kind": "METRIC",
  "object_name": "NO_SHOW_RATE",
  "property": "COMMENT",
  "property_value": "Booked but did not attend, percent"
 },
 {
  "object_kind": "METRIC",
  "object_name": "NO_SHOW_RATE",
  "property": "ACCESS_MODIFIER",
  "property_value": "PUBLIC"
 },
 {
  "object_kind": "METRIC",
  "object_name": "UTILISATION_PCT",
  "property": "TABLE",
  "property_value": "UTIL"
 },
 {
  "object_kind": "METRIC",
  "object_name": "UTILISATION_PCT",
  "property": "EXPRESSION",
  "property_value": "DIV0(SUM(util.attended), SUM(util.capacity)) * 100"
 },
 {
  "object_kind": "METRIC",
  "object_name": "UTILISATION_PCT",
  "property": "DATA_TYPE",
  "property_value": "NUMBER(38,6)"
 },
 {
  "object_kind": "METRIC",
  "object_name": "UTILISATION_PCT",
  "property": "COMMENT",
  "property_value": "Attended places as a percentage of capacity"
 },
 {
  "object_kind": "METRIC",
  "object_name": "UTILISATION_PCT",
  "property": "ACCESS_MODIFIER",
  "property_value": "PUBLIC"
 }
]

B2_TIMETRAVEL = [
 {
  "STILL_IN_TIME_TRAVEL": 1
 }
]

B2_VIEWER_ROWS = [
 {
  "MEMBER_ID": "M-01002",
  "HOME_SITE_ID": "S01",
  "FIRST_NAME": "*** MASKED ***",
  "EMAIL": "*****@example.co.uk",
  "HEALTH_NOTES": "*** MASKED ***"
 },
 {
  "MEMBER_ID": "M-01007",
  "HOME_SITE_ID": "S01",
  "FIRST_NAME": "*** MASKED ***",
  "EMAIL": "*****@example.co.uk",
  "HEALTH_NOTES": "*** MASKED ***"
 },
 {
  "MEMBER_ID": "M-01014",
  "HOME_SITE_ID": "S01",
  "FIRST_NAME": "*** MASKED ***",
  "EMAIL": "*****@example.co.uk",
  "HEALTH_NOTES": "*** MASKED ***"
 }
]

F_FAULTS = [
 {
  "SHORT_NAME": "NIELS",
  "FAULT_NO": 1,
  "FAULT_CODE": "BIFROST_REPLAY",
  "DESCRIPTION": "Merge batch B-REPLAY-01 applied twice: 150 duplicate member rows; active members inflated",
  "CAUGHT_BY": "no_duplicate_members (DUPLICATE_COUNT on MEMBERS__MEMBER.member_id)"
 },
 {
  "SHORT_NAME": "NIELS",
  "FAULT_NO": 2,
  "FAULT_CODE": "REFUND_SIGN_FLIP",
  "DESCRIPTION": "Refunds sent as negative PAYMENT rows (batch B-SIGNBUG-01); today's net revenue collapses",
  "CAUGHT_BY": "no_negative_amounts (NEGATIVE_COUNT on SYSTEM__PAYMENT.amount)"
 },
 {
  "SHORT_NAME": "NIELS",
  "FAULT_NO": 3,
  "FAULT_CODE": "MERGE_TASK_STALLED",
  "DESCRIPTION": "Bifrost merge task stopped: no new payments or bookings arrive",
  "CAUGHT_BY": "payments_fresh_3min (FRESHNESS on SYSTEM__PAYMENT)"
 }
]

F_INJECT_1 = [
 {
  "INJECT": "Fault 1 (BIFROST_REPLAY) injected into 2 pipeline(s)"
 }
]

F_INJECT_2 = [
 {
  "INJECT": "Fault 2 (REFUND_SIGN_FLIP) injected into 2 pipeline(s)"
 }
]

F_INJECT_3 = [
 {
  "INJECT": "Fault 3 (MERGE_TASK_STALLED) injected into 2 pipeline(s)"
 }
]

F_INJECT_4 = [
 {
  "INJECT": "Fault 4 (STATUS_DRIFT) injected into 2 pipeline(s)"
 }
]

F_INJECT_5 = [
 {
  "INJECT": "Fault 5 (VOLUME_DROP) injected into 1 pipeline(s)"
 }
]

S1_COUNTS = [
 {
  "T": "MEMBERS__MEMBER",
  "N": 2000
 },
 {
  "T": "SYSTEM__BOOKING",
  "N": 9020
 },
 {
  "T": "SYSTEM__ATTENDANCE",
  "N": 7411
 },
 {
  "T": "SYSTEM__PAYMENT",
  "N": 6030
 },
 {
  "T": "_SYNC_META__MERGE_BATCH",
  "N": 7
 }
]

S1_DTS = [
 {
  "name": "REPORTING__ACTIVE_MEMBERS",
  "target_lag": "1 minute",
  "refresh_mode": "INCREMENTAL",
  "scheduling_state": "ACTIVE",
  "rows": 3
 },
 {
  "name": "REPORTING__CLASS_UTILISATION",
  "target_lag": "1 minute",
  "refresh_mode": "INCREMENTAL",
  "scheduling_state": "ACTIVE",
  "rows": 600
 },
 {
  "name": "REPORTING__DAILY_REVENUE",
  "target_lag": "1 minute",
  "refresh_mode": "INCREMENTAL",
  "scheduling_state": "ACTIVE",
  "rows": 28
 }
]

S1_OBJECTS = [
 {
  "name": "DQ_INCIDENTS",
  "kind": "TABLE",
  "comment": "Data quality incidents opened by the DQ_INCIDENT_ALERT"
 },
 {
  "name": "MEMBERS__MEMBER",
  "kind": "TABLE",
  "comment": "Bronze MEMBERS: member master (synthetic personal data)"
 },
 {
  "name": "MEMBERS__MEMBERSHIP",
  "kind": "TABLE",
  "comment": "Bronze MEMBERS: membership contracts"
 },
 {
  "name": "REPORTING__ACTIVE_MEMBERS",
  "kind": "TABLE",
  "comment": "Silver REPORTING: active members by site (status-based)"
 },
 {
  "name": "REPORTING__CLASS_UTILISATION",
  "kind": "TABLE",
  "comment": "Silver REPORTING: class bookings, attendance and capacity"
 },
 {
  "name": "REPORTING__DAILY_REVENUE",
  "kind": "TABLE",
  "comment": "Silver REPORTING: net revenue per day"
 },
 {
  "name": "SHARED__ACTIVITY",
  "kind": "TABLE",
  "comment": "Bronze SHARED: scheduled classes"
 },
 {
  "name": "SHARED__SITE",
  "kind": "TABLE",
  "comment": "Bronze SHARED: Riverside Leisure sites"
 },
 {
  "name": "SV_RIVERSIDE_KPIS",
  "kind": "VIEW",
  "comment": "Nova Gold layer for Riverside Leisure"
 },
 {
  "name": "SYSTEM__ATTENDANCE",
  "kind": "TABLE",
  "comment": "Bronze SYSTEM: turnstile / class check-ins"
 },
 {
  "name": "SYSTEM__BOOKING",
  "kind": "TABLE",
  "comment": "Bronze SYSTEM: class bookings"
 },
 {
  "name": "SYSTEM__PAYMENT",
  "kind": "TABLE",
  "comment": "Bronze SYSTEM: payments and refunds"
 },
 {
  "name": "_SYNC_META__MERGE_BATCH",
  "kind": "TABLE",
  "comment": "Sync metadata: one row per merge batch (stands in for Bifrost)"
 }
]

S1_REVENUE = [
 {
  "PAYMENT_DATE": "2026-10-14",
  "NET_REVENUE": "7168.03"
 },
 {
  "PAYMENT_DATE": "2026-10-15",
  "NET_REVENUE": "7283.07"
 },
 {
  "PAYMENT_DATE": "2026-10-16",
  "NET_REVENUE": "7772.86"
 }
]

S1_TASKS = [
 {
  "name": "TSK_BIFROST_MERGE",
  "schedule": "1 MINUTE",
  "state": "started",
  "definition": "CALL GLADSTONE_DQ_LITE.ADMIN.BIFROST_MERGE('RIVERSIDE_NIELS')"
 }
]

S1_TWO_ACTIVE = [
 {
  "ACTIVE_MEMBERS": 1598,
  "PAID_MEMBERS_35D": 1520
 }
]

S2_ALERTS = [
 {
  "name": "DQ_INCIDENT_ALERT",
  "schedule": "1 MINUTE",
  "state": "started",
  "warehouse": "DQ_LITE_WH"
 }
]

S2_ATTACHED = [
 {
  "METRIC_NAME": "ACTIVE_BUT_LEFT",
  "REF_ENTITY_NAME": "MEMBERS__MEMBER",
  "REF_ARGUMENTS": "[{\"domain\":\"COLUMN\",\"id\":\"2297015\",\"name\":\"STATUS\"},{\"domain\":\"COLUMN\",\"id\":\"2297009\",\"name\":\"LEFT_ON\"}]",
  "SCHEDULE_STATUS": "STARTED"
 },
 {
  "METRIC_NAME": "DUPLICATE_COUNT",
  "REF_ENTITY_NAME": "MEMBERS__MEMBER",
  "REF_ARGUMENTS": "[{\"domain\":\"COLUMN\",\"id\":\"2297011\",\"name\":\"MEMBER_ID\"}]",
  "SCHEDULE_STATUS": "STARTED"
 },
 {
  "METRIC_NAME": "FRESHNESS",
  "REF_ENTITY_NAME": "SYSTEM__PAYMENT",
  "REF_ARGUMENTS": "[]",
  "SCHEDULE_STATUS": "STARTED"
 },
 {
  "METRIC_NAME": "NEGATIVE_COUNT",
  "REF_ENTITY_NAME": "SYSTEM__PAYMENT",
  "REF_ARGUMENTS": "[{\"domain\":\"COLUMN\",\"id\":\"2297051\",\"name\":\"AMOUNT\"}]",
  "SCHEDULE_STATUS": "STARTED"
 },
 {
  "METRIC_NAME": "REFERENTIAL_INTEGRITY_COUNT",
  "REF_ENTITY_NAME": "SYSTEM__ATTENDANCE",
  "REF_ARGUMENTS": "[{\"domain\":\"COLUMN\",\"id\":\"2297040\",\"name\":\"BOOKING_ID\"},{\"domain\":\"TABLE\",\"name\":\"GLADSTONE_DQ_LITE.RIVERSIDE_NIELS.SYSTEM__BOOKING\",\"columns\":[{\"domain\":\"COLUMN\",\"name\":\"BOOKING_ID\"}]}]",
  "SCHEDULE_STATUS": "STARTED"
 },
 {
  "METRIC_NAME": "ROW_COUNT",
  "REF_ENTITY_NAME": "SYSTEM__BOOKING",
  "REF_ARGUMENTS": "[]",
  "SCHEDULE_STATUS": "STARTED"
 },
 {
  "METRIC_NAME": "REPORTING_LAG_SECONDS",
  "REF_ENTITY_NAME": "REPORTING__DAILY_REVENUE",
  "REF_ARGUMENTS": "[{\"domain\":\"COLUMN\",\"id\":\"2297093\",\"name\":\"LAST_LOADED_AT\"},{\"domain\":\"TABLE\",\"name\":\"GLADSTONE_DQ_LITE.RIVERSIDE_NIELS.SYSTEM__PAYMENT\",\"columns\":[{\"domain\":\"COLUMN\",\"name\":\"_LOADED_AT\"}]}]",
  "SCHEDULE_STATUS": "STARTED"
 }
]

S2_CLEAN_MEMBERS__MEMBER = [
 {
  "METRIC_NAME": "DUPLICATE_COUNT",
  "EXPECTATION_NAME": "NO_DUPLICATE_MEMBERS",
  "EXPECTATION_EXPRESSION": "VALUE = 0",
  "VALUE": 0,
  "EXPECTATION_VIOLATED": False
 },
 {
  "METRIC_NAME": "ACTIVE_BUT_LEFT",
  "EXPECTATION_NAME": "NO_ACTIVE_LEAVERS",
  "EXPECTATION_EXPRESSION": "VALUE = 0",
  "VALUE": 0,
  "EXPECTATION_VIOLATED": False
 }
]

S2_CLEAN_SYSTEM__ATTENDANCE = [
 {
  "METRIC_NAME": "REFERENTIAL_INTEGRITY_COUNT",
  "EXPECTATION_NAME": "NO_ORPHAN_CHECKINS",
  "EXPECTATION_EXPRESSION": "VALUE = 0",
  "VALUE": 0,
  "EXPECTATION_VIOLATED": False
 }
]

S2_CLEAN_SYSTEM__PAYMENT = [
 {
  "METRIC_NAME": "FRESHNESS",
  "EXPECTATION_NAME": "PAYMENTS_FRESH_3MIN",
  "EXPECTATION_EXPRESSION": "VALUE < 180",
  "VALUE": 32,
  "EXPECTATION_VIOLATED": False
 },
 {
  "METRIC_NAME": "NEGATIVE_COUNT",
  "EXPECTATION_NAME": "NO_NEGATIVE_AMOUNTS",
  "EXPECTATION_EXPRESSION": "VALUE = 0",
  "VALUE": 0,
  "EXPECTATION_VIOLATED": False
 }
]

S2_INCIDENTS_EMPTY = [
 {
  "INCIDENTS": 0
 }
]

S3_BATCHES = [
 {
  "BATCH_ID": "B-REPLAY-01",
  "TABLE_NAME": "MEMBERS__MEMBER",
  "TIMES_APPLIED": 2
 }
]

S3_BREAKER_OPEN = [
 {
  "STATE": "SUCCEEDED",
  "SCHEDULED_TIME": "2026-10-16 09:37:18",
  "RETURN_VALUE": "OPEN: 3 failing Bronze check(s) - REPORTING refresh paused"
 },
 {
  "STATE": "SUCCEEDED",
  "SCHEDULED_TIME": "2026-10-16 09:36:18",
  "RETURN_VALUE": "OPEN: 3 failing Bronze check(s) - REPORTING refresh paused"
 },
 {
  "STATE": "SUCCEEDED",
  "SCHEDULED_TIME": "2026-10-16 09:35:18",
  "RETURN_VALUE": "CLOSED: Bronze clean"
 }
]

S3_DTS_OPEN = [
 {
  "name": "REPORTING__ACTIVE_MEMBERS",
  "refresh_mode": "INCREMENTAL",
  "scheduling_state": "SUSPENDED"
 },
 {
  "name": "REPORTING__CLASS_UTILISATION",
  "refresh_mode": "INCREMENTAL",
  "scheduling_state": "ACTIVE"
 },
 {
  "name": "REPORTING__DAILY_REVENUE",
  "refresh_mode": "INCREMENTAL",
  "scheduling_state": "SUSPENDED"
 }
]

S3_FAILING = [
 {
  "TABLE_NAME": "MEMBERS__MEMBER",
  "METRIC_NAME": "DUPLICATE_COUNT",
  "EXPECTATION_NAME": "NO_DUPLICATE_MEMBERS",
  "VALUE": "150",
  "EXPECTATION_VIOLATED": True,
  "MEASUREMENT_TIME": "2026-10-16 09:35:39"
 },
 {
  "TABLE_NAME": "SYSTEM__PAYMENT",
  "METRIC_NAME": "NEGATIVE_COUNT",
  "EXPECTATION_NAME": "NO_NEGATIVE_AMOUNTS",
  "VALUE": "40",
  "EXPECTATION_VIOLATED": True,
  "MEASUREMENT_TIME": "2026-10-16 09:35:22"
 },
 {
  "TABLE_NAME": "SYSTEM__PAYMENT",
  "METRIC_NAME": "FRESHNESS",
  "EXPECTATION_NAME": "PAYMENTS_FRESH_3MIN",
  "VALUE": "295",
  "EXPECTATION_VIOLATED": True,
  "MEASUREMENT_TIME": "2026-10-16 09:35:32"
 }
]

S3_INCIDENTS = [
 {
  "OPENED_AT": "2026-10-16 09:36:01",
  "TABLE_NAME": "MEMBERS__MEMBER",
  "METRIC_NAME": "DUPLICATE_COUNT",
  "EXPECTATION_NAME": "NO_DUPLICATE_MEMBERS",
  "VALUE": "150",
  "MEASURED_AT": "2026-10-16 09:35:39"
 },
 {
  "OPENED_AT": "2026-10-16 09:36:01",
  "TABLE_NAME": "SYSTEM__PAYMENT",
  "METRIC_NAME": "NEGATIVE_COUNT",
  "EXPECTATION_NAME": "NO_NEGATIVE_AMOUNTS",
  "VALUE": "40",
  "MEASURED_AT": "2026-10-16 09:35:22"
 },
 {
  "OPENED_AT": "2026-10-16 09:36:01",
  "TABLE_NAME": "SYSTEM__PAYMENT",
  "METRIC_NAME": "FRESHNESS",
  "EXPECTATION_NAME": "PAYMENTS_FRESH_3MIN",
  "VALUE": "295",
  "MEASURED_AT": "2026-10-16 09:35:32"
 }
]

S3_NEGATIVE = [
 {
  "_BATCH_ID": "B-SIGNBUG-01",
  "ROWS_": 40,
  "TOTAL_AMOUNT": "-10000.00"
 }
]

S3_REVENUE_BRONZE = [
 {
  "PAYMENT_DATE": "2026-10-14",
  "NET_REVENUE_BRONZE": "7168.03"
 },
 {
  "PAYMENT_DATE": "2026-10-15",
  "NET_REVENUE_BRONZE": "7283.07"
 },
 {
  "PAYMENT_DATE": "2026-10-16",
  "NET_REVENUE_BRONZE": "-1177.44"
 }
]

S3_REVENUE_NOVA = [
 {
  "PAYMENT_DATE": "2026-10-14",
  "NET_REVENUE": "7168.03"
 },
 {
  "PAYMENT_DATE": "2026-10-15",
  "NET_REVENUE": "7283.07"
 },
 {
  "PAYMENT_DATE": "2026-10-16",
  "NET_REVENUE": "-1177.44"
 }
]

S3_SCAN = [
 {
  "MEMBER_ID": "M-01000",
  "STATUS": "ACTIVE",
  "_BATCH_ID": "B-SEED",
  "_LOADED_AT": "2026-10-16 09:26:54"
 },
 {
  "MEMBER_ID": "M-01000",
  "STATUS": "ACTIVE",
  "_BATCH_ID": "B-REPLAY-01",
  "_LOADED_AT": "2026-10-16 09:30:27"
 },
 {
  "MEMBER_ID": "M-01002",
  "STATUS": "ACTIVE",
  "_BATCH_ID": "B-SEED",
  "_LOADED_AT": "2026-10-16 09:26:54"
 },
 {
  "MEMBER_ID": "M-01002",
  "STATUS": "ACTIVE",
  "_BATCH_ID": "B-REPLAY-01",
  "_LOADED_AT": "2026-10-16 09:30:27"
 },
 {
  "MEMBER_ID": "M-01003",
  "STATUS": "ACTIVE",
  "_BATCH_ID": "B-SEED",
  "_LOADED_AT": "2026-10-16 09:26:54"
 },
 {
  "MEMBER_ID": "M-01003",
  "STATUS": "ACTIVE",
  "_BATCH_ID": "B-REPLAY-01",
  "_LOADED_AT": "2026-10-16 09:30:27"
 },
 {
  "MEMBER_ID": "M-01005",
  "STATUS": "ACTIVE",
  "_BATCH_ID": "B-SEED",
  "_LOADED_AT": "2026-10-16 09:26:54"
 },
 {
  "MEMBER_ID": "M-01005",
  "STATUS": "ACTIVE",
  "_BATCH_ID": "B-REPLAY-01",
  "_LOADED_AT": "2026-10-16 09:30:27"
 }
]

S3_TASK = [
 {
  "name": "TSK_BIFROST_MERGE",
  "schedule": "1 MINUTE",
  "state": "suspended"
 }
]

S3_TWO_ACTIVE = [
 {
  "ACTIVE_MEMBERS": 1748,
  "PAID_MEMBERS_35D": 1520
 }
]

S4_BREAKER_CLOSED = [
 {
  "STATE": "SUCCEEDED",
  "SCHEDULED_TIME": "2026-10-16 09:47:18",
  "RETURN_VALUE": "CLOSED: Bronze clean"
 },
 {
  "STATE": "SUCCEEDED",
  "SCHEDULED_TIME": "2026-10-16 09:46:18",
  "RETURN_VALUE": "CLOSED: Bronze clean"
 },
 {
  "STATE": "SUCCEEDED",
  "SCHEDULED_TIME": "2026-10-16 09:45:18",
  "RETURN_VALUE": "OPEN: 4 failing Bronze check(s) - REPORTING refresh paused"
 }
]

S4_DTS_CLOSED = [
 {
  "name": "REPORTING__ACTIVE_MEMBERS",
  "refresh_mode": "INCREMENTAL",
  "scheduling_state": "ACTIVE"
 },
 {
  "name": "REPORTING__CLASS_UTILISATION",
  "refresh_mode": "INCREMENTAL",
  "scheduling_state": "ACTIVE"
 },
 {
  "name": "REPORTING__DAILY_REVENUE",
  "refresh_mode": "INCREMENTAL",
  "scheduling_state": "ACTIVE"
 }
]

S4_FIX = [
 {
  "FIX": "replayed members",
  "ROWS_": 150
 },
 {
  "FIX": "negative payments",
  "ROWS_": 40
 },
 {
  "FIX": "status drift",
  "ROWS_": 292
 }
]

S4_HEALTH_FAIL = [
 {
  "TABLE_NAME": "MEMBERS__MEMBER",
  "EXPECTATION_NAME": "NO_DUPLICATE_MEMBERS",
  "METRIC_NAME": "DUPLICATE_COUNT",
  "VALUE": "150",
  "STATUS": "FAILING",
  "LAST_CHECKED": "2026-10-16 09:40:53",
  "FIRST_INCIDENT_AT": "2026-10-16 09:36:01",
  "INCIDENTS": 2
 },
 {
  "TABLE_NAME": "MEMBERS__MEMBER",
  "EXPECTATION_NAME": "NO_ACTIVE_LEAVERS",
  "METRIC_NAME": "ACTIVE_BUT_LEFT",
  "VALUE": "292",
  "STATUS": "FAILING",
  "LAST_CHECKED": "2026-10-16 09:40:30",
  "FIRST_INCIDENT_AT": "2026-10-16 09:41:06",
  "INCIDENTS": 1
 },
 {
  "TABLE_NAME": "SYSTEM__PAYMENT",
  "EXPECTATION_NAME": "PAYMENTS_FRESH_3MIN",
  "METRIC_NAME": "FRESHNESS",
  "VALUE": "578",
  "STATUS": "FAILING",
  "LAST_CHECKED": "2026-10-16 09:40:15",
  "FIRST_INCIDENT_AT": "2026-10-16 09:36:01",
  "INCIDENTS": 2
 },
 {
  "TABLE_NAME": "SYSTEM__PAYMENT",
  "EXPECTATION_NAME": "NO_NEGATIVE_AMOUNTS",
  "METRIC_NAME": "NEGATIVE_COUNT",
  "VALUE": "40",
  "STATUS": "FAILING",
  "LAST_CHECKED": "2026-10-16 09:40:48",
  "FIRST_INCIDENT_AT": "2026-10-16 09:36:01",
  "INCIDENTS": 2
 },
 {
  "TABLE_NAME": "REPORTING__DAILY_REVENUE",
  "EXPECTATION_NAME": "REPORTING_WITHIN_5MIN",
  "METRIC_NAME": "REPORTING_LAG_SECONDS",
  "VALUE": "0",
  "STATUS": "OK",
  "LAST_CHECKED": "2026-10-16 09:40:20",
  "FIRST_INCIDENT_AT": None,
  "INCIDENTS": 0
 },
 {
  "TABLE_NAME": "SYSTEM__ATTENDANCE",
  "EXPECTATION_NAME": "NO_ORPHAN_CHECKINS",
  "METRIC_NAME": "REFERENTIAL_INTEGRITY_COUNT",
  "VALUE": "0",
  "STATUS": "OK",
  "LAST_CHECKED": "2026-10-16 09:40:57",
  "FIRST_INCIDENT_AT": None,
  "INCIDENTS": 0
 }
]

S4_HEALTH_OK = [
 {
  "TABLE_NAME": "REPORTING__DAILY_REVENUE",
  "EXPECTATION_NAME": "REPORTING_WITHIN_5MIN",
  "METRIC_NAME": "REPORTING_LAG_SECONDS",
  "VALUE": "851",
  "STATUS": "FAILING",
  "LAST_CHECKED": "2026-10-16 09:45:19",
  "FIRST_INCIDENT_AT": "2026-10-16 09:46:00",
  "INCIDENTS": 1
 },
 {
  "TABLE_NAME": "MEMBERS__MEMBER",
  "EXPECTATION_NAME": "NO_ACTIVE_LEAVERS",
  "METRIC_NAME": "ACTIVE_BUT_LEFT",
  "VALUE": "0",
  "STATUS": "OK",
  "LAST_CHECKED": "2026-10-16 09:45:43",
  "FIRST_INCIDENT_AT": "2026-10-16 09:41:06",
  "INCIDENTS": 1
 },
 {
  "TABLE_NAME": "MEMBERS__MEMBER",
  "EXPECTATION_NAME": "NO_DUPLICATE_MEMBERS",
  "METRIC_NAME": "DUPLICATE_COUNT",
  "VALUE": "0",
  "STATUS": "OK",
  "LAST_CHECKED": "2026-10-16 09:45:14",
  "FIRST_INCIDENT_AT": "2026-10-16 09:36:01",
  "INCIDENTS": 2
 },
 {
  "TABLE_NAME": "SYSTEM__ATTENDANCE",
  "EXPECTATION_NAME": "NO_ORPHAN_CHECKINS",
  "METRIC_NAME": "REFERENTIAL_INTEGRITY_COUNT",
  "VALUE": "0",
  "STATUS": "OK",
  "LAST_CHECKED": "2026-10-16 09:45:49",
  "FIRST_INCIDENT_AT": None,
  "INCIDENTS": 0
 },
 {
  "TABLE_NAME": "SYSTEM__PAYMENT",
  "EXPECTATION_NAME": "NO_NEGATIVE_AMOUNTS",
  "METRIC_NAME": "NEGATIVE_COUNT",
  "VALUE": "0",
  "STATUS": "OK",
  "LAST_CHECKED": "2026-10-16 09:45:24",
  "FIRST_INCIDENT_AT": "2026-10-16 09:36:01",
  "INCIDENTS": 2
 },
 {
  "TABLE_NAME": "SYSTEM__PAYMENT",
  "EXPECTATION_NAME": "PAYMENTS_FRESH_3MIN",
  "METRIC_NAME": "FRESHNESS",
  "VALUE": "0",
  "STATUS": "OK",
  "LAST_CHECKED": "2026-10-16 09:45:48",
  "FIRST_INCIDENT_AT": "2026-10-16 09:36:01",
  "INCIDENTS": 2
 }
]

S4_HEALTH_OK2 = [
 {
  "TABLE_NAME": "MEMBERS__MEMBER",
  "EXPECTATION_NAME": "NO_ACTIVE_LEAVERS",
  "METRIC_NAME": "ACTIVE_BUT_LEFT",
  "VALUE": "0",
  "STATUS": "OK",
  "LAST_CHECKED": "2026-10-16 09:50:26",
  "FIRST_INCIDENT_AT": "2026-10-16 09:41:06",
  "INCIDENTS": 1
 },
 {
  "TABLE_NAME": "MEMBERS__MEMBER",
  "EXPECTATION_NAME": "NO_DUPLICATE_MEMBERS",
  "METRIC_NAME": "DUPLICATE_COUNT",
  "VALUE": "0",
  "STATUS": "OK",
  "LAST_CHECKED": "2026-10-16 09:50:22",
  "FIRST_INCIDENT_AT": "2026-10-16 09:36:01",
  "INCIDENTS": 2
 },
 {
  "TABLE_NAME": "REPORTING__DAILY_REVENUE",
  "EXPECTATION_NAME": "REPORTING_WITHIN_5MIN",
  "METRIC_NAME": "REPORTING_LAG_SECONDS",
  "VALUE": "61",
  "STATUS": "OK",
  "LAST_CHECKED": "2026-10-16 09:50:22",
  "FIRST_INCIDENT_AT": "2026-10-16 09:46:00",
  "INCIDENTS": 1
 },
 {
  "TABLE_NAME": "SYSTEM__ATTENDANCE",
  "EXPECTATION_NAME": "NO_ORPHAN_CHECKINS",
  "METRIC_NAME": "REFERENTIAL_INTEGRITY_COUNT",
  "VALUE": "0",
  "STATUS": "OK",
  "LAST_CHECKED": "2026-10-16 09:50:23",
  "FIRST_INCIDENT_AT": None,
  "INCIDENTS": 0
 },
 {
  "TABLE_NAME": "SYSTEM__PAYMENT",
  "EXPECTATION_NAME": "PAYMENTS_FRESH_3MIN",
  "METRIC_NAME": "FRESHNESS",
  "VALUE": "19",
  "STATUS": "OK",
  "LAST_CHECKED": "2026-10-16 09:50:07",
  "FIRST_INCIDENT_AT": "2026-10-16 09:36:01",
  "INCIDENTS": 2
 },
 {
  "TABLE_NAME": "SYSTEM__PAYMENT",
  "EXPECTATION_NAME": "NO_NEGATIVE_AMOUNTS",
  "METRIC_NAME": "NEGATIVE_COUNT",
  "VALUE": "0",
  "STATUS": "OK",
  "LAST_CHECKED": "2026-10-16 09:50:27",
  "FIRST_INCIDENT_AT": "2026-10-16 09:36:01",
  "INCIDENTS": 2
 }
]

S4_INCIDENTS = [
 {
  "OPENED_AT": "2026-10-16 09:36:01",
  "TABLE_NAME": "MEMBERS__MEMBER",
  "EXPECTATION_NAME": "NO_DUPLICATE_MEMBERS",
  "VALUE": "150"
 },
 {
  "OPENED_AT": "2026-10-16 09:36:01",
  "TABLE_NAME": "SYSTEM__PAYMENT",
  "EXPECTATION_NAME": "NO_NEGATIVE_AMOUNTS",
  "VALUE": "40"
 },
 {
  "OPENED_AT": "2026-10-16 09:36:01",
  "TABLE_NAME": "SYSTEM__PAYMENT",
  "EXPECTATION_NAME": "PAYMENTS_FRESH_3MIN",
  "VALUE": "295"
 },
 {
  "OPENED_AT": "2026-10-16 09:41:06",
  "TABLE_NAME": "MEMBERS__MEMBER",
  "EXPECTATION_NAME": "NO_ACTIVE_LEAVERS",
  "VALUE": "292"
 },
 {
  "OPENED_AT": "2026-10-16 09:41:06",
  "TABLE_NAME": "MEMBERS__MEMBER",
  "EXPECTATION_NAME": "NO_DUPLICATE_MEMBERS",
  "VALUE": "150"
 },
 {
  "OPENED_AT": "2026-10-16 09:41:06",
  "TABLE_NAME": "SYSTEM__PAYMENT",
  "EXPECTATION_NAME": "NO_NEGATIVE_AMOUNTS",
  "VALUE": "40"
 },
 {
  "OPENED_AT": "2026-10-16 09:41:06",
  "TABLE_NAME": "SYSTEM__PAYMENT",
  "EXPECTATION_NAME": "PAYMENTS_FRESH_3MIN",
  "VALUE": "578"
 }
]

S4_TWO_ACTIVE = [
 {
  "ACTIVE_MEMBERS": 1598,
  "PAID_MEMBERS_35D": 1520
 }
]

ST_BOOKINGS = [
 {
  "DAY": "2026-10-09",
  "BOOKINGS": 188
 },
 {
  "DAY": "2026-10-10",
  "BOOKINGS": 347
 },
 {
  "DAY": "2026-10-11",
  "BOOKINGS": 353
 },
 {
  "DAY": "2026-10-12",
  "BOOKINGS": 306
 },
 {
  "DAY": "2026-10-13",
  "BOOKINGS": 316
 },
 {
  "DAY": "2026-10-14",
  "BOOKINGS": 310
 },
 {
  "DAY": "2026-10-15",
  "BOOKINGS": 136
 }
]

B2_CLASSIFY_JSON = {
 "classification_result": {
  "DATE_OF_BIRTH": {
   "alternates": [],
   "recommendation": {
    "confidence": "HIGH",
    "coverage": 1,
    "details": [],
    "privacy_category": "QUASI_IDENTIFIER",
    "semantic_category": "DATE_OF_BIRTH",
    "tags": [
     {
      "tag_applied": False,
      "tag_name": "snowflake.core.semantic_category",
      "tag_value": "DATE_OF_BIRTH"
     },
     {
      "tag_applied": False,
      "tag_name": "snowflake.core.privacy_category",
      "tag_value": "QUASI_IDENTIFIER"
     }
    ]
   },
   "valid_value_ratio": 1
  },
  "EMAIL": {
   "alternates": [],
   "recommendation": {
    "confidence": "HIGH",
    "coverage": 1,
    "details": [],
    "privacy_category": "IDENTIFIER",
    "semantic_category": "EMAIL",
    "tags": [
     {
      "tag_applied": False,
      "tag_name": "snowflake.core.semantic_category",
      "tag_value": "EMAIL"
     },
     {
      "tag_applied": False,
      "tag_name": "snowflake.core.privacy_category",
      "tag_value": "IDENTIFIER"
     }
    ]
   },
   "valid_value_ratio": 1
  },
  "FIRST_NAME": {
   "alternates": [],
   "recommendation": {
    "confidence": "HIGH",
    "coverage": 1,
    "details": [],
    "privacy_category": "IDENTIFIER",
    "semantic_category": "NAME",
    "tags": [
     {
      "tag_applied": False,
      "tag_name": "snowflake.core.semantic_category",
      "tag_value": "NAME"
     },
     {
      "tag_applied": False,
      "tag_name": "snowflake.core.privacy_category",
      "tag_value": "IDENTIFIER"
     }
    ]
   },
   "valid_value_ratio": 1
  },
  "HEALTH_NOTES": {
   "alternates": []
  },
  "HOME_SITE_ID": {
   "alternates": []
  },
  "JOINED_ON": {
   "alternates": []
  },
  "LAST_ACTIVITY_AT": {
   "alternates": []
  },
  "LAST_NAME": {
   "alternates": [],
   "recommendation": {
    "confidence": "HIGH",
    "coverage": 1,
    "details": [],
    "privacy_category": "IDENTIFIER",
    "semantic_category": "NAME",
    "tags": [
     {
      "tag_applied": False,
      "tag_name": "snowflake.core.semantic_category",
      "tag_value": "NAME"
     },
     {
      "tag_applied": False,
      "tag_name": "snowflake.core.privacy_category",
      "tag_value": "IDENTIFIER"
     }
    ]
   },
   "valid_value_ratio": 1
  },
  "LEFT_ON": {
   "alternates": []
  },
  "MARKETING_CONSENT": {
   "alternates": []
  },
  "MEMBER_ID": {
   "alternates": []
  },
  "OPERATOR_ID": {
   "alternates": []
  },
  "PHONE": {
   "alternates": []
  },
  "POSTCODE": {
   "alternates": [],
   "recommendation": {
    "confidence": "LOW",
    "coverage": 0.4645,
    "details": [
     {
      "coverage": 0.4645,
      "semantic_category": "UK_POSTAL_CODE"
     }
    ],
    "privacy_category": "QUASI_IDENTIFIER",
    "semantic_category": "POSTAL_CODE",
    "tags": [
     {
      "tag_applied": False,
      "tag_name": "snowflake.core.semantic_category",
      "tag_value": "POSTAL_CODE"
     },
     {
      "tag_applied": False,
      "tag_name": "snowflake.core.privacy_category",
      "tag_value": "QUASI_IDENTIFIER"
     }
    ]
   },
   "valid_value_ratio": 1
  },
  "STATUS": {
   "alternates": []
  },
  "_BATCH_ID": {
   "alternates": []
  },
  "_LOADED_AT": {
   "alternates": []
  }
 }
}

B2_SAR_JSON = {
 "data": {
  "MEMBERS__MEMBER": [
   {
    "DATE_OF_BIRTH": "1967-03-10",
    "EMAIL": "member1043@example.co.uk",
    "FIRST_NAME": "Amelia",
    "HEALTH_NOTES": "Asthma - inhaler on poolside",
    "HOME_SITE_ID": "S01",
    "JOINED_ON": "2023-06-04",
    "LAST_ACTIVITY_AT": "2026-10-11 09:26:54.093 -0700",
    "LAST_NAME": "Smith",
    "MARKETING_CONSENT": False,
    "MEMBER_ID": "M-01043",
    "OPERATOR_ID": "RIVERSIDE",
    "PHONE": "07700 938200",
    "POSTCODE": "OX1 4AB",
    "STATUS": "ACTIVE",
    "_BATCH_ID": "B-SEED",
    "_LOADED_AT": "2026-10-16 09:26:54.093 -0700"
   }
  ],
  "MEMBERS__MEMBERSHIP": [
   {
    "LAST_PAID_ON": "2026-10-05",
    "MEMBERSHIP_ID": "MS-01043",
    "MEMBER_ID": "M-01043",
    "MONTHLY_FEE": 49.99,
    "OPERATOR_ID": "RIVERSIDE",
    "PLAN_NAME": "Premium Plus",
    "START_DATE": "2023-06-04",
    "_LOADED_AT": "2026-10-16 09:26:54.832 -0700"
   }
  ],
  "SYSTEM__ATTENDANCE": [
   {
    "ATTENDANCE_ID": "AT-000206",
    "BOOKING_ID": "BK-000206",
    "CHECKED_IN_AT": "2026-10-12 19:46:55.513 -0700",
    "MEMBER_ID": "M-01043",
    "OPERATOR_ID": "RIVERSIDE",
    "_LOADED_AT": "2026-10-16 09:26:56.213 -0700"
   },
   {
    "ATTENDANCE_ID": "AT-003371",
    "BOOKING_ID": "BK-003371",
    "CHECKED_IN_AT": "2026-09-21 15:25:55.513 -0700",
    "MEMBER_ID": "M-01043",
    "OPERATOR_ID": "RIVERSIDE",
    "_LOADED_AT": "2026-10-16 09:26:56.213 -0700"
   },
   {
    "ATTENDANCE_ID": "AT-006995",
    "BOOKING_ID": "BK-006995",
    "CHECKED_IN_AT": "2026-10-06 03:52:55.513 -0700",
    "MEMBER_ID": "M-01043",
    "OPERATOR_ID": "RIVERSIDE",
    "_LOADED_AT": "2026-10-16 09:26:56.213 -0700"
   },
   {
    "ATTENDANCE_ID": "AT-008122",
    "BOOKING_ID": "BK-008122",
    "CHECKED_IN_AT": "2026-10-11 10:05:55.513 -0700",
    "MEMBER_ID": "M-01043",
    "OPERATOR_ID": "RIVERSIDE",
    "_LOADED_AT": "2026-10-16 09:26:56.213 -0700"
   }
  ],
  "SYSTEM__BOOKING": [
   {
    "ACTIVITY_ID": "A00465",
    "BOOKED_AT": "2026-10-12 19:41:55.513 -0700",
    "BOOKING_ID": "BK-000206",
    "MEMBER_ID": "M-01043",
    "OPERATOR_ID": "RIVERSIDE",
    "_LOADED_AT": "2026-10-16 09:26:55.513 -0700"
   },
   {
    "ACTIVITY_ID": "A00246",
    "BOOKED_AT": "2026-09-21 15:20:55.513 -0700",
    "BOOKING_ID": "BK-003371",
    "MEMBER_ID": "M-01043",
    "OPERATOR_ID": "RIVERSIDE",
    "_LOADED_AT": "2026-10-16 09:26:55.513 -0700"
   },
   {
    "ACTIVITY_ID": "A00459",
    "BOOKED_AT": "2026-10-06 03:47:55.513 -0700",
    "BOOKING_ID": "BK-006995",
    "MEMBER_ID": "M-01043",
    "OPERATOR_ID": "RIVERSIDE",
    "_LOADED_AT": "2026-10-16 09:26:55.513 -0700"
   },
   {
    "ACTIVITY_ID": "A00566",
    "BOOKED_AT": "2026-10-11 10:00:55.513 -0700",
    "BOOKING_ID": "BK-008122",
    "MEMBER_ID": "M-01043",
    "OPERATOR_ID": "RIVERSIDE",
    "_LOADED_AT": "2026-10-16 09:26:55.513 -0700"
   }
  ],
  "SYSTEM__PAYMENT": [
   {
    "AMOUNT": 49.99,
    "MEMBER_ID": "M-01043",
    "OPERATOR_ID": "RIVERSIDE",
    "PAYMENT_DATE": "2026-10-05",
    "PAYMENT_ID": "PY-0001691",
    "PAYMENT_TYPE": "PAYMENT",
    "_BATCH_ID": "B-SEED",
    "_LOADED_AT": "2026-10-16 09:26:56.981 -0700"
   },
   {
    "AMOUNT": 24.99,
    "MEMBER_ID": "M-01043",
    "OPERATOR_ID": "RIVERSIDE",
    "PAYMENT_DATE": "2026-10-07",
    "PAYMENT_ID": "PY-0001885",
    "PAYMENT_TYPE": "PAYMENT",
    "_BATCH_ID": "B-SEED",
    "_LOADED_AT": "2026-10-16 09:26:56.981 -0700"
   },
   {
    "AMOUNT": 24.99,
    "MEMBER_ID": "M-01043",
    "OPERATOR_ID": "RIVERSIDE",
    "PAYMENT_DATE": "2026-09-23",
    "PAYMENT_ID": "PY-0003635",
    "PAYMENT_TYPE": "PAYMENT",
    "_BATCH_ID": "B-SEED",
    "_LOADED_AT": "2026-10-16 09:26:56.981 -0700"
   }
  ]
 },
 "generated_at": "2026-10-16 09:55:03.551 -0700",
 "member_id": "M-01043",
 "note": "REPORTING dynamic tables hold aggregates only (no member_id)",
 "operator": "RIVERSIDE_NIELS"
}

B2_ERASE_JSON = {
 "attendance_deleted": 6,
 "bookings_deleted": 8,
 "member_rows": 1,
 "payments_pseudonymised": 3
}

AGENT_QUESTION = 'How many active members do we have?'
AGENT_ANSWER = "You currently have **1,520 active members**.\n\nThis uses the \"active members\" definition from the operator KPIs (members whose last payment was within the past 35 days)."
AGENT_USED_VERIFIED_QUERY = True

B3_CREATE_OUT = "Creating DCM Project 'GLADSTONE_DQ_LITE.RIVERSIDE_NIELS_DCM.OPERATOR_PIPELINE'\nDCM Project 'GLADSTONE_DQ_LITE.RIVERSIDE_NIELS_DCM.OPERATOR_PIPELINE' successfully created."
B3_PLAN_OUT = "Uploading definition files\n  Creating temporary stage GLADSTONE_DQ_LITE.RIVERSIDE_NIELS_DCM.DCM_OPERATOR_PIPELINE_1792169737_TMP_STAGE.\n  Local changes to be deployed:\n    added:    manifest.yml -> manifest.yml\n    added:    sources/definitions/bronze.sql -> sources/definitions/bronze.sql\n    added:    sources/definitions/expectations.sql -> sources/definitions/expectations.sql\n    added:    sources/definitions/reporting.sql -> sources/definitions/reporting.sql\n  Uploading files from local ./dcm_project/output/bundle directory to temporary stage.\n\nArtifacts saved to: ./dcm_project/out\nCREATE   DYNAMIC_TABLE        GLADSTONE_DQ_LITE.RIVERSIDE_NIELS_DCM.REPORTING__ACTIVE_MEMBERS\nCREATE   DYNAMIC_TABLE        GLADSTONE_DQ_LITE.RIVERSIDE_NIELS_DCM.REPORTING__DAILY_REVENUE\nCREATE   TABLE                GLADSTONE_DQ_LITE.RIVERSIDE_NIELS_DCM.MEMBERS__MEMBER\nCREATE   TABLE                GLADSTONE_DQ_LITE.RIVERSIDE_NIELS_DCM.SYSTEM__PAYMENT\nALTER    ROLE                 DQ_LITE_ATTENDEE\n\nPlanned 5 entities (4 to create, 1 to alter, 0 to drop)."
B3_DEPLOY_OUT = "Uploading definition files\n  Creating temporary stage GLADSTONE_DQ_LITE.RIVERSIDE_NIELS_DCM.DCM_OPERATOR_PIPELINE_1792169749_TMP_STAGE.\n  Local changes to be deployed:\n    added:    manifest.yml -> manifest.yml\n    added:    sources/definitions/bronze.sql -> sources/definitions/bronze.sql\n    added:    sources/definitions/expectations.sql -> sources/definitions/expectations.sql\n    added:    sources/definitions/reporting.sql -> sources/definitions/reporting.sql\n  Uploading files from local ./dcm_project/output/bundle directory to temporary stage.\n\nCREATE   DYNAMIC_TABLE        GLADSTONE_DQ_LITE.RIVERSIDE_NIELS_DCM.REPORTING__ACTIVE_MEMBERS\nCREATE   DYNAMIC_TABLE        GLADSTONE_DQ_LITE.RIVERSIDE_NIELS_DCM.REPORTING__DAILY_REVENUE\nCREATE   TABLE                GLADSTONE_DQ_LITE.RIVERSIDE_NIELS_DCM.MEMBERS__MEMBER\nCREATE   TABLE                GLADSTONE_DQ_LITE.RIVERSIDE_NIELS_DCM.SYSTEM__PAYMENT\nALTER    ROLE                 DQ_LITE_ATTENDEE\n\nDeployed 5 entities (4 created, 1 altered, 0 dropped)."
B3_TEST_OUT = "\u2713 PASS      GLADSTONE_DQ_LITE.RIVERSIDE_NIELS_DCM.MEMBERS__MEMBER (NO_ACTIVE_LEAVERS)\n\u2713 PASS      GLADSTONE_DQ_LITE.RIVERSIDE_NIELS_DCM.MEMBERS__MEMBER (NO_DUPLICATE_MEMBERS)\n\u2713 PASS      GLADSTONE_DQ_LITE.RIVERSIDE_NIELS_DCM.REPORTING__DAILY_REVENUE (REVENUE_ALWAYS_COMPUTED)\n\u2713 PASS      GLADSTONE_DQ_LITE.RIVERSIDE_NIELS_DCM.SYSTEM__PAYMENT (NO_NEGATIVE_AMOUNTS)\n\n4 passed, 0 failed out of 4 total."
B3_TEST_FAIL_OUT = "\u2713 PASS      GLADSTONE_DQ_LITE.RIVERSIDE_NIELS_DCM.MEMBERS__MEMBER (NO_ACTIVE_LEAVERS)\n\u2717 FAIL      GLADSTONE_DQ_LITE.RIVERSIDE_NIELS_DCM.MEMBERS__MEMBER (NO_DUPLICATE_MEMBERS)\n  \u2514\u2500 Expected: value = 0, Got: 1 (Metric: DUPLICATE_COUNT)\n\u2713 PASS      GLADSTONE_DQ_LITE.RIVERSIDE_NIELS_DCM.REPORTING__DAILY_REVENUE (REVENUE_ALWAYS_COMPUTED)\n\u2713 PASS      GLADSTONE_DQ_LITE.RIVERSIDE_NIELS_DCM.SYSTEM__PAYMENT (NO_NEGATIVE_AMOUNTS)\n\u256d\u2500 Error \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u256e\n\u2502 3 passed, 1 failed out of 4 total.                                           \u2502\n\u2570\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u256f"
B3_TEST_FAIL_EXIT = 1
