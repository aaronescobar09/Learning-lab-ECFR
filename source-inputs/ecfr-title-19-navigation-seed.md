# eCFR Title 19 Navigation Seed Data

Purpose: raw source material for a future `/teach` workspace in this repo. This is not a lesson, mission, or scaffold. It preserves the learner context, official source pointers, and exam-style examples Aaron provided.

## Teaching goal context

Students need to learn how to navigate Title 19 of the eCFR for Customs Duties while studying. For exam conditions, Aaron noted that students cannot use the eCFR during the exam, so digital navigation practice is for learning and familiarity, not an exam-time tactic.

## Official source

- eCFR Title 19 current page: https://www.ecfr.gov/current/title-19
- eCFR structure API used for verification: https://www.ecfr.gov/api/versioner/v1/structure/current/title-19.json
- eCFR section renderer used for 19 CFR 11.1 verification: https://www.ecfr.gov/api/renderer/v1/content/enhanced/current/title-19?part=11&section=11.1
- Retrieved by Hermes: 2026-07-07 21:28:12 UTC

## Aaron-provided AI summary to preserve

Ignore item 3 for exam-time teaching because students cannot use the eCFR during the exam.

1. Understand the Structure
   - Title 19 is codified into Chapters, which dictate the specific agency enforcing the rule.
   - Chapter I: U.S. Customs and Border Protection (CBP), Dept. of Homeland Security.
   - Chapter II: U.S. International Trade Commission.
   - Chapter III: International Trade Administration.
   - Chapter IV: U.S. Immigration and Customs Enforcement (ICE).

2. Locate Relevant "Parts" (Topics)
   - Chapter I contains Parts 0 through 199 according to the AI summary. Note: the eCFR structure API currently showed 57 Chapter I part nodes ranging from Part 0 through Part 192, so exact part range should be verified live before teaching.
   - Parts 1-199: core customs-duty regulations for importers, according to the AI summary.
   - 19 CFR 10: Rules regarding Free Trade Agreements, Carnets, and temporary importations under bond.
   - 19 CFR 111: Regulations for Customs Brokers and licensing.
   - 19 CFR 141-142: Entry of merchandise and the specific entry process.
   - 19 CFR 145: Mail importations.

3. Use Digital Navigation Tools
   - Study-only, not exam-time: eCFR browsing, eCFR search, specific citation lookup such as 19 CFR 141.1, govinfo.gov search, PDFs, and change tracking.

4. Reading the Citation Format
   - Standard CFR citation format: [Title] CFR [Part].[Section].
   - Example: 19 CFR 111.28(b) means Title 19, Part 111, Section 28, Subsection b.
   - Students should learn to parse the title, part, section, and subsection quickly.

## Verified current eCFR structure highlights

Source: eCFR structure API listed above.

| Unit | Current eCFR label or description | Teaching note |
|---|---|---|
| Title 19 | Title 19 - Customs Duties | Top-level subject students are navigating. |
| Chapter I | U.S. Customs and Border Protection, Department of Homeland Security; Department of the Treasury | Main chapter for CBP/customs broker exam navigation. |
| Chapter II | United States International Trade Commission | Separate agency chapter. |
| Chapter III | International Trade Administration, Department of Commerce | Separate agency chapter. |
| Chapter IV | U.S. Immigration and Customs Enforcement, Department of Homeland Security [Reserved] | Reserved in current structure. |

## Verified part map for provided examples and distractors

Source: eCFR structure API listed above.

| Part | Current eCFR label | Why it matters |
|---:|---|---|
| 10 | Articles Conditionally Free, Subject to a Reduced Rate, Etc. | Mentioned in Aaron's summary as FTAs, carnets, and temporary importations under bond. |
| 11 | Packing and Stamping; Marking | Used by exam sample question about 19 CFR 11.1. |
| 111 | Customs Brokers | Correct answer for licensing of Customs Brokers. |
| 113 | CBP Bonds | Distractor in broker licensing question. |
| 141 | Entry of Merchandise | Mentioned in Aaron's summary as entry of merchandise. |
| 142 | Entry Process | Mentioned in Aaron's summary as entry process. |
| 145 | Mail Importations | Mentioned in Aaron's summary. |
| 159 | Liquidation of Duties | Distractor in drawback question. |
| 171 | Fines, Penalties, and Forfeitures | Distractor in drawback question. |
| 172 | Claims for Liquidated Damages; Penalties Secured by Bonds | Distractor in drawback question. |
| 185 | Not found in current Title 19 structure API | Distractor in broker licensing question. Verify if historical/reserved context matters. |
| 190 | Modernized Drawback | Correct answer for drawback question. |
| 198 | Not found in current Title 19 structure API | Distractor in broker licensing question. Verify if historical/reserved context matters. |

## Verified section 19 CFR 11.1

Source: eCFR section renderer listed above.

- Citation: 19 CFR 11.1
- Current section heading: `§ 11.1 Cigars, cigarettes, medicinal preparations, and perfumery.`
- Relevant content signal: paragraph (a) discusses imported cigars and cigarettes being inspected, weighed, and repacked if necessary; paragraph (b) discusses package requirements before release; paragraph (c) discusses domestic cigars, cigarettes, medicinal preparations, and perfumery returned to the United States and stamped by Customs.
- Teaching note: this supports the exam answer that associates Part/Section 11.1 with packing and stamping requirements for cigars, cigarettes, medicinal preparations, and perfumery.

## Exam sample image

Stored copy:

```text
source-inputs/images/exam-sample-001.jpg
```

Original Hermes cache path when provided:

```text
/Users/gtcai/.hermes/cache/images/img_4ee9b7ec23f0.jpg
```

## OCR / transcription of exam sample

### Question 1

Drawbacks are addressed in which part of the CFR?

A) Part 190  
B) Part 172  
C) Part 171  
D) Part 159  

ANSWER: A

Verified teaching key: Part 190 is `Modernized Drawback` in the current eCFR structure API.

### Question 2

The regulations regarding the licensing of Customs Brokers is addressed in which part of the CFR?

A) Part 111  
B) Part 113  
C) Part 185  
D) Part 198  

ANSWER: A

Verified teaching key: Part 111 is `Customs Brokers` in the current eCFR structure API.

### Question 3

Which of the following is described in Part 11.1?

A) Packing and stamping requirements for cigars, cigarettes, medicinal preparation, and perfumery  
B) Labeling of fur products to indicate composition  
C) Labeling textile fiber products  
D) False designations of origin and false descriptions; false marking of articles of gold or silver.  

ANSWER: A

Verified teaching key: 19 CFR 11.1 is headed `Cigars, cigarettes, medicinal preparations, and perfumery`, with content related to packaging and stamping.

## Future `/teach` usage notes

When `/teach` is eventually invoked in this repo:

- Treat this file as source input, not as the mission itself.
- The likely mission is exam-prep navigation of Title 19/eCFR for customs regulations.
- Start by interviewing Aaron about the learner audience and exam constraints.
- Use this seed data to build a first lesson around:
  1. Title -> Chapter -> Part -> Section navigation.
  2. Reading `19 CFR 111.28(b)` style citations.
  3. Turning part labels into fast mental lookup cues.
  4. Practicing exam-style questions without relying on digital search during the exam.
- Keep official-source claims tied to eCFR or other government sources.
