---
layout: phenotype
title: PHE00174 - Infection – Other Organisms
phenotype_id: PHE00174
name: Infection – Other Organisms
type: Disease or Syndrome
group: Infections
data_sources: Primary care (CPRD), Hospital Admission Data (HES), Mortality Data (ONS)
clinical_terminologies: Read, ICD-10, ICD-9, OPCS-4
validation: cross-source, casenote, aetiology, prognosis, genetic external
primary_care_code_lists: 
secondary_care_code_lists: /secondary_care/ICD_oth_organisms.csv
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

{% include csv.html csvdata=site.data.secondary_care.ICD_oth_organisms %}


### Death

### Implementation

**Combining evidence across sources to define and date phenotypes**

<pre>
At the specified date, a patient is defined as having had Diseases caused by Other or unspecified infectious organisms IF they meet the criteria for any of the following on or before the specified date. The earliest date on which the individual meets any of the following criteria on or before the specified date is defined as the first event date:

Secondary care
1. ALL diagnoses of Diseases caused by Other or unspecified infectious organisms or history of diagnosis during a hospitalization
OR
2. ALL possible diagnosis of Diseases caused by Other or unspecified infectious organisms during a hospitalization IF NO record satisfying criteria for Bacterial Diseases, Tuberculosis, Viral diseases, Chronic viral Hepatitis, HIV, Mycoses or Parasitic Infections 30 days before or 30 days after the first event date for Diseases caused by Other or unspecified infectious organisms.
</pre>

### Validations

### Publications

