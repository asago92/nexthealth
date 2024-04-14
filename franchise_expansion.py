import streamlit as st
import streamlit_highcharts as hg
import requests


chartDef={ 'accessibility': { 'description': 'A '
                                    'tile '
                                    'map '
                                    'represents '
                                    'the '
                                    'states '
                                    'of '
                                    'the '
                                    'USA '
                                    'by '
                                    'population '
                                    'in '
                                    '2016. '
                                    'The '
                                    'hexagonal '
                                    'tiles '
                                    'are '
                                    'positioned '
                                    'to '
                                    'geographically '
                                    'echo '
                                    'the '
                                    'map '
                                    'of '
                                    'the '
                                    'USA. '
                                    'A '
                                    'color-coded '
                                    'legend '
                                    'states '
                                    'the '
                                    'population '
                                    'levels '
                                    'as '
                                    'below '
                                    '1 '
                                    'million '
                                    '(beige), '
                                    '1 '
                                    'to '
                                    '5 '
                                    'million '
                                    '(orange), '
                                    '5 '
                                    'to '
                                    '20 '
                                    'million '
                                    '(pink) '
                                    'and '
                                    'above '
                                    '20 '
                                    'million '
                                    '(hot '
                                    'pink). '
                                    'The '
                                    'chart '
                                    'is '
                                    'interactive, '
                                    'and '
                                    'the '
                                    'individual '
                                    'state '
                                    'data '
                                    'points '
                                    'are '
                                    'displayed '
                                    'upon '
                                    'hovering. '
                                    'Three '
                                    'states '
                                    'have '
                                    'a '
                                    'population '
                                    'of '
                                    'above '
                                    '20 '
                                    'million: '
                                    'California '
                                    '(39.3 '
                                    'million), '
                                    'Texas '
                                    '(27.9 '
                                    'million) '
                                    'and '
                                    'Florida '
                                    '(20.6 '
                                    'million). '
                                    'The '
                                    'northern '
                                    'US '
                                    'region '
                                    'from '
                                    'Massachusetts '
                                    'in '
                                    'the '
                                    'Northwest '
                                    'to '
                                    'Illinois '
                                    'in '
                                    'the '
                                    'Midwest '
                                    'contains '
                                    'the '
                                    'highest '
                                    'concentration '
                                    'of '
                                    'states '
                                    'with '
                                    'a '
                                    'population '
                                    'of '
                                    '5 '
                                    'to '
                                    '20 '
                                    'million '
                                    'people. '
                                    'The '
                                    'southern '
                                    'US '
                                    'region '
                                    'from '
                                    'South '
                                    'Carolina '
                                    'in '
                                    'the '
                                    'Southeast '
                                    'to '
                                    'New '
                                    'Mexico '
                                    'in '
                                    'the '
                                    'Southwest '
                                    'contains '
                                    'the '
                                    'highest '
                                    'concentration '
                                    'of '
                                    'states '
                                    'with '
                                    'a '
                                    'population '
                                    'of '
                                    '1 '
                                    'to '
                                    '5 '
                                    'million '
                                    'people. '
                                    '6 '
                                    'states '
                                    'have '
                                    'a '
                                    'population '
                                    'of '
                                    'less '
                                    'than '
                                    '1 '
                                    'million '
                                    'people; '
                                    'these '
                                    'include '
                                    'Alaska, '
                                    'Delaware, '
                                    'Wyoming, '
                                    'North '
                                    'Dakota, '
                                    'South '
                                    'Dakota '
                                    'and '
                                    'Vermont. '
                                    'The '
                                    'state '
                                    'with '
                                    'the '
                                    'lowest '
                                    'population '
                                    'is '
                                    'Wyoming '
                                    'in '
                                    'the '
                                    'Northwest '
                                    'with '
                                    '584,153 '
                                    'people.',
                     'point': { 'valueDescriptionFormat': '{index}. '
                                                          '{xDescription}, '
                                                          '{point.value}.'},
                     'screenReaderSection': { 'beforeChartFormat': '<h5>{chartTitle}</h5>+<div>{chartSubtitle}</div>+<div>{chartLongdesc}</div>+<div>{viewTableButton}</div>'}},
  'chart': { 'height': '80%',
             'inverted': True,
             'type': 'tilemap'},
  'colorAxis': { 'dataClasses': [ { 'color': '#F9EDB3',
                                    'from': 0,
                                    'name': '< '
                                            '1M',
                                    'to': 1000000},
                                  { 'color': '#FFC428',
                                    'from': 1000000,
                                    'name': '1M '
                                            '- '
                                            '5M',
                                    'to': 5000000},
                                  { 'color': '#FF7987',
                                    'from': 5000000,
                                    'name': '5M '
                                            '- '
                                            '20M',
                                    'to': 20000000},
                                  { 'color': '#FF2371',
                                    'from': 20000000,
                                    'name': '> '
                                            '20M'}]},
  'plotOptions': { 'series': { 'dataLabels': { 'color': '#000000',
                                               'enabled': True,
                                               'format': '{point.hc-a2}',
                                               'style': { 'textOutline': False}}}},
  'series': [ { 'data': [ { 'hc-a2': 'AL',
                            'name': 'Alabama',
                            'region': 'South',
                            'value': 4849377,
                            'x': 6,
                            'y': 7},
                          { 'hc-a2': 'AK',
                            'name': 'Alaska',
                            'region': 'West',
                            'value': 737732,
                            'x': 0,
                            'y': 0},
                          { 'hc-a2': 'AZ',
                            'name': 'Arizona',
                            'region': 'West',
                            'value': 6745408,
                            'x': 5,
                            'y': 3},
                          { 'hc-a2': 'AR',
                            'name': 'Arkansas',
                            'region': 'South',
                            'value': 2994079,
                            'x': 5,
                            'y': 6},
                          { 'hc-a2': 'CA',
                            'name': 'California',
                            'region': 'West',
                            'value': 39250017,
                            'x': 5,
                            'y': 2},
                          { 'hc-a2': 'CO',
                            'name': 'Colorado',
                            'region': 'West',
                            'value': 5540545,
                            'x': 4,
                            'y': 3},
                          { 'hc-a2': 'CT',
                            'name': 'Connecticut',
                            'region': 'Northeast',
                            'value': 3596677,
                            'x': 3,
                            'y': 11},
                          { 'hc-a2': 'DE',
                            'name': 'Delaware',
                            'region': 'South',
                            'value': 935614,
                            'x': 4,
                            'y': 9},
                          { 'hc-a2': 'DC',
                            'name': 'District '
                                    'of '
                                    'Columbia',
                            'region': 'South',
                            'value': 7288000,
                            'x': 4,
                            'y': 10},
                          { 'hc-a2': 'FL',
                            'name': 'Florida',
                            'region': 'South',
                            'value': 20612439,
                            'x': 8,
                            'y': 8},
                          { 'hc-a2': 'GA',
                            'name': 'Georgia',
                            'region': 'South',
                            'value': 10310371,
                            'x': 7,
                            'y': 8},
                          { 'hc-a2': 'HI',
                            'name': 'Hawaii',
                            'region': 'West',
                            'value': 1419561,
                            'x': 8,
                            'y': 0},
                          { 'hc-a2': 'ID',
                            'name': 'Idaho',
                            'region': 'West',
                            'value': 1634464,
                            'x': 3,
                            'y': 2},
                          { 'hc-a2': 'IL',
                            'name': 'Illinois',
                            'region': 'Midwest',
                            'value': 12801539,
                            'x': 3,
                            'y': 6},
                          { 'hc-a2': 'IN',
                            'name': 'Indiana',
                            'region': 'Midwest',
                            'value': 6596855,
                            'x': 3,
                            'y': 7},
                          { 'hc-a2': 'IA',
                            'name': 'Iowa',
                            'region': 'Midwest',
                            'value': 3107126,
                            'x': 3,
                            'y': 5},
                          { 'hc-a2': 'KS',
                            'name': 'Kansas',
                            'region': 'Midwest',
                            'value': 2904021,
                            'x': 5,
                            'y': 5},
                          { 'hc-a2': 'KY',
                            'name': 'Kentucky',
                            'region': 'South',
                            'value': 4413457,
                            'x': 4,
                            'y': 6},
                          { 'hc-a2': 'LA',
                            'name': 'Louisiana',
                            'region': 'South',
                            'value': 4649676,
                            'x': 6,
                            'y': 5},
                          { 'hc-a2': 'ME',
                            'name': 'Maine',
                            'region': 'Northeast',
                            'value': 1330089,
                            'x': 0,
                            'y': 11},
                          { 'hc-a2': 'MD',
                            'name': 'Maryland',
                            'region': 'South',
                            'value': 6016447,
                            'x': 4,
                            'y': 8},
                          { 'hc-a2': 'MA',
                            'name': 'Massachusetts',
                            'region': 'Northeast',
                            'value': 6811779,
                            'x': 2,
                            'y': 10},
                          { 'hc-a2': 'MI',
                            'name': 'Michigan',
                            'region': 'Midwest',
                            'value': 9928301,
                            'x': 2,
                            'y': 7},
                          { 'hc-a2': 'MN',
                            'name': 'Minnesota',
                            'region': 'Midwest',
                            'value': 5519952,
                            'x': 2,
                            'y': 4},
                          { 'hc-a2': 'MS',
                            'name': 'Mississippi',
                            'region': 'South',
                            'value': 2984926,
                            'x': 6,
                            'y': 6},
                          { 'hc-a2': 'MO',
                            'name': 'Missouri',
                            'region': 'Midwest',
                            'value': 6093000,
                            'x': 4,
                            'y': 5},
                          { 'hc-a2': 'MT',
                            'name': 'Montana',
                            'region': 'West',
                            'value': 1023579,
                            'x': 2,
                            'y': 2},
                          { 'hc-a2': 'NE',
                            'name': 'Nebraska',
                            'region': 'Midwest',
                            'value': 1881503,
                            'x': 4,
                            'y': 4},
                          { 'hc-a2': 'NV',
                            'name': 'Nevada',
                            'region': 'West',
                            'value': 2839099,
                            'x': 4,
                            'y': 2},
                          { 'hc-a2': 'NH',
                            'name': 'New '
                                    'Hampshire',
                            'region': 'Northeast',
                            'value': 1326813,
                            'x': 1,
                            'y': 11},
                          { 'hc-a2': 'NJ',
                            'name': 'New '
                                    'Jersey',
                            'region': 'Northeast',
                            'value': 8944469,
                            'x': 3,
                            'y': 10},
                          { 'hc-a2': 'NM',
                            'name': 'New '
                                    'Mexico',
                            'region': 'West',
                            'value': 2085572,
                            'x': 6,
                            'y': 3},
                          { 'hc-a2': 'NY',
                            'name': 'New '
                                    'York',
                            'region': 'Northeast',
                            'value': 19745289,
                            'x': 2,
                            'y': 9},
                          { 'hc-a2': 'NC',
                            'name': 'North '
                                    'Carolina',
                            'region': 'South',
                            'value': 10146788,
                            'x': 5,
                            'y': 9},
                          { 'hc-a2': 'ND',
                            'name': 'North '
                                    'Dakota',
                            'region': 'Midwest',
                            'value': 739482,
                            'x': 2,
                            'y': 3},
                          { 'hc-a2': 'OH',
                            'name': 'Ohio',
                            'region': 'Midwest',
                            'value': 11614373,
                            'x': 3,
                            'y': 8},
                          { 'hc-a2': 'OK',
                            'name': 'Oklahoma',
                            'region': 'South',
                            'value': 3878051,
                            'x': 6,
                            'y': 4},
                          { 'hc-a2': 'OR',
                            'name': 'Oregon',
                            'region': 'West',
                            'value': 3970239,
                            'x': 4,
                            'y': 1},
                          { 'hc-a2': 'PA',
                            'name': 'Pennsylvania',
                            'region': 'Northeast',
                            'value': 12784227,
                            'x': 3,
                            'y': 9},
                          { 'hc-a2': 'RI',
                            'name': 'Rhode '
                                    'Island',
                            'region': 'Northeast',
                            'value': 1055173,
                            'x': 2,
                            'y': 11},
                          { 'hc-a2': 'SC',
                            'name': 'South '
                                    'Carolina',
                            'region': 'South',
                            'value': 4832482,
                            'x': 6,
                            'y': 8},
                          { 'hc-a2': 'SD',
                            'name': 'South '
                                    'Dakota',
                            'region': 'Midwest',
                            'value': 853175,
                            'x': 3,
                            'y': 4},
                          { 'hc-a2': 'TN',
                            'name': 'Tennessee',
                            'region': 'South',
                            'value': 6651194,
                            'x': 5,
                            'y': 7},
                          { 'hc-a2': 'TX',
                            'name': 'Texas',
                            'region': 'South',
                            'value': 27862596,
                            'x': 7,
                            'y': 4},
                          { 'hc-a2': 'UT',
                            'name': 'Utah',
                            'region': 'West',
                            'value': 2942902,
                            'x': 5,
                            'y': 4},
                          { 'hc-a2': 'VT',
                            'name': 'Vermont',
                            'region': 'Northeast',
                            'value': 626011,
                            'x': 1,
                            'y': 10},
                          { 'hc-a2': 'VA',
                            'name': 'Virginia',
                            'region': 'South',
                            'value': 8411808,
                            'x': 5,
                            'y': 8},
                          { 'hc-a2': 'WA',
                            'name': 'Washington',
                            'region': 'West',
                            'value': 7288000,
                            'x': 2,
                            'y': 1},
                          { 'hc-a2': 'WV',
                            'name': 'West '
                                    'Virginia',
                            'region': 'South',
                            'value': 1850326,
                            'x': 4,
                            'y': 7},
                          { 'hc-a2': 'WI',
                            'name': 'Wisconsin',
                            'region': 'Midwest',
                            'value': 5778708,
                            'x': 2,
                            'y': 5},
                          { 'hc-a2': 'WY',
                            'name': 'Wyoming',
                            'region': 'West',
                            'value': 584153,
                            'x': 3,
                            'y': 3}],
                'name': ''}],
  'subtitle': { 'text': 'Source:<a '
                        'href="https://simple.wikipedia.org/wiki/List_of_U.S._states_by_population">Wikipedia</a>'},
  'title': { 'text': 'U.S. states by '
                     'population in '
                     '2016'},
  'tooltip': { 'headerFormat': '',
               'pointFormat': 'The '
                              'population '
                              'of <b> '
                              '{point.name}</b> '
                              'is '
                              '<b>{point.value}</b>'},
  'xAxis': {'visible': False},
  'yAxis': {'visible': False}}


hg.streamlit_highcharts(chartDef,640)


