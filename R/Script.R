library(tidyverse)

# 1. Chargement des données
# 1.1 Données usage internet
aggregation_mci_par_communes_techno <- read_csv2('Data/mci/Agregation_MCI_par_Commune_commune-techno-beta.csv', skip = 1)
base_eligibilite_Rhones_Alpes <- read_csv('Data/mci/Auvergne-Rhone-Alpes_Base_Eligibilite_20210115.csv') 
base_immeuble_Rhones_Alpes <- read_csv('/Users/lmp/Documents/Programming/CNAM/SIG/Fracture_numerique/Data/mci/Auvergne-Rhone-Alpes_Base_Immeuble_20210115.csv')
# 1.2 Données vote
vote_region <- read_csv2('Data/socio-demo/votes_reg_2015_TOUR2_dpt.csv')
# 1.3 Données administratives


# 2. Représenter les données d'internet à échelle départementale
