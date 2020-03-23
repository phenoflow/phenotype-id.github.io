---
layout: home
title: Biomarkers
---

## Biomarkers
{% assign biomarker_phenotypes = site.phenotypes | where: "type", "Biomarker" %}
| ID | Phenotype | Data Sources | Validation |
|----|-----------|--------------|------------|{% for phenotype in biomarker_phenotypes %}
| [{{ phenotype.phenotype_id}}]({{ phenotype.url }}) | [{{ phenotype.name }}]({{ phenotype.url }}) | {{ phenotype.data_sources }} | {{ phenotype.validation }} |{% endfor %}

