---
layout: phenotype
title: PHE00272 - Stable Angina
phenotype_id: PHE00272
name: Stable Angina
type: Disease or Syndrome
group: Cardiovascular
data_sources: Primary care (CPRD), Hospital Admission Data (HES), Mortality Data (ONS)
clinical_terminologies: Read, ICD-10, ICD-9, OPCS-4
validation: cross-source, casenote, aetiology, prognosis, genetic external
primary_care_code_lists: /primary_care/CPRD_stable_angina.csv
secondary_care_code_lists: /secondary_care/ICD_stable_angina.csv
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

{% include csv.html csvdata=site.data.primary_care.CPRD_stable_angina %}

Read terms are hierarhically organized in top-level chapters i.e. chapter G....00 is related to Circulatory System Diseases and sub-headings i.e. heading G2...00 is related to Hypertensive Heart Disease while G3...00 is related to Ischaemic Heart Disease.

### Secondary Care

In Hospital Episode Statistics (HES, hospital admission data) we used ICD-10 terms (see below) for {{ page.name }} diagnosis when marked as the primary diagnosis i.e. the main condition treated or investigated during the relevant episode of healthcare. We used the date of admission to hospital as the date of the event. We additionally searched for OPCS-4 terms indicating the emergency repair of an aneurysmal segment of the aorta.

{% include csv.html csvdata=site.data.secondary_care.ICD_stable_angina %}


### Death

### Implementation

**Combining evidence across sources to define and date phenotypes**

<pre>
Use MODIFIED CALIBER 'Stable angina' phenotyping algorithm:

At the specified date, a patient is considered to have had 'Stable angina' IF they meet the criteria for any of the following on or before the specified date:
    1. Recorded diagnosis of 'Stable angina' in primary or secondary care
    2. Coronary revascularisation without un'Stable angina' or myocardial infarction in the previous 30 days
    3. Primary care record of abnormal coronary angiogram or test showing evidence of myocardial ischaemia

The earliest date on which the individual meets any of the following criteria on or before the specified date is defined as the first event date. Include terms for h/o 'Stable angina':
1.	Recorded diagnosis:
    a)	Primary care diagnosis of ischaemic chest pain: chest_pain_gprd, category 4
    b)	Primary care diagnosis of 'Stable angina': sa_diagnosis_gprd, category 1, category 4
    c)	Secondary care diagnosis of 'Stable angina': angina_hes, category 4
2.	Coronary revascularisation without un'Stable angina' (phenotype_ua) or myocardial infarction (phenotype_mi) in the previous 30 days:
    a)	Primary care record of percutaneous coronary intervention (PCI): pci_gprd, category 2
    b)	Secondary care record of PCI: pci_opcs, category 2
    c)	Primary care record of coronary artery bypass graft (CABG): cabg_gprd, category 2
    d)	Secondary care record of CABG: cabg_opcs, category 2
3.	Test results:
    a)	Primary care record of abnormal stress echocardiogram: stress_echo_gprd, category 3
    b)	Primary care record of abnormal invasive coronary angiogram: angio_gprd, category 3
    c)	Primary care record of abnormal computed tomography coronary angiogram: ct_angio_gprd, category 3
    d)	Primary care record of abnormal magnetic resonance coronary angiogram: mr_angio_gprd, category 3
    e)	Primary care record of abnormal exercise ECG: eecg_gprd, category 3
    f)	Primary care record of myocardial ischaemia on resting ECG: recg_gprd, category 2
    g)	Primary care record of abnormal myocardial perfusion scan: radio_scan_gprd, category 3
</pre>

### Validations

### Publications

