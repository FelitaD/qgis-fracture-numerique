import pandas as pd

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

# Chargement et combinaison des jeux de données immeubles et éligibilité
dtypes = {
    "imb_id": "int64",
    "addr_code": "string",
    "imb_code": "category",
    "code_techno": "category",
    "classe_debit_montant": "string",
    "classe_debit_descendant": "string",
}
eligibilite = pd.read_csv('Data/Auvergne-Rhone-Alpes_Base_Eligibilite_20210115.csv', low_memory=False, dtype=dtypes,
                          usecols=list(dtypes))
immeubles = pd.read_csv('Data/Auvergne-Rhone-Alpes_Base_Immeuble_20210115.csv', low_memory=False)
eligibilite_immeubles = pd.merge(eligibilite, immeubles, how='left', on='imb_id')

# Filtrage sur le département de l'Isère
# eligibilite_immeubles['imb_code_insee'].to_string()
# eligibilite_immeubles[eligibilite_immeubles["imb_code_insee"] == "imb_code_insee".startswith(38)]

# eligibilite.drop_duplicates(subset = ['imb_id', 'code_techno'], inplace = True)

# for imb in eligibilite_immeubles['imb_id'].unique():
#     new_imb = eligibilite_immeubles[eligibilite_immeubles["imb_id"] == imb]
#     liste_debits  = new_imb['classe_debit_descendant'].value_counts()

# eligibilite_immeubles['rank'] = np.nan

class_ranks = {'INEL': 1,
               'HD05': 2,
               'HD3': 3,
               'BHD8': 4,
               'THD30': 5,
               'THD100': 6,
               'THD1G': 7}

eligibilite_immeubles['rank'] = eligibilite_immeubles['classe_debit_descendant'].map(class_ranks)
print(1, eligibilite_immeubles.head())

ranked = eligibilite_immeubles.groupby('imb_id')['rank'].agg(lambda x: x.sort_values().take([-1]))
# ranked.drop_duplicates(subset=['imb_id', 'rank'], inplace=True)
eligibilite_immeubles_ranked = pd.merge(ranked, eligibilite_immeubles, how='inner', on=['imb_id', 'rank'])
print(2, eligibilite_immeubles_ranked.head())

class_means = {
    "INEL_mean": 0 + (0.512 - 0)/2,
    "HD05_mean": 0.512 + (4 - 0.512)/2,
    "HD3_mean": 2 + (10 - 2)/2,
    "BHD8_mean": 6 + (25 - 6)/2,
    "THD30_mean": 20 + (100 - 20)/2,
    "THD100_mean": 100 + (1000 - 100)/2,
    "THD1G_mean": 1000
}

eligibilite_immeubles_ranked['debit_mean'] = eligibilite_immeubles_ranked['classe_debit_descendant'].map(class_means)

# groupby('code_insee')['debit-max-mean-commune']
# eligibilite_immeubles_Gr_ranked.head(30)
# eligibilite_immeubles_Gr = eligibilite_immeubles[eligibilite_immeubles['imb_code_insee']==38185]
# eligibilite_immeubles_Gr_ranked.to_csv('debit_max.csv')
