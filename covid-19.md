---
layout: page
title: PHE00000 - COVID-19
phenotype_id: PHE00000
name: COVID-19
type: Disease or Syndrome
group: Influenza
data_sources: Primary care (CPRD), Hospital Admission Data (HES), Mortality Data (ONS)
clinical_terminologies: ICD-10, ICD-11, CTV3, EMIS, Vision, SNOMED-CT (UK), SNOMED-CT(Int.), LOINC, openEHR
validation: 
primary_care_code_lists:
secondary_care_code_lists:
death:
valid_event_data_range: 01/01/1999 - 01/07/2016
sex: Female/Male
author: Spiros Denaxas, Susheel Varma
status: DRAFT
date: 2020-03-26
modified_date: 2020-03-26
version: Revision 0
---

A comprehensive, open-access resource providing the research community with information, tools and phenotyping algorithms for defining COVID-19 related phenotypes in UK electronic health records data

<hr>

* [Controlled clinical terminology terms](#section-ehr-terms)
    * [ICD-10](#section-ehr-terms-icd)
    * [ICD-11](#section-ehr-terms-icd)
    * [Clinical Terms Version 3 (CTV3)](#section-primary-care-terms-ctv3)
    * [EMIS](#section-primary-care-terms-emis)
    * [Vision](#section-primary-care-terms-vision)
    * [UK SNOMED-CT](#section-primary-care-terms-snomed-uk)
    * [Intl. SNOMED-CT](#section-primary-care-terms-snomed)
    * [LOINC](#section-ehr-terms-loinc)
    * [opernEHR](#section-ehr-terms-openehr)
* [Prevalence estimates](#section-estimates)
* [Public Health England high risk definition](#section-high-risk)
    * [Phenotyping algorithms](#section-algorithms)
* [How to contribute](#section-contribute)

<hr>

# Modelled Prevalence Estimates <a name="section-estimates">

| Phenotype | Data Sources | Country | Authors | Ref |
|-----------|--------------|---------|---------|-----|
| CVD, diabetes, CKD, COPD, HIV, others | CALIBER primary care, hospitalization, mortality EHR | UK | Banerjee A. | * [Preprint on ResearchGate](https://www.researchgate.net/publication/340092652_Estimating_excess_1-_year_mortality_from_COVID-19_according_to_underlying_conditions_and_age_in_England_a_rapid_analysis_using_NHS_health_records_in_38_million_adults) <br> * [Algorithms](https://caliberresearch.org/portal/) | 
| COPD, CHD, stroke, PAD, HF, HT, depression | Clinical Practice Research Datalink | UK | Public Health England, Imperial College | [PHE fingertips](https://fingertips.phe.org.uk/profile/prevalence) |
| CVD, Respiratory, high-dependency conditions | Primary care - QoF | UK | NHS Digital | [Quality and Outcomes Framework, Achievement, prevalence and exceptions data 2018-19](https://digital.nhs.uk/data-and-information/publications/statistical/quality-and-outcomes-framework-achievement-prevalence-and-exceptions-data/2018-19-pas#resources)
| Comorbidities for severe COVID-19 infections | meta analyses | China | Jain V | [Systematic review and meta-analysis of predictive symptoms and comorbidities for severe COVID-19 infection](https://www.medrxiv.org/content/10.1101/2020.03.15.20035360v1.full.pdf) |

<hr>

## [Public Health England definition](https://www.gov.uk/government/publications/covid-19-guidance-on-social-distancing-and-for-vulnerable-people/guidance-on-social-distancing-for-everyone-in-the-uk-and-protecting-older-people-and-vulnerable-adults) for populations at increased risk of severe illness from coronavirus (COVID-19): <a name="section-high-risk">

1. Aged 70 or older (regardless of medical conditions).

2. Under 70 with an underlying health condition listed below (ie anyone instructed to get a flu jab as an adult each year on medical grounds):

* chronic (long-term) [respiratory diseases](#algo-respiratory), such as asthma, chronic obstructive pulmonary disease (COPD), emphysema or bronchitis
* [chronic heart disease](#algo-chd), such as heart failure
* [chronic kidney disease](#algo-renal)
* chronic liver disease, such as hepatitis
* chronic neurological conditions, such as Parkinson’s disease, motor neurone disease, multiple sclerosis (MS), a learning disability or cerebral palsy
*  [diabetes](#algo-endocrine)
*  problems with your spleen – for example, sickle cell disease or if you have had your spleen removed
*  a weakened immune system as the result of conditions such as HIV and AIDS, or medicines such as steroid tablets or chemotherapy
*  being seriously overweight (a body mass index (BMI) of 40 or above)
*  those who are [pregnant](#algo-pregnancy)

There are some clinical conditions which put people at even higher risk of severe illness from COVID-19:

* people who have received an organ transplant and remain on ongoing immunosuppression medication
* people with cancer who are undergoing active chemotherapy or radiotherapy
* people with cancers of the blood or bone marrow such as leukaemia who are at any stage of treatment
* people with severe chest conditions such as cystic fibrosis or severe asthma (requiring hospital admissions or courses of steroid tablets)
* people with severe diseases of body systems, such as severe kidney disease (dialysis)

### Phenotyping algorithms <a name="section-algorithms">

#### Respiratory <a name="algo-respiratory">
{% assign disease_phenotypes = site.phenotypes | where: "group", "Respiratory" | sort: "name" %}

| Phenotype | Data Sources | Country | Authors | PMID/URL |
|-----------|--------------|------------|{% for phenotype in disease_phenotypes %}
| [{{ phenotype.name }}]({{ phenotype.url }}) | {% for p in phenotype.data_sources %} {{ p }} <br> {% endfor %} | {{ phenotype.country }} | {{ phenotype.contact_author }} | <a href="https://www.ncbi.nlm.nih.gov/pubmed/{{ phenotype.PMID }}">{{ phenotype.PMID}}</a> | {% endfor %}


#### Endocrine <a name="algo-endocrine">
{% assign disease_phenotypes = site.phenotypes | where: "group", "Endocrine" | sort: "name" %}

| Phenotype | Data Sources | Country | Authors | PMID/URL |
|-----------|--------------|------------|{% for phenotype in disease_phenotypes %}
| [{{ phenotype.name }}]({{ phenotype.url }}) | {% for p in phenotype.data_sources %} {{ p }} <br> {% endfor %} | {{ phenotype.country }} | {{ phenotype.contact_author }} | <a href="https://www.ncbi.nlm.nih.gov/pubmed/{{ phenotype.PMID }}">{{ phenotype.PMID}}</a> | {% endfor %}

#### Renal disease <a name="algo-renal">

| Phenotype | Data Sources | Country | Authors | PMID/URL |
|-----------|--------------|---------|---------|----------|
| End Stage Renal Disease | UK Biobank | UK | Kathryn Bush, John Nolan, Qiuli Zhang, Will Herrington and Cathie Sudlow | [URL](http://biobank.ctsu.ox.ac.uk/crystal/crystal/docs/alg_outcome_esrd.pdf) | 

#### Coronary Heart Disease <a name="algo-chd">

| Phenotype | Data Sources | Country | Authors | PMID/URL |
|-----------|--------------|---------|---------|----------|
| HF | Clinical Practice Research Datalink, Hospital Episode Statistics, Office of National Statistics | UK | CALIBER team | [URL](https://caliberresearch.org/portal/phenotypes/heartfailure) | 
| CHD | Clinical Practice Research Datalink, Hospital Episode Statistics, Office of National Statistics | UK | CALIBER team | [URL](https://caliberresearch.org/portal/phenotypes/coronaryheartdisease) | 

#### Pregnancy <a name="algo-pregnancy">

| Phenotype | Data Sources | Country | Authors | PMID/URL |
|-----------|--------------|---------|---------|----------|
| Pregnancy | Clinical Practice Research Datalink, Hospital Episode Statistics | UK | CALIBER team | [URL](https://caliberresearch.org/portal/phenotypes/pregnancy) | 


<hr>

## EHR case definitions and related codes <a name="section-ehr-terms">

<p>Codes used to record COVID-19 related events in electronic health records.</p>
<strong>Contributors</strong>: Aziz Sheikh, Jenni Quint, the [Health Data Research Hub for Respiratory Health (BREATHE)](https://www.hdruk.ac.uk/infrastructure/the-hubs/breathe/), Neil Sebire (GOSH), Susheel Varma (HDR UK), David Seymour (HDR UK).

#### International Classification of Diseases 10th revision (ICD-10) <a name="section-ehr-terms-icd">

<p>New International Classification of Diseases emergency codes have been <a href="https://www.who.int/classifications/icd/covid19/en/">established by the WHO</a>. </p>

<p>In the UK, the National Clinical Coding Standards have been updated to include confirmed/probably cases of COVID-19 and related manifestations (e.g. pneumonia) which should be followed by the addition of <i>B97.2 Coronavirus as the cause of diseases classified to other chapters.</i> - more information available from the <a href="https://hscic.kahootz.com/connect.ti/t_c_home/view?objectID=19099248">NHS Digital guidance.</a></p>

| ICD-10 code | Term | 
|-------------|------|
| U07.1 | Diagnosis of COVID-19 confirmed by laboratory testing |
| U07.2 | Diagnosis of COVID-19 suspected or probable |

#### International Classification of Diseases 10th revision (ICD-11)

| ICD-10 code | Term | 
|-------------|------|
| RA01.0 | Diagnosis of COVID-19 confirmed by laboratory testing |
| RA01.2 | Diagnosis of COVID-19 suspected or probable |

#### Clinical Terms Version 3 (CTV3) <a name="section-primary-care-terms-ctv3">

 | CTv3 Code | Code description | 
 |-----------|------------------|
 | Y20d2 | Excluded 2019-nCoV (Wuhan) infection |
 | Y20d1 | Confirmed 2019-nCoV (Wuhan) infection | 
 | Y20d0 | Tested for 2019-nCoV (Wuhan) infection | 
 | Y20cf | Suspected 2019-nCoV (Wuhan) infection | 
 | Y20ce | Exposure to 2019-nCoV (Wuhan) infection  | 

#### EMIS <a name="section-primary-care-terms-emis">

| Code | Term |
|------|------|
| EMISNQEX58   |                  Exposure to 2019-nCoV (Wuhan) infection | 
| EMISNQSU106  |                Suspected 2019-nCoV (Wuhan) infection | 
| EMISNQTE31   |                  Tested for 2019-nCoV (Wuhan) infection | 
| EMISNQCO303  |                2019-nCoV (Wuhan) infection | 
| EMISNQEX59   |                  Excluded 2019-nCoV (Wuhan) infection | 
 
#### Vision <a name="section-primary-care-terms-vision">

| Type | Code | Term | 
|------|------|------|
| Clinical finding | 4J3R100 | 2019-nCoV (novel coronavirus) detected |
| Clinical finding |4J3R200 | 2019-nCoV (novel coronavirus) not detected |
| Clinical finding |9Niq. |Did not attend 2019-nCoV (novel coronavirus) vaccination |
| Clinical finding | A7951 | Disease caused by 2019-nCoV (novel coronavirus) |
| Event | 65PW100 | Exposure to 2019-nCoV (novel coronavirus) infection |
| Observable entity | 4J3R. |                                      2019-nCoV (novel coronavirus) serology |
| Procedure          |9N312            |                       Telephone consultation for suspected 2019-nCoV (novel coronavirus) |
| Situation with explicit context | 8CAO1 |                                 Advice given about 2019-nCoV (novel coronavirus) by telephone |
| Situation with explicit context | 8CAO.  |                                 Advice given about 2019-nCoV (novel coronavirus) infection |
| Situation with explicit context | 1JX1. |                                      Suspected disease caused by 2019-nCoV (novel coronavirus) |

#### UK SNOMED-CT <a name="section-primary-care-terms-snomed-uk">

SNOMED-CT terms used in UK primary care extracted from <i>de Lusignan S, et al. (2020) Emergence of a Novel Coronavirus (COVID-19): A Protocol for Extending Surveillance Used by the Royal College of General Practitioners (RCGP) Research and Surveillance Centre (RSC) and Public Health England (PHE). JMIR Public Health and Surveillance. DOI: <a href="https://doi.org/10.2196/18606">10.2196/18606</a>.

| Type | ConceptID		| DescriptionID	| 
|---------------|-----------|---------------|-----------|
| Clinical finding | 1240581000000104  | 2019-nCoV (novel coronavirus) detected |
| Clinical finding | 1240591000000102  | 2019-nCoV (novel coronavirus) not detected |
| Clinical finding | 1240631000000102  | Did not attend 2019-nCoV (novel coronavirus) vaccination |
| Clinical finding | 1240751000000100  | Disease caused by 2019-nCoV (novel coronavirus) |
| Clinical finding | 1240561000000108  | Encephalopathy caused by 2019-nCoV (novel coronavirus) |
| Clinical finding | 1240571000000101  | Gastroenteritis caused by 2019-nCoV (novel coronavirus) |
| Clinical finding | 1240601000000108  | High priority for 2019-nCoV (novel coronavirus) vaccination |
| Clinical finding | 1240531000000103  | Myocarditis caused by 2019-nCoV (novel coronavirus) |
| Clinical finding | 1240521000000100  |  Otitis media caused by 2019-nCoV (novel coronavirus) |
| Clinical finding | 1240551000000105  | Pneumonia caused by 2019-nCoV (novel coronavirus) |
| Clinical finding | 1240541000000107  |  Upper respiratory tract infection caused by 2019-nCoV (novel coronavirus) |
| Event | 1240431000000104  | Exposure to 2019-nCoV (novel coronavirus) infection |
| Observable entity | 1240741000000103 2019-nCoV |(novel coronavirus) serology |
| Procedure | 1240491000000103 | 2019-nCoV (novel coronavirus) vaccination |
| Procedure | 1240511000000106  |Detection of 2019-nCoV (novel coronavirus) using polymerase chain reaction technique |
| Procedure | 1240461000000109  |Measurement of 2019-nCoV (novel coronavirus) antibody |
| Procedure | 1240471000000102  |Measurement of 2019-nCoV (novel coronavirus) antigen |
| Procedure | 1240451000000106  |Telephone consultation for suspected 2019-nCoV (novel coronavirus) |
| Qualifier value | 1240421000000101 | Serotype 2019-nCoV (novel coronavirus) | 
| Situation with explicit context | 1240661000000107  | 2019-nCoV (novel coronavirus) vaccination contraindicated  | 
| Situation with explicit context | 1240651000000109  | 2019-nCoV (novel coronavirus) vaccination declined | 
| Situation with explicit context | 1240781000000106  | 2019-nCoV (novel coronavirus) vaccination invitation short message service text nessage | 
| Situation with explicit context | 1240681000000103 |  2019-nCoV (novel coronavirus) vaccination not done | 
| Situation with explicit context | 1240671000000100 |  2019-nCoV (novel coronavirus) vaccination not indicated | 
| Situation with explicit context | 1240701000000101 |  2019-nCoV (novel coronavirus) vaccine not available | 
| Situation with explicit context | 1240731000000107 |  Advice given about 2019-nCoV (novel coronavirus) by telephone | 
| Situation with explicit context | 1240721000000105 |  Advice given about 2019-nCoV (novel coronavirus) infection | 
| Situation with explicit context | 1240711000000104 |  Educated about 2019-nCoV (novel coronavirus) infection | 
| Situation with explicit context | 1240761000000102 | Suspected disease caused by 2019-nCoV (novel coronavirus) | 
| Substance | 1240401000000105  | Antibody to 2019-nCoV (novel coronavirus) |
| Substance | 1240391000000107  | Antigen of 2019-nCoV (novel coronavirus) |
| Substance| 1240411000000107 |  Ribonucleic acid of 2019-nCoV (novel coronavirus) |

#### SNOMED-CT <a name="section-primary-care-terms-snomed">

The March 2020 release contains relevant COVID-19 concepts including any applicable changes to descriptions ([source](http://www.snomed.org/news-and-events/articles/march-2020-interim-snomedct-release-COVID-19)). These terms are not compatible with current UK clinical codes)


| ConceptID		| Type		| DescriptionID	| 	Term	| 
|---------------|-----------|---------------|-----------|
| 138875005	| 	FSN		| 3947198019		| SNOMED Clinical Terms version: 20200309 [R] (March 2020 Interim Release)	| 
| 840539006	| 	FSN		| 3947183016		| Disease caused by severe acute respiratory syndrome coronavirus 2 (disorder)	| 
| 840539006	| 	Synonym		| 3947184010	| 	Disease caused by severe acute respiratory syndrome coronavirus 2	| 
| 840539006	| 	Synonym		| 3947185011	| 	COVID-19	| 
| 840544004	| 	FSN		| 3947197012		| Suspected disease caused by severe acute respiratory coronavirus 2 (situation)	| 
| 840544004	| 	Synonym		| 3947196015	| 	Suspected disease caused by severe acute respiratory coronavirus 2	| 
| 840544004	| 	Synonym		| 3947195016	| 	Suspected disease caused by SARS-CoV-2	| 
| 840544004	| 	Synonym		| 3950926016	| 	Suspected COVID-19	| 
| 840546002	| 	FSN		| 3947186012	| 	Exposure to severe acute respiratory syndrome coronavirus 2 (event)	| 
| 840546002	| 	Synonym		| 3947187015	| 	Exposure to SARS-CoV-2	| 
| 840546002	| 	Synonym		| 3947188013	| 	Exposure to severe acute respiratory syndrome coronavirus 2	| 
| 840533007	| 	FSN		| 3947189017		| Severe acute respiratory syndrome coronavirus 2 (organism)	| 
| 840533007	| 	Synonym		| 3947191013	| 	Severe acute respiratory syndrome coronavirus 2	| 
| 840533007	| 	Synonym		| 3947190014	| 	SARS-CoV-2	| 
| 840536004	| 	FSN		| 3947180018		| Antigen of severe acute respiratory syndrome coronavirus 2 (substance)	| 
| 840536004	| 	Synonym		| 3947181019	| 	Antigen of severe acute respiratory syndrome coronavirus 2	| 
| 840536004	| 	Synonym		| 3947182014	| 	Antigen of SARS-CoV-2	| 
| 840535000	| 	FSN		| 3947177019		| Antibody to severe acute respiratory syndrome coronavirus 2 (substance)	| 
| 840535000	| 	Synonym		| 3947178012	| 	Antibody to severe acute respiratory syndrome coronavirus 2	| 
| 840535000	| 	Synonym		| 3947179016		| Antibody to SARS-CoV-2	| 
| 840534001	| 	FSN	| 	3947192018		| Severe acute respiratory syndrome coronavirus 2 vaccination (procedure)	| 
| 840534001	| 	Synonym		| 3947194017	| 	Severe acute respiratory syndrome coronavirus 2 vaccination	| 
| 840534001	| 	Synonym		| 3947193011	| 	SARS-CoV-2 vaccination	| 
| 840534001	| Synonym		| 3950925017	| 	COVID-19 vaccination	| 

#### Logical Observation Identifiers Names and Codes (LOINC) <a name="section-ehr-terms-loinc">

* [LOINC terms](https://loinc.org/sars-coronavirus-2/) for commercial in vitro diagnostics (IVD) test kits/

#### openEHR <a name="section-ehr-terms-openehr">

* [Archetypes and templates](https://www.openehr.org/ckm/projects/1013.30.81) related to data sets representing all aspects of COVID-19 data recording and capture, including but not limited to risk assessment, contact tracing and reporting. 


## Contributing <a name="section-contribute">
Contributions are encouraged!

You can contribute by:
* a pull request to this repository
* or emailing s.denaxas[@]ucl.ac.uk