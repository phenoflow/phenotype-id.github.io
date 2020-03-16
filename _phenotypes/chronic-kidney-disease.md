---
layout: phenotype
title: PHE00302 - Chronic Kidney Disease
phenotype_id: PHE00302
name: Chronic Kidney Disease
type: Disease or Syndrome
group: Genitourinary
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
Apply modified CALIBER 'Chronic Kidney Disease' algorithm in CPRD primary care data as follows:

A patient is defined as having had CKD stage 3 or above at a specified date:

IF egfr_ckdepi recorded on or before specified date, THEN 
IF egfr_ckdepi <60 ml/min on the most recent date (index date) before the specified date
AND
IF egfr_ckdepi <60 ml/min on any date greater than 90 days BEFORE the index date above
THEN classify as having CKD3 or above
ELSE the patient is not defined as having CKD stage 3 or above.

Where egfr_ckdepi up to and including 31 Dec 2013 is defined as: 
egfr_ckdepi = 141 * min(crea_gprd * 0.010746 / K, 1)^alpha
* max(crea_gprd * 0.010746 / K, 1)^-1.209 
* 0.993^age * 1.018 [if female]  * 1.159 [if black]

where:
alpha = -0.329 for females, -0.411 for males
K = 0.7 for females, 0.9 for males

Where egfr_ckdepi from and including 1 Jan 2014 is defined as: 
egfr_ckdepi = 141 * min(crea_gprd * 0.010746 / K, 1)^alpha
* max(crea_gprd * 0.0.011312/ K, 1)^-1.209 
* 0.993^age * 1.018 [if female]  * 1.159 [if black]

where:
alpha = -0.329 for females, -0.411 for males
K = 0.7 for females, 0.9 for males

Where crea_gprd is defined as:
IF enttype = 165 [Serum creatinine] 
AND data1 [Operator] = 3 ["="] AND data2 [Value] > 0
THEN crea_gprd = data2
</pre>

### Validations

### Publications

