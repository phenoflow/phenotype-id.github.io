---
layout: phenotype
title: PHE00303 - Low Hdl-c
phenotype_id: PHE00303
name: Low Hdl-c
type: Disease or Syndrome
group: Endocrine
data_sources: Primary care (CPRD), Hospital Admission Data (HES), Mortality Data (ONS)
clinical_terminologies: Read, ICD-10, ICD-9, OPCS-4
validation: cross-source, casenote, aetiology, prognosis, genetic external
primary_care_code_lists: 
secondary_care_code_lists: 
valid_event_data_range: 01/01/1999 - 01/07/2016
sex: Female/Male
author: Julie George, Emily Herrett, Liam Smeeth, Harry Hemingway, Anoop Shah, Spiros Denaxas
status: DRAFT
date: 2012-11-23
modified_date: 2012-11-23
version: Revision 2
---

### Primary Care

In the Clinical Practice Research Datalink (CPRD, primary care data) we ascertained {{ page.name }} cases by searching for Read terms related to an {{ page.name }} diagnosis or evidence of endovascular/transluminal procedures related to the emergency repair of an aneurysmal segment of the aorta.


Read terms are hierarhically organized in top-level chapters i.e. chapter G....00 is related to Circulatory System Diseases and sub-headings i.e. heading G2...00 is related to Hypertensive Heart Disease while G3...00 is related to Ischaemic Heart Disease.

### Secondary Care

In Hospital Episode Statistics (HES, hospital admission data) we used ICD-10 terms (see below) for {{ page.name }} diagnosis when marked as the primary diagnosis i.e. the main condition treated or investigated during the relevant episode of healthcare. We used the date of admission to hospital as the date of the event. We additionally searched for OPCS-4 terms indicating the emergency repair of an aneurysmal segment of the aorta.


### Death

### Implementation

**Combining evidence across sources to define and date phenotypes**

<pre>
At the specified date, a patient is defined as having had Low HDL Cholesterol IF they meet the criteria for any of the following on or before the specified date. 

Primary care
1. IF FEMALE the lowest value EVER recorded for HDL Cholesterol for a patient on or before the specified date is less than:
a) serum: 1.2 mmol/L
OR
b) serum: 46.404 mg/dL
OR
c) plasma: 1.1650 mmol/L
OR
d) plasma: 45.0524 mg/dL

2. IF MALE the lowest value EVER recorded for HDL Cholesterol for a patient on or before the specified date is less than:
a) serum: 1 mmol/L
OR
b) serum: 38.67 mg/dL
OR
c) plasma: 0.9709 mmol/L
OR
d) plasma: 37.5437 mg/dL
</pre>

### Validations

### Publications

