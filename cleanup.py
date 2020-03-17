import re
import os
import string
import csv
import glob

DATA_DIR = "_data"
PRIMARY_CARE_DIR = os.path.join(DATA_DIR,"primary_care")
PRIMARY_CARE_FILES = [f for f in os.listdir(PRIMARY_CARE_DIR) if os.path.isfile(os.path.join(PRIMARY_CARE_DIR,f))]

SECONDARY_CARE_DIR = os.path.join(DATA_DIR,"secondary_care")
SECONDARY_CARE_FILES = [f for f in os.listdir(SECONDARY_CARE_DIR) if os.path.isfile(os.path.join(SECONDARY_CARE_DIR,f))]
FIELDNAMES = []

def read_csv(filename):
    data = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        FIELDNAMES = reader.fieldnames
        for row in reader:
            data.append(row)
    return data, FIELDNAMES

def write_csv(filename, data, fieldnames=FIELDNAMES):
    print(fieldnames)
    with open(filename, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


def cleanup_data(data, FIELDNAMES):
    COUNT = 1
    FIELDNAMES.extend(['id', 'primary_care', 'secondary_care', 'type', 'data_sources', 'clinical_terminologies', 'validation',
                        'valid_event_data_range', 'sex', 'date', 'modified_date', 'version', 'authors'])
    for d in data:
        d['id'] = "PHE" + format(COUNT, '05d')
        d['phenotype'] = string.capwords(d['name_portal'])
        d['primary_care'] = []
        d['secondary_care'] = []
        d['data_sources'] = ['Primary care (CPRD)', 'Hospital Admission Data (HES)', 'Mortality Data (ONS)']
        d['clinical_terminologies'] = ['Read', 'ICD-10', 'ICD-9', 'OPCS-4']
        d['validation'] = ["cross-source", "casenote", "aetiology", "prognosis", "genetic external"]
        d['valid_event_data_range'] = "01/01/1999 - 01/07/2016"
        d['sex'] = "Female/Male"
        d['date'] = "2012-11-23"
        d['modified_date'] = "2012-11-23"
        d['version'] = "Revision 2"
        d['authors'] = ['Julie George', 'Emily Herrett', 'Liam Smeeth', 'Harry Hemingway', 'Anoop Shah', 'Spiros Denaxas']

        for key, value in d.items():
            # print(d['name_portal'])
            if key in ['CPRD', 'ICD', 'OPCS']:
                # print(key, value)
                if value in PRIMARY_CARE_FILES:
                    value = os.path.join(PRIMARY_CARE_DIR,value)
                    d['primary_care'].append(value)
                elif value in SECONDARY_CARE_FILES:
                    value = os.path.join(SECONDARY_CARE_DIR,value)
                    d['secondary_care'].append(value)
                # print(key, value)
                d[key] = value
        COUNT += 1
    return data, FIELDNAMES

def template_markdown(dir, data):
    from jinja2 import Template

    files = glob.glob(dir + "/*.md")
    for f in files:
        try:
            os.remove(f)
        except OSError as e:
            print("Error: %s : %s" % (f, e.strerror))

    TEMPLATE = Template("""---
layout: phenotype
title: {{ id }} - {{ phenotype }}
phenotype_id: {{ id }}
name: {{ phenotype }}
type: {{ type }}
group: {{ group }}
data_sources: {{ data_sources|join(', ') }}
clinical_terminologies: {{ clinical_terminologies|join(', ') }}
validation: {{ validation|join(', ') }}
primary_care_code_lists: {{ primary_care|join(', ') }}
secondary_care_code_lists: {{ secondary_care|join(', ') }}
valid_event_data_range: {{ valid_event_data_range }}
sex: {{ sex }}
author: {{ authors|join(', ') }}
status: DRAFT
date: {{ date }}
modified_date: {{ modified_date }}
version: {{ version }}
---

### Primary Care

In the Clinical Practice Research Datalink (CPRD, primary care data) we ascertained {% raw %}{{ page.name }}{% endraw %} cases by searching for Read terms related to an {% raw %}{{ page.name }}{% endraw %} diagnosis or evidence of endovascular/transluminal procedures related to the emergency repair of an aneurysmal segment of the aorta.
{% for data_file in primary_care %}{% set data = data_file|replace("/primary_care/", "")|replace(".csv", "") %}
{% raw %}{% include csv.html csvdata=site.primary_care.{% endraw %}{{ data }}{% raw %} %}{% endraw %}{% endfor %}

Read terms are hierarhically organized in top-level chapters i.e. chapter G....00 is related to Circulatory System Diseases and sub-headings i.e. heading G2...00 is related to Hypertensive Heart Disease while G3...00 is related to Ischaemic Heart Disease.

### Secondary Care

In Hospital Episode Statistics (HES, hospital admission data) we used ICD-10 terms (see below) for {% raw %}{{ page.name }}{% endraw %} diagnosis when marked as the primary diagnosis i.e. the main condition treated or investigated during the relevant episode of healthcare. We used the date of admission to hospital as the date of the event. We additionally searched for OPCS-4 terms indicating the emergency repair of an aneurysmal segment of the aorta.
{% for data_file in secondary_care %}{% set data = data_file|replace("/secondary_care/", "")|replace(".csv", "") %}
{% raw %}{% include csv.html csvdata=site.secondary_care.{% endraw %}{{ data }}{% raw %} %}{% endraw %}
{% endfor %}

### Death

### Implementation

**Combining evidence across sources to define and date phenotypes**

<pre>
{{ implementation }}
</pre>

### Validations

### Publications


""")
    for d in data:
        filename = re.sub(r" ?\([^)]+\)", "", d['name_portal'])
        filename = filename.replace('_', ' ').replace('/', '-').replace(', ', '-').replace('\'', '').replace(' - ', '-').replace(' ', '-').lower()
        d['primary_care'] = [f[5:] for f in d['primary_care']]
        d['secondary_care'] = [f[5:] for f in d['secondary_care']]
        with open(os.path.join(dir, filename + ".md"), mode='w') as mdfile:
            mdfile.write(TEMPLATE.render(d))


def main():
    data, FIELDNAMES = read_csv("_data/catalogue.csv")
    data, FIELDNAMES  = cleanup_data(data, FIELDNAMES)
    write_csv('_data/phenotype_catalogue.csv', data, FIELDNAMES)
    template_markdown('_phenotypes', data)
    

if __name__ == "__main__":
    main()