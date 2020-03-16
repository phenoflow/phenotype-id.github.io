---
layout: phenotype
title: PHE00154 - Myocardial Infarction
phenotype_id: PHE00154
name: Myocardial Infarction
type: Disease or Syndrome
group: Cardiovascular
data_sources: Primary care (CPRD), Hospital Admission Data (HES), Mortality Data (ONS)
clinical_terminologies: Read, ICD-10, ICD-9, OPCS-4
validation: cross-source, casenote, aetiology, prognosis, genetic external
primary_care_code_lists: /primary_care/CPRD_myocardial_infarction.csv
secondary_care_code_lists: /secondary_care/ICD_myocardial_infarction.csv
death: /death/ICD_myocardial_infarction.csv
valid_event_data_range: 01/01/1999 - 01/07/2016
sex: Female/Male
author: Julie George, Emily Herrett, Liam Smeeth, Harry Hemingway, Anoop Shah, Spiros Denaxas
status: DRAFT
date: 2012-11-23
modified_date: 2012-11-23
version: Revision 2
---

### Primary Care

In the Clinical Practice Research Datalink (CPRD, primary care data) we ascertained myocardial infarction (MI) cases by searching for Read terms related to MI diagnosis OR ST elevation MI (STEMI), OR non-ST elevation MI (NSTEMI).

{% include csv.html csvdata=site.data.primary_care.CPRD_myocardial_infarction %}

Read terms are hierarhically organized in top-level chapters i.e. chapter G....00 is related to Circulatory System Diseases and sub-headings i.e. heading G2...00 is related to Hypertensive Heart Disease while G3...00 is related to Ischaemic Heart Disease.

### Secondary Care

In Hospital Episode Statistics (HES, secondary care data) we used primary diagnosis of ICD-10 codes (see below) for MI diagnosis, OR ST elevation MI (STEMI), OR non-ST elevation MI, OR procedural codes (OPCS 4) of transluminal coronary thrombolysis.

{% include csv.html csvdata=site.data.secondary_care.ICD_myocardial_infarction %}

In the Myocardial Ischaemia National Audit Project (MINAP) we used the discharge diagnosis of acute STEMI OR acute NSTEMI as diagnosis of MI. Further classification was based on raised cardiac enzymes and electrocardiogram determing treatment.

### Death

In the Office for National Statistics (ONS) mortality register, we used ICD-10 and ICD-9 terms to identify fatal MI cases where an MI diagnosis was recorded as the underlying cause of death.

{% include csv.html csvdata=site.data.death.ICD_myocardial_infarction %}

### Implementation

**Combining evidence across sources to define and date phenotypes**

If there are records of non-ST elevation MI and ST elevation MI on the same date, the more severe diagnosis (STEMI) is taken as correct. If there is a record of unspecified MI and STEMI / NSTEMI on the same date, the non-specific diagnosis is ignored. MI may be recorded multiple times in the different datasets with slightly different dates. It is up to the researcher to decide what time interval should be used as a cut-off for considering that two events close to each other are distinct events rather than multuiple records of the same event; we would suggest 7 days because this is just greater than the usual duration of hospitalization for myocardial infarction.

<pre>
Use MODIFIED CALIBER 'Myocardial infarction' phenotyping algorithm:

At the specified date, a patient is considered to have had a 'Myocardial infarction' IF they meet any of the criteria below on or before the specified date. 

The earliest date on which the individual meets any of the following criteria on or before the specified date is defined as the first event date. 
1.	Primary care diagnosis of MI: myo_infarct_gprd: category 1, category 2, category 3,  category 4, category 5, category 6, category 7
2.	Secondary care diagnosis of MI: myo_infarct_hes: category 1, category 5, category 6, category 7
3.	Secondary care procedure code for coronary thrombolysis: lysis_opcs category 2
</pre>

### Validations

#### Case Note Review

For primary care or hospital discharge patients with an associated record in the disease registry (MINAP), the positive predictive value of the acute myocardial infarction diagnosis (the probability that the diagnosis recorded in the disease registry was myocardial infarction rather than unstable angina or a non-cardiac diagnosis) was 92.2% (6660/7224, 95% confidence interval 91.6% to 92.8%) in primary care and 91.5% (6851/7489, 90.8% to 92.1%) in hospital care. Eighty five per cent of patients recorded in primary care and hospital discharge (7386/8707) had a record of raised cardiac markers and half (3766/8707) had a record of ST segment elevation on electrocardiography.

#### EHR Sources

![AMI EHR Sources](/assets/img/phenotypes/ami_ehr_sources.jpeg)

