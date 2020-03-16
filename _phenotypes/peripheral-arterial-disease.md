---
layout: phenotype
title: PHE00182 - Peripheral Arterial Disease
phenotype_id: PHE00182
name: Peripheral Arterial Disease
type: Disease or Syndrome
group: Cardiovascular
data_sources: Primary care (CPRD), Hospital Admission Data (HES), Mortality Data (ONS)
clinical_terminologies: Read, ICD-10, ICD-9, OPCS-4
validation: cross-source, casenote, aetiology, prognosis, genetic external
primary_care_code_lists: /primary_care/CPRD_peripheral_arterial_disease.csv
secondary_care_code_lists: /secondary_care/ICD_peripheral_arterial_disease.csv, /secondary_care/OPCS_peripheral_arterial_disease.csv
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

{% include csv.html csvdata=site.data.primary_care.CPRD_peripheral_arterial_disease %}

Read terms are hierarhically organized in top-level chapters i.e. chapter G....00 is related to Circulatory System Diseases and sub-headings i.e. heading G2...00 is related to Hypertensive Heart Disease while G3...00 is related to Ischaemic Heart Disease.

### Secondary Care

In Hospital Episode Statistics (HES, hospital admission data) we used ICD-10 terms (see below) for {{ page.name }} diagnosis when marked as the primary diagnosis i.e. the main condition treated or investigated during the relevant episode of healthcare. We used the date of admission to hospital as the date of the event. We additionally searched for OPCS-4 terms indicating the emergency repair of an aneurysmal segment of the aorta.

{% include csv.html csvdata=site.data.secondary_care.ICD_peripheral_arterial_disease %}

{% include csv.html csvdata=site.data.secondary_care.OPCS_peripheral_arterial_disease %}


### Death

### Implementation

**Combining evidence across sources to define and date phenotypes**

<pre>
Use MODIFIED CALIBER 'Peripheral arterial disease' (PAD) phenotyping algorithm: 

At the specified date, a patient is considered to have 'Peripheral arterial disease' IF they meet any of the criteria below on or before the specified date. 

The earliest date on which the individual meets any of the following criteria on or before the specified date is defined as the first event date:
1.	Primary care
    1.	Peripheral vascular disease diagnosis during a consultation. arterial_gprd: category 7
    2.	Record of history of PVD during a consultation. The following Read codes from CPRD:
        1.	Read:14F7.00	Medcode: 106762	Descr:H/O: arterial lower limb ulcer
        2.	Read:14NB.00	Medcode: 59534	Descr: H/O: Peripheral vascular disease procedure
    3.	Leg or aortic embolism or thrombosis diagnosis during a consultation. arterial_gprd: category 8
    4.	'Peripheral arterial disease' procedures, excluding repair of AAA recording during a consultation. pad_opcs_gprd: category 3
    5.	Abnormal 'Peripheral arterial disease' (PAD) ultrasound or Doppler study results recorded during a consultation. As per implementation of pad_ud_gprd in CALIBER
    6.	Abnormal 'Peripheral arterial disease' angiography results recorded during a consultation. As per implementation of pad_angio_gprd in CALIBER
2.	Secondary care
    1.	Primary or secondary diagnosis of Peripheral vascular disease during a hospitalization. arterial_hes: category 7
    2.	Primary or secondary diagnosis of leg or aortic embolism or thrombosis during a hospitalization. arterial_hes: category 8
    3.	Recording of 'Peripheral arterial disease' procedures, excluding repair of AAA. pad_procs_opcs: category 3
</pre>

### Validations

### Publications

