---
layout: phenotype
title: PHE00062 - Diabetes
phenotype_id: PHE00062
name: Diabetes
type: Disease or Syndrome
group: Endocrine
data_sources: Primary care (CPRD), Hospital Admission Data (HES), Mortality Data (ONS)
clinical_terminologies: Read, ICD-10, ICD-9, OPCS-4
validation: cross-source, casenote, aetiology, prognosis, genetic external
primary_care_code_lists: /primary_care/CPRD_diabetes.csv
secondary_care_code_lists: /secondary_care/ICD_diabetes.csv
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

{% include csv.html csvdata=site.data.primary_care.CPRD_diabetes %}

Read terms are hierarhically organized in top-level chapters i.e. chapter G....00 is related to Circulatory System Diseases and sub-headings i.e. heading G2...00 is related to Hypertensive Heart Disease while G3...00 is related to Ischaemic Heart Disease.

### Secondary Care

In Hospital Episode Statistics (HES, hospital admission data) we used ICD-10 terms (see below) for {{ page.name }} diagnosis when marked as the primary diagnosis i.e. the main condition treated or investigated during the relevant episode of healthcare. We used the date of admission to hospital as the date of the event. We additionally searched for OPCS-4 terms indicating the emergency repair of an aneurysmal segment of the aorta.

{% include csv.html csvdata=site.data.secondary_care.ICD_diabetes %}


### Death

### Implementation

**Combining evidence across sources to define and date phenotypes**

<pre>
Use MODIFIED CALIBER 'Diabetes' phenotyping algorithm for 
1.	T1DM, 
2.	T2DM, 
3.	'Diabetes' other or uncertain type:

IF there is at least one record for code for type 2 'Diabetes' (diabdiag_gprd = 4)
    and no record for type 1 'Diabetes' (no record with diabdiag_gprd = 3)
    then classify the patient as type 2 'Diabetes'

ELSE if there is at least one record for code for type I 'Diabetes' (diabdiag_gprd = 3)
    and no record for type 2 'Diabetes' (no record with diabdiag_gprd = 4)
    then classify the patient as type 1 'Diabetes'

ELSE if there is at least one record of type 1 'Diabetes' (diabdiag_gprd = 3)
    and type 2 'Diabetes' (diabdiag_gprd = 4)
    then classify as 'Diabetes' other or uncertain type

ELSE if there are no diabdiag_gprd records for this patient:

    If there is at least one record for Non-insulin-dependent 'Diabetes' mellitus (NIDDM) (dm_gprd = 4 or dm_hes = 4)
        and no record for IDDM (no record with dm_gprd = 3 or dm_hes = 3)
        then classify the patient as type 2 'Diabetes'

    ELSE if there is at least one record for Insulin-dependent 'Diabetes' mellitus (IDDM) (dm_gprd = 3 or dm_hes = 3)
        and no record for NIDDM (no record with dm_gprd = 4 or dm_hes = 4)
        then classify the patient as type 1 'Diabetes'

    ELSE if there is at least one record of 'Diabetes' (dm_gprd or dm_hes category 3, 4, 5 or 6)
        then classify as 'Diabetes' other or uncertain type

ELSE classify as no 'Diabetes'
</pre>

### Validations

### Publications

