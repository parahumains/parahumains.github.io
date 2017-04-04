# -*- coding: utf-8 -*-
import os
import sys

arcs = [
    'Gestation',
    'Insinuation',
    'Agitation',
    'Coquille',
    'Ruche',
    'Fouillis',
    'Bourdonnement',
    'Extermination',
    'Sentinelle',
    'Parasite',
    'Infestation',
    'Peste',
    'Piège',
    'Proie',
    'Colonie',
    'Monarque',
    'Migration',
    'Reine',
    'Fléau',
    'Chrysalide',
    'Imago',
    'Cellule',
    'Rouage',
    'Écrasé',
    'Scarabée',
    'Piqûre',
    'Disparition',
    'Cafards',
    'Venin',
    'Grain',
    'Épilogue'
]


def main():
    arc = get_input('Chapter arc: ').title()

    if arc not in arcs:
        print('Are you sure that {} is an arc?'.format(arc))
        exit()

    name = get_input('Chapter name: ')
    filename = get_input('File name (w/ ext.): ')

    sep = os.linesep

    with open(os.path.join('_drafts', filename), 'w+') as file:
        file.write('---' + sep)
        file.write('layout: post' + sep)
        file.write('title: {} {}'.format(arc, name + sep))
        file.write('category: {}'.format(arc + sep))
        file.write('---' + sep)
        file.write(sep)

if __name__ == '__main__':
    get_input = input

    if sys.version_info[:2] <= (2, 7):
        get_input = raw_input
    main()

