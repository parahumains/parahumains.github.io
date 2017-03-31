---
layout: default
---

## Sommaire
{% assign arcs =
    "Gestation,
    Insinuation,
    Agitation,
    Coquille,
    Ruche,
    Fouillis,
    Bourdonnement,
    Extermination,
    Sentinelle,
    Parasite,
    Infestation,
    Peste,
    Piège,
    Proie,
    Colonie,
    Monarque,
    Migration,
    Reine,
    Fléau,
    Chrysalide,
    Imago,
    Cellule,
    Rouage,
    Écrasé,
    Scarabée,
    Piqûre,
    Disparition,
    Cafards,
    Venin,
    Grain,
    Épilogue" | split: "," %}

<div>
{% for arc_with_newline in arcs %}
    {% assign arc = arc_with_newline | strip %}
    {% assign chapter_in_arc = site.categories[arc] %}

    {% if chapter_in_arc != null %}
    <div>
        {{ arc }}
        <ul>
        {% for chapter in chapter_in_arc reversed %}
            <li><a href="{{ chapter.url }}">{{ chapter.title }}</a></li>
        {% endfor %}
        </ul>
    </div>
    {% endif %}
{% endfor %}
</div>