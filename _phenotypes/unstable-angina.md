---
layout: phenotype
title: PHE00290 - Unstable Angina
phenotype_id: PHE00290
name: Unstable Angina
type: Disease or Syndrome
group: Cardiovascular
data_sources: Primary care (CPRD), Hospital Admission Data (HES), Mortality Data (ONS)
clinical_terminologies: Read, ICD-10, ICD-9, OPCS-4
validation: cross-source, casenote, aetiology, prognosis, genetic external
primary_care_code_lists: /primary_care/CPRD_unstable_angina.csv
secondary_care_code_lists: /secondary_care/ICD_unstable_angina.csv
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

{% include csv.html csvdata=site.data.primary_care.CPRD_unstable_angina %}

Read terms are hierarhically organized in top-level chapters i.e. chapter G....00 is related to Circulatory System Diseases and sub-headings i.e. heading G2...00 is related to Hypertensive Heart Disease while G3...00 is related to Ischaemic Heart Disease.

### Secondary Care

In Hospital Episode Statistics (HES, hospital admission data) we used ICD-10 terms (see below) for {{ page.name }} diagnosis when marked as the primary diagnosis i.e. the main condition treated or investigated during the relevant episode of healthcare. We used the date of admission to hospital as the date of the event. We additionally searched for OPCS-4 terms indicating the emergency repair of an aneurysmal segment of the aorta.

{% include csv.html csvdata=site.data.secondary_care.ICD_unstable_angina %}


### Death

### Implementation

**Combining evidence across sources to define and date phenotypes**

<pre>
Use MODIFIED CALIBER 'Unstable Angina' phenotyping algorithm:

At the specified date, a patient is considered to have had 'Unstable Angina' IF they meet the criteria for any of the following on or before the specified date: 
A hospitalization with the non-specific diagnosis of 'angina' as the primary diagnosis, where there is no procedure giving a reason for admission (PCI or CABG), is considered to be 'Unstable Angina'.

The earliest date on which the individual meets any of the following criteria on or before the specified date is defined as the first event date:
1.	Primary care
    a)	Diagnosis of 'Unstable Angina'; unangina_gprd,  category 2, 3
    b)	Diagnosis of acute coronary syndrome not otherwise specified; acs_gprd, category 3
2.	Secondary care
    a)	Primary or secondary diagnosis of unspecified angina (ICD-10 I20.9) during a hospitalization that did not have a PCI or CABG procedure performed
    b)	Primary or secondary diagnosis of acute ischaemic heart disease during a hospitalization; acute_ihd_hes, category 3
    c)	Primary or secondary diagnosis of 'Unstable Angina' during a hospitalization; uangina_hes, category 1
</pre>

### Validations

### Publications