Number and percentage of records recorded in primary care (Clinical Practice Research Datalink), hospital care (Hospital Episode Statistics), and disease registry (Myocardial Ischaemia National Audit Project) for non-fatal myocardial infarction across the three sources (n=17 964 patients). [More information](https://www.bmj.com/content/346/bmj.f2350).

![AMI EHR Sources 2](/assets/img/phenotypes/ami_ehr_sources_2.jpg)

Crude incidence of acute fatal and non-fatal myocardial infarction estimated using different combinations of data from primary care (Clinical Practice Research Datalink), hospital admissions (Hospital Episode Statistics), disease registry (MINAP, Myocardial Ischaemia National Audit Project), and death registry (Office for National Statistics). [More information](https://www.bmj.com/content/346/bmj.f2350).

#### Prognosis

![AMI Prognosis](/assets/img/phenotypes/ami_prognosis.jpg)

Kaplan Meier curves showing all cause mortality, stratified by record source in 20 819 patients: Clinical Practice Research Datalink (n=15 819), Hospital Episode Statistics (n=13 831), Myocardial Ischaemia National Audit Project (MINAP) (n=10 351). Myocardial infarctions recorded by the Office for National Statistics are not shown as they are by definition fatal on the date of myocardial infarction. [More information](https://www.bmj.com/content/346/bmj.f2350).

#### Genetic

<pre>
Denaxas, SC; Fatemifar, G; Patel, R; Hemingway, H; (2017) Deriving research-quality phenotypes from national electronic health records to advance precision medicine: a UK Biobank case-study. In: Proceedings of the BHI-2017 International Conference on Biomedical and Health Informatics. IEEE Engineering in Medicine and Biology Society (EMBS): Orlando, FL, USA.
</pre>

#### Cross-Country

![AMI Cross-Country](/assets/img/phenotypes/ami_crosscountry_1.jpg)

Risks of all-cause death in post-myocardial infarction survivors aged 65 years and older followed from 1 year after the index myocardial infarction. Observed (Kaplan–Meier) risks (top left), adjusted risks (top right), and relative risks vs. Sweden (bottom) in post-myocardial infarction survivors from Sweden (n = 54 841), USA (n = 53 909), England (n = 4653), and France (n = 961). CABG, coronary artery bypass graft; CI, confidence interval; KM, Kaplan–Meier; PCI, percutaneous coronary intervention; RR, relative risk. [More information](https://www.ncbi.nlm.nih.gov/pubmed/29474617).

![AMI Cross-Country](/assets/img/phenotypes/ami_crosscountry_2.jpg)

Kaplan-Meier curves for cumulative mortality at 30 days after admission with acute myocardial infarction in Sweden and the UK. [More information](https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(13)62070-X/fulltext).

### Publications

| Citation |
|----------|
| Gho JMIH et al. An electronic health records cohort study on heart failure following myocardial infarction in England: incidence and predictors. BMJ Open. 2018 Mar 3;8(3):e018331. doi: 10.1136/bmjopen-2017-018331. PMID: 29502083 |
| Steele AJ et al. Machine learning models in electronic health records can outperform conventional survival models for predicting patient mortality in coronary artery disease. PLoS One. 2018 Aug 31;13(8):e0202344. doi: 10.1371/journal.pone.0202344. eCollection 2018. PMID: 30169498 |
| Archangelidi O et al. Clinically recorded heart rate and incidence of 12 coronary, cardiac, cerebrovascular and peripheral arterial diseases in 233,970 men and women: A linked electronic health record study. Eur J Prev Cardiol. 2018 Sep;25(14):1485-1495. doi: 10.1177/2047487318785228. Epub 2018 Jul 2. PMID: 29966429 |
| Koudstaal S et al. Prognostic burden of heart failure recorded in primary care, acute hospital admissions, or both: a population-based linked electronic health record cohort study in 2.1 million people. Eur J Heart Fail. 2017 Sep;19(9):1119-1127. doi: 10.1002/ejhf.709. Epub 2016 Dec 23. PMID: 28008698 |
| Chung SC et al. Time spent at blood pressure target and the risk of death and cardiovascular diseases. PLoS One. 2018 Sep 5;13(9):e0202359. doi: 10.1371/journal.pone.0202359. eCollection 2018. PMID: 30183734 |
| Bell S et al. Association between clinically recorded alcohol consumption and initial presentation of 12 cardiovascular diseases: population based cohort study using linked health records. BMJ. 2017 Mar 22;356:j909. PMID: 28331015 |
| Pasea L et al. Personalising the decision for prolonged dual antiplatelet therapy: development, validation and potential impact of prognostic models for cardiovascular events and bleeding in myocardial infarction survivors. Eur Heart J. 2017 Apr 7;38(14):1048-1055. doi: 10.1093/eurheartj/ehw683. PMID: 28329300 |
| Shah AD et al. Neutrophil Counts and Initial Presentation of 12 Cardiovascular Diseases: A CALIBER Cohort Study. J Am Coll Cardiol. 2017 Mar 7;69(9):1160-1169. doi: 10.1016/j.jacc.2016.12.022. PMID: 28254179 |
| Asaria M et al. Using electronic health records to predict costs and outcomes in stable coronary artery disease. Heart. 2016 May 15;102(10):755-62. doi: 10.1136/heartjnl-2015-308850. Epub 2016 Feb 10. PMID: 26864674 |
| Daskalopoulou M et al. Depression as a Risk Factor for the Initial Presentation of Twelve Cardiac, Cerebrovascular, and Peripheral Arterial Diseases: Data Linkage Study of 1.9 Million Women and Men. PLoS One. 2016 Apr 22;11(4):e0153838. doi: 10.1371/journal.pone.0153838. eCollection 2016. PMID: 27105076 |
| Pujades-Rodriguez M et al. Associations between polymyalgia rheumatica and giant cell arteritis and 12 cardiovascular diseases. Heart. 2016 Mar;102(5):383-9. doi: 10.1136/heartjnl-2015-308514. Epub 2016 Jan 19. PMID: 26786818 |
| Pujades-Rodriguez M et al. Rheumatoid Arthritis and Incidence of Twelve Initial Presentations of Cardiovascular Disease: A Population Record-Linkage Cohort Study in England. PLoS One. 2016 Mar 15;11(3):e0151245. doi: 10.1371/journal.pone.0151245. eCollection 2016. PMID: 26978266 |
| Shah AD et al. Low eosinophil and low lymphocyte counts and the incidence of 12 cardiovascular diseases: a CALIBER cohort study. Open Heart. 2016 Sep 5;3(2):e000477. doi: 10.1136/openhrt-2016-000477. eCollection 2016. PMID: 27621833 |
| Timmis A et al. Prolonged dual antiplatelet therapy in stable coronary disease: comparative observational study of benefits and harms in unselected versus trial populations. BMJ. 2016 Jun 22;353:i3163. PMID: 27334486 |
| Walker S et al. Long-term healthcare use and costs in patients with stable coronary artery disease: a population-based cohort using linked health records (CALIBER). Eur Heart J Qual Care Clin Outcomes. 2016 Jan 20;2(2):125-140. doi: 10.1093/ehjqcco/qcw003. PMID: 27042338 |
| George J et al. How Does Cardiovascular Disease First Present in Women and Men? Incidence of 12 Cardiovascular Diseases in a Contemporary Cohort of 1,937,360 People. Circulation. 2015 Oct 6;132(14):1320-8. doi: 10.1161/CIRCULATIONAHA.114.013797. Epub 2015 Sep 1. PMID: 26330414 |
| Morley KI et al. Defining disease phenotypes using national linked electronic health records: a case study of atrial fibrillation. PLoS One. 2014 Nov 4;9(11):e110900. doi: 10.1371/journal.pone.0110900. eCollection 2014. PMID: 25369203 |
| Pujades-Rodriguez M et al. Heterogeneous associations between smoking and a wide range of initial presentations of cardiovascular disease in 1937360 people in England: lifetime risks and implications for risk prediction. Int J Epidemiol. 2015 Feb;44(1):129-41. doi: 10.1093/ije/dyu218. Epub 2014 Nov 20. PMID: 25416721 |
| Pujades-Rodriguez M et al. Socioeconomic deprivation and the incidence of 12 cardiovascular diseases in 1.9 million women and men: implications for risk prediction and prevention. PLoS One. 2014 Aug 21;9(8):e104671. doi: 10.1371/journal.pone.0104671. eCollection 2014. PMID: 25144739 |
| Rapsomaniki E et al. Blood pressure and incidence of twelve cardiovascular diseases: lifetime risks, healthy life-years lost, and age-specific associations in 1.25 million people. Lancet. 2014 May 31;383(9932):1899-911. doi: 10.1016/S0140-6736(14)60685-1. PMID: 24881994 |
| Shah AD et al. Type 2 diabetes and incidence of cardiovascular diseases: a cohort study in 1.9 million people. Lancet Diabetes Endocrinol. 2015 Feb;3(2):105-13. doi: 10.1016/S2213-8587(14)70219-0. Epub 2014 Nov 11. PMID: 25466521 |
| Rapsomaniki E et al. Prognostic models for stable coronary artery disease based on electronic health record cohort of 102 023 patients. Eur Heart J. 2014 Apr;35(13):844-52. doi: 10.1093/eurheartj/eht533. Epub 2013 Dec 17. PMID: 24353280 |