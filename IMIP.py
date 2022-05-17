import pandas as pd
import numpy as np

data =np.array([['Yasmin Oliveira', 'Estagiária de Engenharia', 'TecSaude', 'Engenharia Biomédica', 2022],
                   ['Camila Cristina', 'Estagiária de Engenharia', 'TecSaude', 'Engenharia Elétrica', 2021],
                   ['Liliane Martins', 'Aux de Engenharia', 'IMIP', 'Engenharia Eletrônica', 2020],
                   ['Bruna Oliveira', 'Aux de Engenharia', 'IMIP', 'Engenharia Eletrônica', 2019],
                   ['Kellyane Karol', 'Supervisora de Engenharia', 'IMIP', 'Engenharia Elétrica', 2018],
                   ['Melina Carla', 'Aux Admnistrativo', 'IMIP', 'Contabilidade', 2018],
                   ['Leonardo', 'Técnico de Eletrônica', 'TecSaude', 'Técnico em Eletrotécnica', 2021],
                   ['Gabriel Maior', 'Estagiário Técnico', 'TecSaude', 'Técnico em Eletrônica', 2022]])

data = pd.DataFrame(data, index = range(1, 9), columns=['Nome', 'Cargo', 'Empresa', 'Graduação', 'Ano'])
data.head(9)

#Procurando os funcionários a partir do ano de entrada
ano = input("Entre com o ano de entrada do funcionário: ")
data1 = data[(data.Ano == ano)]
data1.head()

#Pesquisando pelo cargo do funcionário 
cargo = input("Cargo do funcionário: ")
data2 = data[(data.Cargo == cargo)]
data2.head()