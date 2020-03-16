---
layout: phenotype
title: PHE00024 - Atrial Fibrillation
phenotype_id: PHE00024
name: Atrial Fibrillation
type: Disease or Syndrome
group: Cardiovascular
data_sources: Primary care (CPRD), Hospital Admission Data (HES), Mortality Data (ONS)
clinical_terminologies: Read, ICD-10, ICD-9, OPCS-4
validation: cross-source, casenote, aetiology, prognosis, genetic external
primary_care_code_lists: /primary_care/CPRD_AF.csv
secondary_care_code_lists: /secondary_care/ICD_AF.csv
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

{% include csv.html csvdata=site.data.primary_care.CPRD_AF %}

Read terms are hierarhically organized in top-level chapters i.e. chapter G....00 is related to Circulatory System Diseases and sub-headings i.e. heading G2...00 is related to Hypertensive Heart Disease while G3...00 is related to Ischaemic Heart Disease.

### Secondary Care

In Hospital Episode Statistics (HES, hospital admission data) we used ICD-10 terms (see below) for {{ page.name }} diagnosis when marked as the primary diagnosis i.e. the main condition treated or investigated during the relevant episode of healthcare. We used the date of admission to hospital as the date of the event. We additionally searched for OPCS-4 terms indicating the emergency repair of an aneurysmal segment of the aorta.

{% include csv.html csvdata=site.data.secondary_care.ICD_AF %}


### Death

### Implementation

**Combining evidence across sources to define and date phenotypes**

<pre>
Use MODIFIED CALIBER 'Atrial fibrillation' phenotyping algorithm: 

At the specified date, a patient is considered to have had 'Atrial fibrillation' or flutter IF they meet any of the criteria below on or before the specified date. 

The earliest date on which the individual meets any of the following criteria on or before the specified date is defined as the first event date:
1.	1.	Historical & Diagnosed: first recorded AF code indicates monitoring of an existing condition, or reference to a previous AF diagnosis, or a diagnosis code for AF; preference given to the earliest dated record rather than diagnosis source (i.e. no preference for primary versus secondary care).
    1.	af_gprd: category 1, 2, 3, 4, 5, 6, 7
    2.	af_hes: category 6
</pre>

### Validations

### Publications

